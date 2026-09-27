#!/usr/bin/env python3
"""Run the shared GitHub Copilot model evaluation suite.

The runner intentionally performs read-only planning evaluations. It does not
grade model output automatically; raw evidence is recorded for later review.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
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


def load_suite(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("suite") != "copilot-model-contracts":
        raise ValueError("unexpected suite")
    if {case["id"] for case in data["cases"]} != set("ABCDEFG"):
        raise ValueError("cases must contain exactly A-G")
    if set(data["failure_classes"]) != FAILURE_CLASSES:
        raise ValueError("failure_classes do not match the documented taxonomy")
    if len(data["models"]) != 4:
        raise ValueError("the baseline suite must contain four models")
    return data


def build_prompt(suite: dict, case: dict) -> str:
    rules = "\n".join(f"- {rule}" for rule in suite["common_rules"])
    criteria = "\n".join(f"- {criterion}" for criterion in case["criteria"])
    return (
        "This is a controlled GitHub Copilot evaluation.\n"
        "Apply the repository Instructions and Skills available in the current working tree.\n"
        f"{rules}\n\n"
        f"CASE {case['id']}: {case['title']}\n"
        f"{case['prompt']}\n\n"
        "Acceptance criteria used by the evaluator (do not self-score):\n"
        f"{criteria}\n"
    )


def run_command(command: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command,
        cwd=cwd,
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


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
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if args.repeat < 1:
        parser.error("--repeat must be >= 1")

    root = Path.cwd()
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

    executable = shutil.which("copilot")
    if executable is None:
        print("copilot executable not found", file=sys.stderr)
        return 2

    version = run_command([executable, "--version"], root)
    if version.returncode != 0:
        print(version.stderr or version.stdout, file=sys.stderr)
        return 2
    copilot_version = (version.stdout or version.stderr).strip()

    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    output_dir = args.output_dir or Path("evals/copilot-models/results") / timestamp
    output_dir.mkdir(parents=True, exist_ok=False)

    repo_sha = run_command(["git", "rev-parse", "HEAD"], root)
    repo_sha_text = repo_sha.stdout.strip() if repo_sha.returncode == 0 else None

    manifest = {
        "suite": suite["suite"],
        "suite_version": suite["version"],
        "started_at": datetime.now(timezone.utc).isoformat(),
        "repo_sha": repo_sha_text,
        "copilot_version": copilot_version,
        "repeat": args.repeat,
        "runs": [],
    }

    for model, case, attempt in planned:
        prompt = build_prompt(suite, case)
        prompt_hash = hashlib.sha256(prompt.encode("utf-8")).hexdigest()
        stem = f"{model['cli_model']}__{case['id']}__{attempt}"
        stdout_path = output_dir / f"{stem}.jsonl"
        stderr_path = output_dir / f"{stem}.stderr.txt"

        command = [
            executable,
            "-p",
            prompt,
            f"--model={model['cli_model']}",
            "--mode=plan",
            "--no-ask-user",
            "--no-auto-update",
            "--output-format=json",
        ]
        started = time.monotonic()
        result = run_command(command, root)
        elapsed = time.monotonic() - started
        stdout_path.write_text(result.stdout, encoding="utf-8")
        stderr_path.write_text(result.stderr, encoding="utf-8")

        manifest["runs"].append({
            "model": model["name"],
            "cli_model": model["cli_model"],
            "case_id": case["id"],
            "attempt": attempt,
            "prompt_sha256": prompt_hash,
            "return_code": result.returncode,
            "elapsed_seconds": round(elapsed, 3),
            "stdout": stdout_path.name,
            "stderr": stderr_path.name,
            "quality": {
                "criteria_met": None,
                "tdd_or_navigator_gate_misses": None,
                "scope_expansion": None,
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
            "failure_class": None,
            "notes": None,
        })

    manifest["finished_at"] = datetime.now(timezone.utc).isoformat()
    (output_dir / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(output_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
