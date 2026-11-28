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

1. 既存のcommitlintジョブを再利用する場合は、次のイベントと検査範囲に照らして不足分を補う。新規のPR専用ワークフローには[commitlint.yml](../assets/commitlint.yml)を導入先の `.github/workflows/commitlint.yml` に配置する。マージキューで必須にする場合は、下記の集約チェックに組み込む。
2. PRで対象のジョブが実行されることを確認する。必須チェックにする場合は、[必須チェックの設定](#commitlintを必須チェックにする)に従う。

同梱ワークフローはPRイベントで実行する。検査対象は次のとおり。

| イベント | 対象 |
| --- | --- |
| PRの作成・再開・コミット追加・編集 | base SHAからhead SHAまでの各コミットメッセージと、PRタイトル・空行・本文をつないだ一つのメッセージ |

PRの `edited` を含め、タイトル・本文だけの編集でも検査する。PR本文だけを独立したコミットメッセージとして検査しない。マージコミットを選ぶ場合も、PR内の各コミットを検査対象にする。

各イベントで、PR本文にHTMLコメントの開始記号 `<!--` が残っていないことも検査する。コード例の中や閉じていないコメントも対象にし、開始記号があれば失敗させる。commitlintのルールとは別のステップで実行するため、利用者の設定や標準の除外条件にかかわらず検査する。PRの作成・更新前に、案内用のコメントを含むすべてのHTMLコメントを削除する。

コミット範囲の取得には全履歴を使い、GitHubがPR検証用に作る仮のマージコミットを対象に混ぜない。ジョブ名は `commitlint` とし、Draft状態や変更ファイルによるスキップを設けない。PRの文字列は環境変数から引用して渡す。設定ファイルの実行を伴うため、書き込み権限を持つ `pull_request_target` には置き換えない。

commitlintが検査するのは書式であり、本文の有無や判断理由の十分性を保証しない。標準の除外条件に合うメッセージは検査が省略される。記録内容はレビューで確認する。マージ時は、検査したメッセージと実際のコミットを揃える。[GitHub設定ガイド](github-settings.md)

## commitlintを必須チェックにする

対象ブランチのマージ方法に合わせて、必須にするチェックを選ぶ。

| マージ方法 | 必須チェックと成功条件 |
| --- | --- |
| マージキューを使わない | PRで実行するcommitlintジョブを必須にできる。同梱ワークフローのチェック名は `commitlint`、提供元はGitHub Actions。 |
| マージキューを使う | PRと `merge_group` で同名の集約チェックを報告する。PRでは最新のタイトル・本文を含む `commitlint` と `screening`（ビルド・テストなど）、キューではグループのhead SHAに対する `screening` と `inspection`（成果物の検査）の成功を条件にする。 |

キューを使う場合は、PRの集約チェックを持つワークフローに同梱例の `commitlint` ジョブを組み込み、`edited` でも起動するようにする。後続の編集で古いcommitlintを取り消す `concurrency` は、そのジョブに設定する。ワークフロー全体に適用すると、同時に進んでいる製品検証まで取り消される。キュー側は `merge_group` の `checks_requested` で集約チェックを報告する。[GitHubのマージキューの設定](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue)

PRのタイトル・本文だけを編集した場合はcommitlintを再実行する。集約チェックは、同じbase・head・テスト用マージSHAに対する `screening` の完了を待つか、その成功結果を再利用する。マージ先が変われば新しい組み合わせで `screening` を実行する。ジョブのスキップや過去のSHAでの成功は製品検証の結果に含めない。

ファイルの配置だけを依頼された場合は、必須にするチェック名と設定手順を案内する。設定変更の依頼には次の順で対応する。

1. 対象ブランチのPRで選んだチェックが成功し、キューを使う場合は `merge_group` でも集約チェックが成功したことを確認する。
2. 対象のルールセットまたは既存のブランチ保護で `Require status checks to pass before merging` を有効にし、確認したチェック名を指定する。提供元を指定できる場合は実際の提供元を選ぶ。別用途のジョブには別のチェック名を使う。
3. 置き換え先を必須にしてから、同じ検査を担っていた `prlint` などの旧チェック名を外す。設定を再取得し、対象ブランチで新しいチェックと他の既存チェックが要求されていることを確認する。
