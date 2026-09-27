---
type: Reference
title: XP Principlesを補助lensとして診断する
description: XP第2版のnamed Principlesを個別の補助lensとして使うための診断意味を示します。
sources:
  - id: xp-second-edition-principles
    resource: https://www.oreilly.com/library/view/extreme-programming-explained/0321278658/ch05.xhtml
---

## XP Principles

個別のPrincipleを他のengineering lensへ補助的に適用するときに読む。XP全taxonomyを読む必要はない。

本リポジトリで採用する14 named Principlesの診断意味は次のとおり。原文の置換ではなく、現在のproblemと観測証拠へ結びつけるための適用パラフレーズである。

| Principle | 診断上の意味・観測例 |
| --- | --- |
| Humanity | 人が継続して良い仕事をできるneeds・関係・安全性を尊重する。疲弊、孤立、責任と権限の不一致を確認する |
| Economics | time・cost・value・opportunity costを含む経済的結果から優先順位とscopeを判断し、技術的好みだけで投資を増やさない |
| Mutual Benefit | 今日の成果と将来の変更容易性など、関係者の利益を同時に増やす選択を探し、一方の犠牲を常態化しない |
| Self-Similarity | 別scaleで機能したfeedback・分割・検証のpatternを類似問題へ仮説として適用し、同じ結果になるか確認する |
| Improvement | 完璧な最終状態を待たず、現在状態から測定可能な小さい改善を続ける |
| Diversity | 異なる経験・専門性・観点を早く衝突させ、見落としを減らす。形式的な全員一致を目的にしない |
| Reflection | 結果と進め方を振り返り、何が起きたか・なぜか・次に変えることをfeedbackへ戻す |
| Flow | 価値あるworkを小さく連続して進め、queue・handoff・WIP・batchによる滞留を減らす |
| Opportunity | problem・変更・制約を単なる障害ではなく、systemを改善する学習機会として扱う |
| Redundancy | 重大な失敗を一つの防御だけに依存せず、test・review・monitoring等の相補的な安全策を必要性に応じて持つ。無目的な重複とは区別する |
| Failure | 安全に小さく試せる範囲では失敗から学び、失敗を隠さず再現・原因・次の実験へfeedbackする |
| Quality | speedのためにqualityを恒常的に下げる前提を置かず、scope・方法・順序を調整して持続可能なqualityを守る |
| Baby Steps | reversibleで検証可能な最小のstepへ分割し、各stepのfeedbackから次を決める |
| Accepted Responsibility | 実行責任を引き受ける人・teamが判断に必要な権限と情報を持つようにし、責任だけを一方的に割り当てない |

Principleの採用数を成熟度やscoreにしない。現在のproblemに関係するPrincipleだけを選ぶ。

[^xp-second-edition-principles]: [Chapter 5. Principles — Extreme Programming Explained, 2nd Edition](https://www.oreilly.com/library/view/extreme-programming-explained/0321278658/ch05.xhtml)。PrinciplesをValuesと具体的behaviorの橋渡しとして扱う章構成の参照。2026-09-27確認。
