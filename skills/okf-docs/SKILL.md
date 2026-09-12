---
name: okf-docs
description: 文書・仕様・ADRを作成・更新し、OKF v0.2と固有形式を区別して検証する。docs外のOpenAPI・JSON Schemaも対象。読み取り・説明だけには使わない。
---

# OKFで文書を作成する

文書作成・更新では依存スキル `task-workflow` も適用する。以下の `docs/` は作業対象リポジトリ、`scripts/` と `references/` はこのスキルの同梱資源を指す。

## 適用と参照資料

- 通常のMarkdown・feature文書はOKF v0.2で作成する。GitHubのIssue・PR本文・コメント、Agent Skillsの `SKILL.md`、OpenAPI・JSON Schema等の契約文書は固有形式を維持し、OKF frontmatterを付けない。
- 要求・外部契約・受け入れ条件、設計判断・ADRを作成・更新するときは[既存文書を使って仕様を明確にする](references/specification.md)を読み、既存feature・ADR・API仕様の正本を先に確認する。
- OKF文書を作成・更新するときは[基本形式と参照](references/basic-format.md)を読む。索引・履歴と通常概念の例外、Bundleの境界、リンク解決を確認する。
- 外部資料に依拠する文書、出典付き文書の更新、信頼・鮮度・状態の判断では[出典・信頼・ライフサイクル](references/provenance.md)を読む。軽微な修正でも既存の出典・未知メタデータ・確認履歴を保持する。
- 計算の定義・確認方法を扱う場合は[Attested Computation](references/computation.md)を読む。数値を含むだけの文書に計算契約を新設しない。
- 仕様の適合条件や採用理由を調べる場合は[仕様の節別監査](references/specification-audit.md)を読む。固定SHAの正本、参考実装、サンプル、将来提案を区別する。

## 作成・更新の流れ

1. 対象アクター、文書の目的・成功条件、正本、モデルの境界と既存の用語を確認する。`docs/` を既定のKnowledge Bundleとし、別の配布単位を扱う場合はそのルートを明示する。
2. 対象が通常概念・予約ファイル・固有形式のどれかを判定する。既存の本文とfrontmatterを読んでから差分を作り、未知のキーや出典を再生成で落とさない。
3. 通常概念は1ファイル1概念とし、`type` を記載する。本環境で自作する概念には推奨項目の `title`・`description` も付ける。この追加条件をOKF適合の必須条件と呼ばない。
4. 外部資料に依拠する内容には `sources` を記録し、個別の主張を安定したsource IDの脚注へ結ぶ。関連文書への移動用リンクを出典の代わりにしない。
5. 意味のある変更か誤字・整形だけかを判断し、実際に確認した生成・確認事実だけを更新する。日時・人間の確認・期限を推測で補わず、古い確認を更新後の内容の確認として主張しない。
6. [検証手順](references/validation.md)を実施し、形式の合否、内容の確認、未検証・期限切れの注意、実行不能な検査を分けて報告する。

## 配置と本文

- 文書は目的に合う既存分類へ追加する。設計判断は `docs/adr/`、ふるまいは `docs/behavior/`、その他は `docs/<分類>/<page-name>.md` とする。全体案内は `docs/<page-name>.md` に置ける。
- 新しい分類は既存分類に収まらない場合に作る。索引・履歴を全ディレクトリへ一律に新設しない。
- `*.feature.md` はOKF frontmatterと、依存スキル `bdd-tdd` の[共有仕様・形式資料](../bdd-tdd/references/behavior.md)のMarkdown with Gherkinで記述する。
- GitHub・APMで閲覧できるよう、同梱資料はファイル相対リンクで結ぶ。外部の出典は完全URLで記録し、導入先に原本リポジトリがあることを前提にしない。
- 画像などMarkdownに含められない外部アセットは使用しない。これは本環境の文書作成方針であり、OKFの適合条件ではない。
- 見出し・リスト・表・コードブロックを使い、判断に必要な構造を示す。空の節や装飾のための表は作らない。

## 検証

公開前に[OKFとMarkdownの検証](references/validation.md)を読み、同梱validatorとrumdlを実行する。外部Bundleの適合判定（conformance）と自作の公開品質（authoring）を区別し、固有形式は各形式で検査する。検証依存は既存環境を確認して隔離環境へ準備する。

形式検査の成功を、出典の真偽・人間による内容確認・計算の実行証明にしない。分類・用語・リンク・コマンド・最終差分と内容も照合し、未検証・期限切れ・実行不能を区別して報告する。
