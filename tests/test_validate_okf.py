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

    def concept(self, extra='', body='A fact.\n'):
        return '---\ntype: Reference\ntitle: Fact\ndescription: A fact.\n' + extra + '---\n' + body

    def test_sources_and_footnotes_are_keyed_not_positional(self):
        sources = ('sources:\n  - {id: alpha, resource: "https://example.com/a"}\n'
                   '  - {id: beta, resource: "all queries in project X"}\n')
        body = 'A.[^alpha] B.[^beta]\n\n[^alpha]: First\n[^beta]: Second\n'
        text = self.concept(sources, body)
        self.assertEqual([], self.errors(self.check(text, 'authoring')))
        reordered = text.replace('  - {id: alpha, resource: "https://example.com/a"}\n'
                                '  - {id: beta, resource: "all queries in project X"}',
                                '  - {id: beta, resource: "all queries in project X"}\n'
                                '  - {id: alpha, resource: "https://example.com/a"}')
        self.assertEqual([], self.errors(self.check(reordered, 'authoring')))
        for bad in [text.replace('id: beta', 'id: alpha'),
                    text.replace('resource: "https://example.com/a"', 'title: Missing'),
                    text.replace('A.[^alpha]', 'A.[^missing]'),
                    text.replace('[^alpha]: First\n', ''),
                    text + '[^alpha]: Duplicate\n']:
            with self.subTest(bad=bad):
                self.assertTrue(self.errors(self.check(bad, 'authoring')))
                self.assertEqual([], self.errors(self.check(bad)))

    def test_examples_and_ordinary_footnotes(self):
        body = ('A footnote.[^note]\n\n[^note]: An explanation, not an external claim.\n'
                '````md\nExample.[^missing]\n[^fake]: Example\n```\n````\n'
                '`[^inline]` and \\[^escaped].\n    [^indented]: Code\n')
        self.assertEqual([], self.errors(self.check(self.concept(body=body), 'authoring')))
        self.assertTrue(self.errors(self.check(self.concept(body='Fact.[^missing]\n'), 'authoring')))

    def test_known_metadata_formats_and_optional_families(self):
        valid = ('tags: [finance]\nstatus: stable\n'
                 'generated: {by: writer/1, at: 2026-06-30T14:00:00Z}\n'
                 'verified: {by: process:nightly, at: "2026-07-01T23:00:00+09:00"}\n'
                 'sources:\n  - resource: all queries in project X\n'
                 '    author: team:finance\n    usage_count: 0\n'
                 '    last_modified: 2026-06-01T00:00:00Z\n'
                 'usage_window: {from: 2026-06-01T00:00:00Z, to: 2026-07-01T00:00:00Z}\n')
        self.assertEqual([], self.errors(self.check(self.concept(valid), 'authoring')))
        for bad in ['tags: text\n', 'status: unknown\n', 'generated: {}\n',
                    'verified: [{by: human:reader}]\n',
                    'verified: {by: reader, at: 2026-07-01T00:00:00Z}\n',
                    'generated: {by: writer/1, at: 2026-06-30T14:00:00}\n',
                    'stale_after: 2026-09-23\n', 'sources: {}\n',
                    'sources: [{resource: scope, usage_count: true}]\n',
                    'usage_window: {from: 2026-07-01T00:00:00Z, to: 2026-06-01T00:00:00Z}\n']:
            with self.subTest(bad=bad):
                self.assertTrue(self.errors(self.check(self.concept(bad), 'authoring')))
                self.assertEqual([], self.errors(self.check(self.concept(bad))))

    def test_stale_boundary_verifier_mapping_and_read_only(self):
        from datetime import datetime, timezone
        now = datetime(2026, 9, 23, tzinfo=timezone.utc)
        text = self.concept('stale_after: 2026-09-23T00:00:00Z\n'
                            'verified: {by: human:reader, at: 2026-09-22T00:00:00Z}\n'
                            'x-history: [{opaque: keep}]\n')
        path = self.write('concept.md', text)
        for profile in ('conformance', 'authoring'):
            issues = okf.validate_file(path, self.root, profile, now=now)
            self.assertEqual([], self.errors(issues))
            self.assertIn('stale_after', [x.field for x in issues])
            self.assertTrue(all(x.severity == 'warning' for x in issues))
        self.assertEqual(text, path.read_text())
        before = now.replace(day=22)
        self.assertEqual([], self.check(text, now=before))
        as_list = text.replace('verified: {', 'verified:\n  - {')
        self.assertEqual(self.check(text, now=now), self.check(as_list, now=now))
        self.assertIn('verified', [x.field for x in self.check(self.concept(), now=now)])
