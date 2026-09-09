---
type: Instruction
title: レビューとマージ
description: PR作成、レビュー対応、CI確認、リベース、スカッシュマージの手順を定めます。
---

# レビューとマージ

## PRとレビュー

- プッシュ後にドラフトPRを作成し、対象のIssueまたはSub-issueに紐づける。
- オーバーエンジニアリングを避けるため、PR本文に「やらないこと」「許容すること」の見出しを設ける。
- 「やらないこと」には、今回の変更で対象外とする作業を明記する。
- 「許容すること」には、目標を満たしたうえで受け入れる制約を明記する。
- 「やらないこと」「許容すること」に該当する項目がない場合は、それぞれ「なし」と記載する。
- ドラフトPRで [Copilot Code Review](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/request-a-code-review/use-code-review) または [Codex Code Review](https://learn.chatgpt.com/docs/third-party/github) を依頼する。
- Copilotへの依頼にはこの文書の「Copilot Code Reviewの依頼」を使用する。
- 初回・再レビューの依頼後は、レビュー完了までセルフレビューを行う。
- セルフレビューで修正すべき点を見つけたら、修正・検証・コミット・プッシュしてPRを更新する。
- レビュー待ちの間に、CIの結果とコンフリクトの有無を確認する。
- CIが未設定の場合は、マージ条件上「CIがパス」とみなす。
- CIが未設定の場合は、未設定なのでパスとみなす旨と、CI設定を強く推奨する旨をPRにコメントする。
- CIの失敗やコンフリクトがあれば、修正・検証・コミット・プッシュしてPRを更新する。
- レビュー指摘は重要度・緊急度・発生条件・再現性を検討し、修正すべきか判断する。
- 再現に必要な前提条件が多く複雑である、再現性が低いなどの指摘は修正しない。
- レビュー結果で「Suppressed comments」などと明示され、レビュアーが抑制した指摘は修正しない。
- 修正しない指摘は判断理由を対象スレッドに返信し、対応が必要な未解決の指摘と区別する。
- 修正した指摘は、対応内容、変更コミット、検証結果を対象スレッドに返信する。
- レビュースレッドをResolveする前に、対応内容または対応しない理由の返信が投稿されたことを確認する。
- 返信の投稿に失敗した場合はResolveしない。
- 修正する指摘は、修正・検証・コミット・プッシュした後に再レビューを依頼する。
- セルフレビューやCI対応、リベースでレビュー対象のコミットが変わった場合も、最新コミットへの再レビューを依頼する。
- 対応が必要な指摘がゼロになるまでレビューと修正を繰り返す。
- Copilot Code Reviewを利用する場合は、CopilotのApproveを得るまで完了としない。

## リベースとマージ

- マージ先の更新を作業ブランチに取り込むときはリベースし、Git履歴をLinear historyに保つ。
- リベース後は関連する検証を再実行し、リモートへプッシュする。
- プッシュ済みの履歴をリベースした場合は `git push --force-with-lease` を使い、リモートに未知の更新があれば上書きせず確認する。
- マージ直前に、最新コミットのレビューが完了し、対応が必要な指摘がゼロ、CIがパス、コンフリクトがゼロであることを確認する。
- すべての条件を満たしたらドラフトPRをReady for reviewに変更し、スカッシュマージする。
- スカッシュコミットのメッセージも[コミットメッセージの指示](conventional-commits.md)に従う。
- PRがマージ済みで、マージ先の履歴が直線状であることを確認する。

## Copilot Code Reviewの依頼

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
