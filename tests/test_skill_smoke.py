from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import subprocess

from scripts.skill_smoke import main, validate_install, verify_upgrade


class InstallationTests(unittest.TestCase):
    def test_migration_fixture_is_independent_of_the_recovery_baseline(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / 'source'
            (source / '.github').mkdir(parents=True)
            (source / '.github/delivery.json').write_text('{"baseline_sha":"' + 'a' * 40 + '"}')
            with patch('scripts.skill_smoke.subprocess.check_output',
                       side_effect=RuntimeError('archive boundary')) as archive:
                with self.assertRaisesRegex(RuntimeError, 'archive boundary'):
                    verify_upgrade(source, root)
            self.assertEqual(['git', 'archive', '6e09d5166a8f49aa3a71edc102446d92a59e939d'],
                             archive.call_args.args[0])

    def test_retired_owned_skill_is_rejected_without_changing_other_files(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source, previous, target = root / 'source', root / 'previous', root / 'installed'
            legacy = '---\nname: retired\ndescription: Previous package skill.\n---\n# Retired\n'
            sample = '---\nname: sample\ndescription: Current package skill.\n---\n# Sample\n'
            for path, body in {
                    source / 'skills/sample/SKILL.md': sample,
                    previous / 'skills/sample/SKILL.md': sample,
                    previous / 'skills/retired/SKILL.md': legacy,
                    target / 'sample/SKILL.md': sample,
                    target / 'retired/SKILL.md': legacy,
                    target / 'unrelated/SKILL.md': 'Independent skill',
                    target / 'unrelated/notes.txt': 'local notes'}.items():
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(body)
            before = {p.relative_to(target): p.read_bytes() for p in target.rglob('*') if p.is_file()}
            self.assertEqual([], validate_install(source, target))
            errors = validate_install(source, target, previous_source=previous)
            after = {p.relative_to(target): p.read_bytes() for p in target.rglob('*') if p.is_file()}
            self.assertTrue(errors)
            self.assertEqual(before, after)
            backup = root / 'retired-backup'
            (target / 'retired').rename(backup)
            self.assertEqual([], validate_install(source, target, previous_source=previous))
            self.assertEqual(b'local notes', (target / 'unrelated/notes.txt').read_bytes())
            self.assertEqual(legacy, (backup / 'SKILL.md').read_text())

    def test_listing_cannot_prompt_or_install_outside_temporary_directory(self):
        with patch('scripts.skill_smoke.subprocess.run') as run, patch(
                'scripts.skill_smoke.validate_install', return_value=[]), patch(
                'scripts.skill_smoke.verify_upgrade') as upgrade:
            main()
        installs = [call for call in run.call_args_list if call.args[0][1:3] == ['skill', 'install']]
        self.assertEqual(3, len(installs))
        for call in installs:
            self.assertIn('--dir', call.args[0])
            self.assertEqual(subprocess.DEVNULL, call.kwargs.get('stdin'))
        listing = installs[0]
        self.assertEqual(subprocess.DEVNULL, listing.kwargs.get('stdin'))
        self.assertTrue(listing.kwargs.get('capture_output'))
        upgrade.assert_called_once()
        command = listing.args[0]
        self.assertEqual(upgrade.call_args.args[1], Path(command[command.index('--dir') + 1]).parent)

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
