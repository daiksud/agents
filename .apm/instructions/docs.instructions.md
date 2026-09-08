---
type: Instruction
title: ドキュメントの構成
description: Open Knowledge Formatに準拠したdocs以下の文書の形式・分類・記法を定めます。
---

# ドキュメントの構成

## 文書の形式

- `docs/` をKnowledge Bundleとして扱い、文書の作成・更新時は [Open Knowledge Format（OKF）](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) v0.2に従う。
- 通常の文書は1ファイル1概念とし、UTF-8のMarkdown本文と、`---` で囲んだYAML frontmatterで構成する。
- frontmatterには文書の種類を表す `type` を必ず記載し、`title` と `description` を付ける。
- `index.md` はディレクトリの索引、`log.md` は更新履歴にのみ使用し、通常の概念文書には使わない。作成する場合はOKFの各形式に従う。
- 出典・検証・履歴などの任意メタデータを記載する場合は、OKFのフィールド定義に従い、確認できた事実だけを書く。
- `*.feature.md` もOKFのfrontmatterを付け、本文はMarkdown with Gherkinで記述する。

## 配置と記法

- 文書の目的に応じて `docs/` 以下にディレクトリを作成し、分類する。設計判断は `docs/adr/`、ふるまいの定義は `docs/behavior/` に配置する。
- 既存の分類に該当する文書はそのディレクトリに追加し、新しい分類が必要な場合にディレクトリを作成する。
- ページは `docs/<分類>/<page-name>.md` に作成する。全体の案内など、分類に属さない文書は `docs/<page-name>.md` に配置する。
- 画像など Markdown に含められない外部アセットは使用しない。
- GitHub Flavored Markdown（GFM）を積極的に活用し、見出し、リスト、タスクリスト、表、コードブロックで情報を読みやすく整理する。
- Emojiは見出しや状態の識別に、GitHub Alertsは注意事項や重要な制約の強調に使用する。
