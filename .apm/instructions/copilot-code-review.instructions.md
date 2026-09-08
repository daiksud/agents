---
type: Instruction
title: Copilot Code Review
description: Copilot Code Review をリクエストする方法
---

# Copilot Code Review

1. Pull Request ID を取得する:
   ```bash
   PR_ID=$(gh pr view <PR_NUMBER> --json id --jq .id)
   ```
2. Copilot Code Review を依頼する:
   ```bash
   gh api graphql \
     -f query='mutation($pullRequestId: ID!) { requestReviews(input:{pullRequestId:$pullRequestId, botIds:["BOT_kgDOCnlnWA"]}) { clientMutationId } }' \
     -f pullRequestId="$PR_ID"
   ```
