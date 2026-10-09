#!/usr/bin/env bash
set -euo pipefail

workflow=.github/workflows/approve-codex-review.yml
! grep -qi python "$workflow"
grep -Fq 'Withdraw approval while Codex review is running' "$workflow"
grep -Fq 'Approve current clean Codex evidence' "$workflow"

pages='[[{"user":{"login":"other-reviewer"},"state":"APPROVED"}],[{"user":{"login":"github-actions[bot]"},"state":"APPROVED","body":"<!-- codex-automation-approval:v1 -->"}]]'
reviews=$(jq 'add' <<<"$pages")
test "$(jq 'length' <<<"$reviews")" = 2
test "$(jq '[.[] | select(.user.login == "other-reviewer")] | length' <<<"$reviews")" = 1

summary='| 📝 **Code Review** | 🔄 **Running** | `abc1234` | Manual |'
! grep -Fq '✅ **Completed**' <<<"$summary"
grep -Fq '🔄 **Running**' <<<"$summary"
