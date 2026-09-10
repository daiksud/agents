import json
from pathlib import Path
import tempfile
import unittest

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
        return validate_file(path)

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
