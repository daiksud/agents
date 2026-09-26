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
        common = Path(__file__).resolve().parents[1] / 'skills/issue-management/assets/rumdl.toml'
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
        common = Path(__file__).resolve().parents[1] / 'skills/issue-management/assets/rumdl.toml'
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

    def test_workflow_eval_split_preserves_legacy_case_lineage(self):
        root = Path(__file__).resolve().parents[1]
        migrated = []
        for skill in ('issue-management', 'change-delivery'):
            path = root / 'skills' / skill / 'evals' / 'evals.json'
            self.assertTrue(path.is_file(), f'{skill} evals must exist')
            data = json.loads(path.read_text(encoding='utf-8'))
            self.assertEqual(skill, data['skill_name'])
            legacy = [case for case in data['evals'] if 'source_id' in case]
            self.assertEqual(69, len(legacy))
            for case in legacy:
                self.assertEqual(f'task-workflow/{case["id"]}', case['source_id'])
            migrated.extend(case['source_id'] for case in legacy)
        self.assertCountEqual(
            [f'task-workflow/{number}' for number in range(1, 139)], migrated)

    def test_change_delivery_has_installable_skill_entry(self):
        root = Path(__file__).resolve().parents[1]
        skill = root / 'skills/change-delivery/SKILL.md'
        self.assertTrue(skill.is_file(), 'change-delivery needs an installable SKILL.md')
        self.assertEqual([], validate_file(skill, root))

    def test_reviewer_candidate_routes_to_issue_management(self):
        root = Path(__file__).resolve().parents[1]
        reviewer = (root / 'skills/code-review/SKILL.md').read_text(encoding='utf-8')
        decision = (root / '.apm/instructions/decision-making.instructions.md').read_text(encoding='utf-8')
        routing = (root / '.apm/instructions/skill-routing.instructions.md').read_text(encoding='utf-8')
        candidate_exception = next(line for line in routing.splitlines()
                                   if '相談・比較・説明・読み取り調査' in line)
        self.assertIn('`issue-management`', reviewer)
        self.assertNotIn('`task-workflow`', reviewer)
        self.assertIn('`issue-management`', decision)
        self.assertNotIn('`task-workflow`', decision)
        self.assertIn('`issue-management`', candidate_exception)
        self.assertIn('投稿しない', candidate_exception)

    def test_issue_only_route_does_not_select_delivery(self):
        root = Path(__file__).resolve().parents[1]
        routing = (root / '.apm/instructions/skill-routing.instructions.md').read_text(encoding='utf-8')
        rows = [line for line in routing.splitlines() if line.startswith('| ')]
        issue_rows = [line for line in rows
                      if '`~/.agents/skills/issue-management/SKILL.md`' in line]
        self.assertEqual(1, len(issue_rows))
        self.assertIn('Issueの検索・作成・更新', issue_rows[0])
        self.assertIn('計画', issue_rows[0])
        self.assertIn('共通スタンダード候補', issue_rows[0])
        delivery_route = next(line for line in rows if 'リポジトリの変更・成果物作成' in line)
        self.assertNotIn('Issue・PRの作成・更新', delivery_route)
        self.assertNotIn('Issueの検索・作成・更新', delivery_route)
        self.assertNotIn('Issue計画の保存', delivery_route)
        self.assertIn('PR', delivery_route)
        self.assertIn('`~/.agents/skills/change-delivery/SKILL.md`', delivery_route)
        self.assertNotIn('`~/.agents/skills/task-workflow/SKILL.md`', delivery_route)

    def test_approved_change_common_instructions_use_split_skills(self):
        root = Path(__file__).resolve().parents[1]
        routing = (root / '.apm/instructions/skill-routing.instructions.md').read_text(encoding='utf-8')
        review_only = next(line for line in routing.splitlines() if 'レビューだけの依頼' in line)
        self.assertIn('`change-delivery`', review_only)
        self.assertNotIn('`task-workflow`', review_only)

        safety = (root / '.apm/instructions/change-safety.instructions.md').read_text(encoding='utf-8')
        safety_sentences = safety.split('。')
        issue_scope = next(sentence for sentence in safety_sentences if 'Issue計画の記録' in sentence)
        branch_scope = next(sentence for sentence in safety_sentences if 'ブランチ保護' in sentence)
        self.assertIn('`issue-management`', issue_scope)
        self.assertNotIn('`change-delivery`', issue_scope)
        self.assertIn('`change-delivery`', branch_scope)
        self.assertNotIn('`issue-management`', branch_scope)
        self.assertNotIn('`task-workflow`', safety)

        delivery = (root / '.apm/instructions/delivery.instructions.md').read_text(encoding='utf-8')
        delivery_sentences = delivery.split('。')
        fallback = next(sentence for sentence in delivery_sentences if '代替レビュー' in sentence)
        recovery = next(sentence for sentence in delivery_sentences if '復旧の実行範囲' in sentence)
        checks = next(sentence for sentence in delivery_sentences if '必要チェックと復旧変更' in sentence)
        self.assertIn('`change-delivery`', fallback)
        self.assertIn('`issue-management`', recovery)
        self.assertNotIn('`change-delivery`', recovery)
        self.assertIn('`change-delivery`', checks)
        self.assertNotIn('`issue-management`', checks)
        self.assertNotIn('`task-workflow`', delivery)

    def test_assessment_diagnosis_stops_before_approved_delivery(self):
        root = Path(__file__).resolve().parents[1]
        skill = (root / 'skills/engineering-assessment/SKILL.md').read_text(encoding='utf-8')
        guide = (root / 'skills/engineering-assessment/references/assessment.md').read_text(encoding='utf-8')
        issue_path = root / 'skills/issue-management/references/issue-recording.md'
        self.assertIn('### 診断・計画専用のIssue記録', issue_path.read_text(encoding='utf-8'))
        self.assertIn(
            '[診断・計画専用経路](../issue-management/references/issue-recording.md#診断計画専用のissue記録)',
            skill)
        self.assertIn('`issue-management`', skill.split('## 範囲と参照資料')[0])
        self.assertIn('保存・再取得・表示確認とURL・本文の提示で終了', skill)
        self.assertIn('投稿禁止・保存不能・未確認なら未保存案', skill)
        self.assertIn('main失敗も証拠と復旧優先度を計画に記録するだけ', skill)
        self.assertIn('`issue-management` を利用できなければIssueへ投稿せず', skill)
        self.assertIn('`change-delivery` を利用できなければ実装を開始せず', skill)
        handoff = next(sentence for sentence in skill.split('。') if '実装を依頼されたら' in sentence)
        self.assertIn('`issue-management`', handoff)
        self.assertIn('`change-delivery`', handoff)
        self.assertNotIn('`task-workflow`', skill)

        self.assertIn(
            '[診断・計画専用経路](../../issue-management/references/issue-recording.md#診断計画専用のissue記録)',
            guide)
        self.assertIn('[承認済み変更のdelivery](../../change-delivery/SKILL.md)', guide)
        self.assertIn('Issueを記録しただけでSub-issueを実行対象として確定したり、実装承認を得たことにしたりしない', guide)
        self.assertNotIn('`task-workflow`', guide)

        evals = json.loads((root / 'skills/engineering-assessment/evals/evals.json').read_text(encoding='utf-8'))
        by_id = {case['id']: case for case in evals['evals']}
        for case_id in (7, 11, 16):
            with self.subTest(case_id=case_id):
                self.assertNotIn('task-workflow', json.dumps(by_id[case_id], ensure_ascii=False))
        self.assertIn('issue-management', by_id[7]['expected_output'])
        self.assertIn('change-delivery', by_id[11]['expected_output'])
        self.assertIn('issue-management', by_id[16]['expected_output'])
        self.assertIn(17, by_id, 'diagnosis follow-on needs a scoped, explicitly approved delivery scenario')
        self.assertIn(18, by_id, 'missing Issue dependency must not silently fall back to the retired root')
        self.assertIn(19, by_id, 'missing delivery dependency must not start implementation')

    def test_code_changes_use_issue_planning_and_approved_delivery(self):
        root = Path(__file__).resolve().parents[1]
        skill = (root / 'skills/software-development/SKILL.md').read_text(encoding='utf-8')
        testing = (root / 'skills/software-development/references/testing.md').read_text(encoding='utf-8')
        entry = skill.split('工程に対応する資料を読む')[0]
        self.assertIn('`issue-management`', entry)
        self.assertIn('`change-delivery`', entry)
        self.assertIn('Issue計画', entry)
        self.assertIn('公開許可', entry)
        self.assertIn('main', entry)
        self.assertIn('`issue-management` を利用できなければIssueへ投稿せず', skill)
        self.assertIn('`change-delivery` を利用できなければコード変更を開始せず', skill)
        subissue = next(sentence for sentence in skill.split('。') if '確認が必要な変更は' in sentence)
        self.assertIn('`issue-management`', subissue)
        self.assertIn('[behavior-specification](../behavior-specification/SKILL.md)', skill)
        self.assertIn('DriverとNavigatorが同じ共有ToDoを育て', skill)
        self.assertIn('テストファースト', skill)
        self.assertNotIn('`task-workflow`', skill)

        recovery = next(sentence for sentence in testing.split('。') if 'CIの再試行・復旧' in sentence)
        self.assertIn('`change-delivery`', recovery)
        self.assertIn('必要な統合検証を一律にマージ後へ送らない', recovery)
        self.assertNotIn('task-workflow', testing)

        evals = json.loads((root / 'skills/software-development/evals/evals.json').read_text(encoding='utf-8'))
        by_id = {case['id']: case for case in evals['evals']}
        for case_id in (1, 8, 35):
            with self.subTest(case_id=case_id):
                self.assertNotIn('task-workflow', json.dumps(by_id[case_id], ensure_ascii=False))
        self.assertIn('issue-management', by_id[1]['expected_output'])
        self.assertIn('change-delivery', by_id[1]['expected_output'])
        self.assertIn('change-delivery', by_id[8]['expected_output'])
        self.assertIn('change-delivery', by_id[35]['expected_output'])
        self.assertIn(39, by_id, 'missing Issue dependency must not silently substitute the retired Skill')
        self.assertIn(40, by_id, 'missing delivery dependency must not start code changes')

    def test_behavior_specification_separates_planning_from_document_delivery(self):
        root = Path(__file__).resolve().parents[1]
        skill = (root / 'skills/behavior-specification/SKILL.md').read_text(encoding='utf-8')
        handoff = skill.split('## 引き渡しと完了')[1]
        self.assertIn('`issue-management`', handoff)
        self.assertIn('`change-delivery`', handoff)
        self.assertIn('Issue計画', handoff)
        self.assertIn('公開許可', handoff)
        self.assertIn('main', handoff)
        self.assertIn('`okf-docs`', skill)
        self.assertIn('コード変更が依頼された場合', handoff)
        self.assertIn('Plan Mode・読み取り限定では文案を提示', handoff)
        self.assertIn('計画だけの依頼では `change-delivery` や `okf-docs` の導入を前提にしない', handoff)
        self.assertIn('仕様保存だけを実装承認にしない', handoff)
        self.assertIn('`issue-management` を利用できなければIssueへ投稿せず', handoff)
        self.assertIn('`change-delivery` を利用できなければ文書を保存せず', handoff)
        self.assertIn('`okf-docs` を利用できなければ文書を保存せず', handoff)
        self.assertNotIn('`task-workflow`', skill)

        evals = json.loads((root / 'skills/behavior-specification/evals/evals.json').read_text(encoding='utf-8'))
        by_id = {case['id']: case for case in evals['evals']}
        for case_id in (2, 36):
            with self.subTest(case_id=case_id):
                self.assertNotIn('task-workflow', json.dumps(by_id[case_id], ensure_ascii=False))
        self.assertIn('コード変更が依頼された場合', by_id[2]['expected_output'])
        self.assertIn('issue-management', by_id[2]['expected_output'])
        self.assertIn('change-delivery', by_id[36]['expected_output'])
        self.assertIn('TDDやコード編集を始めない', by_id[36]['expected_output'])
        self.assertIn('Plan Modeでは編集せず', by_id[14]['expected_output'])
        self.assertIn('仕様整理だけでsoftware-developmentのTDD', by_id[35]['expected_output'])
        self.assertIn('コード変更を依頼された場合だけ', by_id[37]['expected_output'])
        for case_id, missing in ((38, 'issue-management'), (39, 'change-delivery'), (40, 'okf-docs')):
            with self.subTest(case_id=case_id):
                self.assertIn(case_id, by_id, f'missing {missing} must stop document delivery')
                self.assertIn(missing, by_id[case_id]['prompt'])
                self.assertIn('旧task-workflow', by_id[case_id]['expected_output'])
                self.assertIn('文書', by_id[case_id]['expected_output'])
        self.assertIn(41, by_id, 'issue-only plans must not require delivery or document authoring')
        self.assertIn('change-delivery', by_id[41]['prompt'])
        self.assertIn('okf-docs', by_id[41]['prompt'])
        self.assertIn('issue-management', by_id[41]['expected_output'])
        self.assertIn('妨げない', by_id[41]['expected_output'])
        self.assertIn('未投稿', by_id[41]['expected_output'])


if __name__ == '__main__':
    unittest.main()
