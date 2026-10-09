import pathlib
import unittest


class WorkflowShapeTests(unittest.TestCase):
    def test_approval_workflow_is_native_actions(self):
        workflow = pathlib.Path('.github/workflows/approve-codex-review.yml').read_text()
        self.assertNotIn('python', workflow.lower())
        self.assertIn('Withdraw approval while Codex review is running', workflow)
        self.assertIn('Approve current clean Codex evidence', workflow)


if __name__ == '__main__':
    unittest.main()
