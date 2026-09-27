#!/usr/bin/env python3
"""Run controlled, isolated GitHub Copilot model evaluations."""

from __future__ import annotations

import argparse
import hashlib
import io
import importlib.util
import json
import math
import os
import shutil
import subprocess
import sys
import tarfile
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path

FAILURE_CLASSES = {
    "instruction_delivery",
    "ambiguity",
    "tool_or_permission",
    "task_granularity",
    "runtime",
    "model_specific",
    "none",
}
EXPECTED_CASE_IDS = list("ABCDEFG")
EXPECTED_MODELS = [
    ("GPT-6 Sol", "gpt-6-sol"),
    ("GPT-6 Luna", "gpt-6-luna"),
    ("Claude Opus 5.5", "claude-opus-5.5"),
    ("Claude Sonnet 5", "claude-sonnet-5"),
]
EXPECTED_MODEL_IDS = [model_id for _, model_id in EXPECTED_MODELS]
GRADER_ONLY_PATHS = (
    Path("evals/copilot-models"),
    Path("docs/guides/copilot-model-evaluation.md"),
    Path("scripts/run_copilot_model_eval.py"),
    Path("tests/test_copilot_model_eval.py"),
)
AUTH_VARIABLES = ("COPILOT_GITHUB_TOKEN", "GH_TOKEN", "GITHUB_TOKEN")


def _nonempty_string(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _nonempty_string_list(value: object) -> bool:
    return (
        isinstance(value, list)
        and bool(value)
        and all(_nonempty_string(item) for item in value)
    )


def load_suite(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("suite must be a JSON object")
    if data.get("suite") != "copilot-model-contracts":
        raise ValueError("unexpected suite")
    if type(data.get("version")) is not int or data["version"] < 1:
        raise ValueError("suite version must be a positive integer")
    if not _nonempty_string_list(data.get("common_rules")):
        raise ValueError("common_rules must be a non-empty string list")

    failure_classes = data.get("failure_classes")
    if (
        not isinstance(failure_classes, list)
        or not all(_nonempty_string(item) for item in failure_classes)
        or set(failure_classes) != FAILURE_CLASSES
    ):
        raise ValueError("failure_classes do not match the documented taxonomy")

    models = data.get("models")
    if not isinstance(models, list):
        raise ValueError("models must be a list")
    normalized_models = []
    for model in models:
        if not isinstance(model, dict):
            raise ValueError("each model must be an object")
        name, cli_model = model.get("name"), model.get("cli_model")
        if not _nonempty_string(name) or not _nonempty_string(cli_model):
            raise ValueError("each model requires non-empty name and cli_model")
        normalized_models.append((name, cli_model))
    if (
        normalized_models != EXPECTED_MODELS
        or len({cli_model for _, cli_model in normalized_models})
        != len(EXPECTED_MODELS)
    ):
        raise ValueError("models must contain exactly one ordered baseline model set")

    cases = data.get("cases")
    if not isinstance(cases, list):
        raise ValueError("cases must be a list")
    ids = []
    for case in cases:
        if not isinstance(case, dict):
            raise ValueError("each case must be an object")
        case_id = case.get("id")
        if not _nonempty_string(case_id):
            raise ValueError("each case requires a non-empty id")
        if not _nonempty_string(case.get("title")):
            raise ValueError(f"case {case_id} requires a non-empty title")
        if not _nonempty_string(case.get("prompt")):
            raise ValueError(f"case {case_id} requires a non-empty prompt")
        if not _nonempty_string_list(case.get("criteria")):
            raise ValueError(f"case {case_id} requires non-empty criteria")
        ids.append(case_id)
    if ids != EXPECTED_CASE_IDS or len(ids) != len(set(ids)):
        raise ValueError("cases must contain exactly one ordered A-G sequence")
    return data

def build_prompt(suite: dict, case: dict) -> str:
    rules = "\n".join(f"- {rule}" for rule in suite["common_rules"])
    return (
        "This is a controlled GitHub Copilot evaluation.\n"
        "Apply the installed common Instructions and Skills.\n"
        f"{rules}\n\n"
        f"CASE {case['id']}: {case['title']}\n"
        f"{case['prompt']}\n"
    )


def run_command(
    command: list[str],
    cwd: Path,
    *,
    env: dict[str, str] | None = None,
    timeout: float | None = None,
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command,
        cwd=cwd,
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=env,
        timeout=timeout,
    )


def require_success(
    command: list[str],
    cwd: Path,
    *,
    env: dict[str, str],
    timeout: float,
) -> subprocess.CompletedProcess[str]:
    result = run_command(command, cwd, env=env, timeout=timeout)
    if result.returncode != 0:
        detail = (result.stderr or result.stdout).strip()
        raise RuntimeError(f"{' '.join(command)} failed: {detail}")
    return result


def current_head(root: Path) -> str | None:
    try:
        result = run_command(["git", "rev-parse", "HEAD"], root, timeout=30)
    except (OSError, subprocess.SubprocessError):
        return None
    return result.stdout.strip() if result.returncode == 0 else None


def require_clean_checkout(root: Path) -> str:
    result = run_command(
        ["git", "status", "--porcelain=v1", "--untracked-files=all"],
        root,
        timeout=30,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "git status failed")
    if result.stdout.strip():
        raise RuntimeError("evaluation requires a clean checkout")
    head = run_command(["git", "rev-parse", "HEAD"], root, timeout=30)
    if head.returncode != 0:
        raise RuntimeError(head.stderr.strip() or "git rev-parse failed")
    return head.stdout.strip()


def require_tracked_suite(
    root: Path,
    repo_sha: str,
    relative: Path,
    suite_path: Path,
) -> None:
    object_name = f"{repo_sha}:{relative.as_posix()}"
    try:
        result = subprocess.run(
            ["git", "show", object_name],
            cwd=root,
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=30,
        )
    except (OSError, subprocess.SubprocessError) as error:
        raise RuntimeError(f"cannot verify selected suite at HEAD: {error}") from error
    if result.returncode != 0:
        raise RuntimeError(
            "selected suite must be tracked in the recorded repository commit"
        )
    if result.stdout != suite_path.read_bytes():
        raise RuntimeError(
            "selected suite differs from the recorded repository commit"
        )


def grader_paths(extra_paths: tuple[Path, ...] = ()) -> tuple[Path, ...]:
    seen: set[Path] = set()
    result: list[Path] = []
    for path in (*GRADER_ONLY_PATHS, *extra_paths):
        if path not in seen:
            seen.add(path)
            result.append(path)
    return tuple(result)


def remove_grader_material(
    root: Path,
    extra_paths: tuple[Path, ...] = (),
) -> None:
    for relative in grader_paths(extra_paths):
        target = root / relative
        if target.is_dir():
            shutil.rmtree(target)
        elif target.exists():
            target.unlink()


def remove_deployed_grader_material(
    home: Path,
    extra_paths: tuple[Path, ...],
) -> None:
    for relative in extra_paths:
        if len(relative.parts) >= 2 and relative.parts[0] == "skills":
            target = home / ".agents" / relative
            if target.is_dir():
                shutil.rmtree(target)
            elif target.exists():
                target.unlink()


def remove_skill_evals(root: Path) -> None:
    for base in (
        root / "skills",
        root / ".github/skills",
        root / ".agents/skills",
    ):
        if not base.is_dir():
            continue
        for eval_dir in base.glob("*/evals"):
            if eval_dir.is_dir():
                shutil.rmtree(eval_dir)


def stage_workspace(
    root: Path,
    destination: Path,
    *,
    revision: str,
    extra_grader_paths: tuple[Path, ...] = (),
) -> None:
    archive = subprocess.check_output(["git", "archive", revision], cwd=root)
    destination.mkdir(parents=True, exist_ok=False)
    with tarfile.open(fileobj=io.BytesIO(archive)) as bundle:
        bundle.extractall(destination, filter="data")
    remove_grader_material(destination, extra_grader_paths)
    remove_skill_evals(destination)


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def sha256_tree(root: Path) -> str:
    digest = hashlib.sha256()
    for path in sorted(p for p in root.rglob("*") if p.is_file()):
        digest.update(path.relative_to(root).as_posix().encode("utf-8"))
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def resolve_output_dir(requested: Path | None, root: Path) -> Path:
    if requested is None:
        timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        path = Path(tempfile.gettempdir()) / "copilot-model-eval-results" / timestamp
    else:
        path = requested.expanduser()
        if not path.is_absolute():
            path = (Path.cwd() / path).resolve()
    path = path.resolve()
    if path == root or path.is_relative_to(root):
        raise ValueError("evaluation output must be outside the repository")
    return path


def isolated_environment(home: Path, base: dict[str, str]) -> dict[str, str]:
    environment = base.copy()
    environment["HOME"] = str(home)
    environment["COPILOT_HOME"] = str(home / ".copilot")
    environment["COPILOT_AUTO_UPDATE"] = "false"
    environment["GITHUB_COPILOT_PROMPT_MODE_EXTENSIONS"] = "false"
    environment["GITHUB_COPILOT_PROMPT_MODE_REPO_HOOKS"] = "false"
    environment["GITHUB_COPILOT_PROMPT_MODE_WORKSPACE_MCP"] = "false"
    environment.pop("COPILOT_ALLOW_ALL", None)
    environment.pop("COPILOT_MODEL", None)
    return environment


def load_delivery_helpers():
    module_path = Path(__file__).with_name("apm_smoke.py")
    spec = importlib.util.spec_from_file_location("copilot_eval_apm_smoke", module_path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load APM delivery verifier")
    module = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(module)
    except ModuleNotFoundError as error:
        missing = error.name or "unknown module"
        raise RuntimeError(f"delivery dependency missing: {missing}") from error
    return module.candidate_environment, module.validate_deployment


def prepare_delivery(
    root: Path,
    repo_sha: str,
    base_dir: Path,
    *,
    timeout: float,
    extra_grader_paths: tuple[Path, ...] = (),
) -> tuple[Path, Path, dict[str, str], dict[str, str]]:
    candidate_environment, validate_deployment = load_delivery_helpers()

    workspace = base_dir / "workspace"
    home = base_dir / "home"
    mirror = base_dir / "origin.git"
    stage_workspace(
        root,
        workspace,
        revision=repo_sha,
        extra_grader_paths=extra_grader_paths,
    )
    home.mkdir(parents=True)

    environment = isolated_environment(home, os.environ.copy())
    environment.update(candidate_environment(root, mirror))

    require_success(
        [
            "apm",
            "install",
            "--global",
            "--target",
            "codex,copilot",
            f"daiksud/agents#{repo_sha}",
        ],
        workspace,
        env=environment,
        timeout=timeout,
    )
    require_success(
        ["apm", "compile", "--global"],
        workspace,
        env=environment,
        timeout=timeout,
    )
    errors = validate_deployment(workspace, home, repo_sha)
    if errors:
        raise RuntimeError("candidate delivery verification failed: " + "; ".join(errors))

    cached_candidate = home / ".apm/apm_modules/daiksud/agents"
    remove_grader_material(cached_candidate, extra_grader_paths)
    remove_skill_evals(cached_candidate)
    remove_deployed_grader_material(home, extra_grader_paths)
    remove_skill_evals(home)

    fingerprints = {
        "workspace_sha256": sha256_tree(workspace),
        "copilot_instructions_sha256": sha256_file(home / ".copilot/AGENTS.md"),
        "installed_skills_sha256": sha256_tree(home / ".agents/skills"),
    }
    return workspace, home, environment, fingerprints


def create_private_directory(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=False, mode=0o700)
    os.chmod(path, 0o700)


def _open_private(path: Path, *, binary: bool):
    flags = os.O_WRONLY | os.O_CREAT | os.O_TRUNC
    descriptor = os.open(path, flags, 0o600)
    os.fchmod(descriptor, 0o600)
    if binary:
        return os.fdopen(descriptor, "wb")
    return os.fdopen(descriptor, "w", encoding="utf-8")


def write_private_text(path: Path, value: str) -> None:
    with _open_private(path, binary=False) as stream:
        stream.write(value)
        stream.flush()
        os.fsync(stream.fileno())


def _atomic_write(path: Path, payload: bytes) -> None:
    temporary = path.with_name(f".{path.name}.tmp")
    try:
        descriptor = os.open(
            temporary,
            os.O_WRONLY | os.O_CREAT | os.O_EXCL,
            0o600,
        )
        os.fchmod(descriptor, 0o600)
        with os.fdopen(descriptor, "wb") as stream:
            stream.write(payload)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
        os.chmod(path, 0o600)
    finally:
        try:
            temporary.unlink()
        except FileNotFoundError:
            pass


def snapshot_suite(path: Path, output_dir: Path) -> Path:
    target = output_dir / "suite.json"
    _atomic_write(target, path.read_bytes())
    return target

def write_manifest(path: Path, manifest: dict) -> None:
    payload = (
        json.dumps(manifest, ensure_ascii=False, indent=2, allow_nan=False)
        + "\n"
    ).encode("utf-8")
    _atomic_write(path, payload)

def finish_preflight_failure(
    manifest_path: Path,
    manifest: dict,
    *,
    failure_class: str,
    notes: str,
) -> int:
    manifest["setup"] = {
        "status": "failed",
        "failure_class": failure_class,
        "notes": notes,
    }
    manifest["finished_at"] = datetime.now(timezone.utc).isoformat()
    write_manifest(manifest_path, manifest)
    print(notes, file=sys.stderr)
    return 2


def text_from_timeout(value: str | bytes | None) -> str:
    if value is None:
        return ""
    if isinstance(value, bytes):
        return value.decode("utf-8", errors="replace")
    return value


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--cases",
        type=Path,
        default=Path("evals/copilot-models/cases.json"),
    )
    parser.add_argument("--models", help="comma-separated cli_model values")
    parser.add_argument("--repeat", type=int, default=1)
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--timeout-seconds", type=float, default=600)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if args.repeat < 1:
        parser.error("--repeat must be >= 1")
    if not math.isfinite(args.timeout_seconds) or args.timeout_seconds <= 0:
        parser.error("--timeout-seconds must be a finite value > 0")

    root = Path.cwd().resolve()
    suite_path = args.cases.resolve()
    if not suite_path.is_relative_to(root):
        parser.error("--cases must resolve to a file inside the repository")
    suite = load_suite(suite_path)
    selected = suite["models"]
    if args.models is not None:
        wanted = {item.strip() for item in args.models.split(",") if item.strip()}
        if not wanted:
            parser.error("--models must include at least one model id")
        selected = [model for model in selected if model["cli_model"] in wanted]
        missing = wanted - {model["cli_model"] for model in selected}
        if missing:
            parser.error(f"unknown model(s): {', '.join(sorted(missing))}")

    planned = [
        (model, case, attempt)
        for model in selected
        for case in suite["cases"]
        for attempt in range(1, args.repeat + 1)
    ]
    planned_runs = [
        {
            "model": model["name"],
            "cli_model": model["cli_model"],
            "case_id": case["id"],
            "attempt": attempt,
        }
        for model, case, attempt in planned
    ]

    if args.dry_run:
        print(json.dumps({
            "runs": len(planned),
            "models": [model["cli_model"] for model in selected],
            "cases": [case["id"] for case in suite["cases"]],
            "repeat": args.repeat,
        }, ensure_ascii=False, indent=2))
        return 0

    try:
        output_dir = resolve_output_dir(args.output_dir, root)
        create_private_directory(output_dir)
    except (OSError, ValueError) as error:
        print(str(error), file=sys.stderr)
        return 2

    manifest_path = output_dir / "manifest.json"
    try:
        suite_snapshot = snapshot_suite(suite_path, output_dir)
    except OSError as error:
        print(f"failed to preserve evaluation suite: {error}", file=sys.stderr)
        return 2
    suite_sha256 = sha256_file(suite_path)
    selected_suite_paths = (suite_path.relative_to(root),)
    manifest = {
        "suite": suite["suite"],
        "suite_version": suite["version"],
        "suite_sha256": suite_sha256,
        "suite_snapshot": suite_snapshot.name,
        "started_at": datetime.now(timezone.utc).isoformat(),
        "repo_sha": current_head(root),
        "auth_source": None,
        "selected_models": [
            {"name": model["name"], "cli_model": model["cli_model"]}
            for model in selected
        ],
        "planned_runs": planned_runs,
        "repeat": args.repeat,
        "timeout_seconds": args.timeout_seconds,
        "setup": {"status": "pending"},
        "runs": [],
    }
    write_manifest(manifest_path, manifest)

    missing_executables = [
        executable
        for executable in ("copilot", "apm", "git")
        if shutil.which(executable) is None
    ]
    if missing_executables:
        return finish_preflight_failure(
            manifest_path,
            manifest,
            failure_class="runtime",
            notes="missing executable(s): " + ", ".join(missing_executables),
        )

    provider_variables = sorted(
        key for key in os.environ if key.startswith("COPILOT_PROVIDER_")
    )
    if provider_variables:
        return finish_preflight_failure(
            manifest_path,
            manifest,
            failure_class="runtime",
            notes=(
                "BYOK provider variables are not allowed for GitHub Copilot "
                "comparison: " + ", ".join(provider_variables)
            ),
        )

    auth_variable = next(
        (name for name in AUTH_VARIABLES if os.environ.get(name)),
        None,
    )
    if auth_variable is None:
        return finish_preflight_failure(
            manifest_path,
            manifest,
            failure_class="tool_or_permission",
            notes=(
                "isolated evaluation requires COPILOT_GITHUB_TOKEN, GH_TOKEN, "
                "or GITHUB_TOKEN"
            ),
        )
    manifest["auth_source"] = auth_variable
    write_manifest(manifest_path, manifest)

    try:
        repo_sha = require_clean_checkout(root)
    except (OSError, RuntimeError, subprocess.SubprocessError) as error:
        return finish_preflight_failure(
            manifest_path,
            manifest,
            failure_class="runtime",
            notes=str(error),
        )
    manifest["repo_sha"] = repo_sha
    try:
        require_tracked_suite(
            root,
            repo_sha,
            suite_path.relative_to(root),
            suite_path,
        )
    except RuntimeError as error:
        return finish_preflight_failure(
            manifest_path,
            manifest,
            failure_class="runtime",
            notes=str(error),
        )
    write_manifest(manifest_path, manifest)

    executable = shutil.which("copilot")
    assert executable is not None
    try:
        version = run_command([executable, "--version"], root, timeout=30)
    except (OSError, subprocess.SubprocessError) as error:
        return finish_preflight_failure(
            manifest_path,
            manifest,
            failure_class="runtime",
            notes=f"Copilot version probe failed: {error}",
        )
    if version.returncode != 0:
        return finish_preflight_failure(
            manifest_path,
            manifest,
            failure_class="runtime",
            notes=(
                f"Copilot version probe exited with code {version.returncode}; "
                "inspect stdout/stderr in the local environment."
            ),
        )
    manifest["copilot_version"] = (version.stdout or version.stderr).strip()
    write_manifest(manifest_path, manifest)

    try:
        with tempfile.TemporaryDirectory(prefix="copilot-eval-base-") as directory:
            base_dir = Path(directory)
            workspace_base, home_base, base_env, fingerprints = prepare_delivery(
                root,
                repo_sha,
                base_dir,
                timeout=min(args.timeout_seconds, 180),
                extra_grader_paths=selected_suite_paths,
            )
            manifest["input_fingerprints"] = fingerprints
            manifest["setup"] = {
                "status": "verified",
                "failure_class": None,
                "grader_paths_excluded": [
                    path.as_posix()
                    for path in grader_paths(selected_suite_paths)
                ],
                "skill_evals_excluded": True,
                "agent_tools_denied": ["shell", "write", "url", "memory"],
            }
            write_manifest(manifest_path, manifest)

            for model, case, attempt in planned:
                prompt = build_prompt(suite, case)
                prompt_hash = hashlib.sha256(prompt.encode("utf-8")).hexdigest()
                stem = f"{model['cli_model']}__{case['id']}__{attempt}"
                stdout_path = output_dir / f"{stem}.jsonl"
                stderr_path = output_dir / f"{stem}.stderr.txt"
                attempt_started = time.monotonic()
                invocation_started = None
                setup_seconds = None
                timed_out = False
                failure_class = None
                notes = None
                stdout = ""
                stderr = ""
                return_code = None

                try:
                    with tempfile.TemporaryDirectory(
                        prefix=f"copilot-eval-{case['id']}-"
                    ) as run_directory:
                        run_root = Path(run_directory)
                        workspace = run_root / "workspace"
                        home = run_root / "home"
                        shutil.copytree(workspace_base, workspace)
                        shutil.copytree(home_base, home)
                        environment = isolated_environment(home, base_env)

                        command = [
                            executable,
                            "-p",
                            prompt,
                            f"--model={model['cli_model']}",
                            "--mode=plan",
                            "--no-ask-user",
                            "--no-auto-update",
                            "--output-format=json",
                            "--deny-tool=shell,write,url,memory",
                        ]
                        setup_seconds = time.monotonic() - attempt_started
                        invocation_started = time.monotonic()
                        result = run_command(
                            command,
                            workspace,
                            env=environment,
                            timeout=args.timeout_seconds,
                        )
                        stdout = result.stdout
                        stderr = result.stderr
                        return_code = result.returncode
                        if return_code != 0:
                            failure_class = "runtime"
                            notes = (
                                f"Copilot exited with code {return_code}; "
                                "inspect stderr evidence."
                            )
                except subprocess.TimeoutExpired as error:
                    timed_out = True
                    stdout = text_from_timeout(error.stdout)
                    stderr = text_from_timeout(error.stderr)
                    failure_class = "runtime"
                    notes = (
                        "Copilot invocation exceeded the configured "
                        f"{args.timeout_seconds:g}s timeout."
                    )
                except (OSError, subprocess.SubprocessError) as error:
                    failure_class = "runtime"
                    notes = f"Run-side operation failed: {error}"
                finished = time.monotonic()
                if setup_seconds is None:
                    setup_seconds = finished - attempt_started
                elapsed = (
                    finished - invocation_started
                    if invocation_started is not None
                    else None
                )

                stdout_name = stdout_path.name
                stderr_name = stderr_path.name
                try:
                    write_private_text(stdout_path, stdout)
                    write_private_text(stderr_path, stderr)
                except OSError as error:
                    failure_class = failure_class or "runtime"
                    suffix = f"Evidence write failed: {error}"
                    notes = f"{notes} {suffix}".strip() if notes else suffix
                    stdout_name = None
                    stderr_name = None

                manifest["runs"].append({
                    "model": model["name"],
                    "cli_model": model["cli_model"],
                    "case_id": case["id"],
                    "attempt": attempt,
                    "prompt_sha256": prompt_hash,
                    "return_code": return_code,
                    "timed_out": timed_out,
                    "setup_seconds": round(setup_seconds, 3),
                    "elapsed_seconds": (
                        round(elapsed, 3) if elapsed is not None else None
                    ),
                    "stdout": stdout_name,
                    "stderr": stderr_name,
                    "input_fingerprints": fingerprints,
                    "quality": {
                        "criteria_met": None,
                        "tdd_or_navigator_gate_misses": None,
                        "premature_stop": None,
                        "scope_expansion": None,
                        "defect_requirement_or_regression_miss": None,
                        "evidence_free_success_claim": None,
                        "stop_boundary_violation": None,
                    },
                    "efficiency": {
                        "turn_count": None,
                        "tool_call_count": None,
                        "token_usage": None,
                        "loaded_skills": None,
                        "loaded_references": None,
                        "redundant_reads": None,
                    },
                    "failure_class": failure_class,
                    "notes": notes,
                })
                write_manifest(manifest_path, manifest)

    except (OSError, RuntimeError, subprocess.SubprocessError) as error:
        if manifest["setup"].get("status") == "verified":
            manifest["batch_failure"] = {
                "failure_class": "runtime",
                "notes": str(error),
                "completed_runs": len(manifest["runs"]),
            }
        else:
            manifest["setup"] = {
                "status": "failed",
                "failure_class": "instruction_delivery",
                "notes": str(error),
            }
        manifest["finished_at"] = datetime.now(timezone.utc).isoformat()
        try:
            write_manifest(manifest_path, manifest)
        except OSError:
            pass
        print(str(error), file=sys.stderr)
        return 2

    manifest["finished_at"] = datetime.now(timezone.utc).isoformat()
    write_manifest(manifest_path, manifest)
    print(output_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
