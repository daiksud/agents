---
type: Guide
title: バージョン戦略スキルの出典
description: コミット規約、形式検査、バージョン計算の方針と一次資料の対応を示す。
sources:
  - id: agents-versioning
    resource: https://github.com/daiksud/agents/issues/281
  - id: agents-versioning-adoption
    resource: https://github.com/daiksud/agents/issues/283
  - id: agents-skill-independence
    resource: https://github.com/daiksud/agents/issues/285
  - id: agents-release-versioning
    resource: https://github.com/daiksud/agents/issues/279
  - id: recording-source
    resource: https://github.com/daiksud/agents/blob/d4e677be602be08f24dfc72fae8dea444be86b37/skills/decision-recording/references/conventional-commits.md
  - id: commitlint-workflow-source
    resource: https://github.com/daiksud/agents/blob/d4e677be602be08f24dfc72fae8dea444be86b37/skills/decision-recording/assets/commitlint.yml
  - id: semver
    resource: https://semver.org/spec/v2.0.0.html
  - id: conventional-commits
    resource: https://www.conventionalcommits.org/en/v1.0.0/
  - id: commitlint-configuration
    resource: https://commitlint.js.org/reference/configuration.html
  - id: commitlint-cli
    resource: https://commitlint.js.org/reference/cli.html
  - id: commitlint-ci
    resource: https://commitlint.js.org/guides/ci-setup.html
  - id: semantic-release-commit-analyzer
    resource: https://github.com/semantic-release/commit-analyzer
  - id: semantic-release-faq
    resource: https://semantic-release.org/support/faq/
  - id: actions-checkout
    resource: https://github.com/actions/checkout
  - id: github-workflow-dispatch-inputs
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#onworkflow_dispatchinputs
  - id: setup-bun
    resource: https://github.com/oven-sh/setup-bun
  - id: bunx
    resource: https://bun.com/docs/pm/bunx
  - id: github-required-checks
    resource: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets
  - id: github-merge-queue
    resource: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue
---

## 対象と方針

[versioning](../../skills/versioning/SKILL.md)はセマンティックバージョニングとConventional Commitsを使い、コミット規約とバージョン戦略を整備する。規約・commitlintだけの導入と、コミット履歴からの自動計算の両方に対応する。[^agents-versioning][^agents-versioning-adoption]

バージョン計算の設定はversioningが扱い、デプロイ・リリースとの接続はcontinuous-deliveryが扱う。commitlintの導入ガイドとワークフローはversioningとdecision-recordingの両方に同梱し、それぞれのスキル内で導入を完結できるようにする。共通の導入手順や検査内容、固定バージョンを変更するときは両方の同梱資料を揃える。[^agents-skill-independence] [スキルの選び方](../../README.md)

元の継続的デリバリー文書の出典と確認履歴は[その出典文書](continuous-delivery.md)に保持している。

## 記述と出典の対応

| 記述 | 根拠と適用範囲 |
| --- | --- |
| [コミットの形式](../../skills/versioning/references/conventional-commits.md) | Conventional Commitsは件名、本文、フッターと破壊的変更の表記を定める。PRタイトルへの適用と、最終タイトル・本文の検査はこのスキルの運用方針であり、規格自体の必須条件ではない。[^conventional-commits][^recording-source] |
| [更新規則](../../skills/versioning/references/semantic-versioning.md) | SemVerは公開APIの互換性、非推奨化、下位番号のリセットを定める。Conventional Commitsは `feat`、`fix`、破壊的変更を採番に対応付ける。[^semver][^conventional-commits] このスキルでは、互換性を保つ公開APIの非推奨化を `feat` で記録し、minorとする。速度改善の `perf` もminorとする。機能を変えずに利用者への配布物を変える変更はpatch、配布物が変わらない `docs`・`test`・`ci` は更新対象外とする。 |
| 計算する履歴 | 対象SHAと前回の正式リリースタグを固定し、完全なコミットメッセージを解析する。checkoutの `fetch-depth: 0` は履歴とタグの取得に使う。[^agents-release-versioning][^actions-checkout] |
| 初回・0.x・プレリリース | SemVerは `0.x` とプレリリースを認める。このスキルでは初めて更新対象があるときに `v0.1.0` を公開し、以後 `0.x` の破壊的変更はminorとする。semantic-releaseはmajor 0の特別な扱いをサポートしないため、この規則に対応する計算ツールを選ぶ。[^semver][^semantic-release-faq] |
| v1への昇格 | GitHub Actionsの `workflow_dispatch` はboolean入力を `inputs` で真偽値として参照できる。[^github-workflow-dispatch-inputs] このスキルでは `0.x` のリリースワークフローに既定値falseの `promote to v1` チェックボックスを設ける。選択すると追加の変更がなくても `v1.0.0` を公開し、公開に成功した後で入力と昇格処理を削除する。 |
| パーサーと計算ツール | commitlintのconventional設定はConventional Commitsのプリセットを使う。commit-analyzerは `angular` が既定で、独自規則に一致しない場合は既定規則を適用する。既定では `perf` がpatchになるため、minorを明示する。破壊的変更はどのtypeでも優先し、配布物の差分も判定に使う。[^commitlint-configuration][^semantic-release-commit-analyzer] |
| [commitlintの設定](../../skills/versioning/references/commitlint.md) | 標準の設定探索は `commitlint.config.mjs` や `package.json` の `commitlint` を扱う。`--default-config` はルールが見つからない場合の内蔵設定を選ぶ。既存設定を尊重し、設定エラーを標準設定への切り替えで隠さない。[^commitlint-configuration][^commitlint-cli] |
| [ワークフロー](../../skills/versioning/assets/commitlint.yml) | PRのコミット範囲とタイトル・本文を検査する。別のステップで、PR本文にHTMLコメントの開始記号が残っていないことを確認する。Bun `1.4.4`、commitlint `21.2.4`、外部ActionのSHAを固定する。バージョン指定付きのbunxはローカルCLIを選ばず、`--bun` は実行ランタイムを指定する。[^commitlint-workflow-source][^commitlint-ci][^setup-bun][^bunx] |
| 必須チェック | 同梱の `commitlint` はPRで結果を報告する。GitHubのマージキューでは `merge_group` にも必須チェックの結果が要る。このスキルではPRでcommitlintと製品の基本検証、キューでグループの基本検証と成果物検査を集約し、両イベントで結果を確認してから必須条件を切り替える。[^github-required-checks][^github-merge-queue] |

[^agents-versioning]: [独立スキル作成の目的と範囲](https://github.com/daiksud/agents/issues/281)。
[^agents-versioning-adoption]: [スキルの採用と使用する規約の方針](https://github.com/daiksud/agents/issues/283)。
[^agents-skill-independence]: [スキル間参照の解消と設定手順の分担](https://github.com/daiksud/agents/issues/285)。
[^conventional-commits]: [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/)。
[^recording-source]: [移設元のコミット規約と導入ガイド](https://github.com/daiksud/agents/blob/d4e677be602be08f24dfc72fae8dea444be86b37/skills/decision-recording/references/conventional-commits.md)。
[^semver]: [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html)。
[^agents-release-versioning]: [自動バージョン計算の方針](https://github.com/daiksud/agents/issues/279)。
[^actions-checkout]: [checkoutの履歴取得](https://github.com/actions/checkout)。
[^semantic-release-faq]: [semantic-releaseの初回バージョンの制約](https://semantic-release.org/support/faq/)。
[^github-workflow-dispatch-inputs]: [GitHub Actionsの手動実行時の入力](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#onworkflow_dispatchinputs)。
[^commitlint-configuration]: [commitlintの設定とパーサー](https://commitlint.js.org/reference/configuration.html)。
[^semantic-release-commit-analyzer]: [commit-analyzerの設定と判定規則](https://github.com/semantic-release/commit-analyzer)。
[^commitlint-cli]: [commitlint CLI](https://commitlint.js.org/reference/cli.html)。
[^commitlint-workflow-source]: [移設元の固定バージョン付きワークフロー](https://github.com/daiksud/agents/blob/d4e677be602be08f24dfc72fae8dea444be86b37/skills/decision-recording/assets/commitlint.yml)。
[^commitlint-ci]: [commitlintのCI設定](https://commitlint.js.org/guides/ci-setup.html)。
[^setup-bun]: [Bunのバージョン指定](https://github.com/oven-sh/setup-bun)。
[^bunx]: [bunxのパッケージとランタイムの指定](https://bun.com/docs/pm/bunx)。
[^github-required-checks]: [ルールセットの必須ステータスチェック](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets)。
[^github-merge-queue]: [マージキューで必須チェックを実行する](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue)。
