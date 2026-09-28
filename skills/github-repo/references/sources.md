---
type: Guide
title: リポジトリ設定の出典と適用判断
description: GitHubの仕様と個人基準を分け、可用性・API・課金条件を実行時に再確認するための資料です。
sources:
  - id: personal-policy
    resource: https://github.com/daiksud/agents/issues/152
  - id: security-features
    resource: https://docs.github.com/en/code-security/getting-started/github-security-features
  - id: advanced-security
    resource: https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security
  - id: release-setting
    resource: https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/establish-provenance-and-integrity/prevent-release-changes
  - id: immutable-release
    resource: https://docs.github.com/en/code-security/concepts/supply-chain-security/immutable-releases
  - id: repository-api
    resource: https://docs.github.com/en/rest/repos/repos
  - id: rules-api
    resource: https://docs.github.com/en/rest/repos/rules
  - id: actions-settings
    resource: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository
  - id: actions-permissions-api
    resource: https://docs.github.com/en/rest/actions/permissions
  - id: code-scanning-api
    resource: https://docs.github.com/en/rest/code-scanning/code-scanning
---

## 仕様と採用判断

5項目の期待値、対象を単一リポジトリに限定すること、無料条件と既存保護を守ることは個人の採用判断である。GitHub一般の必須条件、他リポジトリのレビュー方針、有料機能の購入指示へ読み替えない。[^personal-policy]

文書作成時の仕様確認日は2026-09-28。これは人間によるレビュー、対象リポジトリの適合、設定の実機適用テストを証明するものではない。GitHub Docsは更新されるため、機能の無料範囲・提供条件・API対応・権限・UI名を実行時に再確認し、観測日時を対象の診断記録に残す。

## 必要な資料の選択

| 判断 | 公式根拠と読み方 |
| --- | --- |
| リリース設定と影響 | 有効化手順・非遡及性と、タグ/アセット保護・draft公開手順を分けて読む。リリース個体のimmutable情報をリポジトリ設定の代用にしない。[^release-setting][^immutable-release] |
| マージ方式とセキュリティ設定 | repository APIの取得権限、マージ関連フィールド、security_and_analysisとDependabot設定の個別契約を読む。[^repository-api] |
| mainの保護 | Rulesetの詳細とbranch実効ルールを併用する。実効ルールAPIがmainの実在を証明しない点を保つ。[^rules-api] |
| ActionのSHA必須 | ネイティブ設定の対象・再利用workflowの例外と、permissions APIの必須フィールドを照合する。[^actions-settings][^actions-permissions-api] |
| 無料セキュリティ | 標準機能一覧とCode Security/Secret Protectionの提供条件を機能単位で読む。一部機能のpublic無料を製品全体やprivateへ拡張しない。[^security-features][^advanced-security] |
| CodeQLの設定と結果 | default setupと既存advanced setupを区別し、設定の受付・完了・解析結果を別に確認する。[^code-scanning-api] |

同梱資料は[設定基準](settings.md)、[セキュリティ](security.md)、[操作と判定](operations.md)。workflowの実装判断は配布された `github-actions` を使い、外部Actionの固定・コンテナ・ランナーの方針をここに複製しない。

公式資料・対象UI・APIが一致しない場合は確認できた範囲と相違を残し、未確認の仕様やendpointを補完しない。承認済みの範囲でも費用・権限・破壊的影響の不明点は該当操作の保留理由にする。

[^personal-policy]: Issue #152 の目的・基準・受け入れ条件。
[^security-features]: GitHubのセキュリティ機能一覧。
[^advanced-security]: Advanced Security製品の構成と提供条件。
[^release-setting]: リポジトリでのrelease immutabilityの有効化。
[^immutable-release]: 公開後に保護される対象と公開手順。
[^repository-api]: repositoryとセキュリティ関連のREST API。
[^rules-api]: Rulesetとbranch実効ルールのREST API。
[^actions-settings]: SHA必須設定の適用対象と限界。
[^actions-permissions-api]: Actions permissionsのREST API。
[^code-scanning-api]: Code scanningの設定・実行結果のREST API。
