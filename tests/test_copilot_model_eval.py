import json
import subprocess
import sys
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

    def test_guide_requires_same_criteria_and_no_unmeasured_claims(self):
        guide = self.guide_path.read_text(encoding="utf-8")
        self.assertIn("モデルごとに成功条件を変えない", guide)
        self.assertIn("未知を0へ変換しない", guide)
        self.assertIn("同じ失敗が同じモデルで複数回再現する", guide)
        self.assertIn("実機結果が得られるまでモデル固有overlayを追加しない", guide)


if __name__ == "__main__":
    unittest.main()
