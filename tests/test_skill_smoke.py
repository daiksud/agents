from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import subprocess

from scripts.skill_smoke import main, validate_install


class InstallationTests(unittest.TestCase):
    def test_listing_cannot_prompt_or_install_outside_temporary_directory(self):
        with patch('scripts.skill_smoke.subprocess.run') as run, patch(
                'scripts.skill_smoke.validate_install', return_value=[]):
            main()
        installs = [call for call in run.call_args_list if call.args[0][1:3] == ['skill', 'install']]
        self.assertEqual(3, len(installs))
        for call in installs:
            self.assertIn('--dir', call.args[0])
            self.assertEqual(subprocess.DEVNULL, call.kwargs.get('stdin'))
        listing = installs[0]
        self.assertEqual(subprocess.DEVNULL, listing.kwargs.get('stdin'))
        self.assertTrue(listing.kwargs.get('capture_output'))

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
