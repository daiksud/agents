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
        self.write('next/placeholder.txt', '')
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

    def test_paths_and_computation_contract(self):
        self.write('references/run.py', '# not executed\n')
        self.write('references/query.sql', 'SELECT :year\n')
        self.write('nested/other.md', self.concept())
        extra = ('runtime: python\nparameters: [{name: year, type: integer, required: true}]\n'
                 'computation: /references/query.sql\n'
                 'executor: {resource: ../references/run.py, receipt: [result]}\n'
                 'attester: {resource: https://example.com/attester.py}\n')
        text = self.concept(extra, '[Other](./other.md) [External](https://example.com/missing)\n')
        text = text.replace('type: Reference', 'type: Attested Computation')
        self.assertEqual([], self.errors(self.check(text, 'authoring', 'nested/calc.md')))
        for bad in [text.replace('runtime: python\n', ''),
                    text.replace('required: true', 'required: yes-please'),
                    text.replace('parameters: [', 'parameters: [{name: year, type: string, required: false}, '),
                    text.replace('/references/query.sql', '/references/missing.sql'),
                    text.replace('../references/run.py', './missing.py'),
                    text.replace('./other.md', '/missing.md')]:
            with self.subTest(bad=bad):
                self.assertTrue(self.errors(self.check(bad, 'authoring', 'nested/calc.md')))
                self.assertEqual([], self.errors(self.check(bad, name='nested/calc.md')))

    def test_inline_computation_is_a_single_fence_and_not_execution(self):
        extra = ('runtime: python\nverified: {by: human:reader, at: 2026-09-11T00:00:00Z}\n')
        text = self.concept(extra, '# Computation\n```python\nraise RuntimeError("do not run")\n```\n')
        text = text.replace('type: Reference', 'type: Attested Computation')
        self.assertEqual([], self.errors(self.check(text, 'authoring')))
        for bad in [text.replace('# Computation', '# Example'),
                    text + '\n```python\nprint(2)\n```\n',
                    text.replace('runtime: python', 'runtime: python\ncomputation: https://example.com/code.py')]:
            self.assertTrue(self.errors(self.check(bad, 'authoring')))
        # Definition-only verification never becomes a per-run verdict.
        self.assertFalse(any('attestation succeeded' in x.message for x in self.check(text)))

    def test_links_in_examples_are_ignored_and_symlinks_not_followed(self):
        body = '[Missing](/missing.md)\n```md\n[Example](/also-missing.md)\n```\n'
        issues = self.errors(self.check(self.concept(body=body), 'authoring'))
        self.assertEqual(1, len(issues))
        self.assertEqual('links', issues[0].field)
        self.assertEqual([], self.errors(self.check(self.concept(body=body))))
        with tempfile.TemporaryDirectory() as outside:
            external = Path(outside) / 'target.md'
            external.write_text('secret-not-valid')
            (self.root / 'escape.md').symlink_to(external)
            issues = self.errors(self.check(self.concept(body='[Escape](escape.md)'), 'authoring'))
            self.assertTrue(issues)
            self.assertNotIn('secret-not-valid', str(issues))

    def cli(self, *args, no_site=False):
        import subprocess
        return subprocess.run([sys.executable, *(['-S'] if no_site else []), str(SCRIPT),
                               *map(str, args)], capture_output=True, text=True)

    def test_cli_exit_codes_and_diagnostics(self):
        self.write('concept.md', '---\ntype: Custom\n---\n')
        result = self.cli(self.root)
        self.assertEqual(0, result.returncode, result.stderr)
        result = self.cli(self.root, 'concept.md', '--profile', 'authoring')
        self.assertEqual(1, result.returncode)
        for detail in ('concept.md', 'title', 'authoring', 'nonempty'):
            self.assertIn(detail, result.stdout + result.stderr)
        for args in [(), (self.root, '--profile', 'unknown'),
                     (self.root, 'absent.md'), (self.root / 'absent',),
                     (self.root, '../escape.md'), (self.root, 'folder')]:
            self.assertEqual(2, self.cli(*args).returncode, str(args))
        result = self.cli(self.root, no_site=True)
        self.assertEqual(2, result.returncode)
        self.assertIn('PyYAML', result.stderr)
        self.assertNotIn('Traceback', result.stderr)

    def test_cli_selection_and_symlink_boundary(self):
        good = self.write('good.md', self.concept())
        self.write('invalid.md', 'invalid')
        self.assertEqual(0, self.cli(self.root, good).returncode)
        self.assertEqual(1, self.cli(self.root).returncode)
        (self.root / 'invalid.md').unlink()
        with tempfile.TemporaryDirectory() as outside:
            self.write('not-markdown.txt', 'anything')
            foreign = Path(outside) / 'secret.md'
            foreign.write_text('secret-invalid')
            (self.root / 'external').symlink_to(Path(outside), target_is_directory=True)
            (self.root / 'external.md').symlink_to(foreign)
            result = self.cli(self.root)
            self.assertEqual(0, result.returncode, result.stderr)
            self.assertNotIn('secret-invalid', result.stdout + result.stderr)
            self.assertEqual(2, self.cli(self.root, 'external.md').returncode)
            self.assertEqual(2, self.cli(self.root, 'external/secret.md').returncode)
        bad_utf8 = self.root / 'bad.md'
        bad_utf8.write_bytes(b'\xff')
        result = self.cli(self.root, 'bad.md')
        self.assertEqual(1, result.returncode)
        self.assertIn('UTF-8', result.stdout + result.stderr)

    def test_invalid_dates_are_document_errors_not_environment_failures(self):
        self.write('bad.md', self.concept('stale_after: 2026-13-30T00:00:00Z\n'))
        self.assertEqual(1, self.cli(self.root, '--profile', 'authoring').returncode)
        issues = self.errors(self.check(self.concept('resource: "https://[invalid"\n'), 'authoring'))
        self.assertTrue(issues)

    def test_scope_descriptors_are_not_paths_and_extensions_remain_opaque(self):
        text = self.concept('sources: [{resource: "all queries in BigQuery project X/Y"}]\n'
                            'x-future: {stale_after: not-a-date, verified: {custom: true}}\n')
        self.assertEqual([], self.errors(self.check(text, 'authoring')))

    def test_setext_index_headings_and_ordered_entries(self):
        self.write('other.md', self.concept())
        self.assertEqual([], self.errors(self.check('Group\n=====\n1. [Other](other.md)\n',
                                                    name='index.md')))

    def test_empty_or_unclosed_index_frontmatter_is_not_ignored(self):
        for text in ['---\r\nokf_version: "0.2"\r\n# Group\r\n- [X](x)\r\n',
                     '---\n---\n# Group\n- [X](x)\n']:
            self.assertTrue(self.errors(self.check(text, name='index.md')))

    def test_markdown_links_with_parentheses_and_reference_labels(self):
        self.write('version(2).md', self.concept())
        for body in ['[Version](version(2).md)\n',
                     '[Version][POLICY]\n\n[policy]: version(2).md\n',
                     '[Version](<version(2).md> "Title")\n']:
            self.assertEqual([], self.errors(self.check(self.concept(body=body), 'authoring')))
        self.assertTrue(self.errors(self.check(self.concept(body='[V][MISSING]\n\n[missing]: gone.md\n'), 'authoring')))

    def test_quoted_code_examples_and_html_comments_do_not_create_footnotes(self):
        body = ('A fact.\n\n> ```markdown\n> [^fake]\n> ```\n'
                '<!-- [^comment] -->\n')
        self.assertEqual([], self.errors(self.check(self.concept(body=body), 'authoring')))

    def test_cli_profile_may_precede_file_selection(self):
        self.write('good.md', self.concept())
        self.assertEqual(0, self.cli(self.root, '--profile', 'authoring', 'good.md').returncode)

    def test_authoring_rejects_concept_metadata_on_root_index(self):
        text = '---\nokf_version: "0.2"\ntitle: Not a concept\nx-extension: kept\n---\n# Group\n- [X](https://example.com)\n'
        self.assertEqual([], self.errors(self.check(text, name='index.md')))
        issues = self.errors(self.check(text, 'authoring', 'index.md'))
        self.assertEqual(['title'], [x.field for x in issues])
        self.assertEqual(['authoring'], [x.rule for x in issues])
        self.assertEqual([], self.errors(self.check(text.replace('title: Not a concept\n',''), 'authoring', 'index.md')))

    def test_historical_verification_warning_is_authoring_only(self):
        text = self.concept('generated: {by: writer/1, at: 2026-09-11T00:00:00Z}\n'
                            'verified: {by: human:reader, at: 2026-09-10T00:00:00Z}\n')
        self.assertEqual([], self.check(text))
        warnings = self.check(text, 'authoring')
        self.assertEqual(['verified'], [x.field for x in warnings])
        self.assertTrue(all(x.rule == 'authoring' and x.severity == 'warning' for x in warnings))

    def test_invalid_http_authority_and_nul_paths_are_document_errors(self):
        for value in ['https://', 'https:///missing', 'https://user@', 'https://bad host/path']:
            for extra in [f'resource: "{value}"\n',f'sources: [{{resource: "{value}"}}]\n']:
                self.write('bad.md', self.concept(extra))
                self.assertEqual(1, self.cli(self.root, '--profile', 'authoring').returncode, value)
                self.assertEqual(0, self.cli(self.root).returncode)
        self.write('bad.md', self.concept(body='[Reference](%00)\n'))
        self.assertEqual(1, self.cli(self.root, '--profile', 'authoring').returncode)

    def test_empty_inline_computation_is_not_a_definition(self):
        for content in ['', '  \n\t\n']:
            text = self.concept('runtime: python\n', '# Computation\n```python\n'+content+'\n```\n')
            text = text.replace('type: Reference', 'type: Attested Computation')
            self.assertTrue(self.errors(self.check(text, 'authoring')))
            self.assertEqual([], self.errors(self.check(text)))

    def test_cli_uses_one_time_for_all_documents(self):
        from datetime import datetime, timezone
        from unittest.mock import patch
        from contextlib import redirect_stdout
        import io
        first = datetime(2026, 9, 22, 23, 59, 59, tzinfo=timezone.utc)
        second = datetime(2026, 9, 23, tzinfo=timezone.utc)
        for name in ['a.md', 'b.md']:
            self.write(name, self.concept('stale_after: "2026-09-23T00:00:00Z"\n'))
        class Clock(datetime):
            calls = 0
            @classmethod
            def now(cls, tz=None):
                cls.calls += 1
                return first if cls.calls == 1 else second
        output = io.StringIO()
        with patch.object(okf, 'datetime', Clock), redirect_stdout(output):
            self.assertEqual(0, okf.main([str(self.root)]))
        self.assertEqual(1, Clock.calls)
        self.assertNotIn('stale_after', output.getvalue())

    def test_unrelated_example_does_not_change_computation_fence_state(self):
        body = '# Computation\n```python\nprint(1)\n```\n# Examples\n```text\nExample continues to EOF\n'
        text = self.concept('runtime: python\n', body).replace('type: Reference','type: Attested Computation')
        self.assertEqual([], self.errors(self.check(text, 'authoring')))

    def test_nested_list_links_are_not_indented_code(self):
        for body in ['- Parent\n    - [Child](missing.md)\n',
                     'Paragraph\n    continuation [Child](missing.md)\n']:
            self.assertTrue(self.errors(self.check(self.concept(body=body), 'authoring')))
        for body in ['- Parent\n\n      [Code](missing.md)\n',
                     '> ```md\n> [Code](missing.md)\n> ```\n']:
            self.assertEqual([], self.errors(self.check(self.concept(body=body), 'authoring')))

    def test_escaped_and_nested_link_labels(self):
        for label in [r'a\]b', 'a [nested] label']:
            self.assertTrue(self.errors(self.check(self.concept(body=f'[{label}](missing.md)\n'), 'authoring')))
        self.write('real.md', self.concept())
        self.assertEqual([], self.errors(self.check(self.concept(body=r'[a\]b](real.md)'), 'authoring')))

    def test_computation_local_reference_must_be_a_file(self):
        (self.root / 'refs').mkdir()
        text = self.concept('runtime: python\ncomputation: refs/\n').replace('type: Reference','type: Attested Computation')
        self.assertTrue(self.errors(self.check(text, 'authoring')))
        self.assertEqual([], self.errors(self.check(text)))

    def test_yaml_duplicate_keys_are_errors_but_merge_overrides_are_valid(self):
        for text in ['---\ntype: Wrong\ntype: Guide\n---\n',
                     self.concept('x-extension: {key: first, key: second}\n')]:
            for profile in ['conformance', 'authoring']:
                self.assertTrue(self.errors(self.check(text, profile)))
        text = self.concept('x-base: &base {key: first}\nx-extension: {<<: *base, key: override}\n')
        self.assertEqual([], self.errors(self.check(text, 'authoring')))

    def test_optional_datetimes_are_not_validated_by_yaml_resolution(self):
        text = self.concept('stale_after: 2026-13-30T00:00:00Z\n')
        self.assertEqual([], self.errors(self.check(text)))
        self.assertTrue(self.errors(self.check(text, 'authoring')))
        opaque = self.concept('x-extension: {date: 2026-13-30T00:00:00Z}\n')
        self.assertEqual([], self.errors(self.check(opaque, 'authoring')))

    def test_fence_on_list_marker_line_masks_its_contents(self):
        body = '- ```markdown\n  [Example](missing.md)\n  [^fake]\n  ```\n'
        self.assertEqual([], self.errors(self.check(self.concept(body=body), 'authoring')))

    def test_index_uses_the_shared_escaped_label_parser(self):
        self.write('page.md', self.concept())
        text = '# Group\n- [a\\]b](page.md)\n'
        for profile in ('conformance', 'authoring'):
            self.assertEqual([], self.errors(self.check(text, profile, 'index.md')))

    def test_reference_definition_target_can_be_on_next_line(self):
        self.write('page.md', self.concept())
        body = '[Page][target]\n\n[target]:\n  page.md\n'
        self.assertEqual([], self.errors(self.check(self.concept(body=body), 'authoring')))
        self.assertTrue(self.errors(self.check(self.concept(body=body.replace('page.md','missing.md')), 'authoring')))

    def test_malformed_verification_does_not_suppress_unverified_warning(self):
        for value in ['garbage', '[null]', '{x: y}', '{by: human:reader}']:
            issues = self.check(self.concept(f'verified: {value}\n'))
            self.assertEqual([], self.errors(issues))
            self.assertTrue(any(x.field=='verified' and x.severity=='warning' for x in issues))

    def test_comments_do_not_count_as_reserved_file_structure(self):
        for name, body in [('index.md', '# Group\n- [Page](page.md)\n'),
                           ('log.md', '# Log\n## 2026-09-11\n- Created\n')]:
            self.assertTrue(self.errors(self.check('<!--\n'+body+'-->\n', name=name)))

    def test_computation_ignores_comments_but_preserves_comment_text_in_code(self):
        code = '# Computation\n```python\nprint("<!--")\n```\n'
        text = self.concept('runtime: python\n', code).replace('type: Reference','type: Attested Computation')
        self.assertEqual([], self.errors(self.check(text, 'authoring')))
        hidden = self.concept('runtime: python\n', '<!--\n'+code+'-->\n').replace('type: Reference','type: Attested Computation')
        self.assertTrue(self.errors(self.check(hidden, 'authoring')))

    def test_links_respect_escaped_image_markers_and_first_reference_definition(self):
        self.write('real.md', self.concept())
        with self.subTest(marker='escaped'):
            self.assertTrue(self.errors(self.check(self.concept(body=r'\![X](missing.md)'), 'authoring')))
        self.assertEqual([], self.errors(self.check(self.concept(body=r'![X](missing.md)'), 'authoring')))
        for first, second, broken in [('missing.md', 'real.md', True), ('real.md', 'missing.md', False)]:
            body = f'[X][ref]\n\n[REF]: {first}\n[ref]: {second}\n'
            with self.subTest(first=first):
                self.assertEqual(broken, bool(self.errors(self.check(self.concept(body=body), 'authoring'))))
