---
type: Reference
title: 設計とテストの出典
description: 実装・設計・テストの出典、既存の確認履歴と採用判断を保持します。
sources:
  - id: fowler-beck-design-rules
    resource: https://martinfowler.com/bliki/BeckDesignRules.html
  - id: fowler-yagni
    resource: https://martinfowler.com/bliki/Yagni.html
  - id: newsletter-p-canon-tdd
    resource: https://newsletter.kentbeck.com/p/canon-tdd
  - id: continuousdelivery-foundations-test-automation
    resource: https://continuousdelivery.com/foundations/test-automation/
  - id: continuousdelivery-implementing-architecture
    resource: https://continuousdelivery.com/implementing/architecture/
  - id: www-05-ddd-reference-2015-03-pdf
    resource: https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf
  - id: github-instructions-oop-design-patterns-instructions-md
    resource: https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/instructions/oop-design-patterns.instructions.md
  - id: github-instructions-self-explanatory-code-commenting-instructions-md
    resource: https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/instructions/self-explanatory-code-commenting.instructions.md
  - id: github-instructions-qa-engineering-best-practices-instructions-md
    resource: https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/instructions/qa-engineering-best-practices.instructions.md
  - id: context-engineering
    resource: https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/instructions/context-engineering.instructions.md
  - id: taming-copilot
    resource: https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/instructions/taming-copilot.instructions.md
---

## 設計とテストの出典

### 一次資料

参照日は2026-09-11です。日付なしは公開・更新日を確定できない資料です。以下は定義・提言の出典で、このスキル自体の効果測定ではありません。

| 著者・資料 | 日付・参照箇所 | 本スキルでの用途 |
| --- | --- | --- |
| Kent Beck, Canon TDD[^newsletter-p-canon-tdd] | 2023-12-11 | テストリスト、一つずつの反復、期待値を弱めないこと |
| Jez Humble, Continuous Testing[^continuousdelivery-foundations-test-automation]、Architecture[^continuousdelivery-implementing-architecture] | 日付なし | 速いフィードバック、探索、テスト可能性、段階的な設計改善 |
| Eric Evans, DDD Reference[^www-05-ddd-reference-2015-03-pdf] | 2015年3月、冊子39–41頁等 | Bounded Context、Ubiquitous Language、Context Map |

### Simple DesignとYAGNIの採用判断

2026-09-25にMartin FowlerのBeck Design Rules[^fowler-beck-design-rules]とYagni[^fowler-yagni]を確認した。現在のテスト・契約、意図の明瞭さ、同じルールの重複、必要な要素から設計を判断する。仮想の将来機能を先取りせず、実際のフィードバックで小さく改善する。明瞭さと重複の間に機械的な優先順位や点数を付けず、必要なテスト・Refactor・CIを省略しない。アサートファーストと同じNavigatorの段階確認は本環境の方針で、XP原典の要件として帰属させない。

### 指示例の参照元と適用判断

2026-09-11に確認したGitHub awesome-copilotの以下の指示例を要約・再構成した。リンクは確認コミットに固定する。これらはコミュニティの指示例であり、OOP・テストの普遍的な必須規則として扱わない。

| 資料 | 取り込む内容と調整 |
| --- | --- |
| OOP Design Patterns[^github-instructions-oop-design-patterns-instructions-md] | 責務・契約・合成・依存方向を使う。抽象型先行、全関数のログ、固定docstring形式は要求しない |
| Self-explanatory Code Commenting[^github-instructions-self-explanatory-code-commenting-instructions-md] | 命名・構造を優先し、理由と見えない契約を残す。公開契約の説明を理由以外というだけで削除しない |
| QA Engineering Best Practices[^github-instructions-qa-engineering-best-practices-instructions-md] | 状態分離、UIの状態待ち、代表負荷での検証を使う。固定比率・網羅率・再試行回数・特定ツールは義務化しない |

2026-09-13に確認した以下の指示例も、同じ固定コミットから要約・再構成した。

| 資料 | 取り込む内容と調整 |
| --- | --- |
| Context Engineering[^context-engineering] | 意味のある名前・パス・定数、関連情報を見つけやすい配置、境界の型・公開契約、複雑な流れの説明を使う。既存配置と言語慣習を優先し、局所的な型推論の禁止、一律のindexファイル・内部公開・IDE操作は要求しない |
| Taming Copilot[^taming-copilot] | 標準機能・既存依存を先に検討し、必要な変更を既存構造へ統合する。必要な契約・異常系・TDDを省かず、最短コードやユーザーが列挙したファイルだけを変更範囲の基準にしない |

[^newsletter-p-canon-tdd]: [Canon TDD](https://newsletter.kentbeck.com/p/canon-tdd)。本文に記した参照範囲と採用判断の根拠。
[^continuousdelivery-foundations-test-automation]: [Continuous Testing](https://continuousdelivery.com/foundations/test-automation/)。本文に記した参照範囲と採用判断の根拠。
[^continuousdelivery-implementing-architecture]: [Architecture](https://continuousdelivery.com/implementing/architecture/)。本文に記した参照範囲と採用判断の根拠。
[^www-05-ddd-reference-2015-03-pdf]: [DDD Reference](https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf)。本文に記した参照範囲と採用判断の根拠。
[^fowler-beck-design-rules]: [Beck Design Rules](https://martinfowler.com/bliki/BeckDesignRules.html)。Kent Beck本人のレビューを受けたFowlerの定式化。
[^fowler-yagni]: [Yagni](https://martinfowler.com/bliki/Yagni.html)。未要求の機能と現在の変更を支える健全性を区別する。
[^github-instructions-oop-design-patterns-instructions-md]: [OOP Design Patterns](https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/instructions/oop-design-patterns.instructions.md)。本文に記した参照範囲と採用判断の根拠。
[^github-instructions-self-explanatory-code-commenting-instructions-md]: [Self-explanatory Code Commenting](https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/instructions/self-explanatory-code-commenting.instructions.md)。本文に記した参照範囲と採用判断の根拠。
[^github-instructions-qa-engineering-best-practices-instructions-md]: [QA Engineering Best Practices](https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/instructions/qa-engineering-best-practices.instructions.md)。本文に記した参照範囲と採用判断の根拠。
[^context-engineering]: [Context Engineering](https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/instructions/context-engineering.instructions.md)。命名・配置・型・公開境界とコメントの設計へ適用する。
[^taming-copilot]: [Taming Copilot](https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/instructions/taming-copilot.instructions.md)。標準機能・既存依存と最小の構造を選ぶ判断へ適用する。
