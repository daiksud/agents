---
type: Guide
title: GitHubの記録とマージ設定
description: PRタイトルと本文をコミットに保存するため、マージ方式とメッセージを設定する。
---

## 現在の設定と変更箇所を確認する

対象リポジトリのマージ設定、既定ブランチのルールセット・ブランチ保護、PRテンプレート、既存のコミット検査を確認する。期待値との差分と変更箇所を示す。同等の設定はそのまま利用する。

設定変更を依頼されている範囲で適用し、変更後に読み戻して確認する。ファイルの配置やガイドの作成だけを依頼されている場合は、設定の変更箇所を案内する。確認できない設定を適用済みとして報告しない。

## マージ方式とメッセージを設定する

GitHubの **Settings → General → Pull Requests** で、次のように設定する。

1. `Allow squash merging` と `Allow merge commits` を有効にする。
2. `Allow rebase merging` を無効にする。
3. スカッシュとマージコミットの両方で、既定メッセージに `Pull request title and description` を選ぶ。

[スカッシュの設定](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/configuring-commit-squashing-for-pull-requests)と[マージコミットの設定](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/configuring-commit-merging-for-pull-requests)に対応する[REST API](https://docs.github.com/en/rest/repos/repos#update-a-repository)の期待値は次のとおり。

| 設定 | 値 |
| --- | --- |
| `allow_squash_merge` | `true` |
| `allow_merge_commit` | `true` |
| `allow_rebase_merge` | `false` |
| `squash_merge_commit_title` | `PR_TITLE` |
| `squash_merge_commit_message` | `PR_BODY` |
| `merge_commit_title` | `PR_TITLE` |
| `merge_commit_message` | `PR_BODY` |

APIで設定する場合は、対象を示す `OWNER/REPO` を置き換える。現状を取得して差分を確認し、変更対象のフィールドを送る。両方式をまとめて設定する例は次のとおり。

```sh
gh api --method PATCH repos/OWNER/REPO \
  -F allow_squash_merge=true \
  -F allow_merge_commit=true \
  -F allow_rebase_merge=false \
  -f squash_merge_commit_title=PR_TITLE \
  -f squash_merge_commit_message=PR_BODY \
  -f merge_commit_title=PR_TITLE \
  -f merge_commit_message=PR_BODY
```

実行後に `gh api repos/OWNER/REPO` で再取得し、表の期待値と比較する。書き込みAPIの成功だけで確認を終えない。

## ブランチのルールと揃える

`Settings → Rules → Rulesets` と、利用している場合は `Settings → Branches` のブランチ保護を確認する。組織から適用されるルールも含め、対象ブランチに効くルールを確認する。

- `Require linear history` はマージコミットを禁止するため、この運用を適用するブランチでは解除する。
- `Require a pull request before merging` の許可するマージ方式も、スカッシュとマージコミットに揃える。
- 変更対象以外のレビュー要件、必須チェック、権限などは保持する。変更できないルールがある場合は、対象と未適用の差分を報告する。

各項目の仕様は[ルールセットで利用できるルール](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets)で確認する。

## 最終PRタイトルと本文を保存する

形式検査を導入している場合は、PRタイトル・本文の編集にも適用し、マージ前に最新の結果が成功していることを確認する。

1. 最終PRタイトル・本文がレビュー済みの変更、判断理由、実際の検証状況を表していることを確認する。リンク先を読まなくても判断を理解できる内容にし、案内用のHTMLコメントをすべて除去する。
2. マージ直前にPRタイトル、本文、head SHAを取得する。スカッシュかマージコミットを選び、取得したタイトルと本文をマージ時のメッセージに指定する。
3. マージが完了したことと生成されたコミットSHAを確認し、そのコミットの件名・本文が最終PRタイトル・本文と一致することを確認する。

GitHubのメッセージ設定は既定値であり、マージ時に編集できる。既定値の設定だけで本文の保存を保証したとみなさず、翻訳・要約・別の説明への置き換えをせずに保存する。

[マージAPI](https://docs.github.com/en/rest/pulls/pulls#merge-a-pull-request)を使う場合は、`commit_title` に最終タイトル、`commit_message` に最終本文、`sha` に確認したhead SHAを渡す。`merge_method` は `squash` または `merge` とする。どちらの方式でも、必要な承認・CI・競合解消を満たしてからマージする。
