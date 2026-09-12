---
type: Reference
title: 一次資料と適用上の判断
description: 診断の根拠にした一次資料、版の違い、資料の要約と本スキルの適用判断を区別します。
sources:
  - id: github-instructions-devops-core-principles-instructions-md
    resource: https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/instructions/devops-core-principles.instructions.md
  - id: www-explore-lean-what-is-lean
    resource: https://www.lean.org/explore-lean/what-is-lean/
  - id: tech-lean-practice
    resource: https://tech.lean.org/lean-practice
  - id: dora-guides-how-to-transform
    resource: https://dora.dev/guides/how-to-transform/
  - id: dora-capabilities-wip-limits
    resource: https://dora.dev/capabilities/wip-limits/
  - id: dora-capabilities-generative-organizational-culture
    resource: https://dora.dev/capabilities/generative-organizational-culture/
  - id: continuousdelivery
    resource: https://continuousdelivery.com/
  - id: continuousdelivery-principles
    resource: https://continuousdelivery.com/principles/
  - id: continuousdelivery-foundations-continuous-integration
    resource: https://continuousdelivery.com/foundations/continuous-integration/
  - id: martinfowler-articles-continuousintegration-html
    resource: https://martinfowler.com/articles/continuousIntegration.html
  - id: continuousdelivery-implementing-patterns
    resource: https://continuousdelivery.com/implementing/patterns/
  - id: continuousdelivery-foundations-configuration-management
    resource: https://continuousdelivery.com/foundations/configuration-management/
  - id: continuousdelivery-foundations-test-automation
    resource: https://continuousdelivery.com/foundations/test-automation/
  - id: continuousdelivery-implementing-architecture
    resource: https://continuousdelivery.com/implementing/architecture/
  - id: dora-guides-dora-metrics
    resource: https://dora.dev/guides/dora-metrics/
  - id: dora-insights-dora-metrics-history
    resource: https://dora.dev/insights/dora-metrics-history/
  - id: dora-assets-dora-core-v2-1-0-detail-pdf
    resource: https://dora.dev/research/core/assets/dora-core-v2.1.0-detail.pdf
  - id: dora-research
    resource: https://dora.dev/research/
  - id: cucumber-docs-bdd
    resource: https://cucumber.io/docs/bdd/
  - id: cucumber-bdd-example-mapping
    resource: https://cucumber.io/docs/bdd/example-mapping/
  - id: cucumber-bdd-better-gherkin
    resource: https://cucumber.io/docs/bdd/better-gherkin/
  - id: agilealliance-glossary-atdd
    resource: https://agilealliance.org/glossary/atdd/
  - id: curiousduck-collections-2024-06-27-atdd
    resource: https://curiousduck.io/posts/collections/2024-06-27-atdd/
  - id: newsletter-p-canon-tdd
    resource: https://newsletter.kentbeck.com/p/canon-tdd
  - id: www-05-ddd-reference-2015-03-pdf
    resource: https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf
  - id: www-04-gettingstartedwithdddwhensurroundedbylegacysystemsv1-pdf
    resource: https://www.domainlanguage.com/wp-content/uploads/2016/04/GettingStartedWithDDDWhenSurroundedByLegacySystemsV1.pdf
  - id: teamtopologies-key-concepts
    resource: https://teamtopologies.com/key-concepts
  - id: github-teamtopologies-team-api-template
    resource: https://github.com/TeamTopologies/Team-API-template
  - id: github-teamtopologies-team-dependencies-tracking
    resource: https://github.com/TeamTopologies/Team-Dependencies-Tracking
  - id: teamtopologies-s-finding-software-boundaries-for-fast-flow-team-topologies-and-domain-driven-design-mini-book-mb81-v1-pdf
    resource: https://teamtopologies.com/s/Finding-software-boundaries-for-fast-flow-Team-Topologies-and-Domain-Driven-Design-mini-book-MB81-v1.pdf
---

## 一次資料と適用上の判断

2026-09-11確認。以下を翻訳転載せず、[原則の関係](principles.md)と[診断手順](assessment.md)へ要約・再構成した。更新日がない資料に確認日を公開日として付けない。後日の診断では、実際に参照した版・確認日を記録する。

### DevOps・Lean・改善

| 資料・著者 | 参照点と注意 |
| --- | --- |
| DevOps Core Principles — GitHub awesome-copilot[^github-instructions-devops-core-principles-instructions-md]（2026-09-11確認） | CALMS、エンドツーエンドの責任、運用の観測・手順共有を診断へ具体化。全自動化や特定製品を必須にせず、固定のFour Keys・MTTR・Elite値は現行DORAの定義へ更新する。コミュニティの指示例として参照する |
| What is Lean? — Lean Enterprise Institute[^www-explore-lean-what-is-lean] | 顧客の問題から価値、仕事、人と継続的な実験を考える |
| Lean practice — LEI[^tech-lean-practice] | 価値・価値の流れ・フロー・プル・改善を扱う |
| How to transform — Jez Humble / DORA[^dora-guides-how-to-transform]（2025-10-06更新） | 現状、目標状態、制約、小さな実験から改善する |
| WIP limits — DORA[^dora-capabilities-wip-limits] | 見えない仕事も含む仕掛かりと詰まりを扱う |
| Generative organizational culture — DORA[^dora-capabilities-generative-organizational-culture] | 協力・情報共有・学習を、方針ファイルだけでは判定しない |

### CI・CD・測定

| 資料・著者 | 参照点と注意 |
| --- | --- |
| Continuous Delivery — Jez Humble[^continuousdelivery]・原則[^continuousdelivery-principles] | 配布可能な状態、品質の組み込み、小さいバッチ、共同責任 |
| CIの基礎[^continuousdelivery-foundations-continuous-integration]・Continuous Integration — Martin Fowler[^martinfowler-articles-continuousintegration-html]（2024-01-18版） | 頻繁な共有mainへの統合、速い自動検証、壊れたビルドの修復。CIツールとの違い |
| 配布パターン[^continuousdelivery-implementing-patterns]・構成管理[^continuousdelivery-foundations-configuration-management] | 成果物を一度作り環境間で昇格させ、構成・依存と復旧を追跡する |
| テスト自動化[^continuousdelivery-foundations-test-automation]・アーキテクチャ[^continuousdelivery-implementing-architecture] | 小さな足場から検証・配布可能性を改善し、探索を含める |
| Software delivery performance metrics — Nathen Harvey / DORA[^dora-guides-dora-metrics]（2026-01-05更新） | 現行5指標の定義、アプリケーション単位の測定、競争・単一指標・過剰な測定投資を避ける |
| Metrics history — DORA[^dora-insights-dora-metrics-history]（2026-01-02更新） | 復旧指標の対象変更、rework追加、信頼性と配信指標の区別 |
| DORA Core v2.1.0[^dora-assets-dora-core-v2-1-0-detail-pdf]・研究モデルの説明[^dora-research] | Coreは安定した研究モデルで、最新ガイドと更新周期が異なる。4指標の図を現行5指標と混同しない |

DORAの文章・図はGoogle LLCによるCC BY 4.0（各ページの例外を除く）。本スキルは資料の要約と適用指針を作成したもので、DORAによる認定や普遍的な因果の保証ではない。

### BDD・ATDD・TDD・DDD・チームトポロジー

| 資料・著者 | 参照点と注意 |
| --- | --- |
| BDD — Cucumber[^cucumber-docs-bdd]・Example Mapping[^cucumber-bdd-example-mapping]・Better Gherkin[^cucumber-bdd-better-gherkin] | 発見・定式化・自動化、ルール・例・質問、宣言的な具体例。ファイル形式だけをBDDにしない |
| ATDD — Agile Alliance[^agilealliance-glossary-atdd] | 顧客・開発・検証の観点から実装前に受け入れテストを作る |
| ATDD revisited — Elisabeth Hendrickson[^curiousduck-collections-2024-06-27-atdd]（2024-06-27） | 重い全員参加の会議や自然言語自動化を目的化しないという実践上の振り返り。BDDの定義を置き換えるものではない |
| Canon TDD — Kent Beck[^newsletter-p-canon-tdd]（2023-12-11） | テストリストから一つずつ失敗・最小実装・必要な整理を反復する |
| DDD Reference — Eric Evans[^www-05-ddd-reference-2015-03-pdf]（2015-03） | 用語、モデル、境界、コンテキストマップと業務の複雑さへの集中 |
| LegacyでDDDを始める — Eric Evans[^www-04-gettingstartedwithdddwhensurroundedbylegacysystemsv1-pdf]（2013） | 既存システムに囲まれた小さな境界から始める |
| Key Concepts — Team Topologies[^teamtopologies-key-concepts] | 4つのチーム型・3つの相互作用、価値の流れと認知負荷 |
| Team API[^github-teamtopologies-team-api-template]・Dependencies Tracking[^github-teamtopologies-team-dependencies-tracking] | 責任と関わり方、進行を止める依存とサービス利用を区別する |
| Finding software boundaries — Team Topologies / DDD mini-book[^teamtopologies-s-finding-software-boundaries-for-fast-flow-team-topologies-and-domain-driven-design-mini-book-mb81-v1-pdf]（2023-05-19） | チームとコンテキストの地図を重ねる。1チームが複数境界を持つ事例も扱う |

本スキルの「単独開発に比例させる」「観測・不足・未確認・適用外で整理する」「Issue保存で診断を完了する」は、これらの資料を作業環境へ適用するための設計判断である。公式の成熟度尺度や組織編成の規格として提示しない。

[^github-instructions-devops-core-principles-instructions-md]: [DevOps Core Principles — GitHub awesome-copilot](https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/instructions/devops-core-principles.instructions.md)。本文に記した参照範囲と採用判断の根拠。
[^www-explore-lean-what-is-lean]: [What is Lean? — Lean Enterprise Institute](https://www.lean.org/explore-lean/what-is-lean/)。本文に記した参照範囲と採用判断の根拠。
[^tech-lean-practice]: [Lean practice — LEI](https://tech.lean.org/lean-practice)。本文に記した参照範囲と採用判断の根拠。
[^dora-guides-how-to-transform]: [How to transform — Jez Humble / DORA](https://dora.dev/guides/how-to-transform/)。本文に記した参照範囲と採用判断の根拠。
[^dora-capabilities-wip-limits]: [WIP limits — DORA](https://dora.dev/capabilities/wip-limits/)。本文に記した参照範囲と採用判断の根拠。
[^dora-capabilities-generative-organizational-culture]: [Generative organizational culture — DORA](https://dora.dev/capabilities/generative-organizational-culture/)。本文に記した参照範囲と採用判断の根拠。
[^continuousdelivery]: [Continuous Delivery — Jez Humble](https://continuousdelivery.com/)。本文に記した参照範囲と採用判断の根拠。
[^continuousdelivery-principles]: [原則](https://continuousdelivery.com/principles/)。本文に記した参照範囲と採用判断の根拠。
[^continuousdelivery-foundations-continuous-integration]: [CIの基礎](https://continuousdelivery.com/foundations/continuous-integration/)。本文に記した参照範囲と採用判断の根拠。
[^martinfowler-articles-continuousintegration-html]: [Continuous Integration — Martin Fowler](https://martinfowler.com/articles/continuousIntegration.html)。本文に記した参照範囲と採用判断の根拠。
[^continuousdelivery-implementing-patterns]: [配布パターン](https://continuousdelivery.com/implementing/patterns/)。本文に記した参照範囲と採用判断の根拠。
[^continuousdelivery-foundations-configuration-management]: [構成管理](https://continuousdelivery.com/foundations/configuration-management/)。本文に記した参照範囲と採用判断の根拠。
[^continuousdelivery-foundations-test-automation]: [テスト自動化](https://continuousdelivery.com/foundations/test-automation/)。本文に記した参照範囲と採用判断の根拠。
[^continuousdelivery-implementing-architecture]: [アーキテクチャ](https://continuousdelivery.com/implementing/architecture/)。本文に記した参照範囲と採用判断の根拠。
[^dora-guides-dora-metrics]: [Software delivery performance metrics — Nathen Harvey / DORA](https://dora.dev/guides/dora-metrics/)。本文に記した参照範囲と採用判断の根拠。
[^dora-insights-dora-metrics-history]: [Metrics history — DORA](https://dora.dev/insights/dora-metrics-history/)。本文に記した参照範囲と採用判断の根拠。
[^dora-assets-dora-core-v2-1-0-detail-pdf]: [DORA Core v2.1.0](https://dora.dev/research/core/assets/dora-core-v2.1.0-detail.pdf)。本文に記した参照範囲と採用判断の根拠。
[^dora-research]: [研究モデルの説明](https://dora.dev/research/)。本文に記した参照範囲と採用判断の根拠。
[^cucumber-docs-bdd]: [BDD — Cucumber](https://cucumber.io/docs/bdd/)。本文に記した参照範囲と採用判断の根拠。
[^cucumber-bdd-example-mapping]: [Example Mapping](https://cucumber.io/docs/bdd/example-mapping/)。本文に記した参照範囲と採用判断の根拠。
[^cucumber-bdd-better-gherkin]: [Better Gherkin](https://cucumber.io/docs/bdd/better-gherkin/)。本文に記した参照範囲と採用判断の根拠。
[^agilealliance-glossary-atdd]: [ATDD — Agile Alliance](https://agilealliance.org/glossary/atdd/)。本文に記した参照範囲と採用判断の根拠。
[^curiousduck-collections-2024-06-27-atdd]: [ATDD revisited — Elisabeth Hendrickson](https://curiousduck.io/posts/collections/2024-06-27-atdd/)。本文に記した参照範囲と採用判断の根拠。
[^newsletter-p-canon-tdd]: [Canon TDD — Kent Beck](https://newsletter.kentbeck.com/p/canon-tdd)。本文に記した参照範囲と採用判断の根拠。
[^www-05-ddd-reference-2015-03-pdf]: [DDD Reference — Eric Evans](https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf)。本文に記した参照範囲と採用判断の根拠。
[^www-04-gettingstartedwithdddwhensurroundedbylegacysystemsv1-pdf]: [LegacyでDDDを始める — Eric Evans](https://www.domainlanguage.com/wp-content/uploads/2016/04/GettingStartedWithDDDWhenSurroundedByLegacySystemsV1.pdf)。本文に記した参照範囲と採用判断の根拠。
[^teamtopologies-key-concepts]: [Key Concepts — Team Topologies](https://teamtopologies.com/key-concepts)。本文に記した参照範囲と採用判断の根拠。
[^github-teamtopologies-team-api-template]: [Team API](https://github.com/TeamTopologies/Team-API-template)。本文に記した参照範囲と採用判断の根拠。
[^github-teamtopologies-team-dependencies-tracking]: [Dependencies Tracking](https://github.com/TeamTopologies/Team-Dependencies-Tracking)。本文に記した参照範囲と採用判断の根拠。
[^teamtopologies-s-finding-software-boundaries-for-fast-flow-team-topologies-and-domain-driven-design-mini-book-mb81-v1-pdf]: [Finding software boundaries — Team Topologies / DDD mini-book](https://teamtopologies.com/s/Finding-software-boundaries-for-fast-flow-Team-Topologies-and-Domain-Driven-Design-mini-book-MB81-v1.pdf)。本文に記した参照範囲と採用判断の根拠。
