---
type: Guide
title: GitHubの記録とマージ設定
description: PRタイトルと本文をコミットに保存するため、マージ方式とメッセージを設定する。
---

PRタイトル・本文をマージ時のコミット件名・本文としてそのまま残すことを強く推奨する。既定メッセージを変える依頼と、許可するマージ方式を変える依頼では、次のように設定を選ぶ。

## 現在の設定と変更箇所を確認する

対象リポジトリのマージ設定、対象ブランチで有効なルールセット・ブランチ保護とマージキュー、PRテンプレート、既存のコミット検査を確認する。依頼された範囲で差分を示し、同等の設定は活かす。ファイルの配置やガイドの作成だけを依頼された場合は、設定の変更箇所を案内する。

## 既定のメッセージを設定する

`Settings → General → Pull Requests` で、対象の方式に `Pull request title and description` を選ぶ。[リポジトリ更新API](https://docs.github.com/en/rest/repos/repos#update-a-repository)では、対象の方式のタイトルと本文を組で指定する。

| 対象の方式 | タイトル | 本文 |
| --- | --- | --- |
| [スカッシュ](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/configuring-commit-squashing-for-pull-requests) | `squash_merge_commit_title=PR_TITLE` | `squash_merge_commit_message=PR_BODY` |
| [マージコミット](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/configuring-commit-merging-for-pull-requests) | `merge_commit_title=PR_TITLE` | `merge_commit_message=PR_BODY` |

例えば、スカッシュ限定で直線履歴が必須のリポジトリで、スカッシュ時にPR本文を残したい場合は次の2項目を送る。`OWNER/REPO` は対象リポジトリに置き換える。

```sh
gh api --method PATCH repos/OWNER/REPO \
  -f squash_merge_commit_title=PR_TITLE \
  -f squash_merge_commit_message=PR_BODY
```

## 許可するマージ方式を変更する

スカッシュとマージコミットの両方を許可し、リベースマージを禁止する方針の導入を依頼された場合は、現在値と照合して次の設定を適用する。

```sh
gh api --method PATCH repos/OWNER/REPO \
  -F allow_squash_merge=true \
  -F allow_merge_commit=true \
  -F allow_rebase_merge=false
```

両方式を対象ブランチで使えるようにするには、`Require a pull request before merging` が許可する方式も揃える。`Require linear history` はマージコミットと両立しないため、両方式の導入を依頼された場合にだけ解除の要否と変更権限を確認する。組織のルールなどにより両立できない場合は差分を報告する。[ルールセットで利用できるルール](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets)

設定後は `gh api repos/OWNER/REPO` と対象ブランチの実効ルールを読み戻し、依頼された値と照合する。

## 最終PRタイトルと本文を保存する

PR作成・更新前にHTMLコメントをすべて除去する。マージ直前に最終タイトル・本文とhead SHAを取得し、記録がレビュー済みの変更、判断理由、実際の検証状況を表し、必要な承認と最新の必須チェックを満たすことを確認する。

| マージ経路 | APIを使う場合の操作 |
| --- | --- |
| 通常のPRを直接マージ | [マージAPI](https://docs.github.com/en/rest/pulls/pulls#merge-a-pull-request)に `sha`、最終タイトルの `commit_title`、最終本文の `commit_message` と、許可された `merge_method`（`squash` または `merge`）を渡す。 |
| ネイティブのStacked PRを直接マージ | 1件ずつ統合するには最下段の未統合PRを選ぶ。[非同期マージAPI](https://docs.github.com/en/rest/pulls/pulls#merge-a-pull-request-asynchronously)に `merge_action=direct_merge` と通常の直接マージと同じ引数を渡す。受付時にUUIDが返ったら、そのUUIDで結果を取得して `merged` とコミットSHAを確認する。[スタックのマージ手順](https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/merging-stacked-pull-requests) |
| マージキュー経由（スタックを含む） | 投入前にキューのマージ方式と、その方式の既定メッセージを確認する。PR単位の原文保存が必須で設定が対応しない場合は、投入を見合わせて差分を伝える。非同期APIでは `merge_action=merge_queue` と `sha` を指定する。方式・タイトル・本文の引数は直接マージ専用。`enqueued` の後は対象PRが実際にマージされるまで状態を確認する。 |

検証失敗などでキューから取り除かれた場合は、その理由を報告する。統合後は対象PRごとに生成されたコミットのSHAを特定し、件名と本文をPRの最終タイトル・本文と照合する。差異があれば実際に保存された内容を報告する。
