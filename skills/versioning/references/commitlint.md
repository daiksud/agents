---
type: Guide
title: commitlintの導入
description: 既存設定を尊重してPRのコミットと最終メッセージを検査し、必須チェックを整える。
---

## 設定の選択

実行の基本形は次のとおり。

```sh
bunx --bun --package @commitlint/cli@21.2.4 commitlint --default-config
```

[commitlintの標準の設定探索](https://commitlint.js.org/reference/configuration.html)を利用する。`commitlint.config.mjs`、`.commitlintrc`、`package.json` の `commitlint` フィールドなど、利用者が用意した設定を尊重する。ファイル名の判定や優先順位をワークフローで作り直さない。

[`--default-config`](https://commitlint.js.org/reference/cli.html)は、ルールが見つからない場合にCLI内蔵の `@commitlint/config-conventional` を使う。標準ではルール、除外条件、警告の扱いを上書きしない。ユーザー設定のルールがあれば、その設定を使う。設定の構文エラーや依存関係の読み込み失敗を、標準設定への切り替えで隠さない。

標準設定ではリポジトリへの依存追加や設定ファイルの作成は不要。次の範囲で実行環境と設定を扱う。

| 対象 | 扱い |
| --- | --- |
| Bun | `setup-bun` の `bun-version: 1.4.4` で導入する |
| commitlint | `bunx` で `@commitlint/cli@21.2.4` を取得し、`--bun` でBunのランタイムを使う |
| リポジトリの設定 | commitlintの標準探索で読み込む |
| リポジトリの依存バージョン・スクリプト | ランタイムやCLIの自動選択には使わず、依存関係の一括インストールもしない |
| 管理済みのランタイム・CLIバージョン | 利用者がワークフローを変更して指定する |
| 設定が参照する外部プリセット・プラグイン | 利用者が必要な依存関係の導入手順をワークフローに追加する |

[`setup-bun`](https://github.com/oven-sh/setup-bun)はバージョン省略時に `package.json` を参照するため、`bun-version` に `1.4.4` を明示する。[`bunx`](https://bun.com/docs/pm/bunx)にも `@commitlint/cli@21.2.4` を指定し、リポジトリ内のCLIを自動選択させない。バージョンを更新するときは、ワークフローとこのガイドを揃える。

## ワークフローの導入

1. [commitlint.yml](../assets/commitlint.yml)を導入先の `.github/workflows/commitlint.yml` に配置する。
2. PRで `commitlint` ジョブの実行を確認し、[必須チェックの設定](#commitlintを必須チェックにする)を行う。

ワークフローはPRイベントだけで実行する。検査対象は次のとおり。

| イベント | 対象 |
| --- | --- |
| PRの作成・再開・コミット追加・編集 | base SHAからhead SHAまでの各コミットメッセージと、PRタイトル・空行・本文をつないだ一つのメッセージ |

PRの `edited` を含め、タイトル・本文だけの編集でも検査する。PR本文だけを独立したコミットメッセージとして検査しない。マージコミットを選ぶ場合も、PR内の各コミットを検査対象にする。

各イベントで、PR本文にHTMLコメントの開始記号 `<!--` が残っていないことも検査する。コード例の中や閉じていないコメントも対象にし、開始記号があれば失敗させる。commitlintのルールとは別のステップで実行するため、利用者の設定や標準の除外条件にかかわらず検査する。PRの作成・更新前に、案内用のコメントを含むすべてのHTMLコメントを削除する。

コミット範囲の取得には全履歴を使い、GitHubがPR検証用に作る仮のマージコミットを対象に混ぜない。ジョブ名は `commitlint` とし、Draft状態や変更ファイルによるスキップを設けない。PRの文字列は環境変数から引用して渡す。設定ファイルの実行を伴うため、書き込み権限を持つ `pull_request_target` には置き換えない。

commitlintが検査するのは書式であり、本文の有無や判断理由の十分性を保証しない。標準の除外条件に合うメッセージは検査が省略される。記録内容はレビューで確認し、[マージ後に残す情報](conventional-commits.md#マージ後に残す情報)と実際のコミットを揃える。

## commitlintを必須チェックにする

設定変更を依頼されている範囲で適用する。ファイルの配置だけを依頼されている場合は、必要な設定を案内する。

1. [ワークフロー](../assets/commitlint.yml)を導入し、PRで `commitlint` ジョブが実行されることを確認する。導入方法と検査対象は[ワークフローの導入](#ワークフローの導入)を使う。
2. 対象ブランチのルールセット、または既存のブランチ保護で `Require status checks to pass before merging` を有効にする。
3. 必須チェックに `commitlint` を追加し、提供元を指定できる場合はGitHub Actionsを選ぶ。
4. 設定を再取得し、対象ブランチに `commitlint` が要求されることを確認する。

他の必須チェックは保持する。同じ検査を担う既存の `prlint` などを置き換える場合は、`commitlint` が実行されることを確認してから、不要になるチェック名を必須条件から外す。別のワークフローに同じジョブ名を付けない。

PRのタイトル・本文の編集でも `commitlint` を実行し、マージ前に最新の検査結果が成功していることを確認する。
