---
type: Guide
title: エージェントペアの手動評価
description: 使い捨てfixtureで共有ToDoと段階確認、継続性を評価する手順。
sources:
  - id: issue-76
    resource: https://github.com/daiksud/agents/issues/76
  - id: issue-80
    resource: https://github.com/daiksud/agents/issues/80
  - id: issue-98
    resource: https://github.com/daiksud/agents/issues/98
  - id: issue-99
    resource: https://github.com/daiksud/agents/issues/99
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
- #98 の短い対話サイクルでは、少なくとも `共同選択 → 小さな編集 → 関連検証 → 同じNavigatorの実物確認 → 必要な修正と再確認 → 次の独立した編集` の時系列を記録する。段階末だけの一括報告ではなく、次の判断を変える差分・想定外結果・指摘修正の時点で確認が入ったことを照合する。[^issue-98]
- #99 の内部通信では、初回に元の依頼・受け入れ条件・範囲・適用指示・制約・関連コード・初期共有ToDoが判断可能な範囲で共有されたことを記録する。後続のRed / Green / Refactorでは、stable IDと明確な `STATUS` を使い、必要な固定フィールドと前回からの差分だけを中心に送って、共有済みの長い前提を繰り返していないことを確認する。コード・識別子・コマンド・ログ等の原文保持、人間向け成果物をControlled Englishへ強制しない境界、履歴・必要コンテキスト喪失時にdelta-onlyを中止して再共有または停止することも照合する。可能ならturn数・token数・wait timeと合わせて通信量の変化を記録するが、少数回の実測から効率や品質を一般化しない。[^issue-99]
- 大きすぎるToDoの評価では、独立した2つの振る舞いと別々のRedを含むfixtureを用意し、複数のRed / Greenをそのまま進めず、`分割 → 共有ToDo更新 → 理由を共有 → 一項目を再選択` したことを確認する。
- 対照評価では、読み取り・検索・設定確認・局所テストなど一つの判断材料を集める連続操作を使い、ツール呼び出しごとの不要なNavigator往復を要求していないことを確認する。
- 品質側は、過大なToDoの分割、回帰・認識違い・方針変更の早期検知、Navigatorの実差分・検証結果確認、不要な逐次確認の有無を記録する。コスト側は可能ならDriver / Navigator間のturn数、token数、wait timeを記録する。少数回の実測から品質向上・高速化・token削減を一般化しない。
- Copilot CLIで評価する場合は [runtime固有手順](../references/copilot-cli-pairing.md) を使い、同じNavigatorへ後続依頼が処理され応答が返った証拠を確認する。
- 起動機能がない環境または実際の起動失敗を確認できる環境では同じ依頼を用い、Driverがペア未実施の制約を報告し、役割演技や独立確認済みの主張をしないことを確認する。安全にその状態を用意できない場合は再現したと扱わず、未確認として記録する。
- 回復の評価では使い捨てfixtureでRedの差分・失敗結果を残したままNavigatorが再開不能になる場合を扱う。Driverがコード変更を停止して確認済み／未確認、HEADと差分、未解決指摘を報告し、今回の喪失への停止報告後の明示承認なしにはGreenへ進まないことを確認する。承認後は元Navigatorを担当から外し、遅れた応答を段階の確認済み証拠にせず、別のNavigatorに初期コンテキストを渡す。未確認Redの実差分・失敗結果と過去の完了項目の最終差分を確認してからGreenへ進む。旧指摘と2往復上限を保持し、再喪失時は前回の承認を使わず再び停止・報告する。実際に再開不能な環境を安全に用意できなければ、読み取り専用の模擬判断と実機での確認を区別する。[^issue-100]

[^issue-76]: [Issue #76](https://github.com/daiksud/agents/issues/76) の独立したペア作業の検証計画。
[^issue-80]: [Issue #80](https://github.com/daiksud/agents/issues/80) の共有ToDoと段階確認の検証計画。
[^issue-98]: [Issue #98](https://github.com/daiksud/agents/issues/98) のToDo粒度、段階内部の早期feedback、不要な逐次報告を避ける評価条件。
[^issue-99]: [Issue #99](https://github.com/daiksud/agents/issues/99) のControlled English、固定フィールド、stable ID、delta-onlyと境界条件の評価。
[^issue-100]: [Issue #100](https://github.com/daiksud/agents/issues/100) の承認付き再ペアを検査する代表条件。
