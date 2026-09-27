---
type: Reference
title: XPをValues・Principles・Practicesとして診断する
description: Extreme Programming第2版のValues、Principles、Primary / Corollary Practicesを区別し、現在の問題に関係する項目だけを証拠から診断します。
sources:
  - id: xp-second-edition
    resource: https://www.informit.com/store/extreme-programming-explained-embrace-change-9780134051987
  - id: ron-jeffries-xp
    resource: https://ronjeffries.com/xprog/what-is-extreme-programming/
  - id: xp-second-edition-principles
    resource: https://www.oreilly.com/library/view/extreme-programming-explained/0321278658/ch05.xhtml
  - id: xp-second-edition-primary-practices
    resource: https://www.oreilly.com/library/view/extreme-programming-explained/0321278658/ch07.xhtml
  - id: xp-second-edition-corollary-practices
    resource: https://www.oreilly.com/library/view/extreme-programming-explained/0321278658/ch09.xhtml
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

第2版の5 Valuesを、診断では次のbehaviorへ結びつける。[^ron-jeffries-xp]

| Value | 診断上の意味・観測例 |
| --- | --- |
| Communication | 目的・制約・具体例・未回答事項を必要な関係者が共有し、異なる理解を早く確かめられるかを見る |
| Simplicity | 現在確認されている要求を満たす理解しやすい最小の設計を選び、仮想の将来要件を先取りしていないかを見る |
| Feedback | test・統合・利用者反応・運用などから短い間隔で結果を得て、次の小さい判断へ反映できるかを見る |
| Courage | 欠陥・不確実性・不要になった設計を隠さず、証拠を根拠に必要な変更・改善へ進めるかを見る |
| Respect | 利用者の判断権限、関係者の知識・時間、持続可能な働き方を尊重し、責任だけを一方的に負わせていないかを見る |

固定会議・固定役割・特定team構成をValueそのものの要件にはしない。

### Principles

InformITのTable of Contentsは次の14 Principlesを列挙する。同じpublisherページの紹介文には「Eleven principles」という不一致があるため、本リポジトリでは列挙されたTOCをtaxonomyの根拠にし、この差をprovenanceへ残す。[^xp-second-edition]

本リポジトリでは、各Principleを次の診断上の意味へ要約する。原文の置換ではなく、現在のproblemと観測証拠へ結びつけるための適用判断である。[^xp-second-edition-principles]

| Principle | 診断上の意味・観測例 |
| --- | --- |
| Humanity | 人が継続して良い仕事をできる基本的なneeds・関係・安全性を尊重する。疲弊、孤立、責任と権限の不一致を確認する |
| Economics | time・cost・value・opportunity costを含む経済的結果から優先順位とscopeを判断する。技術的好みだけで投資を増やさない |
| Mutual Benefit | 今日の成果と将来の変更容易性など、関係者の利益を同時に増やす選択を探す。一方の犠牲を常態化しない |
| Self-Similarity | 別scaleで機能したfeedback・分割・検証のpatternを類似問題へ仮説として適用し、同じ結果になるか確認する |
| Improvement | 完璧な最終状態を待たず、現在状態から測定可能な小さい改善を続ける |
| Diversity | 異なる経験・専門性・観点を早く衝突させ、見落としを減らす。形式的な全員一致を目的にしない |
| Reflection | 結果と進め方を振り返り、何が起きたか・なぜか・次に変えることをfeedbackへ戻す |
| Flow | 価値あるworkを小さく連続して進め、queue・handoff・WIP・batchによる滞留を減らす |
| Opportunity | problem・変更・制約を単なる障害ではなく、systemを改善する学習機会として扱う |
| Redundancy | 重大な失敗を一つの防御だけに依存せず、test・review・monitoring等の相補的な安全策を必要性に応じて持つ。無目的な重複とは区別する |
| Failure | 安全に小さく試せる範囲では失敗から学ぶ。失敗を隠さず、再現・原因・次の実験へfeedbackする |
| Quality | speedのためにqualityを恒常的に下げる前提を置かず、scope・方法・順序を調整して持続可能なqualityを守る |
| Baby Steps | reversibleで検証可能な最小のstepへ分割し、各stepのfeedbackから次を決める |
| Accepted Responsibility | 実行責任を引き受ける人・teamが判断に必要な権限と情報を持つようにし、責任だけを一方的に割り当てない |

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

本リポジトリでは、Practice名の有無ではなく目的と観測可能なbehaviorを診断する。[^xp-second-edition-primary-practices]

| Primary Practice | 診断上の意味・観測例 |
| --- | --- |
| Sit Together | 必要な人が低いcommunication costで継続的に協働できるかを見る。物理同席をremote teamへ機械的に強制しない |
| Whole Team | 価値を届けるために必要なbusiness・development・testing等の視点へアクセスでき、handoffだけに責任を分断していないかを見る |
| Informative Workspace | 進捗・quality・risk等の重要情報を必要な人が容易に把握できるかを見る。物理掲示板に限定しない |
| Energized Work | 判断とqualityを維持できる持続可能な働き方か、慢性的な疲労や過負荷がないかを見る |
| Pair Programming | 実装中に2つの視点で連続的にdesign・review・knowledge sharingできるかを見る。目的を満たす別形態を無条件に不足扱いしない |
| Stories | 利用者価値の単位でscope・cost・期待を会話でき、小さく優先順位を変えられるかを見る。card形式を必須にしない |
| Weekly Cycle | 近い期間のplan・delivery・feedbackを短いcadenceで見直せるかを見る。暦上の7日を絶対条件にしない |
| Quarterly Cycle | より大きなtheme・investment・directionを定期的に見直し、短期計画へcontextを与えられるかを見る。厳密な3か月を強制しない |
| Slack | uncertainty・改善・予期せぬworkを吸収できる余地があり、100% utilizationを目標にしていないかを見る |
| Ten-Minute Build | build / test feedbackが頻繁に実行できるほど速いかを見る。「10分」を全環境の固定SLOにしない |
| Continuous Integration | 小さな変更を頻繁にshared mainへ統合し、速い検証とbroken build修復を続けているかを見る |
| Test-First Programming | 実装より先に期待するbehaviorをtestで表し、失敗→最小実装→整理のfeedbackを使っているかを見る |
| Incremental Design | 現在の要求に必要なdesignを継続的に改善し、将来予測だけで大きなarchitectureを先取りしていないかを見る |

Primaryという分類だけで「すべて今すぐ導入する必須項目」とは扱わない。

現在のproblemに関係するPracticeを選び、既存の働き方、team size、remote / solo環境、権限・制約へ比例させる。

### Corollary Practices

第2版のCorollary Practicesは11個。[^xp-second-edition]

Corollary PracticeはPrimary Practiceの土台なしに名前だけ導入すると危険になり得るため、現在のCapability・制約・目的を確認して選ぶ。[^xp-second-edition-corollary-practices]

| Corollary Practice | 診断上の意味・観測例 |
| --- | --- |
| Real Customer Involvement | systemの影響を実際に受けるcustomer / userから継続的にfeedbackを得られるかを見る。代理人だけで十分かはcontextで確認する |
| Incremental Deployment | 大きな一括移行ではなく、小さい利用可能なsliceへ分けて導入・学習・rollbackできるかを見る |
| Team Continuity | 有効に機能しているteamの関係・domain knowledgeを不必要な再編で失っていないかを見る |
| Shrinking Teams | capability向上で必要workが減ったとき、余力を新しい価値へ移せるかを見る。人員削減をLean / XPの目的として強制しない |
| Root-Cause Analysis | defectやincidentを個人責任で終わらせず、再発へ寄与したsystem / process条件を調べ改善へつなげる |
| Shared Code | teamがcodebase全体を改善できるcollective ownershipと安全策があるかを見る。無責任な自由編集とは区別する |
| Code and Tests | executable behaviorの主要な変更契約としてcodeとautomated testsを一緒に維持できるかを見る。必要な外部文書まで不要とはしない |
| Single Code Base | 同じproductのsource of truthが不要に分岐・複製されず、variantやbranchの意図が管理されているかを見る |
| Daily Deployment | safety foundationがある場合にproduction feedbackを短くできるかを見る。活動がない日までdeploy回数を稼ぐ固定quotaにしない |
| Negotiated Scope Contract | 長期固定scopeだけでなく、短い契約・scope再交渉でcost / value / learningを反映できるかを見る。法務・調達制約を無視しない |
| Pay-Per-Use | 実利用と経済的feedbackを近づけるpricing / business modelが有効かを見る。適合しないproductへ課金方式を強制しない |

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
[^xp-second-edition-principles]: [Chapter 5. Principles — Extreme Programming Explained, 2nd Edition](https://www.oreilly.com/library/view/extreme-programming-explained/0321278658/ch05.xhtml)。PrincipleがValuesと具体的behaviorをつなぐ章構成とnamed principlesを確認し、本リポジトリの診断意味へ要約した。2026-09-27確認。
[^xp-second-edition-primary-practices]: [Chapter 7. Primary Practices — Extreme Programming Explained, 2nd Edition](https://www.oreilly.com/library/view/extreme-programming-explained/0321278658/ch07.xhtml)。Primary Practicesは環境の最大の改善機会に応じて選び安全に始められるpracticeとして説明される。本リポジトリでは固定形式ではなく診断目的へ要約した。2026-09-27確認。
[^xp-second-edition-corollary-practices]: [Chapter 9. Corollary Practices — Extreme Programming Explained, 2nd Edition](https://www.oreilly.com/library/view/extreme-programming-explained/0321278658/ch09.xhtml)。Corollary PracticesはPrimary Practicesの土台なしに導入すると難しい・危険になり得るという注意を含む。本リポジトリでは適用条件と観測例へ要約した。2026-09-27確認。
