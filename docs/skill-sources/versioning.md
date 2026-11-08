---
type: Guide
title: バージョン戦略スキルの出典
description: コミット規約、形式検査、バージョン計算の方針と一次資料の対応を示す。
sources:
  - id: agents-versioning
    resource: https://github.com/daiksud/agents/issues/281
  - id: agents-versioning-adoption
    resource: https://github.com/daiksud/agents/issues/283
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
  - id: setup-bun
    resource: https://github.com/oven-sh/setup-bun
  - id: bunx
    resource: https://bun.com/docs/pm/bunx
  - id: github-required-checks
    resource: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets
---

## 対象と方針

[versioning](../../skills/versioning/SKILL.md)はセマンティックバージョニングとConventional Commitsを使い、コミット規約とバージョン戦略を整備する。規約・commitlintだけの導入と、コミット履歴からの自動計算の両方に対応する。[^agents-versioning][^agents-versioning-adoption]

計算・検査の詳細はversioningが持ち、デプロイ・リリースとの接続は[continuous-delivery](../../skills/continuous-delivery/SKILL.md)、判断理由とPR記録の保存は[decision-recording](../../skills/decision-recording/SKILL.md)が扱う。両スキルはversioningの利用を強く推奨し、採用は任意とする。各スキルには目的に必要な短い方針を残す。[^agents-versioning-adoption]

元の継続的デリバリー文書の出典と確認履歴は[その出典文書](continuous-delivery.md)に保持している。

## 記述と出典の対応

| 記述 | 根拠と適用範囲 |
| --- | --- |
| [コミットの形式](../../skills/versioning/references/conventional-commits.md) | Conventional Commitsは件名、本文、フッターと破壊的変更の表記を定める。PRタイトルへの適用と、最終タイトル・本文の検査はこのスキルの運用方針であり、規格自体の必須条件ではない。[^conventional-commits][^recording-source] |
| [更新規則](../../skills/versioning/references/semantic-versioning.md) | SemVerは公開APIの互換性、非推奨化、major・minor・patchの更新と下位番号のリセットを定める。Conventional Commitsは変更の種類と更新を対応付ける。初回 `1.0.0`、更新対象のない履歴では新しい番号を作らないこと、履歴不足を変更なしと扱わないことは採用した運用方針。[^semver][^conventional-commits][^agents-release-versioning] |
| 計算する履歴 | 対象SHAと前回の正式リリースタグを固定し、完全なコミットメッセージを解析する。checkoutの `fetch-depth: 0` は履歴とタグの取得に使う。[^agents-release-versioning][^actions-checkout] |
| 初回・0.x・プレリリース | SemVerは `0.x` とプレリリースを認める。semantic-releaseは初回 `0.0.1` とmajor 0の特別な扱いをサポートしないため、採用する規則に対応するツールを選ぶ。[^semver][^semantic-release-faq] |
| パーサーと計算ツール | commitlintのconventional設定はConventional Commitsのプリセットを使う。commit-analyzerは `angular` が既定で、独自規則に一致しない場合は既定規則を適用し、`perf` をpatchとする。任意のtypeの破壊的変更を保ったまま計算方針に設定を合わせる。[^commitlint-configuration][^semantic-release-commit-analyzer] |
| [commitlintの設定](../../skills/versioning/references/commitlint.md) | 標準の設定探索は `commitlint.config.mjs` や `package.json` の `commitlint` を扱う。`--default-config` はルールが見つからない場合の内蔵設定を選ぶ。既存設定を尊重し、設定エラーを標準設定への切り替えで隠さない。[^commitlint-configuration][^commitlint-cli] |
| [ワークフロー](../../skills/versioning/assets/commitlint.yml) | PRのコミット範囲とタイトル・本文を検査する。Bun `1.4.4`、commitlint `21.2.4`、外部ActionのSHAは移設元の固定値を保持する。変更したのはステップの表示名。バージョン指定付きのbunxはローカルCLIを選ばず、`--bun` は実行ランタイムを指定する。[^commitlint-workflow-source][^commitlint-ci][^setup-bun][^bunx] |
| 必須チェック | 導入したジョブの実行後に `commitlint` を必須チェックへ追加し、設定を読み戻す。実際の設定変更は依頼された範囲で行う。[^github-required-checks] |

[^agents-versioning]: [独立スキル作成の目的と範囲](https://github.com/daiksud/agents/issues/281)。
[^agents-versioning-adoption]: [スキルの採用と使用する規約の方針](https://github.com/daiksud/agents/issues/283)。
[^conventional-commits]: [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/)。
[^recording-source]: [移設元のコミット規約と導入ガイド](https://github.com/daiksud/agents/blob/d4e677be602be08f24dfc72fae8dea444be86b37/skills/decision-recording/references/conventional-commits.md)。
[^semver]: [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html)。
[^agents-release-versioning]: [自動バージョン計算の方針](https://github.com/daiksud/agents/issues/279)。
[^actions-checkout]: [checkoutの履歴取得](https://github.com/actions/checkout)。
[^semantic-release-faq]: [semantic-releaseの初回バージョンの制約](https://semantic-release.org/support/faq/)。
[^commitlint-configuration]: [commitlintの設定とパーサー](https://commitlint.js.org/reference/configuration.html)。
[^semantic-release-commit-analyzer]: [commit-analyzerの設定と判定規則](https://github.com/semantic-release/commit-analyzer)。
[^commitlint-cli]: [commitlint CLI](https://commitlint.js.org/reference/cli.html)。
[^commitlint-workflow-source]: [移設元の固定バージョン付きワークフロー](https://github.com/daiksud/agents/blob/d4e677be602be08f24dfc72fae8dea444be86b37/skills/decision-recording/assets/commitlint.yml)。
[^commitlint-ci]: [commitlintのCI設定](https://commitlint.js.org/guides/ci-setup.html)。
[^setup-bun]: [Bunのバージョン指定](https://github.com/oven-sh/setup-bun)。
[^bunx]: [bunxのパッケージとランタイムの指定](https://bun.com/docs/pm/bunx)。
[^github-required-checks]: [ルールセットの必須ステータスチェック](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets)。
