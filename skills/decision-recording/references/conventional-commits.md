---
type: Guide
title: Conventional Commitsとcommitlint
description: コミットとPRの書式を揃え、単独で動くcommitlintワークフローを導入する。
---

## 件名と本文

コミット件名とPRタイトルには、[Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)の形式を使う。

```text
<type>[optional scope][!]: <description>
```

- `type` は変更の目的で選ぶ。例は `feat`、`fix`、`docs`、`refactor`、`test`、`ci`。
- `scope` は対象の領域やモジュールを示す。不要なら省く。
- `description` は実際の変更を簡潔に述べる。例は `fix(parser): reject empty input`。
- 互換性を壊す変更は、件名の `!` または `BREAKING CHANGE: 説明` のfooterで示し、影響と必要な移行方法を説明する。
- 本文とfooterは空行で区切る。PRタイトルを件名、PR本文を本文・footerとして、そのままマージ時のコミットに残す。

[PRテンプレート](../assets/pull_request_template.md)の見出しを使い、問題、判断理由、検証状況を変更の規模に合わせて書く。リンク先に説明を委ねない。採用理由や比較結果を省略して書式だけを満たさない。

## 設定の選択

実行の基本形は次のとおり。

```sh
bunx --bun --package @commitlint/cli@latest commitlint --default-config
```

[commitlintの標準の設定探索](https://commitlint.js.org/reference/configuration.html)を利用する。`commitlint.config.mjs`、`.commitlintrc`、`package.json` の `commitlint` フィールドなど、利用者が用意した設定を尊重する。ファイル名の判定や優先順位をワークフローで作り直さない。

[`--default-config`](https://commitlint.js.org/reference/cli.html)は、ルールが見つからない場合にCLI内蔵の `@commitlint/config-conventional` を使う。標準ではルール、除外条件、警告の扱いを上書きしない。ユーザー設定のルールがあれば、その設定を使う。設定の構文エラーや依存関係の読み込み失敗を、標準設定への切り替えで隠さない。

標準設定ではリポジトリへの依存追加や設定ファイルの作成は不要。次の範囲で実行環境と設定を扱う。

| 対象 | 扱い |
| --- | --- |
| Bun | `setup-bun` の `bun-version: latest` で導入する |
| commitlint | `bunx` で `@commitlint/cli@latest` を取得し、`--bun` でBunのランタイムを使う |
| リポジトリの設定 | commitlintの標準探索で読み込む |
| リポジトリの依存バージョン・スクリプト | ランタイムやCLIの自動選択には使わず、依存関係の一括インストールもしない |
| 管理済みのランタイム・CLIバージョン | 利用者がワークフローを変更して指定する |
| 設定が参照する外部プリセット・プラグイン | 利用者が必要な依存関係の導入手順をワークフローに追加する |

[`setup-bun`](https://github.com/oven-sh/setup-bun)はバージョン省略時に `package.json` を参照するため、`latest` を明示する。[`bunx`](https://bun.com/docs/pm/bunx)にも `@latest` を指定し、リポジトリ内のCLIを自動選択させない。

## ワークフローの導入

1. [commitlint.yml](../assets/commitlint.yml)を導入先の `.github/workflows/commitlint.yml` に配置する。
2. PRで `commitlint` ジョブの実行を確認し、[必須チェックの設定](github-settings.md#commitlintを必須チェックにする)を行う。

ワークフローはPRイベントだけで実行する。検査対象は次のとおり。

| イベント | 対象 |
| --- | --- |
| PRの作成・再開・コミット追加・編集 | base SHAからhead SHAまでの各コミットメッセージと、PRタイトル・空行・本文をつないだ一つのメッセージ |

PRの `edited` を含め、タイトル・本文だけの編集でも検査する。PR本文だけを独立したコミットメッセージとして検査しない。マージコミットを選ぶ場合も、PR内の各コミットを検査対象にする。

コミット範囲の取得には全履歴を使い、GitHubがPR検証用に作る仮のマージコミットを対象に混ぜない。ジョブ名は `commitlint` とし、Draft状態や変更ファイルによるスキップを設けない。PRの文字列は環境変数から引用して渡す。設定ファイルの実行を伴うため、書き込み権限を持つ `pull_request_target` には置き換えない。

commitlintが検査するのは書式であり、本文の有無や判断理由の十分性を保証しない。標準の除外条件に合うメッセージは検査が省略される。記録内容はレビューで確認し、[マージ時の保存手順](github-settings.md#最終prタイトルと本文を保存する)で最終的な文字列を揃える。
