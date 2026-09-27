---
type: Reference
title: XP taxonomyとfocused lensを選ぶ
description: Extreme Programming第2版のValues、Principles、Primary / Corollary Practicesを区別し、診断対象に必要なfocused lensだけを選びます。
sources:
  - id: xp-second-edition
    resource: https://www.informit.com/store/extreme-programming-explained-embrace-change-9780134051987
---

## XP taxonomyとfocused lensを選ぶ

XPそのもの、XP第2版、Values / Principles / Practices、Primary / Corollary Practicesの分類や関係を診断するときに読む。

目的はXP項目を全部導入・採点することではない。taxonomyを確認したら、現在のproblemに関係するカテゴリだけをfocused referenceで読む。

### Taxonomyを平坦化しない

XP第2版は抽象度の異なる分類を区別する。[^xp-second-edition]

```text
Values
  ↓
Principles
  ↓
Practices
    ├─ Primary Practices
    └─ Corollary Practices
```

- **Values**: 判断で何を大切にするか。
- **Principles**: Valuesを状況へ適用するときの橋渡し。
- **Practices**: 日常で実行できる具体的な行動。

この矢印を成熟度の点数や強制的な導入順にしない。Practiceの数をXP成熟度スコアにせず、Value名だけで実践済みとも判定しない。

### Values

5 Values:

- Communication
- Simplicity
- Feedback
- Courage
- Respect

Valueを実際の判断へ適用するときは[XP個別項目の軽量lookup](xp-auxiliary.md#values)だけを読む。個別Valueを他のengineering lensへ補助的に使う場合も、全taxonomyを読まず同referenceを使う。

### Principles

InformITのTable of Contentsは次の14 named Principlesを列挙する。同じpublisherページの紹介文には「Eleven principles」という不一致があるため、本リポジトリでは列挙されたTOCをtaxonomyの根拠にし、この差をprovenanceへ残す。[^xp-second-edition]

- Humanity
- Economics
- Mutual Benefit
- Self-Similarity
- Improvement
- Diversity
- Reflection
- Flow
- Opportunity
- Redundancy
- Failure
- Quality
- Baby Steps
- Accepted Responsibility

Principleを実際のproblemへ適用するときは[XP個別項目の軽量lookup](xp-auxiliary.md#principles)だけを読む。個別PrincipleをArchitecture / Delivery / DORA等の補助lensへ使う場合も、全taxonomyを読まない。

### Primary Practices

13 Primary Practices:

- Sit Together
- Whole Team
- Informative Workspace
- Energized Work
- Pair Programming
- Stories
- Weekly Cycle
- Quarterly Cycle
- Slack
- Ten-Minute Build
- Continuous Integration
- Test-First Programming
- Incremental Design

### Corollary Practices

11 Corollary Practices:

- Real Customer Involvement
- Incremental Deployment
- Team Continuity
- Shrinking Teams
- Root-Cause Analysis
- Shared Code
- Code and Tests
- Single Code Base
- Daily Deployment
- Negotiated Scope Contract
- Pay-Per-Use

Primary Practiceの意味や観測証拠が必要なときは[Primary Practices](xp-auxiliary.md#primary-practices)、Corollary Practiceなら[Corollary Practices](xp-auxiliary.md#corollary-practices)だけを読む。Practiceの採用数を成熟度や必須導入数にしない。

### Problemから必要なカテゴリだけを選ぶ

| Problem | 最初に使うXP lens |
| --- | --- |
| 要件の認識違い | [Values](xp-auxiliary.md#values)のCommunication / Feedback。必要なら[Practices](xp-auxiliary.md#primary-practices)のStories / Whole Team |
| 設計の先回り・複雑化 | [Values](xp-auxiliary.md#values)のSimplicity、[Principles](xp-auxiliary.md#principles)のEconomics / Baby Steps、必要なら[Practices](xp-auxiliary.md#primary-practices)のIncremental Design |
| feedbackの遅さ・大きな変更 | [Values](xp-auxiliary.md#values)のFeedback、[Principles](xp-auxiliary.md#principles)のFlow / Baby Steps、必要なら[Practices](xp-auxiliary.md#primary-practices)のCI / Test-First / Incremental Design |
| 継続できない働き方 | [Values](xp-auxiliary.md#values)のRespect、[Principles](xp-auxiliary.md#principles)のHumanity、必要なら[Practices](xp-auxiliary.md#primary-practices)のEnergized Work / Slack |
| 同じ失敗の再発 | [Values](xp-auxiliary.md#values)のCourage、[Principles](xp-auxiliary.md#principles)のReflection / Failure、必要なら[Corollary Practices](xp-auxiliary.md#corollary-practices)のRoot-Cause Analysis |
| 責任と権限のずれ | [Values](xp-auxiliary.md#values)のRespect、[Principles](xp-auxiliary.md#principles)のAccepted Responsibility、必要なら[Practices](xp-auxiliary.md#primary-practices)のWhole Team |

表は唯一のmappingではない。現在のproblemに関係するカテゴリ・項目だけを選び、無関係なXP項目を未確認一覧へ追加しない。

### Runtimeでの役割分担

- Valuesと常時使う短い判断原則は共通Instructionへ置く。
- TDD、Pair Programming、Incremental Design等の具体的実行は `software-development` が担当する。
- 診断時のtaxonomy・選択・証拠判断は `engineering-assessment` が担当する。
- Architecture / Organizationの詳細は[専用lens](architecture-and-organization.md)を読む。
- DORAのCore / Capability / metricsは[DORA lens](dora.md)を読む。

XP-primary診断では、このtaxonomy fileを入口にし、具体的な項目の意味が必要なときだけ[XP個別項目の軽量lookup](xp-auxiliary.md)を追加で読む。分類確認だけならlookupを読まず、全項目を未確認一覧へ展開しない。

[^xp-second-edition]: [Extreme Programming Explained: Embrace Change, 2nd Edition — Kent Beck / Cynthia Andres](https://www.informit.com/store/extreme-programming-explained-embrace-change-9780134051987)。2004年版のTable of Contentsは5 Values、14個のnamed Principles、13 Primary Practices、11 Corollary Practicesを列挙する。同じpublisherページの紹介文には「Eleven principles」とあるため、Principles数はTOCの列挙を採用し不一致を明記する。2026-09-27確認。
