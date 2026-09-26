from contextlib import contextmanager, redirect_stdout
import io
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import subprocess

from scripts.skill_smoke import SKILL_MIGRATION_BASELINE, main, validate_install, verify_upgrade


class InstallationTests(unittest.TestCase):
    @staticmethod
    @contextmanager
    def _upgrade_fixture(root, legacy_names, pruned=None, calls=None):
        def skill(name):
            return f'---\nname: {name}\ndescription: Sample.\n---\n# {name}\n'

        source = root / 'source'
        current = source / 'skills/sample/SKILL.md'
        current.parent.mkdir(parents=True)
        current.write_text(skill('sample'))

        def extract_previous(previous, *, filter):
            for name in legacy_names:
                path = previous / 'skills' / name / 'SKILL.md'
                path.parent.mkdir(parents=True)
                path.write_text(skill(name))

        def install(command, **kwargs):
            if calls is not None:
                calls.append((list(command), dict(kwargs)))
            target = root / 'upgraded'
            if '--force' in command:
                if pruned:
                    (target / pruned / 'SKILL.md').unlink()
                    (target / pruned).rmdir()
            else:
                for path in (root / 'previous-source/skills').glob('*/SKILL.md'):
                    installed = target / path.parent.name / 'SKILL.md'
                    installed.parent.mkdir(parents=True)
                    installed.write_bytes(path.read_bytes())
            return subprocess.CompletedProcess(command, 0)

        with patch('scripts.skill_smoke.subprocess.check_output', return_value=b''), patch(
                'scripts.skill_smoke.tarfile.open') as archive, patch(
                'scripts.skill_smoke.subprocess.run', side_effect=install):
            archive.return_value.__enter__.return_value.extractall.side_effect = extract_previous
            yield source

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

    def test_migration_fixture_requires_bdd_tdd_retirement(self):
        for legacy_names in (('sample',), ('sample', 'other')):
            with self.subTest(legacy_names=legacy_names), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                with self._upgrade_fixture(root, legacy_names) as source:
                    output = io.StringIO()
                    with redirect_stdout(output):
                        with self.assertRaisesRegex(RuntimeError, 'bdd-tdd'):
                            verify_upgrade(source, root)
                    self.assertNotIn('Upgrade from', output.getvalue())

    def test_migration_fixture_requires_task_workflow_retirement(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with self._upgrade_fixture(root, ('sample', 'bdd-tdd')) as source:
                output = io.StringIO()
                with redirect_stdout(output):
                    with self.assertRaisesRegex(RuntimeError, 'task-workflow'):
                        verify_upgrade(source, root)
                self.assertNotIn('Upgrade from', output.getvalue())

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with self._upgrade_fixture(root, ('sample', 'bdd-tdd', 'task-workflow')) as source:
                remaining = source / 'skills/task-workflow/SKILL.md'
                remaining.parent.mkdir()
                remaining.write_text('---\nname: task-workflow\ndescription: Old.\n---\n')
                output = io.StringIO()
                with redirect_stdout(output):
                    with self.assertRaisesRegex(RuntimeError, 'task-workflow'):
                        verify_upgrade(source, root)
                self.assertNotIn('Upgrade from', output.getvalue())

    def test_migration_fixture_requires_okf_docs_retirement(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with self._upgrade_fixture(root, ('sample', 'bdd-tdd', 'task-workflow')) as source:
                with self.assertRaisesRegex(RuntimeError, 'okf-docs'):
                    verify_upgrade(source, root)

    def test_upgrade_rejects_retired_skill_pruned_before_backup(self):
        cases = ((('sample', 'bdd-tdd', 'task-workflow', 'okf-docs'), 'bdd-tdd'),
                 (('sample', 'bdd-tdd', 'task-workflow', 'okf-docs'), 'task-workflow'),
                 (('sample', 'bdd-tdd', 'task-workflow', 'okf-docs'), 'okf-docs'),
                 (('sample', 'bdd-tdd', 'task-workflow', 'okf-docs', 'other'), 'other'))
        for legacy_names, pruned in cases:
            with self.subTest(pruned=pruned), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                with self._upgrade_fixture(root, legacy_names, pruned=pruned) as source:
                    output = io.StringIO()
                    with redirect_stdout(output):
                        with self.assertRaisesRegex(RuntimeError, pruned):
                            verify_upgrade(source, root)
                    self.assertNotIn('Upgrade from', output.getvalue())

    def test_upgrade_backs_up_all_retired_skills_and_preserves_other_owners(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            output = io.StringIO()
            with self._upgrade_fixture(root, ('sample', 'bdd-tdd', 'task-workflow', 'okf-docs', 'other')) as source:
                with redirect_stdout(output):
                    verify_upgrade(source, root)
            backup = root / 'retired-backup'
            moved = sorted(path.name for path in backup.iterdir())
            self.assertEqual(['bdd-tdd', 'okf-docs', 'other', 'task-workflow'], moved)
            for name in moved:
                original = root / 'previous-source/skills' / name / 'SKILL.md'
                self.assertEqual(original.read_bytes(), (backup / name / 'SKILL.md').read_bytes())
                self.assertFalse((root / 'upgraded' / name).exists())
            self.assertEqual(
                f'Upgrade from {SKILL_MIGRATION_BASELINE} verified; '
                f'retired skills outside discovery: {moved}\n', output.getvalue())
            self.assertEqual(b'---\nname: unrelated-fixture\n'
                             b'description: Preserve other owners.\n---\n',
                             (root / 'upgraded/unrelated-fixture/SKILL.md').read_bytes())

    def test_upgrade_install_calls_stay_isolated_and_noninteractive(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            calls = []
            with self._upgrade_fixture(root, ('sample', 'bdd-tdd', 'task-workflow', 'okf-docs'), calls=calls) as source:
                with redirect_stdout(io.StringIO()):
                    verify_upgrade(source, root)
            self.assertEqual(2, len(calls))
            for command, options in calls:
                self.assertEqual(['gh', 'skill', 'install'], command[:3])
                self.assertIn('--dir', command)
                self.assertEqual(str(root / 'upgraded'), command[command.index('--dir') + 1])
                self.assertEqual(subprocess.DEVNULL, options.get('stdin'))
                self.assertIs(True, options.get('check'))

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
