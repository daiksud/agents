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

    def test_suite_rejects_duplicate_model_ids(self):
        data = json.loads(self.cases_path.read_text(encoding="utf-8"))
        data["models"][1]["cli_model"] = data["models"][0]["cli_model"]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "cases.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "ordered baseline model set"):
                self.module.load_suite(path)

    def test_suite_rejects_empty_prompt_and_missing_criteria(self):
        data = json.loads(self.cases_path.read_text(encoding="utf-8"))
        data["cases"][0]["prompt"] = ""
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "cases.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "case prompt"):
                self.module.load_suite(path)

        data = json.loads(self.cases_path.read_text(encoding="utf-8"))
        del data["cases"][0]["criteria"]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "cases.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "case criteria"):
                self.module.load_suite(path)

    def test_suite_rejects_missing_or_empty_case_fields(self):
        data = json.loads(self.cases_path.read_text(encoding="utf-8"))
        data["cases"][0]["prompt"] = "   "
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "cases.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "non-empty prompt"):
                self.module.load_suite(path)

        data = json.loads(self.cases_path.read_text(encoding="utf-8"))
        del data["cases"][0]["criteria"]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "cases.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "non-empty criteria"):
                self.module.load_suite(path)

    def test_suite_rejects_missing_or_empty_model_fields(self):
        data = json.loads(self.cases_path.read_text(encoding="utf-8"))
        data["models"][0]["name"] = ""
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "cases.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "non-empty name and cli_model"):
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
            self.assertEqual([], list((workspace / "skills").glob("*/evals")))

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
            skill_evals = cache / ".agents/skills/example/evals"
            skill_evals.mkdir(parents=True)
            (skill_evals / "evals.json").write_text("{}", encoding="utf-8")
            self.module.remove_grader_material(cache)
            self.module.remove_skill_evals(cache)
            for relative in self.module.GRADER_ONLY_PATHS:
                self.assertFalse((cache / relative).exists())
            self.assertFalse(skill_evals.exists())

    def test_selected_in_repo_suite_path_is_removed_from_workspace(self):
        with tempfile.TemporaryDirectory() as directory:
            workspace = Path(directory) / "workspace"
            self.module.stage_workspace(
                self.root,
                workspace,
                extra_grader_paths=(Path("README.md"),),
            )
            self.assertFalse((workspace / "README.md").exists())

    def test_custom_suite_is_removed_from_installed_skill_tree(self):
        with tempfile.TemporaryDirectory() as directory:
            home = Path(directory)
            relative = Path("skills/example/references/custom-cases.json")
            deployed = home / ".agents" / relative
            deployed.parent.mkdir(parents=True)
            deployed.write_text("grader-only", encoding="utf-8")
            self.module.remove_deployed_grader_material(home, (relative,))
            self.assertFalse(deployed.exists())

    def test_manifest_writer_uses_atomic_replace_without_temp_residue(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "manifest.json"
            self.module.write_manifest(path, {"planned_runs": [1, 2, 3]})
            self.assertEqual(
                {"planned_runs": [1, 2, 3]},
                json.loads(path.read_text(encoding="utf-8")),
            )
            self.assertFalse((path.parent / ".manifest.json.tmp").exists())

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

    def test_runner_dry_run_covers_full_matrix_without_optional_packages(self):
        result = subprocess.run(
            [
                sys.executable,
                "-S",
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

    def test_cli_rejects_external_suite_and_empty_model_selection(self):
        with tempfile.TemporaryDirectory() as directory:
            external = Path(directory) / "cases.json"
            external.write_text(self.cases_path.read_text(encoding="utf-8"), encoding="utf-8")
            external_result = subprocess.run(
                [
                    sys.executable,
                    "scripts/run_copilot_model_eval.py",
                    "--dry-run",
                    "--cases",
                    str(external),
                ],
                cwd=self.root,
                check=False,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            self.assertEqual(2, external_result.returncode)
            self.assertIn("inside the repository", external_result.stderr)

        empty_models = subprocess.run(
            [
                sys.executable,
                "scripts/run_copilot_model_eval.py",
                "--dry-run",
                "--models",
                ",",
            ],
            cwd=self.root,
            check=False,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        self.assertEqual(2, empty_models.returncode)
        self.assertIn("at least one model id", empty_models.stderr)

    def test_preflight_failure_preserves_planned_matrix(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "run"
            environment = {"PATH": ""}
            result = subprocess.run(
                [
                    sys.executable,
                    "scripts/run_copilot_model_eval.py",
                    "--repeat",
                    "2",
                    "--output-dir",
                    str(output),
                ],
                cwd=self.root,
                env=environment,
                check=False,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            self.assertEqual(2, result.returncode)
            manifest = json.loads(
                (output / "manifest.json").read_text(encoding="utf-8")
            )
            self.assertEqual(4, len(manifest["selected_models"]))
            self.assertEqual(56, len(manifest["planned_runs"]))
            self.assertEqual("failed", manifest["setup"]["status"])
            self.assertEqual("runtime", manifest["setup"]["failure_class"])

    def test_runner_rejects_empty_explicit_model_selection(self):
        result = subprocess.run(
            [
                sys.executable,
                "-S",
                "scripts/run_copilot_model_eval.py",
                "--dry-run",
                "--models",
                ",",
            ],
            cwd=self.root,
            check=False,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        self.assertEqual(2, result.returncode)
        self.assertIn("at least one model", result.stderr)

    def test_external_suite_is_preserved_before_preflight_failure(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            external_suite = base / "external-cases.json"
            external_suite.write_bytes(self.cases_path.read_bytes())
            output = base / "run"
            result = subprocess.run(
                [
                    sys.executable,
                    "scripts/run_copilot_model_eval.py",
                    "--cases",
                    str(external_suite),
                    "--output-dir",
                    str(output),
                ],
                cwd=self.root,
                env={"PATH": ""},
                check=False,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            self.assertEqual(2, result.returncode)
            self.assertEqual(
                external_suite.read_bytes(),
                (output / "suite.json").read_bytes(),
            )
            manifest = json.loads(
                (output / "manifest.json").read_text(encoding="utf-8")
            )
            self.assertEqual("suite.json", manifest["suite_snapshot"])
            self.assertEqual(28, len(manifest["planned_runs"]))

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
