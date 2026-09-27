---
type: Reference
title: XP Practicesを補助lensとして診断する
description: XP第2版のPrimary / Corollary Practicesを個別の補助lensとして使うための診断意味を示します。
sources:
  - id: xp-second-edition-primary-practices
    resource: https://www.oreilly.com/library/view/extreme-programming-explained/0321278658/ch07.xhtml
  - id: xp-second-edition-corollary-practices
    resource: https://www.oreilly.com/library/view/extreme-programming-explained/0321278658/ch09.xhtml
---

## Primary Practices

個別のPracticeを他のengineering lensへ補助的に適用するときに読む。Practiceの数を成熟度や必須導入数にしない。

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

## Corollary Practices

Corollary PracticeはPrimary Practiceの土台なしに名前だけ導入すると難しい・危険になり得るため、現在のCapability・制約・目的を確認して選ぶ。

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

[^xp-second-edition-primary-practices]: [Chapter 7. Primary Practices — Extreme Programming Explained, 2nd Edition](https://www.oreilly.com/library/view/extreme-programming-explained/0321278658/ch07.xhtml)。Primary Practicesを環境と最大の改善機会に応じて選ぶ位置づけの参照。2026-09-27確認。
[^xp-second-edition-corollary-practices]: [Chapter 9. Corollary Practices — Extreme Programming Explained, 2nd Edition](https://www.oreilly.com/library/view/extreme-programming-explained/0321278658/ch09.xhtml)。Corollary PracticesをPrimaryの土台と適用条件の上で使う注意の参照。2026-09-27確認。
