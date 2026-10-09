import copy
import pathlib
import re
import textwrap
import unittest

def production():
    workflow = pathlib.Path('.github/workflows/approve-codex-review.yml').read_text()
    body = re.search(r"python3 <<'PY'\n(.*?)\n          PY", workflow, re.S).group(1)
    namespace = {'__name__': 'workflow_test'}
    exec(compile(textwrap.dedent(body), 'approve-codex-review.yml', 'exec'), namespace)
    return namespace

class FakeAPI:
    def __init__(self, state): self.state, self.effects, self.fail = state, [], None
    def __call__(self, path, method='GET', **fields):
        key = path.rsplit('/', 1)[1]
        if self.fail == key: raise RuntimeError('State fetch failed')
        if method == 'PUT':
            rid = int(path.split('/')[-2])
            self.effects.append(('DISMISS', rid))
            next(r for r in self.state['reviews'] if r['id'] == rid)['state'] = 'DISMISSED'
            return {}
        if method == 'POST':
            self.effects.append((fields['event'], fields['commit_id']))
            self.state['reviews'].append({'id': 42, 'user': {'login': 'github-actions[bot]', 'type': 'Bot'}, 'state': 'APPROVED', 'body': fields['body'], 'commit_id': fields['commit_id']})
            return {}
        if '/commits/' in path: return {'sha': self.state['pr']['head']['sha'] if self.state['pr']['head']['sha'].startswith(key) else 'b' * 40}
        return copy.deepcopy(self.state.get(key, self.state['pr']))

class ApprovalTests(unittest.TestCase):
    def setUp(self):
        self.logic, self.sha = production(), 'a' * 40
        author = {'login': 'chatgpt-codex-connector[bot]', 'type': 'Bot', 'id': 7, 'node_id': 'BOT'}
        body = '<!-- codex-pull-request-review-summary -->\n<!-- codex-security-review:v1 {"status":"completed","headSha":"' + self.sha + '","repository":"example/repo","pullRequestNumber":1} -->\n'
        body += '| 📝 **Code Review** | ✅ **Completed** | `aaaaaaa` | Manual |\n| 🔒 **Security Review** | ✅ **Completed** | `aaaaaaa` | Manual |'
        self.state = {'pr': {'state': 'open', 'draft': False, 'head': {'sha': self.sha}}, 'comments': [{'user': author, 'body': body}], 'reactions': [{'user': author, 'content': '+1'}], 'reviews': [], 'repo': 'example/repo', 'number': 1}
        self.api = FakeAPI(self.state)
        self.resolve = lambda value: self.sha if self.sha.startswith(value) else 'b' * 40
    def eligible(self): return self.logic['eligible'](self.state, self.resolve)
    def reconcile(self):
        self.logic['api'] = self.api
        return self.logic['reconcile'](self.api, 'example/repo', 1)
    def approval(self, rid=1, commit=None): return {'id': rid, 'user': {'login': 'github-actions[bot]', 'type': 'Bot'}, 'state': 'APPROVED', 'body': self.logic['APPROVAL'], 'commit_id': commit or self.sha}
    def test_clean_current_reviews_are_eligible(self): self.assertTrue(self.eligible())
    def test_approval_is_created_once_and_bound_to_head(self):
        self.assertTrue(self.reconcile())
        self.assertTrue(self.reconcile())
        self.assertEqual([('APPROVE', self.sha)], self.api.effects)
    def test_draft_and_stale_head_withdraw_own_approval(self):
        self.state['reviews'] = [self.approval()]
        self.state['pr']['draft'] = True
        self.assertFalse(self.reconcile())
        self.assertEqual([('DISMISS', 1)], self.api.effects)
        self.state['reviews'] = [self.approval()]
        self.state['pr']['draft'] = False
        self.state['pr']['head']['sha'] = 'b' * 40
        self.reconcile()
        self.assertEqual(2, len(self.api.effects))
    def test_other_approvals_are_preserved(self):
        self.state['reviews'] = [self.approval(), {'id': 2, 'user': {'login': 'reviewer', 'type': 'User'}, 'state': 'APPROVED'}]
        self.reconcile()
        self.assertEqual('APPROVED', self.state['reviews'][1]['state'])
    def test_failed_review_never_approves(self):
        self.state['comments'][0]['body'] = self.state['comments'][0]['body'].replace('✅ **Completed**', '❌ **Failed**')
        self.assertFalse(self.reconcile())
        self.assertNotIn(('APPROVE', self.sha), self.api.effects)
    def test_missing_reaction_never_approves(self):
        self.state['reactions'] = []
        self.assertFalse(self.reconcile())
    def test_retrieval_failure_never_approves(self):
        self.state['reviews'] = [self.approval()]; self.api.fail = 'comments'
        with self.assertRaises(RuntimeError): self.reconcile()
        self.assertNotIn(('APPROVE', self.sha), self.api.effects)
        self.assertEqual([('DISMISS', 1)], self.api.effects)

if __name__ == '__main__': unittest.main()
