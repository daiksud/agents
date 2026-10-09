#!/usr/bin/env bash
set -euo pipefail
root=$(cd "$(dirname "$0")/.." && pwd)
tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT
fixtures="$tmp/fixtures"; work="$tmp/work"
mkdir "$fixtures" "$work"
cd "$work"
awk '/- name: Fetch current pull request evidence/{capture=1} capture && /^        run: \|/{run=1; next} run && /^      - name: Withdraw known/{exit} run{sub(/^          /,""); print}' "$root/.github/workflows/approve-codex-review.yml" >"$tmp/evidence.sh"
awk '/- name: Approve current clean Codex evidence/{capture=1} capture && /^        run: \|/{run=1; next} run && (/^      - name:/ || /^  controlled-ci:/){exit} run{sub(/^          /,""); print}' "$root/.github/workflows/approve-codex-review.yml" >"$tmp/production.sh"
awk '/- name: Withdraw approval while Codex review is running/{capture=1} capture && /^        run: \|/{run=1; next} run && /^      - name:/{exit} run{sub(/^          /,"" ); print}' "$root/.github/workflows/approve-codex-review.yml" >"$tmp/running.sh"
test -s "$tmp/evidence.sh" -a -s "$tmp/production.sh" -a -s "$tmp/running.sh"
cat >"$tmp/gh" <<'EOF'
#!/usr/bin/env bash
set -euo pipefail
printf '%s %s\n' "${GH_METHOD:-GET}" "$*" >>"$GH_LOG"
if [[ ${1:-} == api ]]; then
  for arg in "$@"; do if [[ $arg == .sha ]]; then printf '%s' "$HEAD"; exit 0; fi; done
  endpoint=''; for arg in "$@"; do [[ $arg == repos/* ]] && endpoint=$arg; done
  endpoint=${endpoint%%\?*}
  case "$endpoint" in
    repos/*/pulls/1/reviews) cat "$GH_FIX/reviews.json";;
    repos/*/pulls/1) cat "$GH_FIX/pr.json";;
    repos/*/issues/1/comments) cat "$GH_FIX/comments.json";;
    repos/*/issues/1/reactions) cat "$GH_FIX/reactions.json";;
    repos/*/issues/1/timeline) printf '[]';;
    repos/*/commits/*) printf '{"sha":"%s"}' "$HEAD";;
  esac
fi
EOF
chmod +x "$tmp/gh"
export PATH="$tmp:$PATH" GH_LOG="$tmp/gh.log" GH_FIX="$fixtures" HEAD=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa GITHUB_REPOSITORY=example/repo PR_NUMBER=1 OPERATION=reconcile GITHUB_RUN_ID=1 GITHUB_RUN_ATTEMPT=1 GITHUB_ACTOR=tester
printf '%s' '{"state":"open","draft":false,"head":{"sha":"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"}}' >"$fixtures/pr.json"
printf '%s' '[[{"user":{"login":"chatgpt-codex-connector[bot]","id":7,"node_id":"N"},"body":"<!-- codex-pull-request-review-summary -->\n<!-- codex-security-review:v1 {\"status\":\"completed\",\"headSha\":\"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\",\"repository\":\"example/repo\",\"pullRequestNumber\":1} -->\n| 📝 **Code Review** | ✅ **Completed** <relative-time datetime=\"2026-10-09T01:00:00Z\">now</relative-time> | `aaaaaaa` |\n| 🔒 **Security Review** | ✅ **Completed** <relative-time datetime=\"2026-10-09T01:00:01Z\">now</relative-time> | `aaaaaaa` |"}]]' >"$fixtures/comments.json"
printf '%s' '[[{"user":{"login":"chatgpt-codex-connector[bot]","id":7,"node_id":"N"},"content":"+1"}]]' >"$fixtures/reactions.json"
printf '%s' '[[]]' >"$fixtures/reviews.json"
bash "$tmp/evidence.sh"; (source "$tmp/production.sh")
grep -q 'POST' "$tmp/gh.log"
printf '%s' '[[{"id":9,"user":{"login":"github-actions[bot]","type":"Bot"},"state":"APPROVED","body":"<!-- codex-automation-approval:v1 -->","commit_id":"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"},{"id":8,"user":{"login":"other-reviewer","type":"User"},"state":"APPROVED"}]]' >"$fixtures/reviews.json"
sed -i '' 's/"draft":false/"draft":true/' "$fixtures/pr.json"
: >"$tmp/gh.log"; bash "$tmp/evidence.sh"; (source "$tmp/production.sh") || true
grep -q 'PUT.*dismissals' "$tmp/gh.log"; ! grep -q 'reviews/8/dismissals' "$tmp/gh.log"
sed -i '' 's/"draft":true/"draft":false/' "$fixtures/pr.json"
perl -0pi -e 's/\*\*Code Review\*\* \| ✅ \*\*Completed/\*\*Code Review** | 🔄 **Running/' "$fixtures/comments.json"
export GITHUB_EVENT_NAME=issue_comment GITHUB_EVENT_ACTION=edited GITHUB_OUTPUT="$tmp/output"
: >"$tmp/gh.log"; bash "$tmp/evidence.sh"; source "$tmp/running.sh"
test "$(grep -c 'PUT.*dismissals' "$tmp/gh.log")" -eq 1
echo 'workflow behavior: approval and selective withdrawal calls observed'
