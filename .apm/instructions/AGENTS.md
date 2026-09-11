---
type: Instruction
title: インストラクションの作成・更新
description: このディレクトリのインストラクションの形式、内容、確認方法を定めます。
---

## インストラクションの作成・更新

このディレクトリの `*.instructions.md` を作成・更新するときに適用する。
編集前に[記入の指針](../../docs/templates/instructions.md#記入の指針)を読む。構成や例が必要なら同資料のテンプレートを使い、目的に必要な節だけを選ぶ。

### 形式

- このディレクトリのMarkdownは [Open Knowledge Format（OKF）](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) v0.2の概念文書として扱う。
- YAML frontmatterに `type: Instruction` と、先頭の見出しに一致する `title` を記載する。
- ファイル名は対象を表す英単語を小文字のハイフン区切りにし、`.instructions.md` を付ける。
- YAML front matter の `description` に、指示の対象と目的を一文で書く。
- 本文は日本語のMarkdownで書き、先頭の見出しにインストラクション名を付ける。
- テンプレートから目的に必要な節だけを選び、未記入の欄や不要な節を残さない。
- APM用の `description` や `applyTo` など既存のメタデータは保持する。

### 共通指示と作業スキル

- グローバルAGENTS.mdの原本は `core.instructions.md` とし、`applyTo` を付けない。
- 作業別の詳細手順は `skills/` に置き、共通指示には読み込む条件とグローバル配布先を書く。グローバルコンパイルは相対リンクを書き換えないため、`~/.agents/skills/<name>/SKILL.md` を明記する。
- スキルは `name` と `description` を持つ `SKILL.md` を入口とし、詳細資料を同梱する。
- 生成されたAGENTS.mdを手動編集しない。公開版の導入・更新と、編集中の原本の検証を区別し、[保守ガイド](../../docs/guides/delivery.md#原本の編集と保守)に従う。
- ルールの移動では、元の指示との対応を確認し、合意していない意味の変更や脱落を防ぐ。

### 配布本文の境界

配布本文には利用先で必要な判断・手順だけを置く。agentsの原本配置・同期・導入検証履歴はローカルAGENTS.mdまたは保守ガイドへ置き、共通本文から管理手順に依存させない。

### 確認と見直し

[適用前の確認](../../docs/templates/instructions.md#適用前の確認)と[運用中の見直し](../../docs/templates/instructions.md#運用中の見直し)に従う。手順・完了条件の検証方法と期待結果を明示し、代表的な依頼で判断を確認する。効果を確認できなかった場合は未確認として報告する。
