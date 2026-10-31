"""Run the actual inline approval script against isolated, paginated gh fixtures.

Evidence cases follow gh-settings' approval_workflow_test.go at 64dd9a6.
No live API calls or ambient credentials are used.
"""
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

HEAD = "a" * 40
BOT = {"login": "chatgpt-codex-connector[bot]", "id": 199175422, "type": "Bot"}
APP = {"id": 1144995, "slug": "chatgpt-codex-connector"}


def comment(identifier, body, at):
    return {"id": identifier, "body": body, "created_at": at, "updated_at": at,
            "user": dict(BOT), "performed_via_github_app": dict(APP)}


def request(identifier, at):
    return {"id": identifier, "body": "@codex review", "created_at": at,
            "updated_at": at, "user": {"login": "author", "type": "User"}}


def fixture(scenario):
    code_state = {"commit_sha": HEAD, "status": "completed",
                  "has_unresolved_findings": False, "has_any_findings": False}
    security_state = dict(code_state, has_unresolved_findings=None, has_any_findings=None)
    req = request(100, "2026-10-31T02:11:22Z")
    summary = comment(101, "", "2026-10-31T02:11:44Z")
    summary["updated_at"] = "2026-10-31T02:13:13Z"
    code = comment(102, "<!-- codex-review-receipt:v1 -->\n\nCodex Review: Didn't find any major issues. Keep them coming!\n\n**Reviewed commit:** `aaaaaaaaaa`\n", "2026-10-31T02:12:36Z")
    security = comment(103, "<!-- codex-review-receipt:v1 -->\n\n### 🛡️ Codex Security Review · _Automatically triggered_\n\nSecurity review completed. No security issues were found in this pull request.\n\n**Reviewed commit:** `aaaaaaaaaa`\n\n[View security finding report](https://chatgpt.com/codex/cloud/tasks/task_example)", "2026-10-31T02:13:10Z")
    for item in (code, security):
        item["body"] += '\n<details>\nReviews are triggered when you comment "@codex review" or "@codex security review".\n</details>\n'
    reaction = {"id": 200, "user": dict(BOT, type="User"), "content": "+1", "created_at": "2026-10-31T02:13:15Z"}
    pr = {"state": "open", "draft": scenario == "draft", "head": {"sha": HEAD}}
    if scenario == "structured clean":
        security_state.update(has_any_findings=False, has_unresolved_findings=False)
    if scenario == "code findings":
        code_state["has_unresolved_findings"] = True
    if scenario == "security findings":
        security_state["has_unresolved_findings"] = True
    if scenario == "security any findings":
        security_state["has_any_findings"] = True
    if scenario == "missing security flag":
        del security_state["has_unresolved_findings"]
    if scenario == "wrong flag type":
        security_state["has_unresolved_findings"] = "false"
    for kind, state in (("code", code_state), ("security", security_state)):
        if scenario == kind + " incomplete":
            state["status"] = "in_progress"
        if scenario == kind + " stale":
            state["commit_sha"] = "b" * 40
    if scenario in ("spoofed summary", "spoofed receipt"):
        (summary if scenario == "spoofed summary" else security)["user"] = {"login": "outsider", "id": 1, "type": "User"}
    if scenario in ("wrong app", "wrong summary app"):
        (summary if scenario == "wrong summary app" else security)["performed_via_github_app"] = {"id": 42}
    if scenario == "receipt missing app":
        del security["performed_via_github_app"]
    if scenario == "initial automatic overlap":
        summary["created_at"] = "2026-10-31T02:11:00Z"
    if scenario == "same-second summary start":
        summary["created_at"] = req["created_at"]
    if scenario == "security receipt findings":
        security["body"] = security["body"].replace("No security issues were found in this pull request.", "Security issues were found.")
    if scenario == "wrong receipt head":
        security["body"] = security["body"].replace("aaaaaaaaaa", "bbbbbbbbbb")
    if scenario == "old same-head receipt":
        security.update(created_at="2026-10-31T02:10:00Z", updated_at="2026-10-31T02:10:00Z")
    if scenario == "edited receipt":
        security["updated_at"] = "2026-10-31T02:13:12Z"
    if scenario == "edited request":
        req["updated_at"] = "2026-10-31T02:11:23Z"
    if scenario == "security-only request":
        req["body"] = "@codex security review"
    if scenario == "old reaction":
        reaction["created_at"] = "2026-10-31T02:11:00Z"
    if scenario == "same-second reaction":
        reaction["created_at"] = summary["updated_at"]
    if scenario == "other reaction":
        reaction["user"] = {"login": "other", "id": 1, "type": "User"}
    if scenario == "wrong reaction account":
        reaction["user"]["id"] = 1
    if scenario == "closed":
        pr["state"] = "closed"
    metadata = {"blockingSeverityThreshold": "P0", "headSha": HEAD, "mergeGateEnabled": False,
                "pullRequestNumber": 7, "repository": "owner/repo", "status": "completed"}
    state = {"code_review": code_state, "security_review": security_state}
    summary["body"] = ("<!-- codex-pull-request-review-summary -->\n<!-- codex-review-state:v1 " + json.dumps(state) + " -->\n<!-- codex-security-review:v1 " + json.dumps(metadata) + " -->\n"
        '| 📝 **Code Review** | ✅ **Completed** <relative-time datetime="2026-10-31T02:12:38.414268Z">2026-10-31T02:12:38.414268Z</relative-time> | `aaaaaaa` | Manual request |\n'
        '| 🔒 **Security Review** | ✅ **Completed** <relative-time datetime="2026-10-31T02:13:11.462255Z">2026-10-31T02:13:11.462255Z</relative-time> | `aaaaaaa` | Manual request |\n'
        '\n<details>\nReviews are triggered when you comment "@codex review" or "@codex security review".\n</details>\n')
    replacements = {
        "automatic nullable cycle": ("Manual request", "Automatic review"),
        "wrong security metadata": ('"pullRequestNumber": 7', '"pullRequestNumber": 8'),
        "completion before receipt": ("02:13:11.462255", "02:13:09.462255"),
        "wrong row head": ("`aaaaaaa`", "`bbbbbbb`"),
    }
    if scenario in replacements:
        summary["body"] = summary["body"].replace(*replacements[scenario])
    if scenario == "malformed summary":
        summary["body"] = "<!-- codex-pull-request-review-summary -->\n<!-- codex-review-state:v1 broken -->"
    if scenario == "duplicate marker":
        summary["body"] += "<!-- codex-review-state:v1 {} -->\n"
    comments = [req, summary, code, security]
    if scenario == "no request":
        comments = comments[1:]
    if scenario == "no security receipt":
        comments = comments[:3]
    if scenario == "duplicate receipt":
        comments.append(comment(104, security["body"], "2026-10-31T02:13:11Z"))
    if scenario == "unknown bot comment":
        comments.append(comment(104, "A security finding needs attention", "2026-10-31T02:13:12Z"))
    if scenario in ("overlapping requests", "prior completed cycle", "edited older request"):
        older = request(90, "2026-10-31T02:00:00Z")
        comments.insert(0, older)
        if scenario != "overlapping requests":
            comments += [comment(91, code["body"], "2026-10-31T02:01:00Z"), comment(92, security["body"], "2026-10-31T02:02:00Z")]
        if scenario == "edited older request":
            older["updated_at"] = "2026-10-31T02:13:14Z"
    if scenario == "new request":
        comments.append(request(104, "2026-10-31T02:13:14Z"))
    if scenario == "same-second requests":
        comments.append(request(99, req["created_at"]))
    return {"comments": comments, "pr": pr, "reaction": reaction, "summary": summary, "scenario": scenario}


class ApprovalWorkflowTests(unittest.TestCase):
    def run_case(self, scenario, approve, fail):
        workflow = Path(os.environ.get("APPROVAL_WORKFLOW_FIXTURE", Path(__file__).resolve().parents[1] / ".github/workflows/approve-codex-review.yml"))
        block = workflow.read_text().split("        run: |\n", 1)[1]
        lines = []
        for line in block.splitlines():
            if line.strip() and not line.startswith("          "):
                break
            lines.append(line[10:] if line.startswith("          ") else line)
        self.assertTrue(lines, "missing inline approval script")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "fixture.json").write_text(json.dumps(fixture(scenario)))
            (root / "workflow.sh").write_text("\n".join(lines) + "\n")
            (root / "gh").write_text(API_STUB)
            (root / "sleep").write_text('#!/bin/sh\ntest "$*" = 30 || exit 1\nprintf "sleep\\n" >> "$FIXTURE_ROOT/sleeps"\n')
            for tool in ("gh", "sleep"):
                (root / tool).chmod(0o700)
            env = {"PATH": tmp + os.pathsep + os.environ["PATH"], "HOME": tmp,
                   "GH_CONFIG_DIR": tmp, "GH_TOKEN": "dummy-not-a-token",
                   "GITHUB_REPOSITORY": "owner/repo", "PR_NUMBER": "7", "FIXTURE_ROOT": tmp,
                   "COMMENT_ID": "101" if scenario == "comment event" else "99" if scenario == "old comment event" else ""}
            result = subprocess.run(["bash", str(root / "workflow.sh")], env=env, capture_output=True, text=True, timeout=20)
            output = result.stdout + result.stderr
            self.assertEqual(result.returncode != 0, fail, output)
            approvals = (root / "approvals").read_text() if (root / "approvals").exists() else ""
            self.assertEqual(approvals, HEAD + "\n" if approve else "", output)
            self.assertNotIn("dummy-not-a-token", output)
            self.assertTrue(output.strip(), "missing approval/hold diagnostic")
            if scenario == "missing reaction":
                self.assertEqual((root / "sleeps").read_text().splitlines(), ["sleep"] * 6)
            if scenario == "delayed reaction":
                self.assertEqual((root / "sleeps").read_text().splitlines(), ["sleep"])


API_STUB = r'''#!/usr/bin/env python3
import json, os, pathlib, sys
root = pathlib.Path(os.environ['FIXTURE_ROOT'])
f = json.loads((root / 'fixture.json').read_text())
s = f['scenario']
a = sys.argv[1:]
assert a[0] == 'api', a
endpoint = a[1]
counts_file = root / 'counts'
counts = json.loads(counts_file.read_text()) if counts_file.exists() else {}
counts[endpoint] = counts.get(endpoint, 0) + 1
counts_file.write_text(json.dumps(counts))
n = counts[endpoint]
if endpoint == '--method':
    assert a[2:] == ['POST', 'repos/owner/repo/pulls/7/reviews', '-f', 'event=APPROVE', '-f', 'commit_id=' + 'a'*40], a
    if s in ('post rejected', 'post non-json'):
        print('dummy-not-a-token', file=sys.stderr)
        print(json.dumps({'message': 'denied', 'errors': [{'field': 'commit_id'}], 'secret': 'dummy-not-a-token'}) if s == 'post rejected' else 'dummy-not-a-token')
        sys.exit(42)
    with (root / 'approvals').open('a') as out: out.write('a'*40 + '\n')
    result = {'state': 'APPROVED', 'commit_id': 'a'*40}
    if s == 'unconfirmed approval': result['state'] = 'PENDING'
elif endpoint == 'repos/owner/repo/pulls/7':
    result = f['pr']
    if n > 1 and s == 'head changed': result['head']['sha'] = 'b'*40
    if n > 1 and s == 'closed during check': result['state'] = 'closed'
elif endpoint == 'repos/owner/repo/issues/7/comments?per_page=100':
    assert a[2:] == ['--paginate', '--slurp'], a
    if s == 'pagination failed': sys.exit(55)
    comments = f['comments']
    if n > 1:
        if s == 'summary changed':
            for c in comments:
                if c['id'] == 101: c['body'] = c['body'].replace('completed', 'in_progress')
        if s == 'receipt edited during check':
            for c in comments:
                if c['id'] == 103: c['body'] += '\nchanged'; c['updated_at'] = '2026-10-31T02:13:20Z'
        if s == 'request during check':
            comments.append({'id': 104, 'body': '@codex review', 'created_at': '2026-10-31T02:13:20Z', 'updated_at': '2026-10-31T02:13:20Z'})
    result = [comments[:2], comments[2:]]
    if s == 'malformed pagination': result = [comments[:2], {'message': 'error'}]
elif endpoint == 'repos/owner/repo/issues/7/reactions?per_page=100':
    assert a[2:] == ['--paginate', '--slurp'], a
    if s == 'reaction fetch failed': sys.exit(55)
    result = [[], [f['reaction']]]
    if s == 'missing reaction' or (s == 'delayed reaction' and n == 1) or (s == 'reaction removed' and n > 1): result = [[], []]
elif endpoint == 'repos/owner/repo/pulls/7/reviews?per_page=100':
    assert a[2:] == ['--paginate', '--slurp'], a
    result = [[], []]
    if s == 'already approved': result[1] = [{'user': {'login': 'github-actions[bot]'}, 'state': 'APPROVED', 'commit_id': 'a'*40}]
    if s == 'changes requested': result[1] = [{'user': {'login': 'reviewer'}, 'state': 'CHANGES_REQUESTED', 'commit_id': 'a'*40}]
elif endpoint == 'repos/owner/repo/commits/aaaaaaaaaa':
    if s == 'ambiguous short sha': sys.exit(22)
    result = {'sha': 'a'*40}
    if s == 'wrong resolved sha': result['sha'] = 'b'*40
else:
    raise AssertionError('unexpected API ' + str(a))
print(json.dumps(result))
'''

CASES = [
    ('nullable clean', True, False),
    ('structured clean', True, False),
    ('draft', True, False),
    ('comment event', True, False),
    ('old comment event', False, False),
    ('prior completed cycle', True, False),
    ('code findings', False, False),
    ('security findings', False, False),
    ('security any findings', False, False),
    ('missing security flag', False, False),
    ('wrong flag type', False, False),
    ('code incomplete', False, False),
    ('security incomplete', False, False),
    ('code stale', False, False),
    ('security stale', False, False),
    ('spoofed summary', False, False),
    ('spoofed receipt', False, False),
    ('wrong app', False, False),
    ('no security receipt', False, False),
    ('security receipt findings', False, False),
    ('wrong receipt head', False, False),
    ('old same-head receipt', False, False),
    ('edited receipt', False, False),
    ('duplicate receipt', False, False),
    ('unknown bot comment', False, False),
    ('no request', False, False),
    ('edited request', False, False),
    ('overlapping requests', False, False),
    ('security-only request', False, False),
    ('new request', False, False),
    ('old reaction', False, False),
    ('same-second reaction', False, False),
    ('other reaction', False, False),
    ('missing reaction', False, False),
    ('delayed reaction', True, False),
    ('closed', False, False),
    ('head changed', False, False),
    ('closed during check', False, False),
    ('summary changed', False, False),
    ('request during check', False, False),
    ('receipt edited during check', False, False),
    ('reaction removed', False, False),
    ('already approved', False, False),
    ('changes requested', False, False),
    ('ambiguous short sha', False, True),
    ('pagination failed', False, True),
    ('reaction fetch failed', False, True),
    ('post rejected', False, True),
    ('post non-json', False, True),
    ('malformed summary', False, False),
    ('automatic nullable cycle', False, False),
    ('initial automatic overlap', False, False),
    ('edited older request', False, False),
    ('wrong summary app', False, False),
    ('receipt missing app', False, False),
    ('duplicate marker', False, False),
    ('wrong security metadata', False, False),
    ('completion before receipt', False, False),
    ('wrong resolved sha', False, False),
    ('unconfirmed approval', True, True),
    ('malformed pagination', False, True),
    ('wrong reaction account', False, False),
    ('same-second requests', False, False),
    ('same-second summary start', False, False),
    ('wrong row head', False, False),
]



def add_case(name, approve, fail):
    def test(self):
        self.run_case(name, approve, fail)
    setattr(ApprovalWorkflowTests, "test_" + name.replace(" ", "_").replace("-", "_"), test)


for case in CASES:
    add_case(*case)

if __name__ == "__main__":
    unittest.main()
