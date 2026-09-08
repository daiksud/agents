---
description: プルリクエストに Copilot Code Review をリクエストする方法。
---

# Copilot Code Review のリクエスト

プルリクエストへ Copilot Code Review を割り当てるには、`gh` CLI の `gh api graphql`
サブコマンドを使い、`requestReviews` ミューテーションで Copilot のボット ID
(`BOT_kgDOCnlnWA`) をレビュアーとして指定します。

## 手順

1. 対象プルリクエストの Node ID (`pullRequestId`) を取得します。

   ```bash
   gh api graphql -f query='
     query($owner: String!, $repo: String!, $number: Int!) {
       repository(owner: $owner, name: $repo) {
         pullRequest(number: $number) { id }
       }
     }' -F owner="OWNER" -F repo="REPO" -F number=PR_NUMBER \
     --jq '.data.repository.pullRequest.id'
   ```

2. 取得した `pullRequestId` を使い、`requestReviews` ミューテーションで
   Copilot をレビュアーとして追加します。

   ```bash
   gh api graphql -f query='
     mutation($pullRequestId: ID!) {
       requestReviews(input: {
         pullRequestId: $pullRequestId,
         botIds: ["BOT_kgDOCnlnWA"]
       }) {
         pullRequest { id }
       }
     }' -f pullRequestId="PR_NODE_ID"
   ```

## 補足

- `botIds: ["BOT_kgDOCnlnWA"]` は Copilot Code Review ボットの GraphQL ノード ID
  です。他のレビュアーと同時に指定する場合は `userIds` や `teamIds` を
  併用できます。
- `gh pr view <number> --json id --jq .id` でも `pullRequestId` を取得できます。
