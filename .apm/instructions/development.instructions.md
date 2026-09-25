---
type: Instruction
title: 開発とフィードバック
description: XPの価値、現在の要求に合う設計、受け入れ条件とテスト先行の反復を定めます。
sources:
  - id: ron-jeffries-xp
    resource: https://ronjeffries.com/xprog/what-is-extreme-programming/
  - id: fowler-yagni
    resource: https://martinfowler.com/bliki/Yagni.html
---

## 開発とフィードバック

Extreme Programming（XP）を日常の開発判断の軸とし、5つの価値を次の行動へ結びつける。[^ron-jeffries-xp]

| 価値 | 判断と行動 |
| --- | --- |
| Communication | 目的・ルール・具体例・未回答事項を共有し、異なる理解を実装前に確かめる |
| Simplicity | 現在確認されている要求と契約を満たす、理解しやすい最小の設計を選ぶ |
| Feedback | Small Stepsでテスト・協働・統合・利用者の反応を早く確かめ、次の小さな変更へ反映する |
| Courage | 欠陥や不確実性を隠さず、テストと既存の承認範囲を根拠に必要な設計改善を行う |
| Respect | 利用者の判断権限、関係者の知識・時間と持続可能な働き方を尊重する |

Simple Design・YAGNIに従い、仮想的な将来変更のために機能や抽象化を追加しない。実際のフィードバックからIncremental DesignとRefactoringを進める。必要なテスト、契約、設計改善、レビュー、CI、承認・公開許可を省く理由にしない。[^fowler-yagni]

### 共有理解と検証

関係者の異なる観点からルール・具体例・未回答の質問を整理し、対応する実装より先に受け入れ条件を定める。ドメインのルール変更ではfeature文書を先に保存する。

コード変更はテストファーストとし、実装後にこう動くという期待を、対応する実装コードより先にテストで表現する。テストを書くときはアサートファーストとし、最後にパスすべきアサーションから書き始める。

TDDでは、テスト項目を含むToDoリストから一つずつ失敗・最小の成功・整理を反復する。技術処理、既存仕様、十分な既存テストを使うふるまい不変の整理の扱いは `software-development` に従う。文書・テストの存在だけを協働やテスト先行の証拠にしない。

[^ron-jeffries-xp]: [Ron Jeffries: What is Extreme Programming?](https://ronjeffries.com/xprog/what-is-extreme-programming/)。5価値、現在の要求に合う設計、短い検証・設計改善を採用する。固定の会議・期間・組織編成や効果数値は共通要件にしない。2026-09-25に確認。
[^fowler-yagni]: [Martin Fowler: Yagni](https://martinfowler.com/bliki/Yagni.html)。将来機能の先取りを避けつつ、現在の変更を支えるテスト・リファクタリング・CIは維持する。アサートファーストとエージェントの段階確認は本環境の運用方針。2026-09-25に確認。
