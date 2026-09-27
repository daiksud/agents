---
type: Reference
title: ArchitectureとOrganizationの境界を診断する
description: DDD・Team Topologies・Conway・Continuous Deliveryの観点から、意味・変更・実行・配布・所有の境界とMicroservices等の選択を証拠で診断します。
sources:
  - id: ddd-reference
    resource: https://www.domainlanguage.com/ddd/reference/
  - id: team-topologies-key-concepts
    resource: https://teamtopologies.com/key-concepts
  - id: continuous-delivery-architecture
    resource: https://continuousdelivery.com/implementing/architecture/
  - id: dora-loosely-coupled-teams
    resource: https://dora.dev/capabilities/loosely-coupled-teams/
---

## ArchitectureとOrganizationの境界を診断する

Domain model、service分割、Microservices、team ownership、cross-team dependencyなど、意味の境界とdelivery上の境界が関係する診断で読む。すべての診断に適用せず、対象の困りごとがboundary・coupling・team interactionに関係するときだけ使う。

目的は特定のarchitecture styleや組織図を導入することではない。利用者の成果へ影響している依存を、種類の違う境界へ分解し、現在必要な最小の改善を選ぶ。

### 境界の種類を先に分ける

同じ線に見えても、境界ごとに答える問いが違う。

| 境界 | 診断する問い | 主な証拠 |
| --- | --- | --- |
| Domain boundary | どの業務問題・知識を扱うか | 利用者の目的、業務能力、用語、業務判断 |
| Bounded Context / semantic boundary | どこまで同じモデルと言葉の意味が通用するか | Ubiquitous Language、モデル、Context Map、翻訳・契約 |
| Change boundary | 何を独立して理解・変更・検証できるか | 実変更の差分、テスト依存、同時変更、review待ち |
| Runtime boundary | 何が別process / componentとして実行されるか | runtime topology、process間通信、failure propagation |
| Deployment boundary | 何を独立してbuild・deploy・rollbackできるか | pipeline、artifact、release履歴、同時deployの必要性 |
| Repository boundary | source・history・automationをどの単位で管理するか | repository、build、ownership設定、tooling |
| Team ownership boundary | 誰が継続的な判断・運用・改善責任を持つか | 実際の責任、on-call、変更承認、問い合わせ、team experience |

一つのBounded Contextが一つのservice・repository・teamになる場合はあるが、それ自体を設計規則にしない。Eric EvansのDDDではBounded Contextはモデルの適用範囲を明示し、Context Mapで他のモデルとの接点・翻訳・影響関係を扱う。[^ddd-reference]

次のような対応は仮説として検証できるが、完全一致を成功条件にしない。

```text
semantic boundary
≈ change boundary
≈ deployment boundary
≈ team ownership boundary
```

Domain boundaryは業務問題・知識の範囲であり、このalignment chainそのものではない。Repository boundaryやRuntime boundaryも、現在のtooling・operational constraintによって別の形を取れる。

### Architectureは独立性の結果で診断する

Architecture styleやservice数ではなく、実際のchange / test / deployment independenceを確認する。

Continuous Deliveryのarchitecture guidanceはtestabilityとdeployabilityを重要な属性として扱い、loosely-coupledでwell-encapsulatedなcomponentを、統合環境や大規模orchestrationへ過度に依存せず検証・配布できる状態として説明する。既存systemを一度に作り直さず、必要に応じてevolutionaryに改善する。[^continuous-delivery-architecture]

DORAのLoosely Coupled Teamsも、使用技術ではなく次のような観測可能な結果を重視する。[^dora-loosely-coupled-teams]

- 他teamの変更を要求せず大きなdesign changeを進められる。
- 日常の作業で細かなcross-team coordinationへ依存しない。
- dependency serviceと独立してdeploy / releaseできる。
- shared integrated test environmentを必須にせず大部分を検証できる。

Mainframeでもこれらを達成でき、Microservicesでも達成できない場合がある。したがって「service数が多い」「repositoryが分かれている」をloose couplingの証拠にしない。

### DDDは意味の境界をarchitectureの数へ変換しない

DDDのSubdomainはproblem space、Bounded Contextは一つのmodelと言語が適用される範囲として扱う。[^ddd-reference]

診断では少なくとも次を確認する。

- 同じ用語が境界を越えて異なる意味を持つか。
- modelを一緒に変更する必要がある理由はdomain上のinvariantか、technical couplingか。
- 境界間で何を共有し、何をtranslate / isolateするか。
- 一方の判断やrelease cadenceが他方へ不必要に波及しているか。

Technical couplingを解消するためだけに新しいSubdomainやBounded Contextを創作しない。逆に、意味が独立しているという理由だけで別runtime・別deploy・別repositoryを必須にしない。

### Team Topologiesはfast flowとcognitive loadから使う

Team Topologiesはfast flow of valueのためのteam-of-teams design approachであり、4つのteam typeと3つのinteraction modeをpattern languageとして使う。[^team-topologies-key-concepts]

4つのteam typeを「4チームを設置する組織図」として導入しない。現在の責任とcognitive loadを調べ、必要な役割を比例させる。

| Team type | 診断上の主な役割 |
| --- | --- |
| Stream-aligned | 一つの価値の流れに沿ってend-to-endで成果を届ける |
| Enabling | 他teamが能力を獲得し、自立できるよう一時的に支援する |
| Complicated Subsystem | 高度な専門知識が必要なsubsystemのcognitive loadを引き受ける |
| Platform | Stream-aligned teamが低いcognitive loadで利用できる内部product / serviceを提供する |

Interactionは目的で選ぶ。

| Interaction | 使う状況 |
| --- | --- |
| Collaboration | discoveryや新しい境界を学ぶため、期間を区切って高bandwidthで協働する |
| X-as-a-Service | ownershipと期待が安定したserviceを、低いcoordination costで利用する |
| Facilitation | 能力獲得や障害除去を支援し、依存の常態化を避ける |

team nameやCODEOWNERSだけでinteraction・cognitive load・autonomyを確定しない。実際の問い合わせ、handoff、待ち、変更・運用責任と関係者の経験を確認する。

### Conway / Inverse Conwayは相互作用の仮説として扱う

Conway's Lawはorganizationのcommunication structureとsystem designが独立ではないことを示す。Team TopologiesとDORAは、この関係を使ってteam communication patternとarchitectureの独立性を考える。[^team-topologies-key-concepts][^dora-loosely-coupled-teams]

Inverse Conway Maneuverを「desired architecture図に人員配置を一致させればよい」という処方箋にしない。

1. 現在のcommunication・変更・deploy dependencyを観測する。
2. desired outcomeを、独立change / test / deployや待ち時間の削減など観測可能な状態で表す。
3. responsibility boundaryまたはinteractionを小さく変更する。
4. flow、coordination、cognitive load、品質への影響を確認する。
5. 学習した結果からarchitectureまたはorganizationの次の変更を決める。

team再編を実施せず、診断では仮説・必要な関係者・確認方法とsmall experimentまでをIssue計画へ残す。

### MicroservicesはArchitecture choiceとして評価する

MicroservicesはBounded Contextの数から導かれる既定解ではない。独立change・deploy・scale・ownershipなど、現在必要なoutcomeへ対する選択肢として評価する。

#### 利点を必要とする証拠

- 独立release cadenceが実際に必要。
- 一部だけを独立scaleする必要がある。
- failure isolationが利用者価値・信頼性へ具体的に効く。
- 複数teamの独立ownershipが必要で、現在のdeployment / change boundaryが阻害している。
- module境界だけでは解けないtechnical / organizational couplingが観測されている。

#### 同時に受け入れるcost

- network latencyとpartial failure。
- distributed data、transaction、consistencyの複雑さ。
- observability、deployment、service discovery、dependency managementの運用負荷。
- API / event compatibilityとversioning。
- 多数のdeployable unitを支えるtooling・platform・on-call capability。

DORAもMicroservicesを採用しただけではloose couplingを保証せず、monolithでも現在の規模とflowに合う場合があると説明する。[^dora-loosely-coupled-teams]

現在の要求をmodule / single deploymentで満たせるなら、Simplicity / YAGNIに照らしてdistributed-system costを先取りしない。必要になった境界からevolutionaryに分離できる余地を、現在不要なextension pointの実装と混同しない。

### 診断結果を証拠に戻す

architecture / organizationの判断は次のいずれかとして記録する。

- **観測した実践・能力**: 実変更、deploy、interaction等の証拠がある。
- **根拠のある不足**: 目的へ影響するcoupling・待ち・failureが観測できる。
- **未確認**: 必要なruntime / ownership / team experience等の証拠がない。
- **適用外**: 現在の規模・目的ではそのboundaryやchoiceを分ける理由がない。

「Microservicesではない」「4 team typesがない」「1 repositoryである」だけを不足にしない。

最初の改善は、問題となる一つのdependencyを対象にする。たとえばcontractの明確化、test seam、deployment dependencyの除去、interaction modeの期間限定変更など、結果を観測できるsmall experimentを優先する。全面的なservice分割や組織再編は、証拠と段階的な学習なしに最初の手段へしない。

[^ddd-reference]: [DDD Reference — Domain Language](https://www.domainlanguage.com/ddd/reference/)。Bounded Context、Context Map等のDDD pattern reference。2026-09-27確認。
[^continuous-delivery-architecture]: [Architecture — Continuous Delivery](https://continuousdelivery.com/implementing/architecture/)。testability、deployability、loosely-coupled component、evolutionary architectureの判断。2026-09-27確認。
[^dora-loosely-coupled-teams]: [Loosely coupled teams — DORA](https://dora.dev/capabilities/loosely-coupled-teams/)。独立change / test / deploy、communication dependency、Inverse ConwayとMicroservicesのtrade-off。2026-09-27確認。
[^team-topologies-key-concepts]: [Key Concepts — Team Topologies](https://teamtopologies.com/key-concepts)。fast flow、4 team types、3 interaction modes、cognitive load、Conway's Law。2026-09-27確認。
