---
type: Reference
title: 開発実践の原則と関係
description: 開発実践の役割と重なりを短く整理し、必要なfocused referenceへ案内します。
---

## 開発実践の原則と関係

各概念は別々の必須チェックリストではない。利用者の成果を起点に、理解・設計・実装・統合・配布・運用のfeedbackをつなぐ。

詳細を毎回ここへ重複記載せず、problemに応じて必要なfocused referenceだけを読む。

### Lensの役割

| Lens | 主に答える問い | 詳細 |
| --- | --- | --- |
| XP | 小さく作り、feedbackから学び、現在の要求へ設計を進化させられるか | [XP taxonomy](xp.md) |
| Lean | 価値が届くまでのWIP・待ち・手戻り・handoffをどう減らすか | この文書と[診断手順](assessment.md) |
| DDD | 何をモデル化し、どこまで同じ意味・言語が通用するか | semantic / architectureの関係は[ArchitectureとOrganization](architecture-and-organization.md) |
| CI | 小さな変更が頻繁にmainへ統合され、速いfeedbackと修復が続いているか | 実装は `change-delivery`、診断は[診断手順](assessment.md) |
| Continuous Delivery | 必要なときに検証済み変更を安全に配布可能な状態へ保てるか | DORA Capabilityとの関係は[DORA lens](dora.md) |
| DevOps | developmentからoperationsまで利用者成果・品質・運用のfeedback loopを閉じられるか | [診断手順](assessment.md) |
| Team Topologies / Conway | ownership・interaction・cognitive loadとsoftware boundaryをどう整えるか | [ArchitectureとOrganization](architecture-and-organization.md) |
| DORA | Capability・Performance・Outcomeを証拠からどう診断するか | [DORA lens](dora.md) |

### 重なる概念を別ルールへ複製しない

同じ概念は体系によって分類や用途が変わる。

| 概念 | 一つのlensでの扱い | 別lensでの扱い |
| --- | --- | --- |
| Continuous Integration | XPのPrimary Practice | DORAのFast feedback Capability |
| Continuous Delivery | delivery system / capability | DORAのFast flow Capability |
| Small Batches | Lean / XPのflow・feedbackを支えるPractice | DORA Capability |
| Loosely Coupled Teams | Architecture / Organization上の独立性 | DORA Fast flow Capability |
| Documentation Quality | 文書作成そのものではなく利用可能な知識の状態 | DORA Climate for learning Capability |

分類差を矛盾とみなさず、現在のproblemで何を観測するかを明示する。

### 成果物だけで実践を断定しない

| 概念 | 成果物だけでは分からないこと |
| --- | --- |
| BDD | Gherkinの存在だけでは共同のDiscovery / Formulationを示さない |
| ATDD | 受け入れテストの存在だけでは実装前に条件を共有した証拠にならない |
| TDD | 完成したテストだけではRedを先に確認した過程を示さない |
| DDD | 用語集やclass名だけではshared meaningやmodel boundaryを示さない |
| CI | workflow YAMLだけでは頻繁なmain統合やbroken build修復を示さない |
| CD | deploy jobだけではon-demandで安全に配布できることを示さない |
| Team Topologies | CODEOWNERSやteam名だけでは責任・interaction・cognitive loadを示さない |
| DORA Capability | tool / configの存在だけでは観測可能なCapabilityを示さない |

実際の変更、履歴、待ち、失敗、配布、関係者の経験などを[診断手順](assessment.md)に従って確認する。

### 必要なlensだけを組み合わせる

例:

- Ubiquitous Languageの食い違いだけ → DDD中心。DORAやArchitectureを無関係に展開しない。
- release承認待ち → Lean / CD + 関連DORA Fast flow Capability。
- cross-team dependency → Architecture / Organization + Team Topologies、必要ならDORA Loosely Coupled Teams。
- Microservices採否 → Architecture / Organization + DDD + XP Simplicity。DORA Catalog全件は評価しない。
- XPの設計・feedback診断 → XP focused lens。全Practiceの導入数を採点しない。

診断対象を広げる場合は、利用者の目的への影響を説明できることを条件にする。

出典・版差は[一次資料と適用判断](sources.md)で確認する。
