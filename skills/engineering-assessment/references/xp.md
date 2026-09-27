---
type: Reference
title: XPをValues・Principles・Practicesとして診断する
description: Extreme Programming第2版のValues、Principles、Primary / Corollary Practicesを区別し、現在の問題に関係する項目だけを証拠から診断します。
sources:
  - id: xp-second-edition
    resource: https://www.informit.com/store/extreme-programming-explained-embrace-change-9780134051987
  - id: ron-jeffries-xp
    resource: https://ronjeffries.com/xprog/what-is-extreme-programming/
---

## XPをValues・Principles・Practicesとして診断する

XPそのもの、XP第2版、Values / Principles / Practices、Primary / Corollary Practicesを使う診断で読む。

目的はXP項目を全部導入・採点することではない。現在の要求、feedback loop、設計・協働上のproblemを、関連するValue・Principle・Practiceへ結びつけて改善する。

### Taxonomyを平坦化しない

XP第2版は、抽象度の異なる3種類を区別する。[^xp-second-edition]

```text
Values
  ↓
Principles
  ↓
Practices
    ├─ Primary Practices
    └─ Corollary Practices
```

この矢印は成熟度の点数や強制的な導入順ではない。

- **Values**: 判断で何を大切にするか。
- **Principles**: Valuesを状況へ適用するときの橋渡し。
- **Practices**: 日常で実行できる具体的な行動。

Practiceの数をXP成熟度スコアにせず、Value名だけで実践済みとも判定しない。

### Values

第2版の5 Values:

- Communication
- Simplicity
- Feedback
- Courage
- Respect

本リポジトリでは、この5 Valuesを日常の開発判断へ使う。固定会議・固定役割・特定team構成をValueそのものの要件にはしない。[^ron-jeffries-xp]

### Principles

InformITのTable of Contentsは次の14 Principlesを列挙する。同じpublisherページの紹介文には「Eleven principles」という不一致があるため、本リポジトリでは列挙されたTOCをtaxonomyの根拠にし、この差をprovenanceへ残す。[^xp-second-edition]

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

Principleは新しい独立ルール一覧としてInstructionへ複製しない。

診断では、現在のproblemを説明するために必要なPrincipleだけを使う。例えば:

| Problem | 関連するPrincipleの例 |
| --- | --- |
| 大きな変更でfeedbackが遅い | Flow、Baby Steps、Improvement |
| 品質を下げて納期を合わせようとしている | Quality、Economics、Mutual Benefit |
| 失敗を隠して再発している | Failure、Reflection、Opportunity |
| 一部の人だけが決定・責任を負う | Humanity、Diversity、Accepted Responsibility |

表は対応表の例であり、唯一のmappingではない。

### Primary Practices

第2版のPrimary Practicesは13個。[^xp-second-edition]

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

Primaryという分類だけで「すべて今すぐ導入する必須項目」とは扱わない。

現在のproblemに関係するPracticeを選び、既存の働き方、team size、remote / solo環境、権限・制約へ比例させる。

### Corollary Practices

第2版のCorollary Practicesは11個。[^xp-second-edition]

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

Corollary Practiceも採用数で評価しない。

現在のCapabilityやPrimary Practiceの土台がない状態で、Daily Deploymentなどの名前だけを目標にしない。必要な安全性・feedback・delivery capabilityを先に証拠で確認する。

### 同じ概念が他体系に現れても重複ルールを作らない

| XPでの位置づけ | 他lensでの位置づけ |
| --- | --- |
| Continuous Integration = Primary Practice | DORAではFast feedback Capability、CDのfoundation |
| Test-First Programming = Primary Practice | TDDとしてsoftware-developmentで具体的に実行 |
| Incremental Design = Primary Practice | Simple Design / YAGNI / Refactoringと開発loopで結びつく |
| Incremental Deployment / Daily Deployment = Corollary Practices | CD / DORAのdelivery capabilityと関係する |
| Whole Team = Primary Practice | Team Topologiesのteam typeや組織図とは別概念 |

同じ名前・近い考えが複数lensへ現れたら、別々の必須ルールを追加せず、「どの観点で何を観測するか」を区別する。

### Problemから関連するXP lensだけを選ぶ

| Problem | 最初に見るXP lens |
| --- | --- |
| 要件の認識違いが多い | Communication、Feedback、Stories、Whole Team |
| 設計が先回りして複雑化する | Simplicity、Economics、Baby Steps、Incremental Design |
| feedbackが遅く変更が大きい | Feedback、Flow、Baby Steps、CI、Test-First、Incremental Design |
| 継続できない働き方 | Respect、Humanity、Energized Work、Slack |
| 同じ失敗を繰り返す | Courage、Reflection、Failure、Root-Cause Analysis |
| 責任と権限がずれる | Respect、Accepted Responsibility、Whole Team |

必要な証拠は、実際の変更、feedback時間、設計判断、関係者の経験、テスト・統合履歴などから取る。

「Pair Programmingをしていない」「Sit Togetherしていない」だけでXP不足と判定しない。remote teamやsolo workでは目的を保った別の実現方法があり得る。

### Runtimeでの役割分担

- Valuesと常時使う短い判断原則は共通Instructionへ置く。
- TDD、Pair Programming、Incremental Design等の具体的実行は `software-development` が担当する。
- 診断時のtaxonomy・選択・証拠判断は `engineering-assessment` が担当する。
- Architecture / Organizationの詳細は[専用lens](architecture-and-organization.md)を読む。
- DORAのCore / Capability / metricsは[DORA lens](dora.md)を読む。

XP全taxonomyを通常runtimeへ常時ロードしない。診断対象がXPまたは関連problemのときだけこのreferenceを読む。

[^xp-second-edition]: [Extreme Programming Explained: Embrace Change, 2nd Edition — Kent Beck / Cynthia Andres](https://www.informit.com/store/extreme-programming-explained-embrace-change-9780134051987)。2004年版のTable of Contentsは5 Values、14個のnamed Principles、13 Primary Practices、11 Corollary Practicesを列挙する。同じpublisherページの紹介文には「Eleven principles」とあるため、Principles数はTOCの列挙を採用し不一致を明記する。2026-09-27確認。
[^ron-jeffries-xp]: [What is Extreme Programming? — Ron Jeffries](https://ronjeffries.com/xprog/what-is-extreme-programming/)。5 Valuesと、小さいfeedback・現在の要求へXPを適用する考え方。2026-09-27確認。
