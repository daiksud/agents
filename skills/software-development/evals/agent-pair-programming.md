---
type: Guide
title: エージェントペアの手動評価
description: 使い捨てfixtureで共有ToDoと段階確認、継続性を評価する手順。
sources:
  - id: issue-76
    resource: https://github.com/daiksud/agents/issues/76
  - id: issue-80
    resource: https://github.com/daiksud/agents/issues/80
  - id: issue-100
    resource: https://github.com/daiksud/agents/issues/100
---

## エージェントペアの手動評価

この評価はペア協働の受け入れ条件を観測するための手順です。実機で確認した結果と読み取り専用の模擬判断を区別します。[^issue-76] [^issue-80]

### 評価用の代表的な依頼

> この依頼は評価用の使い捨てコードfixtureで実行し、製品リポジトリは変更しないでください。設定トークンのlistまたはtupleを受け取り、各文字列の最初の出現順を保った新しいlistを返す関数を実装してください。入力は変更せず、空文字列も有効なトークンです。generatorと文字列以外の入力は対象外です。

### 手動評価の実行方法

- 対応環境では、この依頼を使い捨てコードfixtureに対するDriverの実装タスクとして与え、製品リポジトリを変更しない。Driverはコードを編集する前に、独立コンテキストで継続的に連絡できるNavigatorを1体起動し、同じNavigatorを全サイクルで利用する。
- DriverとNavigatorは、未着手・進行中・完了・要確認を区別する共有ToDoに、選んだ項目と双方が見つけたケース・改善を記録する。各項目でRed、Green、Refactorの順に、実差分、テスト結果、Navigatorの確認を同じコード状態に結びつける。記録から共同選択、実装前の助言、欠けたテストの指摘、読み取り専用、Driverだけの編集、最終確認を照合する。
- Copilot CLIで評価する場合は [runtime固有手順](../references/copilot-cli-pairing.md) を使い、同じNavigatorへ後続依頼が処理され応答が返った証拠を確認する。
- 起動機能がない環境または実際の起動失敗を確認できる環境では同じ依頼を用い、Driverがペア未実施の制約を報告し、役割演技や独立確認済みの主張をしないことを確認する。安全にその状態を用意できない場合は再現したと扱わず、未確認として記録する。
- 回復の評価では使い捨てfixtureでRedの差分・失敗結果を残したままNavigatorが再開不能になる場合を扱う。Driverがコード変更を停止して確認済み／未確認、HEADと差分、未解決指摘を報告し、明示的な再ペアの承認なしにはGreenへ進まないことを確認する。承認後は別のNavigatorに初期コンテキストを渡し、未確認Redの実差分・失敗結果と過去の完了項目の最終差分を確認してからGreenへ進む。旧指摘と2往復上限を保持し、再喪失時は再び停止する。実際に再開不能な環境を安全に用意できなければ、読み取り専用の模擬判断と実機での確認を区別する。[^issue-100]

[^issue-76]: [Issue #76](https://github.com/daiksud/agents/issues/76) の独立したペア作業の検証計画。
[^issue-80]: [Issue #80](https://github.com/daiksud/agents/issues/80) の共有ToDoと段階確認の検証計画。
[^issue-100]: [Issue #100](https://github.com/daiksud/agents/issues/100) の承認付き再ペアを検査する代表条件。
