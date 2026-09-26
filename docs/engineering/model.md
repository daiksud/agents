---
type: Reference
title: Engineering model
description: 開発実践の価値・原則、プラクティス、能力、アーキテクチャ・組織上の選択を区別し、各lensの関係と境界を整理します。
sources:
  - id: ron-jeffries-xp
    resource: https://ronjeffries.com/xprog/what-is-extreme-programming/
  - id: lean-what-is-lean
    resource: https://www.lean.org/explore-lean/what-is-lean/
  - id: ddd-reference
    resource: https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf
  - id: continuous-delivery
    resource: https://continuousdelivery.com/
  - id: continuous-integration
    resource: https://continuousdelivery.com/foundations/continuous-integration/
  - id: team-topologies
    resource: https://teamtopologies.com/key-concepts
  - id: dora-research
    resource: https://dora.dev/research/
  - id: dora-capabilities
    resource: https://dora.dev/capabilities/
  - id: google-cloud-devops
    resource: https://cloud.google.com/devops
---

## Engineering model

この文書は、`daiksud/agents` が参照するソフトウェアエンジニアリングの考え方を、メンテナが矛盾なく配置・更新するための概念モデルである。利用先のプロジェクトへ特定の方法論・組織形態・アーキテクチャを一律に強制する仕様ではない。

既存の runtime Instruction / Skill は作業時の判断と実行手順を担う。この文書はそれらの上位に常時読み込ませるInstructionではなく、概念の分類、関係、配置判断を保守するときの正本として使う。

本文は2026-09-27に一次・公式資料を再確認した。既存体系の詳細・版差・採用判断と、この単位で追加したDORA Capability Catalog / DevOps資料の確認記録は `skills/engineering-assessment/references/sources.md` で管理する。Core / Catalogの詳細mappingなど後続Unitへ延期した判断は、この文書の「後続の整理」で未実装として明示する。

### 分類は成熟度の階層ではない

このリポジトリでは、開発実践を次の4分類で整理する。

| 分類 | 主な役割 | 例 |
| --- | --- | --- |
| Values / Principles | 判断時に何を優先するかを示す | XP Values、Leanの価値・流れ、人の尊重、Simplicity |
| Practices | 繰り返し実行する具体的な行動 | TDD、Pair Programming、CI、Small Batches |
| Capabilities | チーム・システムが実際に持つ観測可能な能力 | Continuous Delivery、Code Maintainability、Loosely Coupled Teams |
| Architectural / Organizational Choices | 現在の条件から選ぶ構造・配置・責任境界 | Microservices、module boundaries、team boundaries |

これらを次のような一方向の成熟度モデルとして扱わない。

```text
Values / Principles
        ↓
Practices
        ↓
Capabilities
        ↓
Choices
```

ValueやPrincipleがPracticeの選択を導き、複数のPracticeがCapabilityを支え、Capability上の制約からArchitectureやOrganizationのChoiceを見直すことはある。しかし実際の関係は多対多であり、Choiceから新しい制約やFeedbackが生まれてPrinciple・Practiceを見直すこともある。

同じ概念が、体系によって別の分類に現れても矛盾とは扱わない。たとえばContinuous IntegrationはXP由来のPracticeとして説明できる一方、DORAではSoftware Deliveryを支えるCapabilityとして扱われる。[^ron-jeffries-xp][^continuous-integration][^dora-capabilities]

### Lensごとに答える問いを分ける

方法論名を同列の必須チェックリストへ変換せず、対象の困りごとへ答えるためのlensとして使う。

| Lens | 主に答える問い |
| --- | --- |
| XP | 現在必要な価値へ向けて、小さく作り、早くFeedbackを得て、設計を進化させられるか |
| Lean | 価値が届くまでの流れで、WIP・待ち・手戻り・handoffをどう減らすか |
| DDD | 何をモデル化し、どこまで同じ意味・言語・モデルが通用するか |
| Continuous Delivery | 変更を小さく安全に、必要なときに配布可能な状態へ保てるか |
| DevOps | DevelopmentからOperationsまで、利用者の成果・品質・運用のFeedback loopを閉じられるか |
| Team Topologies | Cognitive loadを抑えながら、責任とinteractionを価値の流れへ合わせられるか |
| Conway | Communication・ownership構造とsoftware architectureがどう影響し合うか |
| DORA | Deliveryのcapability・performance・outcomeを、観測可能な証拠からどう診断するか |

XPはCommunication・Simplicity・Feedback・Courage・Respectを開発判断へ結びつける。Leanは価値の流れ全体を見て局所最適を避ける。DDDはモデルと意味の境界を扱う。これらは互いを置き換えるものではない。[^ron-jeffries-xp][^lean-what-is-lean][^ddd-reference]

Continuous Deliveryは変更を配布可能に保つsystem of workであり、CIやSmall Batchesなど複数のPracticeに支えられる。DevOpsは、開発と運用を近づけ、software stakeholdersのshared ownership、delivery velocity、service reliabilityを改善するorganizational / cultural movementとして扱う。本リポジトリではこのshared ownershipを、productionでの利用・運用・学習まで含むend-to-end feedbackの判断へ適用する。[^continuous-delivery][^continuous-integration][^google-cloud-devops]

Team Topologiesは4つのteam typeを固定組織図として導入するためではなく、fast flow、cognitive load、team interaction、Conway's Lawを使って組織とsoftware architectureを継続的に見直すために使う。[^team-topologies]

DORAは、Core Model、Capability Catalog、delivery metrics、年次研究を同一の必須一覧として扱わない。Core Modelは繰り返し支持された研究上の関係を比較的保守的に整理し、Capability CatalogにはCore外や新しい研究領域の項目も含まれる。[^dora-research][^dora-capabilities]

### 代表的な関係は多対多になる

一つのValueやPrincipleから一つのPracticeだけが導かれるわけではない。

```text
Feedback
  ├─ Small Batches
  ├─ TDD
  ├─ Continuous Integration
  ├─ observability
  └─ customer / production feedback
       ↓
  shorter feedback loops
```

同じように、Continuous Deliveryは一つのtoolやworkflowではなく、複数のPracticeとCapabilityの組み合わせで成立する。

```text
Small Batches
       ┐
Continuous Integration
       ├─→ Continuous Delivery capability
Test Automation
       │
Deployment Automation
       │
Loosely Coupled Teams
       ┘
```

この関係を使って「DORAに書かれているから別のルールを追加する」のではなく、既存のXP・Lean・CD等の考え方と重なる場合は一つの判断へ統合する。

### 境界は意味・変更・実行・責任で分けて考える

以下はそれぞれ異なる境界である。

| 境界 | 主な問い |
| --- | --- |
| Domain boundary | どの業務問題・知識を扱うか |
| Bounded Context / semantic boundary | どこまで同じモデルと言葉の意味が通用するか |
| Change boundary | 何を独立して理解・変更・検証できるか |
| Runtime boundary | 何が別process・componentとして実行されるか |
| Deployment boundary | 何を独立して配布・rollbackできるか |
| Repository boundary | どのsource・history・automationを同じ管理単位にするか |
| Team ownership boundary | 誰が継続的な意思決定・運用・改善責任を持つか |

DDDはDomainの問題範囲を理解し、モデルと言語の意味が通用するsemantic boundaryをBounded Contextとして明示する。DeliveryとarchitectureはChange・Runtime・Deploymentの依存を扱う。Team TopologiesはTeam ownershipとinteraction、cognitive loadを扱う。これらは関連するが同義ではない。[^ddd-reference][^team-topologies]

望ましい場合には、

```text
Bounded Context / semantic boundary
≈ Change boundary
≈ Deployment boundary
≈ Team ownership boundary
```

のように整合することがある。ただし完全一致を原則にしない。Domain boundaryは業務問題・知識の範囲であり、このalignment chainと同一視しない。Repository、Service、Bounded Context、Teamを機械的に1対1対応させず、実際のchange coupling、deployment dependency、cognitive load、operational responsibilityから関係を説明する。

### MicroservicesはArchitecture choiceである

MicroservicesはValue、Principle、Practice、Capabilityそのものではなく、独立した変更・配布・ownershipなどを実現するために選び得るArchitecture choiceとして扱う。

採否は少なくとも次を区別して調べる。

- Domain boundary
- Bounded Context / semantic boundaries
- change coupling
- independent deliveryの必要性
- team ownershipとcommunication dependency
- scalingやfailure isolationの必要性
- observability・deployment・data consistency等のoperational maturity
- network、latency、partial failure、distributed dataなどのdistributed-system cost

DDDを採用していること、Bounded Contextが存在すること、複数Teamが存在することだけをMicroservices採用理由にしない。現在の要求をより単純なmoduleやsingle deploymentで満たせるなら、Simplicity / YAGNIと照合して複雑さを増やさない。

### 配置の判断

概念を見つけたときは、その名前ではなく責務で配置する。

| 内容 | 主な配置 |
| --- | --- |
| 多くの作業で常に使う短い判断原則 | `.apm/instructions/` |
| 特定作業を実行する具体的な手順 | 対応する `skills/*` |
| 診断時だけ必要な定義・関係・証拠 | `skills/engineering-assessment/references/` |
| メンテナが体系全体の配置・関係を見直すための正本 | `docs/engineering/` |

方法論の全Principle・Practice・CapabilityをInstructionへ列挙しない。通常runtimeがこの文書を全文読む依存も作らない。作業時に必要な最小限の判断だけをInstruction / Skillへ置き、詳細はprogressive disclosureで参照する。

### 後続の整理

この文書は分類と境界だけを定義する。次の詳細は後続の統合単位で扱う。

- XPのValues / Principles / Primary Practices / Corollary Practicesの分類とassessmentでの読み分け
- DDD / Team Topologies / Conway / Architecture choiceを使う診断手順
- DORA Core Model / Capability Catalog / delivery metricsの版と関係
- 問題から必要なlensだけを選ぶ `engineering-assessment` のprogressive disclosure

[^ron-jeffries-xp]: [What is Extreme Programming? — Ron Jeffries](https://ronjeffries.com/xprog/what-is-extreme-programming/)。XPの価値と、小さいFeedbackで設計を進化させる考え方。2026-09-27確認。
[^continuous-integration]: [Continuous Integration](https://continuousdelivery.com/foundations/continuous-integration/)。XP由来のCI、頻繁なmain統合、小さいbatch、壊れたbuildの優先修復。2026-09-27確認。
[^dora-capabilities]: [DORA Capability Catalog](https://dora.dev/capabilities/)。Coreに含まれるCapabilityとCore外・AI関連等の項目が同じCatalogにあることを区別する。2026-09-27確認。
[^lean-what-is-lean]: [What is Lean? — Lean Enterprise Institute](https://www.lean.org/explore-lean/what-is-lean/)。顧客価値、流れ、人、継続的な実験の関係。2026-09-27確認。
[^ddd-reference]: [Domain-Driven Design Reference — Eric Evans](https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf)。Ubiquitous Language、Bounded Context、Context Map等のモデル境界。既存固定資料を2026-09-27再確認。
[^continuous-delivery]: [Continuous Delivery](https://continuousdelivery.com/)。配布可能な状態、小さい変更、共同責任と継続的なFeedback。2026-09-27確認。
[^google-cloud-devops]: [DevOps — Google Cloud](https://cloud.google.com/devops)。DevOpsをsoftware stakeholdersのshared ownershipを含むorganizational / cultural movementとして説明する公式資料。2026-09-27確認。
[^team-topologies]: [Team Topologies — Key Concepts](https://teamtopologies.com/key-concepts)。Team type、interaction、cognitive load、Conway's Lawをfast flowへ結びつける。2026-09-27確認。
[^dora-research]: [DORA Research](https://dora.dev/research/)。Core Modelを繰り返し支持された研究上のcapability・metric・outcomeの関係として扱う。2026-09-27確認。
