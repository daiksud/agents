#!/usr/bin/env python3
"""Run controlled, isolated GitHub Copilot model evaluations."""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
import shutil
import subprocess
import sys
import tarfile
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path

try:
    from scripts.apm_smoke import candidate_environment, validate_deployment
except ModuleNotFoundError:  # direct execution from scripts/
    from apm_smoke import candidate_environment, validate_deployment

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
EXPECTED_MODEL_IDS = [
    "gpt-6-sol",
    "gpt-6-luna",
    "claude-opus-5.5",
    "claude-sonnet-5",
]
GRADER_ONLY_PATHS = (
    Path("evals/copilot-models"),
    Path("docs/guides/copilot-model-evaluation.md"),
    Path("scripts/run_copilot_model_eval.py"),
    Path("tests/test_copilot_model_eval.py"),
)
AUTH_VARIABLES = ("COPILOT_GITHUB_TOKEN", "GH_TOKEN", "GITHUB_TOKEN")


def load_suite(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("suite") != "copilot-model-contracts":
        raise ValueError("unexpected suite")
    ids = [case["id"] for case in data["cases"]]
    if ids != EXPECTED_CASE_IDS or len(ids) != len(set(ids)):
        raise ValueError("cases must contain exactly one ordered A-G sequence")
    if set(data["failure_classes"]) != FAILURE_CLASSES:
        raise ValueError("failure_classes do not match the documented taxonomy")
    model_ids = [model["cli_model"] for model in data["models"]]
    if (
        model_ids != EXPECTED_MODEL_IDS
        or len(model_ids) != len(set(model_ids))
    ):
        raise ValueError("models must contain exactly one ordered baseline model set")
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


def remove_grader_material(root: Path) -> None:
    for relative in GRADER_ONLY_PATHS:
        target = root / relative
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


def stage_workspace(root: Path, destination: Path) -> None:
    archive = subprocess.check_output(["git", "archive", "HEAD"], cwd=root)
    destination.mkdir(parents=True, exist_ok=False)
    with tarfile.open(fileobj=io.BytesIO(archive)) as bundle:
        bundle.extractall(destination, filter="data")
    remove_grader_material(destination)
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


def prepare_delivery(
    root: Path,
    repo_sha: str,
    base_dir: Path,
    *,
    timeout: float,
) -> tuple[Path, Path, dict[str, str], dict[str, str]]:
    workspace = base_dir / "workspace"
    home = base_dir / "home"
    mirror = base_dir / "origin.git"
    stage_workspace(root, workspace)
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
    remove_grader_material(cached_candidate)
    remove_skill_evals(cached_candidate)
    remove_skill_evals(home)

    fingerprints = {
        "workspace_sha256": sha256_tree(workspace),
        "copilot_instructions_sha256": sha256_file(home / ".copilot/AGENTS.md"),
        "installed_skills_sha256": sha256_tree(home / ".agents/skills"),
    }
    return workspace, home, environment, fingerprints


def write_manifest(path: Path, manifest: dict) -> None:
    path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


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
    if args.timeout_seconds <= 0:
        parser.error("--timeout-seconds must be > 0")

    root = Path.cwd().resolve()
    suite = load_suite(args.cases)
    selected = suite["models"]
    if args.models:
        wanted = {item.strip() for item in args.models.split(",") if item.strip()}
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

    if args.dry_run:
        print(json.dumps({
            "runs": len(planned),
            "models": [model["cli_model"] for model in selected],
            "cases": [case["id"] for case in suite["cases"]],
            "repeat": args.repeat,
        }, ensure_ascii=False, indent=2))
        return 0

    for executable in ("copilot", "apm", "git"):
        if shutil.which(executable) is None:
            print(f"{executable} executable not found", file=sys.stderr)
            return 2

    provider_variables = sorted(
        key for key in os.environ if key.startswith("COPILOT_PROVIDER_")
    )
    if provider_variables:
        print(
            "BYOK provider variables are not allowed for GitHub Copilot comparison: "
            + ", ".join(provider_variables),
            file=sys.stderr,
        )
        return 2

    auth_variable = next(
        (name for name in AUTH_VARIABLES if os.environ.get(name)),
        None,
    )
    if auth_variable is None:
        print(
            "isolated evaluation requires COPILOT_GITHUB_TOKEN, GH_TOKEN, "
            "or GITHUB_TOKEN",
            file=sys.stderr,
        )
        return 2

    try:
        repo_sha = require_clean_checkout(root)
        output_dir = resolve_output_dir(args.output_dir, root)
    except (RuntimeError, ValueError) as error:
        print(str(error), file=sys.stderr)
        return 2

    output_dir.mkdir(parents=True, exist_ok=False)
    manifest_path = output_dir / "manifest.json"
    suite_sha256 = sha256_file(args.cases.resolve())
    planned_runs = [
        {
            "model": model["name"],
            "cli_model": model["cli_model"],
            "case_id": case["id"],
            "attempt": attempt,
        }
        for model, case, attempt in planned
    ]
    manifest = {
        "suite": suite["suite"],
        "suite_version": suite["version"],
        "suite_sha256": suite_sha256,
        "started_at": datetime.now(timezone.utc).isoformat(),
        "repo_sha": repo_sha,
        "auth_source": auth_variable,
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

    executable = shutil.which("copilot")
    assert executable is not None
    try:
        version = run_command([executable, "--version"], root, timeout=30)
        if version.returncode != 0:
            raise RuntimeError(version.stderr or version.stdout)
        manifest["copilot_version"] = (version.stdout or version.stderr).strip()

        with tempfile.TemporaryDirectory(prefix="copilot-eval-base-") as directory:
            base_dir = Path(directory)
            workspace_base, home_base, base_env, fingerprints = prepare_delivery(
                root,
                repo_sha,
                base_dir,
                timeout=min(args.timeout_seconds, 180),
            )
            manifest["input_fingerprints"] = fingerprints
            manifest["setup"] = {
                "status": "verified",
                "failure_class": None,
                "grader_paths_excluded": [
                    path.as_posix() for path in GRADER_ONLY_PATHS
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
                started = time.monotonic()
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
                        result = run_command(
                            command,
                            workspace,
                            env=environment,
                            timeout=args.timeout_seconds,
                        )
                        stdout = result.stdout
                        stderr = result.stderr
                        return_code = result.returncode
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
                elapsed = time.monotonic() - started

                stdout_name = stdout_path.name
                stderr_name = stderr_path.name
                try:
                    stdout_path.write_text(stdout, encoding="utf-8")
                    stderr_path.write_text(stderr, encoding="utf-8")
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
                    "elapsed_seconds": round(elapsed, 3),
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
