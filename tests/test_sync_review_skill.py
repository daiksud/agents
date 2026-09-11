"""Runtime copies must match exactly without distributing evaluation data."""
from pathlib import Path
import tempfile
import unittest

from scripts.sync_review_skill import synchronize


class ReviewSkillSyncTests(unittest.TestCase):
    def test_sync_and_check_runtime_tree(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source, target = root / 'source', root / 'target'
            source.mkdir()
            (source / 'SKILL.md').write_text('review instructions')
            (source / 'references').mkdir()
            (source / 'references/rules.md').write_text('evidence')
            (source / 'evals').mkdir()
            (source / 'evals/evals.json').write_text('{}')
            self.assertFalse(synchronize(source, target, check=True))
            self.assertFalse(target.exists(), 'check must not write')
            self.assertTrue(synchronize(source, target))
            self.assertTrue(synchronize(source, target, check=True))
            self.assertFalse((target / 'evals').exists())
            for change in ('different', 'missing', 'extra'):
                with self.subTest(change=change):
                    path = target / 'references/rules.md'
                    if change == 'different':
                        path.write_text('stale')
                    elif change == 'missing':
                        path.unlink()
                    else:
                        (target / 'unexpected.txt').write_text('stale')
                    self.assertFalse(synchronize(source, target, check=True))
                    self.assertTrue(synchronize(source, target))
                    self.assertTrue(synchronize(source, target, check=True))

    def test_missing_source_preserves_target(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            target = root / 'target'
            target.mkdir()
            (target / 'SKILL.md').write_text('keep')
            with self.assertRaises(ValueError):
                synchronize(root / 'missing', target)
            self.assertEqual((target / 'SKILL.md').read_text(), 'keep')
