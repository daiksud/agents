---
type: Reference
title: XP個別項目を補助lensとして使う
description: Architecture・DORA・Lean等の診断で、個別のXP Value / Principle / Practiceだけを補助的に使うための軽量lookupです。
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

## XP個別項目を補助lensとして使う

XPそのものを診断するのではなく、別のlensで一つまたは少数のXP項目だけを補助判断に使う場合に読む。taxonomyの分類はXP第2版を基準にする。[^xp-second-edition]

XP全体のtaxonomy・複数項目の相互関係・XP導入そのものを診断する場合は[XP full lens](xp.md)を使う。このreferenceを「XP全項目の必須チェックリスト」にはしない。

### Values

5 Valuesの意味はXPの公開説明とも照合する。[^ron-jeffries-xp]

| Value | Compact diagnostic cue |
| --- | --- |
| Communication | 目的・制約・具体例・未回答事項の共有と早い認識合わせ |
| Simplicity | 現在要求を満たす最小の理解しやすい設計。将来予測だけの複雑化を避ける |
| Feedback | test・統合・利用者・運用から短い間隔で結果を得て次へ反映する |
| Courage | 欠陥・不確実性・不要な設計を隠さず、証拠から必要な変更へ進む |
| Respect | 利用者の判断権限、関係者の知識・時間、持続可能な働き方を尊重する |

### Principles

Principlesの位置づけは第2版のPrinciples章を参照する。[^xp-second-edition-principles]

| Principle | Compact diagnostic cue |
| --- | --- |
| Humanity | 人が継続して良い仕事をできるneeds・関係・安全性 |
| Economics | time・cost・value・opportunity costを含む経済的判断 |
| Mutual Benefit | 今日と将来、複数関係者の利益を同時に増やす選択 |
| Self-Similarity | 別scaleで機能したfeedback patternを仮説として再利用し検証する |
| Improvement | 完璧を待たず現在状態から小さく改善する |
| Diversity | 異なる経験・専門性・観点を早く意思決定へ入れる |
| Reflection | 結果と進め方を振り返り、次の行動へfeedbackする |
| Flow | queue・handoff・WIP・batchによる滞留を減らし価値を流す |
| Opportunity | problem・変更・制約をsystem改善の学習機会として扱う |
| Redundancy | 重大な失敗を一つの防御に依存せず、相補的な安全策を必要に応じて持つ |
| Failure | 安全に小さく試し、失敗を隠さず次の学習へつなげる |
| Quality | speedのためにqualityを恒常的に下げず、scope・方法・順序を調整する |
| Baby Steps | reversibleで検証可能な最小stepへ分割する |
| Accepted Responsibility | 責任を引き受ける人・teamへ必要な権限と情報を対応させる |

### Primary Practices

Primary Practicesの位置づけは第2版のPrimary Practices章を参照する。[^xp-second-edition-primary-practices]

| Primary Practice | Compact diagnostic cue |
| --- | --- |
| Sit Together | 必要な人が低いcommunication costで継続的に協働できる状態 |
| Whole Team | 価値を届けるために必要な視点へアクセスし、handoffだけに責任を分断しない |
| Informative Workspace | 進捗・quality・risk等を必要な人が容易に把握できる |
| Energized Work | qualityと判断を維持できる持続可能な働き方 |
| Pair Programming | 実装中に複数視点で連続的なdesign・review・knowledge sharingを行う |
| Stories | 利用者価値の単位でscope・cost・期待を会話し、小さく優先順位を変える |
| Weekly Cycle | 近い期間のplan・delivery・feedbackを短いcadenceで見直す |
| Quarterly Cycle | 大きなtheme・investment・directionを定期的に見直す |
| Slack | uncertainty・改善・予期せぬworkを吸収する余地を持つ |
| Ten-Minute Build | build / test feedbackを頻繁に回せる十分な速さを保つ |
| Continuous Integration | 小さな変更を頻繁にshared mainへ統合し、失敗を早く修復する |
| Test-First Programming | 実装より先に期待behaviorをtestで表し、失敗→最小実装→整理を反復する |
| Incremental Design | 現在要求に必要なdesignを継続的に改善する |

### Corollary Practices

Corollary Practicesの適用注意は第2版のCorollary Practices章を参照する。Primary Practicesや必要なdelivery / feedback capabilityの土台がないまま名前だけ導入すると難しい・危険になり得るため、関連するfoundationと現在の制約を先に確認する。[^xp-second-edition-corollary-practices]

| Corollary Practice | Compact diagnostic cue |
| --- | --- |
| Real Customer Involvement | 実際に影響を受けるcustomer / userから継続的にfeedbackを得る |
| Incremental Deployment | 大きな一括移行を避け、小さいsliceで導入・学習・rollbackする |
| Team Continuity | 有効なteam関係・domain knowledgeを不必要な再編で失わない |
| Shrinking Teams | capability向上で生じた余力を新しい価値へ移す。人員削減を目的化しない |
| Root-Cause Analysis | defect / incidentを個人責任で終わらせずsystem / process条件を改善する |
| Shared Code | collective ownershipと安全策の下でcodebase全体を改善できる |
| Code and Tests | codeとautomated testsを主要なexecutable変更契約として一緒に維持する |
| Single Code Base | 同じproductのsource of truthを不要に分岐・複製しない |
| Daily Deployment | safety foundationの上でproduction feedbackを短くする。deploy回数をquota化しない |
| Negotiated Scope Contract | 短い契約・scope再交渉でcost / value / learningを反映する |
| Pay-Per-Use | 実利用と経済的feedbackを近づけるbusiness modelが有効か確認する |

個別項目が現在のproblemの主対象へ広がった場合は、ここで診断を続けず[XP full lens](xp.md)へ切り替える。

[^xp-second-edition]: [Extreme Programming Explained: Embrace Change, 2nd Edition — Kent Beck / Cynthia Andres](https://www.informit.com/store/extreme-programming-explained-embrace-change-9780134051987)。XP第2版のtaxonomy。2026-09-27確認。
[^ron-jeffries-xp]: [What is Extreme Programming? — Ron Jeffries](https://ronjeffries.com/xprog/what-is-extreme-programming/)。5 Valuesと小さいfeedbackの適用。2026-09-27確認。
[^xp-second-edition-principles]: [Chapter 5. Principles — Extreme Programming Explained, 2nd Edition](https://www.oreilly.com/library/view/extreme-programming-explained/0321278658/ch05.xhtml)。Principlesの位置づけ。2026-09-27確認。
[^xp-second-edition-primary-practices]: [Chapter 7. Primary Practices — Extreme Programming Explained, 2nd Edition](https://www.oreilly.com/library/view/extreme-programming-explained/0321278658/ch07.xhtml)。Primary Practicesの位置づけ。2026-09-27確認。
[^xp-second-edition-corollary-practices]: [Chapter 9. Corollary Practices — Extreme Programming Explained, 2nd Edition](https://www.oreilly.com/library/view/extreme-programming-explained/0321278658/ch09.xhtml)。Corollary Practicesの適用注意。2026-09-27確認。
