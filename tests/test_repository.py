import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from scripts.check_repository import validate_file


class MetadataTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def check(self, relative, text):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding='utf-8')
        return validate_file(path, self.root)

    def test_reserved_files_use_bundle_root_and_have_no_concept_metadata(self):
        self.check('docs/page.md', '---\ntype: Guide\ntitle: Page\ndescription: Page.\n---\n')
        self.assertEqual([], self.check('docs/index.md', '# Documents\n\n- [Page](page.md)\n'))
        self.assertEqual([], self.check('docs/log.md', '## 2026-09-12\n\n- Added page.\n'))
        self.assertTrue(self.check('docs/log.md', '## 2026-02-30\n\n- Invalid date.\n'))
        self.assertTrue(self.check('index.md', '---\nokf_version: 2\n---\n# Docs\n\n- [Page](docs/page.md)\n'))
        self.assertEqual([], self.check('index.md', '---\nokf_version: "0.2"\n---\n# Docs\n\n- [Page](docs/page.md)\n'))

    def test_generated_skill_copy_and_unrelated_formats(self):
        self.assertTrue(self.check('.github/skills/sample/references/help.md', '# Missing metadata'))
        self.assertEqual([], self.check('.github/ISSUE_TEMPLATE/bug.md', '# Bug report\n'))
        self.assertEqual([], self.check('AGENTS.md', '# Generated instructions\n'))

    def test_repository_selection_does_not_follow_symlinks(self):
        from scripts.check_repository import repository_paths
        with tempfile.TemporaryDirectory() as outside:
            target = Path(outside) / 'secret.md'
            target.write_text('Do not scan this file.')
            (self.root / 'linked.md').symlink_to(target)
            (self.root / 'linked-dir').symlink_to(outside, target_is_directory=True)
            self.check('docs/page.md', '---\ntype: Guide\ntitle: Page\ndescription: Page.\n---\n')
            self.assertEqual([self.root / 'docs/page.md'], repository_paths(self.root, [
                'linked.md', 'linked-dir/secret.md', 'docs/page.md', 'docs/page.md', '']))

    def test_authoring_checks_known_metadata_and_preserves_unknown_extensions(self):
        valid = '---\ntype: Custom\ntitle: Page\ndescription: Page.\nx-extra: [anything]\n---\n'
        self.assertEqual([], self.check('docs/page.md', valid))
        self.assertTrue(self.check('docs/page.md', valid.replace('x-extra: [anything]', 'tags: 12')))
        self.assertTrue(self.check('docs/page.md', valid.replace('x-extra: [anything]', 'verified: 12')))
        self.assertTrue(self.check('docs/page.md', '---\ntype: Custom\n---\n'))

    def test_authoring_resolves_links_across_repository_directories(self):
        valid = '---\ntype: Guide\ntitle: Page\ndescription: Page.\n---\n'
        self.check('skills/sample/references/help.md', valid)
        for link in ['../skills/sample/references/help.md', '/skills/sample/references/help.md']:
            self.assertEqual([], self.check('docs/page.md', valid + f'[Help]({link})\n'))
        self.assertTrue(self.check('docs/page.md', valid + '[Missing](missing.md)\n'))

    def test_yaml_and_json_syntax(self):
        for path, text in [('apm.yml', 'name: [broken'), ('x.json', '{')]:
            with self.subTest(path=path):
                self.assertTrue(self.check(path, text))
        self.assertEqual([], self.check('apm.yml', 'name: agents\n'))

    def test_skill_identity_and_required_metadata(self):
        valid = '---\nname: sample\ndescription: Review changes.\n---\n# Sample\n'
        self.assertEqual([], self.check('skills/sample/SKILL.md', valid))
        for text in [valid.replace('name: sample', 'name: other'),
                     valid.replace('description: Review changes.', 'description: 5'),
                     valid.replace('name: sample', 'name: bad--name'), '# Missing metadata']:
            with self.subTest(text=text):
                self.assertTrue(self.check('skills/sample/SKILL.md', text))

    def test_okf_and_readme(self):
        valid = '---\ntype: Guide\ntitle: Setup\ndescription: Install.\n---\n## Setup\n'
        self.assertEqual([], self.check('docs/guides/setup.md', valid))
        self.assertTrue(self.check('docs/guides/setup.md', valid.replace('title: Setup', 'title: []')))
        self.assertTrue(self.check('skills/sample/references/help.md', '# Missing metadata'))
        self.assertEqual([], self.check('README.md', '# Repository\n'))
        with patch('scripts.check_repository.ROOT', self.root):
            self.assertEqual([], validate_file(Path('README.md')))

    def test_computation_markdown_preserves_required_heading(self):
        from scripts.check_repository import check_markdown
        common = Path(__file__).resolve().parents[1] / 'skills/task-workflow/assets/rumdl.toml'
        (self.root / '.rumdl.toml').write_text(f'extends = "{common}"\n')
        valid = ('---\ntype: Attested Computation\ntitle: Example\n'
                 'description: Example contract.\nruntime: python\n---\n\n'
                 '# Computation\n\n```python\nprint(1)\n```\n')
        path = self.root / 'docs/calculation.md'
        for text, metadata_ok, markdown_ok in [
                (valid, True, True),
                (valid.replace('# Computation', '## Computation'), False, True),
                (valid + '\n# Another title\n', True, False),
                (valid.replace('Attested Computation', 'Guide'), True, False)]:
            with self.subTest(text=text):
                errors = self.check('docs/calculation.md', text)
                self.assertEqual(metadata_ok, not errors)
                self.assertEqual(markdown_ok, check_markdown(self.root, [path]) == 0)

    def test_external_computation_keeps_normal_title_check(self):
        from scripts.check_repository import check_markdown
        common = Path(__file__).resolve().parents[1] / 'skills/task-workflow/assets/rumdl.toml'
        (self.root / '.rumdl.toml').write_text(f'extends = "{common}"\n')
        (self.root / 'formula.py').write_text('print(1)\n')
        text = ('---\ntype: Attested Computation\ntitle: Example\n'
                'description: Example contract.\nruntime: python\n'
                'computation: ../formula.py\n---\n\n# Notes\n\nA separate definition.\n')
        self.assertEqual([], self.check('docs/external.md', text))
        self.assertNotEqual(0, check_markdown(self.root, [self.root / 'docs/external.md']))
        self.assertEqual([], self.check('docs/external.md', text.replace('# Notes', '## Notes')))
        self.assertEqual(0, check_markdown(self.root, [self.root / 'docs/external.md']))

    def test_eval_contract(self):
        data = {'skill_name': 'sample', 'evals': [
            {'id': 1, 'prompt': 'Review.', 'expected_output': 'Find defect.', 'files': []}]}
        path = 'skills/sample/evals/evals.json'
        self.assertEqual([], self.check(path, json.dumps(data)))
        for field, value in [('id', True), ('prompt', ''), ('expected_output', None), ('files', [5])]:
            bad = json.loads(json.dumps(data))
            bad['evals'][0][field] = value
            with self.subTest(field=field):
                self.assertTrue(self.check(path, json.dumps(bad)))
        data['evals'].append(data['evals'][0].copy())
        self.assertTrue(self.check(path, json.dumps(data)))
        self.assertTrue(self.check(path, '{"skill_name":"other","evals":[]}'))
        self.assertTrue(self.check(path, '[]'))


if __name__ == '__main__':
    unittest.main()
