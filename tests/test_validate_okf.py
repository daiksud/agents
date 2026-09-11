import importlib.util
from pathlib import Path
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'skills/okf-docs/scripts/validate_okf.py'
spec = importlib.util.spec_from_file_location('validate_okf', SCRIPT)
okf = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = okf
spec.loader.exec_module(okf)


class ValidationTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)

    def write(self, name, text):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding='utf-8')
        return path

    def check(self, text, profile='conformance', name='concept.md', **kwargs):
        return okf.validate_file(self.write(name, text), self.root, profile, **kwargs)

    def errors(self, issues):
        return [item for item in issues if item.severity == 'error']

    def test_minimal_unknown_concept_and_authoring_requirements(self):
        text = '---\ntype: Future Type\nx-extension: {anything: [1, 2]}\n---\n'
        self.assertEqual([], self.errors(self.check(text)))
        issues = self.errors(self.check(text, 'authoring'))
        self.assertEqual({'title', 'description'}, {x.field for x in issues})
        self.assertTrue(all(x.rule == 'authoring' for x in issues))

    def test_frontmatter_structure(self):
        for text in ['# No YAML', '---\ntype: [bad\n---\n',
                     '---\n- item\n---\n', '---\ntype: 3\n---\n',
                     '---\ntype: "  "\n---\n']:
            with self.subTest(text=text):
                self.assertTrue(self.errors(self.check(text)))

    def test_reserved_files(self):
        for profile in ('conformance', 'authoring'):
            for name, text in [
                ('index.md', '---\nokf_version: "0.2"\n---\n# Group\n- [Next](next/) - Next\n'),
                ('nested/index.md', '# Group\n- [Other](https://example.com)\n'),
                ('log.md', '# History\n## 2026-09-11\n- Added.\n## 2026-09-10\n- Created.\n')]:
                with self.subTest(profile=profile, name=name):
                    self.assertEqual([], self.errors(self.check(text, profile, name)))
        for name, text in [
            ('nested/index.md', '---\nokf_version: "0.2"\n---\n# Group\n- [Next](next.md)\n'),
            ('index.md', '---\ntype: Concept\n---\n# Group\n- [Next](next.md)\n'),
            ('index.md', '# Group\nJust prose\n'),
            ('log.md', '# History\n## 2026-02-30\n- Bad date\n'),
            ('log.md', '# History\n## 2026-09-10\n- Old\n## 2026-09-11\n- New\n'),
            ('log.md', '# History\n## Yesterday\n- Not ISO\n'),
            ('log.md', '# History\n## 2026-09-11\nJust prose\n')]:
            with self.subTest(name=name, text=text):
                self.assertTrue(self.errors(self.check(text, name=name)))

    def test_examples_do_not_become_reserved_structure(self):
        text = '# History\n## 2026-09-11\n- Added.\n\n````md\n## 2000-99-99\n```\n````\n'
        self.assertEqual([], self.errors(self.check(text, name='log.md')))
        for text in ['```md\n# Group\n- [X](x.md)\n```\n',
                     '    # Group\n    - [X](x.md)\n']:
            self.assertTrue(self.errors(self.check(text, name='index.md')))
