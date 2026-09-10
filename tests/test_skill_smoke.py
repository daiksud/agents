from pathlib import Path
import tempfile
import unittest

from scripts.skill_smoke import validate_install


class InstallationTests(unittest.TestCase):
    def test_empty_source_is_not_a_successful_install(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.assertTrue(validate_install(root, root))

    def test_installed_content_and_missing_files(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source, target = root / 'source', root / 'target'
            for folder in (source / 'skills' / 'sample', target / 'sample'):
                folder.mkdir(parents=True)
                (folder / 'SKILL.md').write_text('---\nname: sample\ndescription: Example.\n---\n\n# Sample\n')
                (folder / 'asset.txt').write_text('expected')
            self.assertEqual([], validate_install(source, target))
            (target / 'sample' / 'asset.txt').unlink()
            self.assertTrue(validate_install(source, target))
            (target / 'sample' / 'asset.txt').write_text('corrupt')
            self.assertTrue(validate_install(source, target))
            (target / 'sample' / 'asset.txt').write_text('expected')
            skill = target / 'sample' / 'SKILL.md'
            original = skill.read_text()
            skill.write_text(original.replace('# Sample', '# Wrong'))
            self.assertTrue(validate_install(source, target))
            skill.write_text(original.replace('name: sample', 'name: other'))
            self.assertTrue(validate_install(source, target))
            skill.write_text(original.replace('name: sample', 'metadata:\n  local-path: source\nname: sample'))
            self.assertEqual([], validate_install(source, target))
