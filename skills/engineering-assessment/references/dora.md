---
type: Reference
title: DORAをCapability lensとして診断する
description: DORA Core Model、Capability Catalog、software delivery metrics、annual researchを区別し、問題に関係するCapabilityだけを証拠から診断します。
sources:
  - id: dora-core-v2-1-0
    resource: https://dora.dev/research/core/assets/dora-core-v2.1.0-detail.pdf
  - id: dora-research
    resource: https://dora.dev/research/
  - id: dora-capabilities
    resource: https://dora.dev/capabilities/
  - id: dora-metrics
    resource: https://dora.dev/guides/dora-metrics/
  - id: dora-metrics-history
    resource: https://dora.dev/insights/dora-metrics-history/
  - id: dora-small-batches
    resource: https://dora.dev/capabilities/working-in-small-batches/
---

## DORAをCapability lensとして診断する

DORA、Capability Catalog、Core Model、delivery metrics、Quick Checkなどを使う診断で読む。DORAを全項目の導入チェックリストや個人評価表として使わず、利用者の困りごとへ関係するCapability・performance・outcomeだけを選ぶ。

### 4つのDORA成果物を分ける

| 対象 | 役割 | 誤用しないこと |
| --- | --- | --- |
| Core Model | DORA研究で繰り返し支持されたCapability・Performance・Outcomeの関係を、保守的にまとめたmodel | 最新のCatalog項目や最新metrics定義を自動的にCoreへ追加しない |
| Capability Catalog | 改善に使えるCapabilityや研究テーマのcatalog。各項目に `core` / `AI` 等のlabelが付く場合がある | Catalog全体をCoreや必須導入一覧とみなさない |
| Software delivery performance metrics | 対象application / serviceのdelivery performanceを時系列で観測するmetrics | Capabilityそのものや個人performanceとみなさない |
| Annual / ongoing research | 新しい技術・働き方・関係を継続的に研究する成果 | 一年の新知見を即座にCoreの固定関係へ読み替えない |

DORA Core Model v2.1.0は、研究全体の中でも比較的確立した関係をpractitioner向けに整理し、ongoing researchより意図的に保守的に更新される。Coreの具体的な構造は固定v2.1.0資料を正本にする。[^dora-research][^dora-core-v2-1-0]

### Core v2.1.0は3つのCapability groupを持つ

Core v2.1.0ではCapabilityを次の3群に整理する。[^dora-core-v2-1-0]

| Group | Coreに記載されるCapability |
| --- | --- |
| Climate for learning | Code Maintainability、Documentation quality、Empowering teams to choose tools、Generative culture |
| Fast flow | Continuous delivery、Database change management、Deployment automation、Flexible infrastructure、Loosely coupled teams、Streamlining change approval、Version control、Working in small batches |
| Fast feedback | Continuous integration、Monitoring and observability、Reliability engineering、Pervasive security、Test automation、Test data management |

これらの名称を、すべての診断で順番に採点する質問票へ変換しない。現在のproblem・value stream・観測証拠から関連するgroupとCapabilityだけを使う。

CoreはCapabilityからPerformanceを予測し、PerformanceからOrganizational performance / Well-beingなどのOutcomeを予測する関係を示す。PerformanceではSoftware deliveryをFour key metrics、ReliabilityをSLOsで扱う。[^dora-core-v2-1-0]

### Capability CatalogはCoreより広い

Capability Catalogには `core` と表示された項目だけでなく、AI関連やCore外の項目も含まれる。たとえばWorking in small batchesには `core` と `AI` の両labelが表示される。[^dora-capabilities]

したがって次を区別する。

- Catalogに存在すること。
- 現在のCore Modelに含まれること。
- AI等の特定研究テーマと関係すること。
- 今回のproblemを診断するのに必要であること。

Catalog全件を「未導入なら不足」と判定しない。新しいCatalog項目をCoreへ含めるかどうかはDORAのCore更新に従い、本スキルが独自に昇格させない。

### CoreのFour key metricsと現行5 metricsを混同しない

Core v2.1.0の図はSoftware delivery performanceをFour key metricsで示す一方、現行DORA metrics guideはsoftware delivery performanceを5指標で扱う。[^dora-metrics]

現行guideの5指標:

| Factor | Metric | 対象 |
| --- | --- | --- |
| Throughput | Change lead time | commitからproduction deploymentまで |
| Throughput | Deployment frequency | 一定期間のdeployment回数または間隔 |
| Throughput | Failed deployment recovery time | failed deploymentからの復旧 |
| Instability | Change fail rate | immediate interventionが必要になったdeploymentの割合 |
| Instability | Deployment rework rate | production incident等に起因する予定外deploymentの割合 |

Deployment rework rateは2024年に追加され、DORAのsoftware delivery performance metricsはFour Keysから5 metricsへ進化した。[^dora-metrics-history]

これは「Core v2.1.0のFour key metricsという図を5項目へ書き換える」という意味ではない。Core Modelと最新metrics guideは更新周期と役割が異なるため、参照した成果物・version・確認日を示して使う。

### PracticeとCapabilityは観点によって分類が変わる

同じ概念が別体系で異なる分類になることを矛盾扱いしない。

| 概念 | 他のlens | DORAでの扱い |
| --- | --- | --- |
| Working in small batches | Leanのflow改善、XPのsmall feedbackと整合するPractice | Core Capability。短いfeedback loopと学習を支える[^dora-small-batches] |
| Continuous integration | XP由来のPractice、CDを支えるdevelopment practice | Core / Fast feedback Capability |
| Continuous delivery | 複数Practiceから成るdelivery system / capability | Core / Fast flow Capability |
| Loosely coupled teams | Architecture / Organizationの独立性という設計・組織特性 | Core / Fast flow Capability |
| Documentation quality | 文書の作成行為そのものではなく利用可能性・品質を含む状態 | Core / Climate for learning Capability |

名前を一つのtaxonomyへ強制的に統一せず、「どのlensで何を観測するか」を示す。

### 設定ではなく実際のCapabilityを観測する

tool・設定・文書の存在だけでCapability達成と判定しない。

| Capabilityの例 | 実際に確認する証拠 |
| --- | --- |
| Continuous integration | branch寿命、mainへの実統合頻度、feedback時間、broken buildの修復例 |
| Continuous delivery | on-demandで安全にdeploy可能か、実配布・復旧・承認待ちの記録 |
| Monitoring and observability | 実際の検知・調査・debugでsignalが使えた記録、担当者の経験 |
| Loosely coupled teams | 他teamの細かな調整なしのchange / test / deploy実績 |
| Documentation quality | 必要な人が文書を見つけ、理解し、実際の作業に利用できた証拠 |
| Working in small batches | 実際のwork item / change size、feedbackまでの時間、WIP・待ち |

「GitHub Actionsがある」「Datadogがある」「Argo CDがある」などをCapabilityの達成と同一視しない。証拠が取れなければ未確認として残す。

### Problemから必要なlensだけを選ぶ

| 観測したproblem | 最初に見るDORA lens | 併用候補 |
| --- | --- | --- |
| PR後のrelease承認待ちが支配的 | Fast flow / Continuous delivery / Streamlining change approval | Lean、DevOps |
| CI feedbackが遅い・main統合が滞る | Fast feedback / Continuous integration / Test automation | XP、Small batches |
| cross-team調整で変更・配布が止まる | Fast flow / Loosely coupled teams | Architecture / Organization、Team Topologies |
| knowledgeが特定担当者へ集中する | Climate for learning / Documentation quality / Generative culture | XP Communication |
| AI導入の効果・摩擦を調べる | CatalogのAI関連項目のうちproblemに関係するもの | Coreのunderlying sociotechnical Capability |

問題へ関係しないCapabilityを機械的に「未確認一覧」へ足さない。

### Metricsは改善のfeedbackであり目標そのものではない

metricsはapplication / service単位で、期間・定義を揃えて変化を見る。複数serviceの不揃いな数字を一つのrankingにまとめず、個人performance評価へ使わない。

Deployment frequencyだけを上げるなど、metricを直接操作することを改善としない。利用者成果、reliability、well-beingと、対象Capabilityの変化を合わせて確認する。固定Elite閾値を普遍的な合否基準として使わない。

最初の改善は、現在の制約へ最も関係するCapabilityを一つまたは小さなまとまりで選び、期待する変化・証拠・見直し条件を整理する。回答だけが依頼された場合は直接提示し、Issue記録が終端成果物として依頼された場合だけIssueへ保存する。

[^dora-research]: [DORA Research / Core Model](https://dora.dev/research/)。Core v2.1.0の3 Capability group、Performance、Outcomeと、Coreを保守的に更新する位置づけ。2026-09-27確認。
[^dora-core-v2-1-0]: [DORA Core v2.1.0 detail](https://dora.dev/research/core/assets/dora-core-v2.1.0-detail.pdf)。3 Capability group、Software delivery / Reliability Performance、Outcomeの固定版正本。2026-09-27確認。
[^dora-capabilities]: [DORA Capability Catalog](https://dora.dev/capabilities/)。`core` / `AI` 等のlabelを持つ広いCatalogとCore Modelを区別するために参照。2026-09-27確認。
[^dora-metrics]: [DORA software delivery performance metrics](https://dora.dev/guides/dora-metrics/)。現行5 metricsとThroughput / Instabilityの定義。2026-09-27確認。
[^dora-metrics-history]: [A history of DORA's software delivery metrics](https://dora.dev/insights/dora-metrics-history/)。2024年のDeployment rework rate追加とFour Keysから5 metricsへの変遷。2026-09-27確認。
[^dora-small-batches]: [Working in small batches — DORA](https://dora.dev/capabilities/working-in-small-batches/)。Core / AI label、feedback loopとLean product managementとの関係。2026-09-27確認。
