import copy
import pathlib
import re
import textwrap
import unittest


def production():
    workflow = pathlib.Path('.github/workflows/approve-codex-review.yml').read_text()
    match = re.search(r"python3 <<'PY'\n(.*?)\n          PY", workflow, re.S)
    namespace = {'__name__': 'workflow_test'}
    if match:
        exec(compile(textwrap.dedent(match[1]), 'approve-codex-review.yml', 'exec'), namespace)
    return namespace


class FakeAPI:
    def __init__(self, state):
        self.state = state
        self.effects = []
        self.fail = None
        self.on_get = None

    def __call__(self, path, method='GET', **fields):
        key = path.rsplit('/', 1)[1]
        if self.fail == key:
            raise RuntimeError('State fetch failed')
        if method == 'PUT':
            review_id = int(path.split('/')[-2])
            self.effects.append(('DISMISS', review_id))
            review = next(r for r in self.state['reviews'] if r['id'] == review_id)
            if review['state'] == 'DISMISSED':
                raise RuntimeError('Already dismissed')
            review['state'] = 'DISMISSED'
            return {}
        if method == 'POST':
            self.effects.append((fields['event'], fields['commit_id']))
            self.state['reviews'].append({
                'id': 42 + len(self.state['reviews']), 'user': {'login': 'github-actions[bot]', 'type': 'Bot'},
                'state': 'APPROVED' if fields['event'] == 'APPROVE' else 'COMMENTED',
                'submitted_at': '2026-10-09T01:00:02Z',
                'body': fields['body'], 'commit_id': fields['commit_id'],
            })
            return {}
        if self.on_get:
            self.on_get(key)
        if '/commits/' in path:
            return {'sha': self.state['pr']['head']['sha'] if self.state['pr']['head']['sha'].startswith(key) else 'b' * 40}
        return copy.deepcopy(self.state[key] if key in self.state else self.state['pr'])


class ApprovalTests(unittest.TestCase):
    def test_clean_current_reviews_are_eligible(self):
        self.assertEqual(self.sha, self.eligible())

    def test_controlled_restart_rejects_cached_completion(self):
        self.state['reviews'] = [dict(self.bot_review(1, self.logic['BARRIER']), submitted_at='2026-10-09T01:00:02Z')]
        self.assertIsNone(self.eligible())

    def test_new_findings_reject_old_clean_reaction(self):
        self.state['reviews'] = [{'user': self.author, 'body': 'Review suggestions', 'commit_id': self.sha, 'submitted_at': '2026-10-09T01:00:02Z'}]
        self.assertIsNone(self.eligible())

    def test_reaction_user_type_matches_trusted_bot_identity(self):
        self.state['reactions'][0]['user']['type'] = 'User'
        self.assertEqual(self.sha, self.eligible())

    def test_security_findings_reject_old_clean_reaction(self):
        self.state['comments'].append({'user': self.author, 'body': '### 🛡️ Codex Security Review\nSecurity findings require action.\n**Reviewed commit:** `aaaaaaa`', 'created_at': '2026-10-09T01:00:02Z'})
        self.assertIsNone(self.eligible())

    def test_reconcile_binds_and_deduplicates_approval(self):
        self.reconcile()
        self.reconcile()
        self.assertEqual([('APPROVE', self.sha)], self.api.effects)

    def test_invalidation_preserves_other_approvals(self):
        self.state['reviews'] = [self.bot_review(1), dict(self.bot_review(2), user={'login': 'other-reviewer', 'type': 'User'}), self.bot_review(3, 'Other automation')]
        self.state['pr']['draft'] = True
        self.reconcile()
        self.assertEqual([('DISMISS', 1)], self.api.effects)
        self.assertEqual('APPROVED', self.state['reviews'][1]['state'])
        self.assertEqual('APPROVED', self.state['reviews'][2]['state'])

    def test_fetch_failure_revokes_known_approval(self):
        self.state['reviews'] = [self.bot_review(1)]
        self.api.fail = 'comments'
        with self.assertRaisesRegex(RuntimeError, 'State fetch failed'):
            self.reconcile()
        self.assertEqual([('DISMISS', 1)], self.api.effects)

    def test_changed_evidence_before_approval_revokes(self):
        self.state['reviews'] = [self.bot_review(1)]
        reads = []
        def changed(key):
            if key == 'reactions':
                reads.append(key)
                if len(reads) == 2:
                    self.state['reactions'] = []
        self.api.on_get = changed
        self.reconcile()
        self.assertEqual([('DISMISS', 1)], self.api.effects)

    def test_late_event_uses_current_ready_history(self):
        self.state['timeline'] = [{'event': 'ready_for_review', 'created_at': '2026-10-09T01:00:02Z'}]
        self.assertIsNone(self.eligible())

    def test_controlled_ready_revokes_before_transition(self):
        self.state['reviews'] = [self.bot_review(1)]
        self.logic['controlled'](self.api, 'example/repo', 1, 'ready', self.sha,
                                 lambda: self.api.effects.append(('READY', self.sha)))
        self.assertEqual([('DISMISS', 1), ('COMMENT', self.sha), ('READY', self.sha)], self.api.effects)
        self.assertIsNone(self.eligible())

    def test_stale_summary_does_not_supersede_findings(self):
        self.state['reviews'] = [{'user': self.author, 'commit_id': self.sha,
                                  'body': 'Review suggestions', 'submitted_at': '2026-10-09T01:00:02Z'}]
        for prefix in ("Codex Review: Didn't find any major issues.", '### 🛡️ Codex Security Review'):
            self.state['comments'].append({'user': self.author,
                'body': prefix + '\nSecurity review completed. No security issues were found in this pull request.\n**Reviewed commit:** `aaaaaaa`',
                'created_at': '2026-10-09T01:00:03Z'})
        self.assertIsNone(self.eligible())

    def test_required_ineligible_states(self):
        original = copy.deepcopy(self.state)
        cases = {
            'draft': lambda s: s['pr'].update(draft=True),
            'closed': lambda s: s['pr'].update(state='closed'),
            'head-change': lambda s: s['pr']['head'].update(sha='b' * 40),
            'no-reaction': lambda s: s.update(reactions=[]),
            'running-reaction': lambda s: s['reactions'].append({'user': self.author, 'content': 'eyes'}),
            'wrong-reaction-author': lambda s: s['reactions'][0]['user'].update(id=88),
            'unknown-author': lambda s: s['comments'][0]['user'].update(type='User'),
            'duplicate-summary': lambda s: s['comments'].append(copy.deepcopy(s['comments'][0])),
            'mixed-metadata': lambda s: s['comments'][0].update(body=s['comments'][0]['body'].replace('"status":"completed"', '"status":"running"')),
            'late-old-summary': lambda s: s['comments'][0].update(body=s['comments'][0]['body'].replace('`aaaaaaa`', '`bbbbbbb`')),
        }
        for kind in ('Code Review', 'Security Review'):
            for status in ('Running', 'Failed', 'Interrupted', 'Unknown', 'Completed / Running'):
                cases[kind + '-' + status] = lambda s, k=kind, v=status: s['comments'][0].update(
                    body=s['comments'][0]['body'].replace('**' + k + '** | ✅ **Completed**', '**' + k + '** | ✅ **' + v + '**'))
        for name, change in cases.items():
            with self.subTest(name=name):
                self.state = copy.deepcopy(original)
                change(self.state)
                self.assertIsNone(self.eligible())

    def test_recovery_after_both_new_clean_completions(self):
        self.state['reviews'] = [{'user': self.author, 'commit_id': self.sha,
                                  'body': 'Review suggestions', 'submitted_at': '2026-10-09T01:00:02Z'}]
        for prefix in ("Codex Review: Didn't find any major issues.", '### 🛡️ Codex Security Review'):
            self.state['comments'].append({'user': self.author,
                'body': prefix + '\nSecurity review completed. No security issues were found in this pull request.\n**Reviewed commit:** `aaaaaaa`',
                'created_at': '2026-10-09T01:00:03Z'})
        self.state['comments'][0]['body'] = self.state['comments'][0]['body'].replace('01:00:00Z', '01:00:04Z').replace('01:00:01Z', '01:00:05Z')
        self.assertEqual(self.sha, self.eligible())

    def test_relevant_requests_and_lifecycle_barriers(self):
        for event in ('ready_for_review', 'convert_to_draft', 'review_requested'):
            with self.subTest(event=event):
                self.state['timeline'] = [{'event': event, 'created_at': '2026-10-09T01:00:02Z',
                                           'requested_reviewer': {'login': self.author['login']}}]
                self.assertIsNone(self.eligible())
        self.state['timeline'][0]['requested_reviewer']['login'] = 'other-reviewer'
        self.assertEqual(self.sha, self.eligible())
        self.state['comments'].append({'body': '@codex review', 'author_association': 'OWNER',
                                       'created_at': '2026-10-09T01:00:02Z'})
        self.assertIsNone(self.eligible())

    def test_failed_dismissal_blocks_transition(self):
        self.state['reviews'] = [self.bot_review(1)]
        self.api.fail = 'dismissals'
        with self.assertRaisesRegex(RuntimeError, 'State fetch failed'):
            self.logic['controlled'](self.api, 'example/repo', 1, 'ready', self.sha,
                                     lambda: self.api.effects.append(('READY', self.sha)))
        self.assertEqual([], self.api.effects)

    def test_fetch_and_resolution_failures_never_approve(self):
        for failure in ('comments', 'timeline', 'reactions', 'aaaaaaa', 'reviews'):
            with self.subTest(failure=failure):
                self.state['reviews'] = [self.bot_review(1)]
                self.api.effects.clear()
                self.api.fail = failure
                with self.assertRaisesRegex(RuntimeError, 'State fetch failed'):
                    self.reconcile()
                self.assertNotIn(('APPROVE', self.sha), self.api.effects)

    def test_observed_start_prevents_late_old_completion_restoration(self):
        old_body = self.state['comments'][0]['body']
        self.state['comments'][0]['body'] = old_body.replace('**Code Review** | ✅ **Completed**', '**Code Review** | 👀 **Running**').replace('01:00:00Z', '01:00:02Z')
        self.reconcile()
        self.state['comments'][0]['body'] = old_body
        self.reconcile()
        self.assertNotIn(('APPROVE', self.sha), self.api.effects)
        self.assertIsNone(self.eligible())

    def test_start_observed_on_second_fetch_is_retained(self):
        old_body = self.state['comments'][0]['body']
        reads = []
        def start(key):
            if key == 'comments':
                reads.append(key)
                if len(reads) == 2:
                    self.state['comments'][0]['body'] = old_body.replace('**Code Review** | ✅ **Completed**', '**Code Review** | 👀 **Running**').replace('01:00:00Z', '01:00:02Z')
        self.api.on_get = start
        self.reconcile()
        self.api.on_get = None
        self.state['comments'][0]['body'] = old_body
        self.reconcile()
        self.assertNotIn(('APPROVE', self.sha), self.api.effects)

    def test_observed_start_dismisses_existing_approval_once(self):
        self.state['reviews'] = [self.bot_review(1)]
        self.state['comments'][0]['body'] = self.state['comments'][0]['body'].replace('**Code Review** | ✅ **Completed**', '**Code Review** | 👀 **Running**').replace('01:00:00Z', '01:00:02Z')
        self.reconcile()
        self.assertEqual([('DISMISS', 1), ('COMMENT', self.sha)], self.api.effects)

    def test_observed_failure_cannot_restore_old_completed_state(self):
        original = copy.deepcopy(self.state)
        for status in ('Failed', 'Interrupted', 'Unknown'):
            with self.subTest(status=status):
                self.state = copy.deepcopy(original)
                self.api = FakeAPI(self.state)
                old_body = self.state['comments'][0]['body']
                self.state['comments'][0]['body'] = old_body.replace('**Code Review** | ✅ **Completed**', '**Code Review** | ❌ **' + status + '**').replace('01:00:00Z', '01:00:02Z')
                self.reconcile()
                self.state['comments'][0]['body'] = old_body
                self.reconcile()
                self.assertNotIn(('APPROVE', self.sha), self.api.effects)
                self.api.effects.clear()

    def test_unrelated_team_review_request_preserves_eligibility(self):
        self.state['timeline'] = [{'event': 'review_requested', 'created_at': '2026-10-09T01:00:02Z',
                                   'requested_reviewer': None, 'requested_team': {'name': 'Example team'}}]
        self.assertEqual(self.sha, self.eligible())

    def test_observed_kind_recovers_without_repeating_other_review(self):
        old_body = self.state['comments'][0]['body']
        self.state['comments'][0]['body'] = old_body.replace('**Code Review** | ✅ **Completed**', '**Code Review** | 👀 **Running**').replace('01:00:00Z', '01:00:02Z')
        self.reconcile()
        self.reconcile()
        self.state['comments'][0]['body'] = old_body.replace('01:00:00Z', '01:00:03Z')
        self.reconcile()
        self.assertEqual([('COMMENT', self.sha), ('APPROVE', self.sha)], self.api.effects)

    def test_missing_start_uses_stable_summary_update(self):
        old_body = self.state['comments'][0]['body']
        self.state['comments'][0]['updated_at'] = '2026-10-09T01:00:02Z'
        self.state['comments'][0]['body'] = old_body.replace('**Code Review** | ✅ **Completed**', '**Code Review** | 👀 **Running**').replace(' <relative-time datetime="2026-10-09T01:00:00Z">now</relative-time>', '')
        self.reconcile()
        self.reconcile()
        self.state['comments'][0]['body'] = old_body
        self.reconcile()
        self.assertEqual([('COMMENT', self.sha)], self.api.effects)

    def test_edited_summary_failure_revokes(self):
        self.reconcile()
        self.state['comments'][0]['body'] = self.state['comments'][0]['body'].replace('**Security Review** | ✅ **Completed**', '**Security Review** | ❌ **Failed**')
        self.state['comments'][0]['updated_at'] = '2026-10-09T01:00:02Z'
        self.reconcile()
        self.assertEqual(1, sum(event[0] == 'APPROVE' for event in self.api.effects))
        self.assertEqual('DISMISSED', self.state['reviews'][0]['state'])

    def test_malformed_summary_and_fence_fail_closed(self):
        original = copy.deepcopy(self.state)
        for target in ('metadata', 'timestamp', 'fence'):
            with self.subTest(target=target):
                self.state = copy.deepcopy(original)
                self.api = FakeAPI(self.state)
                self.state['reviews'] = [self.bot_review(1)]
                if target == 'metadata':
                    self.state['comments'][0]['body'] = self.state['comments'][0]['body'].replace('"status":"completed"', 'broken')
                elif target == 'timestamp':
                    self.state['comments'][0]['body'] = self.state['comments'][0]['body'].replace('2026-10-09T01:00:00Z', 'unknown')
                else:
                    self.state['reviews'].append(dict(self.bot_review(2, self.logic['OBSERVED'] + 'broken'), state='COMMENTED'))
                with self.assertRaises(ValueError):
                    self.reconcile()
                self.assertNotIn(('APPROVE', self.sha), self.api.effects)
                self.assertEqual('DISMISSED', self.state['reviews'][0]['state'])

    def test_duplicate_and_missing_summary_rows_reject(self):
        body = self.state['comments'][0]['body']
        row = body.splitlines()[-1]
        for changed in (body + '\n' + row, body.replace(row, '')):
            self.state['comments'][0]['body'] = changed
            self.assertIsNone(self.eligible())

    def test_head_change_revokes_previous_automation_only(self):
        self.state['reviews'] = [self.bot_review(1)]
        self.state['pr']['head']['sha'] = 'b' * 40
        self.reconcile()
        self.assertEqual([('DISMISS', 1)], self.api.effects)

    def test_superseded_ci_run_and_attempt_reject(self):
        def api(path, **fields):
            if path.endswith('/runs'):
                return {'workflow_runs': [{'id': 10, 'head_repository': {'full_name': 'example/repo'},
                                          'pull_requests': [{'number': 1}]}]}
            return {'run_attempt': 2}
        for run, attempt in ((9, 2), (10, 1)):
            with self.assertRaisesRegex(ValueError, 'superseded'):
                self.logic['guard_ci'](api, 'example/repo', 1, self.sha, 'example-branch', run, attempt)
        self.assertIsNone(self.logic['guard_ci'](api, 'example/repo', 1, self.sha, 'example-branch', 10, 2))

    def test_controlled_base_change_stops_before_transition(self):
        self.state['pr']['base'] = {'ref': 'other-base'}
        with self.assertRaisesRegex(ValueError, 'HEAD/base changed'):
            self.logic['controlled'](self.api, 'example/repo', 1, 'ready', self.sha,
                                     lambda: self.api.effects.append(('READY', self.sha)), 'main')
        self.assertEqual([], self.api.effects)

    def eligible(self):
        return self.logic['eligible'](self.state, self.resolve)

    def reconcile(self):
        return self.logic['reconcile'](self.api, 'example/repo', 1)

    def bot_review(self, identifier, body=None):
        return {'id': identifier, 'user': {'login': 'github-actions[bot]', 'type': 'Bot'},
                'body': body if body is not None else self.logic['APPROVAL'],
                'state': 'APPROVED', 'commit_id': self.sha}

    def setUp(self):
        self.logic = production()
        self.sha = 'a' * 40
        self.resolve = lambda sha: self.sha if self.sha.startswith(sha) else 'b' * 40
        self.author = {'login': 'chatgpt-codex-connector[bot]', 'type': 'Bot', 'id': 77, 'node_id': 'BOT_example'}
        self.state = {
            'pr': {'state': 'open', 'draft': False, 'head': {'sha': self.sha}},
            'comments': [{
                'user': dict(self.author), 'updated_at': '2026-10-09T01:00:01Z',
                'body': '<!-- codex-pull-request-review-summary -->\n'
                        '<!-- codex-security-review:v1 {"status":"completed",'
                        '"headSha":"' + self.sha + '","repository":"example/repo",'
                        '"pullRequestNumber":1} -->\n'
                        '| 📝 **Code Review** | ✅ **Completed** <relative-time datetime="2026-10-09T01:00:00Z">now</relative-time> | `aaaaaaa` | Manual request |\n'
                        '| 🔒 **Security Review** | ✅ **Completed** <relative-time datetime="2026-10-09T01:00:01Z">now</relative-time> | `aaaaaaa` | Manual request |',
            }],
            'reactions': [{'user': dict(self.author), 'content': '+1'}],
            'reviews': [], 'timeline': [], 'repo': 'example/repo', 'number': 1,
        }
        self.api = FakeAPI(self.state)


if __name__ == '__main__':
    unittest.main()
