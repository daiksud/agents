#!/usr/bin/env bash
set -euo pipefail
root=$(cd "$(dirname "$0")/.." && pwd)
tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT
awk '/- name: Approve completed Codex reviews/{capture=1} capture && /^        run: \|/{run=1; next} run{sub(/^          /, ""); print}' "$root/.github/workflows/approve-codex-review.yml" >"$tmp/approve.sh"
test -s "$tmp/approve.sh"
export PATH="$tmp:$PATH" GH_LOG="$tmp/calls" COUNT_FILE="$tmp/count"
export GITHUB_REPOSITORY=example/repo PR_NUMBER=1 COMMENT_ID=7
cat >"$tmp/gh" <<'MOCK'
#!/usr/bin/env bash
set -euo pipefail
printf '%s\n' "$*" >>"$GH_LOG"
case "$*" in
  'api repos/example/repo/issues/comments/7 --jq .body')
    count=$(( $(cat "$COUNT_FILE") + 1 )); echo "$count" >"$COUNT_FILE"
    [[ "$SCENARIO" != comment-error ]] || exit 1
    echo '<!-- codex-pull-request-review-summary -->'
    for kind in 'Code Review' 'Security Review'; do
      status='✅ **Completed**'
      if [[ "$kind" == "${INCOMPLETE_KIND:-}" && ( "$SCENARIO" == incomplete || ( "$SCENARIO" == restart && "$count" -gt 1 ) ) ]]; then
        status='🔄 **Running**'
      fi
      printf '| %s | %s <relative-time datetime="2026-10-09T01:00:00Z">now</relative-time> | `old-sha` |\n' "**$kind**" "$status"
    done;;
  'api repos/example/repo/issues/1/reactions?per_page=100 --paginate --slurp')
    [[ "$SCENARIO" != reaction-error ]] || exit 1
    [[ "$SCENARIO" != retry-error || $(cat "$COUNT_FILE") -eq 1 ]] || exit 1
    reaction=eyes
    if (( $(cat "$COUNT_FILE") >= THUMB_AT )); then reaction=+1; fi
    # Another user's thumbs-up is on page one; Codex's reaction is on page two.
    printf '[[{"user":{"login":"someone-else"},"content":"+1"}],[{"user":{"login":"chatgpt-codex-connector[bot]"},"content":"%s"},{"user":{"login":"chatgpt-codex-connector[bot]"},"content":"eyes"}]]' "$reaction";;
  'pr review 1 --repo example/repo --approve')
    [[ "$SCENARIO" != approval-error ]];;
  *) echo "Unexpected GitHub operation: $*" >&2; exit 1;;
esac
MOCK
cat >"$tmp/sleep" <<'MOCK'
#!/usr/bin/env bash
set -euo pipefail
[[ "$*" == 30 ]]
printf 'sleep %s\n' "$*" >>"$GH_LOG"
MOCK
chmod +x "$tmp/gh" "$tmp/sleep"
check() {
  export SCENARIO=$1 THUMB_AT=$2 INCOMPLETE_KIND=${8:-}
  local expected_approvals=$3 expected_sleeps=$4 expected_summaries=$5 expected_reactions=$6 expected_exit=$7 actual_exit=0
  : >"$GH_LOG"; echo 0 >"$COUNT_FILE"
  bash "$tmp/approve.sh" || actual_exit=$?
  test "$actual_exit" -eq "$expected_exit"
  test "$(grep -c '^pr review ' "$GH_LOG" || true)" -eq "$expected_approvals"
  test "$(grep -c '^sleep ' "$GH_LOG" || true)" -eq "$expected_sleeps"
  test "$(cat "$COUNT_FILE")" -eq "$expected_summaries"
  test "$(grep -c '/reactions?' "$GH_LOG" || true)" -eq "$expected_reactions"
  echo "PASS: $SCENARIO ${INCOMPLETE_KIND:-} (thumb check $THUMB_AT)"
}
# Scenario, first Codex thumbs-up check, approvals, sleeps, summary reads, reaction reads, exit.
check immediate 1 1 0 1 1 0
check delayed 3 1 2 3 3 0
check last-check 7 1 6 7 7 0
check timeout 99 0 6 7 7 0
for kind in 'Code Review' 'Security Review'; do
  check incomplete 1 0 0 1 0 0 "$kind"
  check restart 2 0 1 2 1 0 "$kind"
done
check comment-error 1 0 0 1 0 1
check reaction-error 1 0 0 1 1 1
check retry-error 99 0 1 2 2 1
check approval-error 1 1 0 1 1 1
