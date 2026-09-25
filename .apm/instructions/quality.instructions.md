---
type: Instruction
title: 成果物と変更の品質
description: 成果物の独立性、検証の根拠と未確認範囲の報告を定めます。
sources:
  - id: exclude-prompt-data
    resource: https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/instructions/exclude-prompt-data.instructions.md
  - id: taming-copilot
    resource: https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/instructions/taming-copilot.instructions.md
---

## 成果物と変更の品質

- 成果物は依頼時の会話を知らない読者にも使える内容にする。「依頼どおり追加した」などの応答文、編集の実況、未置換の記入欄を完成本文・コード・コメントへ混ぜず、保存前に差分を確認する。[^exclude-prompt-data]
- 読者に必要な設計理由・制約・出典を保持する。明示された原文転記、指示・テンプレート自体の本文、Issueの計画・承認記録は目的に必要な内容として扱い、この規則を理由に削除しない。変更履歴は変更事実と必要な理由を残し、依頼への応答部分を除く。[^exclude-prompt-data]
- 新しく作る説明用サンプルの人名・メール・組織名などは架空の識別子を使い、依頼の背景やローカル設定から流用しない。成果物に使うよう指定された実データや、正確さに必要な契約値・出典の識別子は保持する。[^exclude-prompt-data]
- 成功条件を満たす最小の変更を既存構造へ統合する。必要な呼び出し元・テスト・文書と異常系を含め、無関係な整理・機能追加を避ける。最小を行数だけで判断せず、必要な検証や契約を省略しない。[^taming-copilot]

探索・受け入れ検証の欠陥は最も小さい再現検証へ反映し、影響・確認できた原因・検出できなかった理由・復旧・残る改善を記録する。実測値はIssue・PRに根拠とともに残し、欠測をゼロや成功にせず、個人評価や単発の効果断定に使わない。

検証不能・権限不足・外部制約は成功とせず、完了範囲・未完了範囲・再開条件を報告する。

[^exclude-prompt-data]: [Exclude Prompt Data](https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/instructions/exclude-prompt-data.instructions.md)。成果物と依頼への応答を区別する考え方を適用し、必要な理由・出典と成果物として指定された内容を保持する。
[^taming-copilot]: [Taming Copilot](https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/instructions/taming-copilot.instructions.md)。既存構造を尊重する最小変更を適用し、必要な関連変更・異常系・検証を含める。参照元の指示優先順位や回答形式の一律制限は採用しない。
