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
        self.assertFalse((root / 'skills/task-workflow/SKILL.md').exists(),
                         'the retired root must not remain installable')
        readme = (root / 'README.md').read_text(encoding='utf-8')
        self.assertIn('| `task-workflow` |', readme)
        migrated = []
        for skill in ('issue-management', 'change-delivery'):
            path = root / 'skills' / skill / 'evals' / 'evals.json'
            self.assertTrue(path.is_file(), f'{skill} evals must exist')
            data = json.loads(path.read_text(encoding='utf-8'))
            self.assertEqual(skill, data['skill_name'])
            legacy = [case for case in data['evals'] if 'source_id' in case]
            for case in legacy:
                self.assertEqual(f'task-workflow/{case["id"]}', case['source_id'])
            migrated.extend(case['source_id'] for case in legacy)
        self.assertCountEqual(
            [f'task-workflow/{number}' for number in range(1, 139)], migrated)

    def test_issue_eval_read_only_excludes_current_skills(self):
        root = Path(__file__).resolve().parents[1]
        data = json.loads((root / 'skills/issue-management/evals/evals.json').read_text(
            encoding='utf-8'))
        case = next(case for case in data['evals']
                    if case.get('source_id') == 'task-workflow/1')
        expected = case['expected_output']
        self.assertIn('読み取りと概念説明だけに留め', expected)
        self.assertIn('issue-management・change-delivery・document-authoringを起動せず', expected)
        self.assertIn('Issue・PRを作成しない', expected)
        self.assertNotIn('task-workflow', expected)

    def test_approved_continuation_evals_belong_to_delivery(self):
        root = Path(__file__).resolve().parents[1]
        issue = json.loads((root / 'skills/issue-management/evals/evals.json').read_text(
            encoding='utf-8'))
        delivery = json.loads((root / 'skills/change-delivery/evals/evals.json').read_text(
            encoding='utf-8'))
        for source_id in ('task-workflow/27', 'task-workflow/91',
                          'task-workflow/92', 'task-workflow/98'):
            with self.subTest(source_id=source_id):
                self.assertIn(source_id, [case.get('source_id') for case in delivery['evals']])
                self.assertNotIn(source_id, [case.get('source_id') for case in issue['evals']])

    def test_approved_issue_evals_handoff_delivery_without_reapproval(self):
        root = Path(__file__).resolve().parents[1]
        data = json.loads((root / 'skills/issue-management/evals/evals.json').read_text(
            encoding='utf-8'))
        cases = {case.get('source_id'): case for case in data['evals']}
        boundaries = {
            4: ('ブランチ準備・修正・検証・既存PR完了手順へ進む', '会話上の再承認待ちを作らず'),
            7: ('修正と既存PR完了手順へ進む', '保存内容を再取得・提示後'),
            9: ('ファイル追加だけを理由に再承認を待たず修正・検証へ進む', '再取得した本文とURLを提示し'),
            11: ('実装へ進む', '必要なfeature文書は実装より先に保存し'),
            26: ('編集・検証・PR・レビュー・マージへ進む', '承認待ちの記録を更新する'),
            43: ('ブランチ準備・実装・検証・既存PR完了手順へ進む', '会話上の再承認を求めず'),
            95: ('計画保存・再取得・提示後に修正へ進む手順を示す', '別のマップ承認や同じ計画の再承認を追加しない'),
        }
        for number, (stale, preserved) in boundaries.items():
            with self.subTest(source_id=f'task-workflow/{number}'):
                case = cases[f'task-workflow/{number}']
                expected = case['expected_output']
                self.assertIn(preserved, expected)
                self.assertIn('change-delivery', expected)
                self.assertIn('引き渡', expected)
                self.assertNotIn(stale, expected)
                if number == 95:
                    self.assertIn(preserved, case['expectations'][2])
                    self.assertIn('change-delivery', case['expectations'][2])
                    self.assertIn('引き渡', case['expectations'][2])
                    self.assertNotIn(stale, case['expectations'][2])

    def test_delivery_evals_name_current_skill_owners(self):
        root = Path(__file__).resolve().parents[1]
        data = json.loads((root / 'skills/change-delivery/evals/evals.json').read_text(
            encoding='utf-8'))
        cases = {case.get('source_id'): case for case in data['evals']}
        for number in (2, 70):
            with self.subTest(source_id=f'task-workflow/{number}'):
                expected = cases[f'task-workflow/{number}']['expected_output']
                self.assertIn('change-delivery', expected)
                self.assertNotIn('task-workflow', expected)
                if number == 2:
                    self.assertIn('issue-management', expected)
                    self.assertIn('document-authoring', expected)
                    self.assertIn('文書のみなのでTDDは要求しない', expected)
                else:
                    self.assertIn('未確認ならissue-management', expected)
                    self.assertIn('利用可能なskill-creator', expected)
                    self.assertIn('software-developmentを適用せず', expected)

    def test_change_delivery_has_installable_skill_entry(self):
        root = Path(__file__).resolve().parents[1]
        skill = root / 'skills/change-delivery/SKILL.md'
        self.assertTrue(skill.is_file(), 'change-delivery needs an installable SKILL.md')
        self.assertEqual([], validate_file(skill, root))

    def test_change_delivery_preserves_execution_and_reporting_rules(self):
        root = Path(__file__).resolve().parents[1]
        entry = (root / 'skills/change-delivery/SKILL.md').read_text(encoding='utf-8')
        for required in (
                'skill-creator', '再現入力と期待判断', '同じ入力・基準の独立した模擬実行',
                '最終差分を依頼', 'TDDの1サイクル',
                '長い作業', '同じ操作を理由なく繰り返さない',
                '最終報告にIssue・PR', '同期・ブランチ整理'):
            with self.subTest(required=required):
                self.assertIn(required, entry)

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

    def test_code_review_eval_excludes_delivery_skills_for_read_only_review(self):
        root = Path(__file__).resolve().parents[1]
        data = json.loads((root / 'skills/code-review/evals/evals.json').read_text(
            encoding='utf-8'))
        case = next(case for case in data['evals'] if case['id'] == 1)
        expected = case['expected_output']
        self.assertNotIn('task-workflow', expected)
        self.assertIn('issue-management', expected)
        self.assertIn('change-delivery', expected)

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
        self.assertIn('`document-authoring`', skill)
        self.assertIn('コード変更が依頼された場合', handoff)
        self.assertIn('Plan Mode・読み取り限定では文案を提示', handoff)
        self.assertIn('計画だけの依頼では `change-delivery` や `document-authoring` の導入を前提にしない', handoff)
        self.assertIn('仕様保存だけを実装承認にしない', handoff)
        self.assertIn('`issue-management` を利用できなければIssueへ投稿せず', handoff)
        self.assertIn('`change-delivery` を利用できなければ文書を保存せず', handoff)
        self.assertIn('`document-authoring` を利用できなければ文書を保存せず', handoff)
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
        for case_id, missing in ((38, 'issue-management'), (39, 'change-delivery'), (40, 'document-authoring')):
            with self.subTest(case_id=case_id):
                self.assertIn(case_id, by_id, f'missing {missing} must stop document delivery')
                self.assertIn(missing, by_id[case_id]['prompt'])
                self.assertIn('旧task-workflow', by_id[case_id]['expected_output'])
                self.assertIn('文書', by_id[case_id]['expected_output'])
        self.assertIn(41, by_id, 'issue-only plans must not require delivery or document authoring')
        self.assertIn('change-delivery', by_id[41]['prompt'])
        self.assertIn('document-authoring', by_id[41]['prompt'])
        self.assertIn('issue-management', by_id[41]['expected_output'])
        self.assertIn('妨げない', by_id[41]['expected_output'])
        self.assertIn('未投稿', by_id[41]['expected_output'])

    def test_actions_repairs_route_plans_delivery_and_application_code_separately(self):
        root = Path(__file__).resolve().parents[1]
        skill = (root / 'skills/github-actions/SKILL.md').read_text(encoding='utf-8')
        description = skill.split('---')[1]
        entry = skill.split('作業に該当する資料だけを読む')[0]
        self.assertIn('issue-management', description)
        self.assertIn('change-delivery', description)
        self.assertIn('`issue-management`', entry)
        self.assertIn('`change-delivery`', entry)
        self.assertIn('Issue計画', entry)
        self.assertIn('公開許可', entry)
        self.assertIn('main', entry)
        self.assertIn('`software-development`', entry)
        self.assertIn('`code-review`', entry)
        self.assertIn('相談・監査だけから編集・Issue投稿・PR作成・実行トリガーへ進まない', entry)
        plan_only = next(sentence for sentence in entry.split('。') if 'Issue計画だけなら' in sentence)
        self.assertIn('`issue-management`', plan_only)
        self.assertIn('`change-delivery` や `software-development` が未導入でも', plan_only)
        self.assertIn('保存・再取得', plan_only)
        self.assertIn('停止', plan_only)
        app_fix = next(sentence for sentence in entry.split('。') if 'アプリコードの修正' in sentence)
        self.assertIn('`software-development`', app_fix)
        self.assertIn('TDD', app_fix)
        workflow_fix = next(sentence for sentence in entry.split('。') if 'workflow設定のみ' in sentence)
        self.assertIn('TDDを始めない', workflow_fix)
        self.assertIn('`issue-management` を利用できなければIssueへ投稿せず', entry)
        self.assertIn('`change-delivery` を利用できなければworkflowを編集せず', entry)
        self.assertIn('`software-development` を利用できなければアプリコードを編集せず', entry)
        self.assertNotIn('task-workflow', skill)

        design = (root / 'skills/github-actions/references/workflow-design.md').read_text(encoding='utf-8')
        recovery = next(sentence for sentence in design.split('。') if '公開条件や権限の変更' in sentence)
        self.assertIn('`issue-management`', recovery)
        self.assertNotIn('task-workflow', recovery)
        self.assertNotIn('task-workflow', design)

        sources = (root / 'skills/github-actions/references/sources.md').read_text(encoding='utf-8')
        boundary = next(line for line in sources.splitlines() if line.startswith('| 作業の境界 |'))
        self.assertIn('issue-management', boundary)
        self.assertIn('change-delivery', boundary)
        self.assertNotIn('task-workflow', boundary)

        evals = json.loads((root / 'skills/github-actions/evals/evals.json').read_text(encoding='utf-8'))
        by_id = {case['id']: case for case in evals['evals']}
        for case_id in (3, 5, 25):
            with self.subTest(case_id=case_id):
                self.assertNotIn('task-workflow', json.dumps(by_id[case_id], ensure_ascii=False))
        self.assertIn('案だけ', by_id[3]['prompt'])
        self.assertIn('承認', by_id[5]['prompt'])
        self.assertIn('未公開内容', by_id[5]['expected_output'])
        self.assertIn('投稿先・本文案', by_id[5]['expected_output'])
        self.assertNotIn('確認済みの計画・公開許可', by_id[5]['expected_output'])
        self.assertIn('software-development', by_id[25]['expected_output'])
        for case_id, missing in ((26, 'issue-management'), (27, 'change-delivery'),
                                 (28, 'software-development')):
            with self.subTest(case_id=case_id):
                self.assertIn(case_id, by_id, f'missing {missing} needs a safe stop')
                self.assertIn(missing, by_id[case_id]['prompt'])
                self.assertIn('旧task-workflow', by_id[case_id]['expected_output'])
        self.assertIn(29, by_id, 'issue-plan-only must not require delivery or code Skills')
        self.assertIn('change-delivery', by_id[29]['prompt'])
        self.assertIn('software-development', by_id[29]['prompt'])
        self.assertIn('issue-management', by_id[29]['expected_output'])
        self.assertIn('妨げない', by_id[29]['expected_output'])

    def test_document_authoring_routes_publication_and_approved_delivery_separately(self):
        root = Path(__file__).resolve().parents[1]
        skill = (root / 'skills/document-authoring/SKILL.md').read_text(encoding='utf-8')
        entry = skill.split('## 適用と参照資料')[0]
        self.assertIn('`issue-management`', entry)
        self.assertIn('`change-delivery`', entry)
        self.assertIn('Issue計画', entry)
        self.assertIn('公開許可', entry)
        self.assertIn('main', entry)
        plan_only = next(sentence for sentence in skill.split('。') if 'Issue計画だけなら' in sentence)
        self.assertIn('`issue-management`', plan_only)
        self.assertIn('`change-delivery` は不要', plan_only)
        self.assertIn('保存・再取得', plan_only)
        issue_only = next(sentence for sentence in skill.split('。') if 'Issue本文・コメントだけなら' in sentence)
        self.assertIn('`issue-management`', issue_only)
        self.assertIn('`change-delivery` は不要', issue_only)
        external = next(sentence for sentence in skill.split('。') if '外部Bundleのconformanceだけなら' in sentence)
        self.assertIn('`issue-management`・`change-delivery` が未導入でも', external)
        self.assertIn('自作のauthoring条件を課さない', external)
        pr_only = next(sentence for sentence in skill.split('。') if 'PR本文だけの更新は' in sentence)
        self.assertIn('`issue-management`', pr_only)
        self.assertIn('`change-delivery`', pr_only)
        self.assertIn('リポジトリ編集・マージを始めない', pr_only)
        self.assertIn('`issue-management` を利用できなければ', skill)
        self.assertIn('`change-delivery` を利用できなければ', skill)
        self.assertNotIn('task-workflow', skill)

        validation = (root / 'skills/document-authoring/references/validation.md').read_text(encoding='utf-8')
        self.assertIn(
            '[検証環境の準備](../../issue-management/references/planning.md#検証環境の準備)',
            validation)
        self.assertIn(
            '[GitHub向けMarkdownの品質](../../issue-management/references/markdown-quality.md)',
            validation)
        self.assertIn('conformance', validation)
        self.assertIn('隔離venv', validation)
        self.assertIn('実行できない検査を合格にしない', validation)
        self.assertNotIn('task-workflow', validation)

        specification = (root / 'skills/document-authoring/references/specification.md').read_text(encoding='utf-8')
        scope = next(sentence for sentence in specification.split('。') if '実装の範囲や方針変更' in sentence)
        self.assertIn('issue-management', scope)
        self.assertNotIn('task-workflow', specification)

        evals = json.loads((root / 'skills/document-authoring/evals/evals.json').read_text(encoding='utf-8'))
        by_id = {case['id']: case for case in evals['evals']}
        for case_id in (1, 2, 4):
            with self.subTest(case_id=case_id):
                self.assertNotIn('task-workflow', json.dumps(by_id[case_id], ensure_ascii=False))
                self.assertIn('issue-management', by_id[case_id]['expected_output'])
                self.assertIn('change-delivery', by_id[case_id]['expected_output'])
        self.assertIn('OKF', by_id[1]['expected_output'])
        self.assertIn('behavior-specification', by_id[2]['expected_output'])
        self.assertIn('OKF', by_id[4]['expected_output'])
        self.assertIn('PR本文だけ', by_id[4]['expected_output'])
        self.assertIn('保存・確認済みなら', by_id[4]['expected_output'])
        self.assertIn('未保存なら', by_id[4]['expected_output'])
        self.assertIn('リポジトリ編集やマージへ進まない', by_id[4]['expected_output'])
        self.assertIn('隔離環境', by_id[5]['expected_output'])
        self.assertIn('自作品質条件と区別する', by_id[18]['expected_output'])
        self.assertIn('TDD', by_id[25]['expected_output'])
        for case_id in (29, 30, 31, 32, 33):
            with self.subTest(case_id=case_id):
                self.assertIn(case_id, by_id)
                self.assertTrue(by_id[case_id]['expectations'])
        self.assertIn('保存', by_id[29]['expected_output'])
        self.assertIn('conformance', by_id[30]['expected_output'])
        self.assertIn('Issue', by_id[31]['expected_output'])
        self.assertIn('change-deliveryを要求せず', by_id[31]['expected_output'])
        self.assertIn('旧task-workflow', by_id[32]['expected_output'])
        self.assertIn('旧task-workflow', by_id[33]['expected_output'])

    def test_document_authoring_owns_the_renamed_skill_and_validator(self):
        root = Path(__file__).resolve().parents[1]
        skill = root / 'skills/document-authoring'
        self.assertTrue((skill / 'SKILL.md').is_file())
        self.assertFalse((root / 'skills/okf-docs').exists())
        self.assertIn('name: document-authoring',
                      (skill / 'SKILL.md').read_text(encoding='utf-8'))
        evals = json.loads((skill / 'evals/evals.json').read_text(encoding='utf-8'))
        self.assertEqual('document-authoring', evals['skill_name'])
        self.assertEqual(list(range(1, 34)), sorted(case['id'] for case in evals['evals']))
        self.assertIn('skills/document-authoring/scripts/requirements.txt',
                      (root / 'requirements-ci.txt').read_text(encoding='utf-8'))
        self.assertIn("skills/document-authoring/scripts/validate_okf.py",
                      (root / 'scripts/check_repository.py').read_text(encoding='utf-8'))

    def test_document_authoring_preserves_approval_without_assuming_a_saved_plan(self):
        root = Path(__file__).resolve().parents[1]
        evals = json.loads((root / 'skills/document-authoring/evals/evals.json').read_text(encoding='utf-8'))
        by_id = {case['id']: case for case in evals['evals']}
        for case_id in (1, 2):
            with self.subTest(case_id=case_id):
                self.assertIn('保存・確認済みなら', by_id[case_id]['expected_output'])
                self.assertIn('未保存なら', by_id[case_id]['expected_output'])
                self.assertIn('公開許可', by_id[case_id]['expected_output'])
                self.assertIn('実行承認を保持', by_id[case_id]['expected_output'])

        skill = (root / 'skills/document-authoring/SKILL.md').read_text(encoding='utf-8')
        missing_delivery = next(sentence for sentence in skill.split('。')
                                if '`change-delivery` を利用できなければ' in sentence)
        self.assertIn('リポジトリ文書・PR', missing_delivery)
        self.assertIn('Issue本文・コメントだけの更新は妨げない', missing_delivery)

    def test_document_and_pr_handoff_checks_plan_record_separately_from_approval(self):
        root = Path(__file__).resolve().parents[1]
        skill = (root / 'skills/document-authoring/SKILL.md').read_text(encoding='utf-8')
        handoff = next((line for line in skill.splitlines()
                        if line.startswith('- PR本文・リポジトリ文書の変更では')), '')
        self.assertIn('計画承認済みでも', handoff)
        self.assertIn('保存・確認済みと推測しない', handoff)
        self.assertIn('保存・確認済みなら再記録せず', handoff)
        self.assertIn('未保存なら公開許可', handoff)
        self.assertIn('`issue-management`', handoff)
        self.assertIn('保存・再取得', handoff)
        self.assertIn('本文・表示・URL', handoff)
        self.assertIn('実行承認を取り直さない', handoff)

    def test_public_maintenance_docs_route_current_split_skills(self):
        root = Path(__file__).resolve().parents[1]
        readme = (root / 'README.md').read_text(encoding='utf-8')
        install = readme.split('## gh skillでスキルを導入')[1].split('### gh skillの更新')[0]
        diagnosis = readme.split('## 開発実践の診断と導入計画')[1].split('## 更新')[0]
        maintenance = readme.split('## 保守と検証')[1]
        for section in (install, diagnosis, maintenance):
            self.assertIn('`issue-management`', section)
            self.assertIn('`change-delivery`', section)
            self.assertNotIn('`task-workflow`', section)
        self.assertIn('保存したIssueを提示して終了', diagnosis)
        self.assertIn('実装・組織変更は行わず', diagnosis)
        self.assertIn('明確な変更依頼と承認がある場合だけ', diagnosis)
        self.assertIn('gh skill install daiksud/agents --all --agent codex --scope user', readme)
        self.assertIn('| `bdd-tdd` |', readme)
        self.assertIn('apm install --global --target codex,copilot daiksud/agents', readme)

        glossary = (root / 'docs/glossary.md').read_text(encoding='utf-8')
        for term, owner in (('継続的インテグレーション', 'change-delivery'),
                            ('スタンダード', 'issue-management'),
                            ('導入計画', 'issue-management')):
            with self.subTest(term=term):
                row = next(line for line in glossary.splitlines() if line.startswith(f'| {term} |'))
                self.assertIn(f'`{owner}`', row)
                self.assertNotIn('`task-workflow`', row)

        instructions = (root / 'skills/AGENTS.md').read_text(encoding='utf-8')
        self.assertIn('`issue-management`', instructions)
        self.assertIn('`change-delivery`', instructions)
        self.assertIn('[GitHub向けMarkdownの品質](issue-management/references/markdown-quality.md)',
                      instructions)
        self.assertNotIn('task-workflow/references/markdown-quality.md', instructions)
        self.assertNotIn('`task-workflow`', instructions)

        guide = (root / 'docs/guides/delivery.md').read_text(encoding='utf-8')
        self.assertIn('`skills/issue-management/`', guide)
        self.assertIn('`skills/change-delivery/`', guide)
        self.assertIn('skills/issue-management/assets/rumdl.toml', guide)
        self.assertIn(
            '[GitHub向けMarkdownの品質](../../skills/issue-management/references/markdown-quality.md)',
            guide)
        self.assertIn(
            '[統合後mainの確認と復旧]'
            '(../../skills/change-delivery/references/review-and-merge.md#統合後mainの確認と復旧)',
            guide)
        self.assertIn(
            '[小さな統合単位と活動日]'
            '(../../skills/change-delivery/references/branches.md#小さな統合単位と活動日)',
            guide)
        self.assertIn(
            '[作業環境整理]'
            '(../../skills/change-delivery/references/review-and-merge.md#マージ後の作業環境の整理)',
            guide)
        self.assertIn(
            '[代替レビュー]'
            '(../../skills/change-delivery/references/review-and-merge.md#代替レビュー)',
            guide)
        self.assertIn('必要な承認・レビュー・CIを省略せず', guide)
        self.assertNotIn('skills/task-workflow/references/', guide)
        self.assertIn('python scripts/sync_review_skill.py --check', guide)

        approvals = (root / 'docs/guides/codex-command-approvals.md').read_text(encoding='utf-8')
        self.assertIn(
            '[検証環境の準備](../../skills/issue-management/references/planning.md#検証環境の準備)',
            approvals)
        self.assertNotIn('skills/task-workflow/references/', approvals)


if __name__ == '__main__':
    unittest.main()
