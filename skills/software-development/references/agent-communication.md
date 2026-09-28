---
type: Reference
title: DriverとNavigatorの内部通信
description: 共通の協働契約に従い、通信フィールド、状態語、IDと初回・後続メッセージを使い分けます。
sources:
  - id: issue-99
    resource: https://github.com/daiksud/agents/issues/99
  - id: issue-140
    resource: https://github.com/daiksud/agents/issues/140
---

## DriverとNavigatorの内部通信

Driverはコード変更で最初のNavigator依頼を送る前に読み、Navigatorには関連する協働契約とともに共有する。Navigatorが直接読めない場合は内容を初回依頼に含め、確認を得るまでコードを編集しない。相談・計画・文書だけの作業には要求しない。役割・編集権限・適用条件・停止と再ペアの判断は共通の協働指示を正本とし、この資料では変更しない。[^issue-140]

DriverとNavigatorの内部通信は、英語化そのものではなく、低エントロピーで誤解しにくく効率的な情報交換を目的とする。依頼・確認・フィードバックでは簡潔なControlled Englishを基本とし、一つの文に一つの意味を持たせ、固定した用語を優先し、不要な丁寧表現・会話的な埋め草・修辞的表現・曖昧な承認表現を避ける。コード、識別子、コマンド、ログ、エラーメッセージ、仕様本文など正確な原文保持が必要な情報は翻訳しない。この内部通信規則を、ユーザー向け回答、Issue、PR、文書、コミットメッセージなど人間が読む成果物の言語規則へ拡張しない。[^issue-99]

内部通信は自由会話より、必要な項目だけを含む軽量な半構造化形式を優先する。代表フィールドは `PHASE`、`TODO`、`STATUS`、`GOAL`、`CHANGES`、`EVIDENCE`、`FINDINGS`、`NEXT`、`REQUEST` とし、すべてを毎回埋めない。レビュー・確認結果の `STATUS` は原則 `APPROVED`、`CHANGES_REQUIRED`、`BLOCKED` を使い、指摘の分類が必要なら `REQUIREMENT`、`TEST`、`REGRESSION`、`DESIGN`、`SCOPE` など短い既知語彙を使う。外部プログラムによる厳密なparseが必要でない限りJSONを必須にせず、Markdownまたはplain textを使う。[^issue-99]

複数回の往復で参照する共有ToDo、finding、未解決事項には、同じタスクと同じNavigatorの継続セッション内で安定する短いIDを付ける。例としてToDoは `T-01`、findingは `F-01` のように表し、後続通信では説明を毎回再送せずIDで対象を参照する。永続的なグローバルID体系は要求しない。[^issue-99]

同じNavigatorとの初回連絡では、判断に必要な元の依頼、受け入れ条件、作業範囲、適用指示、制約、関連コード、初期の共有ToDoを共有する。継続が確認できた後続連絡では、共有済みで変わっていない長い前提を原則として再送せず、現在の `PHASE` と `TODO`、前回からの `CHANGES`、新しい `EVIDENCE`、追加・解消された `FINDINGS`、今回の `REQUEST` を中心に差分だけを送る。履歴喪失、再開不能、または判断に必要なコンテキスト不足が疑われる場合はdelta-onlyを続けず、正確性を優先して必要情報を再共有し、共通の協働指示の停止・再ペア条件を優先する。[^issue-99]

[^issue-140]: [Issue #140](https://github.com/daiksud/agents/issues/140) の、条件別の必読資料とNavigatorへの共有の境界。
[^issue-99]: [Issue #99](https://github.com/daiksud/agents/issues/99) に記録された、低エントロピーなControlled Englishによる内部通信と外部成果物との境界。
