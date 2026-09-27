import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


class CopilotModelEvaluationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[1]
        cls.cases_path = cls.root / "evals/copilot-models/cases.json"
        cls.baseline_path = (
            cls.root
            / "evals/copilot-models/results/2026-09-27-runtime-unavailable.json"
        )
        cls.guide_path = cls.root / "docs/guides/copilot-model-evaluation.md"
        path = cls.root / "scripts/run_copilot_model_eval.py"
        spec = importlib.util.spec_from_file_location("copilot_eval", path)
        cls.module = importlib.util.module_from_spec(spec)
        assert spec.loader is not None
        spec.loader.exec_module(cls.module)

    def test_suite_has_four_models_and_shared_cases(self):
        data = json.loads(self.cases_path.read_text(encoding="utf-8"))
        self.assertEqual("copilot-model-contracts", data["suite"])
        self.assertEqual(
            ["gpt-6-sol", "gpt-6-luna", "claude-opus-5.5", "claude-sonnet-5"],
            [model["cli_model"] for model in data["models"]],
        )
        self.assertEqual(list("ABCDEFG"), [case["id"] for case in data["cases"]])
        for case in data["cases"]:
            self.assertTrue(case["prompt"].strip())
            self.assertGreaterEqual(len(case["criteria"]), 3)

    def test_suite_rejects_duplicate_case_ids(self):
        data = json.loads(self.cases_path.read_text(encoding="utf-8"))
        data["cases"].append(dict(data["cases"][0]))
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "cases.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "exactly one ordered A-G"):
                self.module.load_suite(path)

    def test_failure_taxonomy_separates_model_behavior_from_environment(self):
        data = json.loads(self.cases_path.read_text(encoding="utf-8"))
        self.assertEqual(
            {
                "instruction_delivery",
                "ambiguity",
                "tool_or_permission",
                "task_granularity",
                "runtime",
                "model_specific",
                "none",
            },
            set(data["failure_classes"]),
        )

    def test_runtime_baseline_does_not_claim_model_quality(self):
        data = json.loads(self.baseline_path.read_text(encoding="utf-8"))
        self.assertEqual("blocked", data["execution_status"])
        self.assertEqual("runtime", data["failure_class"])
        self.assertFalse(data["decision"]["add_model_specific_overlay"])
        for model in data["models"]:
            self.assertEqual([], model["cases_run"])
            self.assertIsNone(model["quality_result"])
            self.assertIsNone(model["efficiency_result"])
            self.assertIsNone(model["model_specific_finding"])

    def test_runner_does_not_reveal_grading_criteria_to_model(self):
        suite = self.module.load_suite(self.cases_path)
        prompt = self.module.build_prompt(suite, suite["cases"][0])
        self.assertIn(suite["cases"][0]["prompt"], prompt)
        for criterion in suite["cases"][0]["criteria"]:
            self.assertNotIn(criterion, prompt)

    def test_staged_workspace_excludes_grader_material(self):
        with tempfile.TemporaryDirectory() as directory:
            workspace = Path(directory) / "workspace"
            self.module.stage_workspace(self.root, workspace)
            for relative in self.module.GRADER_ONLY_PATHS:
                self.assertFalse(
                    (workspace / relative).exists(),
                    f"grader material leaked into workspace: {relative}",
                )
            self.assertTrue((workspace / "skills/software-development/SKILL.md").is_file())
            self.assertTrue((workspace / ".apm/instructions/skill-routing.instructions.md").is_file())

    def test_grader_material_is_removed_from_delivery_cache(self):
        with tempfile.TemporaryDirectory() as directory:
            cache = Path(directory) / "candidate"
            for relative in self.module.GRADER_ONLY_PATHS:
                target = cache / relative
                if target.suffix:
                    target.parent.mkdir(parents=True, exist_ok=True)
                    target.write_text("grader-only", encoding="utf-8")
                else:
                    target.mkdir(parents=True, exist_ok=True)
                    (target / "rubric.json").write_text("{}", encoding="utf-8")
            self.module.remove_grader_material(cache)
            for relative in self.module.GRADER_ONLY_PATHS:
                self.assertFalse((cache / relative).exists())

    def test_output_directory_must_be_outside_repository(self):
        with self.assertRaisesRegex(ValueError, "outside the repository"):
            self.module.resolve_output_dir(
                self.root / "evals/copilot-models/results/example",
                self.root,
            )
        with tempfile.TemporaryDirectory() as directory:
            result = self.module.resolve_output_dir(Path(directory) / "run", self.root)
            self.assertFalse(result.is_relative_to(self.root))

    def test_runner_enforces_subprocess_timeout(self):
        with self.assertRaises(subprocess.TimeoutExpired):
            self.module.run_command(
                [sys.executable, "-c", "import time; time.sleep(1)"],
                self.root,
                timeout=0.01,
            )

    def test_runner_dry_run_covers_full_matrix_without_copilot(self):
        result = subprocess.run(
            [
                sys.executable,
                "scripts/run_copilot_model_eval.py",
                "--dry-run",
                "--repeat",
                "3",
            ],
            cwd=self.root,
            check=False,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        self.assertEqual(0, result.returncode, result.stderr)
        data = json.loads(result.stdout)
        self.assertEqual(84, data["runs"])
        self.assertEqual(list("ABCDEFG"), data["cases"])
        self.assertEqual(4, len(data["models"]))
        self.assertEqual(3, data["repeat"])

    def test_guide_requires_isolation_and_no_unmeasured_claims(self):
        guide = self.guide_path.read_text(encoding="utf-8")
        self.assertIn("モデルごとに成功条件を変えない", guide)
        self.assertIn("未知を0へ変換しない", guide)
        self.assertIn("同じ失敗が同じモデルで複数回再現する", guide)
        self.assertIn("実機結果が得られるまでモデル固有overlayを追加しない", guide)
        self.assertIn("grader", guide)
        self.assertIn("clean checkout", guide)
        self.assertIn("COPILOT_GITHUB_TOKEN", guide)
        self.assertIn("repo外", guide)


if __name__ == "__main__":
    unittest.main()
