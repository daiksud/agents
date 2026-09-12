---
type: Reference
title: 設計・共有理解・テストの出典
description: 設計・共有仕様・テスト資料の一次出典、参照日と本環境への採用判断を保持します。
sources:
  - id: cucumber-docs-bdd
    resource: https://cucumber.io/docs/bdd/
  - id: cucumber-bdd-examples
    resource: https://cucumber.io/docs/bdd/examples/
  - id: cucumber-bdd-better-gherkin
    resource: https://cucumber.io/docs/bdd/better-gherkin/
  - id: cucumber-bdd-example-mapping
    resource: https://cucumber.io/docs/bdd/example-mapping/
  - id: cucumber-gherkin-reference
    resource: https://cucumber.io/docs/gherkin/reference/
  - id: newsletter-p-canon-tdd
    resource: https://newsletter.kentbeck.com/p/canon-tdd
  - id: agilealliance-glossary-atdd
    resource: https://agilealliance.org/glossary/atdd/
  - id: curiousduck-collections-2024-06-27-atdd
    resource: https://curiousduck.io/posts/collections/2024-06-27-atdd/
  - id: lizkeogh-20-acceptance-criteria-vs-scenarios
    resource: https://lizkeogh.com/2011/06/20/acceptance-criteria-vs-scenarios/
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
---

## 設計・共有理解・テストの出典

### 一次資料

参照日は2026-09-11です。日付なしは公開・更新日を確定できない資料です。以下は定義・提言の出典で、このスキル自体の効果測定ではありません。

| 著者・資料 | 日付・参照箇所 | 本スキルでの用途 |
| --- | --- | --- |
| Cucumber, Behaviour-Driven Development[^cucumber-docs-bdd] | ページ更新表示2026-09-10。概念の成立日ではない | 共有理解とDiscovery・Formulation・Automation |
| Cucumber, Examples[^cucumber-bdd-examples]、Writing better Gherkin[^cucumber-bdd-better-gherkin] | 日付なし | 業務上意味のある具体性と宣言的な記述 |
| Cucumber, Example Mapping[^cucumber-bdd-example-mapping]、Gherkin Reference[^cucumber-gherkin-reference] | 日付なし | ルール・例・質問の区別、RuleとScenario |
| Kent Beck, Canon TDD[^newsletter-p-canon-tdd] | 2023-12-11 | テストリスト、一つずつの反復、期待値を弱めないこと |
| Agile Alliance, Acceptance Test Driven Development[^agilealliance-glossary-atdd] | 日付なし | 実装前の受け入れテストと異なる観点の協働 |
| Elisabeth Hendrickson, ATDD Revisited[^curiousduck-collections-2024-06-27-atdd] | 2024-06-27 | 2008年の実践の再評価、参加方法と自動化形式の適応 |
| Liz Keogh, Acceptance Criteria vs. Scenarios[^lizkeogh-20-acceptance-criteria-vs-scenarios] | 2011-06-20 | 抽象的な条件と具体例の違い |
| Jez Humble, Continuous Testing[^continuousdelivery-foundations-test-automation]、Architecture[^continuousdelivery-implementing-architecture] | 日付なし | 速いフィードバック、探索、テスト可能性、段階的な設計改善 |
| Eric Evans, DDD Reference[^www-05-ddd-reference-2015-03-pdf] | 2015年3月、冊子39–41頁等 | Bounded Context、Ubiquitous Language、Context Map |

### 指示例の参照元と適用判断

2026-09-11に確認したGitHub awesome-copilotの以下の指示例を要約・再構成した。リンクは確認コミットに固定する。これらはコミュニティの指示例であり、OOP・テストの普遍的な必須規則として扱わない。

| 資料 | 取り込む内容と調整 |
| --- | --- |
| OOP Design Patterns[^github-instructions-oop-design-patterns-instructions-md] | 責務・契約・合成・依存方向を使う。抽象型先行、全関数のログ、固定docstring形式は要求しない |
| Self-explanatory Code Commenting[^github-instructions-self-explanatory-code-commenting-instructions-md] | 命名・構造を優先し、理由と見えない契約を残す。公開契約の説明を理由以外というだけで削除しない |
| QA Engineering Best Practices[^github-instructions-qa-engineering-best-practices-instructions-md] | 状態分離、UIの状態待ち、代表負荷での検証を使う。固定比率・網羅率・再試行回数・特定ツールは義務化しない |

[^cucumber-docs-bdd]: [Behaviour-Driven Development](https://cucumber.io/docs/bdd/)。本文に記した参照範囲と採用判断の根拠。
[^cucumber-bdd-examples]: [Examples](https://cucumber.io/docs/bdd/examples/)。本文に記した参照範囲と採用判断の根拠。
[^cucumber-bdd-better-gherkin]: [Writing better Gherkin](https://cucumber.io/docs/bdd/better-gherkin/)。本文に記した参照範囲と採用判断の根拠。
[^cucumber-bdd-example-mapping]: [Example Mapping](https://cucumber.io/docs/bdd/example-mapping/)。本文に記した参照範囲と採用判断の根拠。
[^cucumber-gherkin-reference]: [Gherkin Reference](https://cucumber.io/docs/gherkin/reference/)。本文に記した参照範囲と採用判断の根拠。
[^newsletter-p-canon-tdd]: [Canon TDD](https://newsletter.kentbeck.com/p/canon-tdd)。本文に記した参照範囲と採用判断の根拠。
[^agilealliance-glossary-atdd]: [Acceptance Test Driven Development](https://agilealliance.org/glossary/atdd/)。本文に記した参照範囲と採用判断の根拠。
[^curiousduck-collections-2024-06-27-atdd]: [ATDD Revisited](https://curiousduck.io/posts/collections/2024-06-27-atdd/)。本文に記した参照範囲と採用判断の根拠。
[^lizkeogh-20-acceptance-criteria-vs-scenarios]: [Acceptance Criteria vs. Scenarios](https://lizkeogh.com/2011/06/20/acceptance-criteria-vs-scenarios/)。本文に記した参照範囲と採用判断の根拠。
[^continuousdelivery-foundations-test-automation]: [Continuous Testing](https://continuousdelivery.com/foundations/test-automation/)。本文に記した参照範囲と採用判断の根拠。
[^continuousdelivery-implementing-architecture]: [Architecture](https://continuousdelivery.com/implementing/architecture/)。本文に記した参照範囲と採用判断の根拠。
[^www-05-ddd-reference-2015-03-pdf]: [DDD Reference](https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf)。本文に記した参照範囲と採用判断の根拠。
[^github-instructions-oop-design-patterns-instructions-md]: [OOP Design Patterns](https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/instructions/oop-design-patterns.instructions.md)。本文に記した参照範囲と採用判断の根拠。
[^github-instructions-self-explanatory-code-commenting-instructions-md]: [Self-explanatory Code Commenting](https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/instructions/self-explanatory-code-commenting.instructions.md)。本文に記した参照範囲と採用判断の根拠。
[^github-instructions-qa-engineering-best-practices-instructions-md]: [QA Engineering Best Practices](https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/instructions/qa-engineering-best-practices.instructions.md)。本文に記した参照範囲と採用判断の根拠。
