---
type: Specification
title: エージェントペアによるコード変更
description: DriverとNavigatorによる共有ToDo、TDD各段階の確認、起動・フィードバックの停止条件を評価するシナリオを定めます。
sources:
  - id: issue-76
    resource: https://github.com/daiksud/agents/issues/76
  - id: issue-80
    resource: https://github.com/daiksud/agents/issues/80
  - id: issue-87
    resource: https://github.com/daiksud/agents/issues/87
  - id: github-copilot-cli-changelog
    resource: https://github.com/github/copilot-cli/blob/v1.0.88/changelog.md#L1710
---

## 機能: 独立したNavigatorとコード変更を進める

開発者は、対応環境で実装前から方針・テスト・小さな変更を確認し、独立したNavigatorと共有ToDoおよびTDD各段階の短いフィードバックサイクルで進めたい。[^issue-76] [^issue-80]

### 評価用の代表的な依頼

> この依頼は評価用の使い捨てコードfixtureで実行し、製品リポジトリは変更しないでください。設定トークンのlistまたはtupleを受け取り、各文字列の最初の出現順を保った新しいlistを返す関数を実装してください。入力は変更せず、空文字列も有効なトークンです。generatorと文字列以外の入力は対象外です。

### 手動評価の実行方法

- 対応環境では、この依頼を使い捨てコードfixtureに対するDriverの実装タスクとして与え、製品リポジトリを変更しない。Driverはコードを編集する前に、独立コンテキストで継続的に連絡できるNavigatorを1体起動し、同じNavigatorを全サイクルで利用する。
- DriverとNavigatorは、未着手・進行中・完了・要確認を区別する共有ToDoに、選んだ項目と双方が見つけたケース・改善を記録する。各項目でRed、Green、Refactorの順に、実差分、テスト結果、Navigatorの確認を同じコード状態に結びつける。記録から共同選択、実装前の助言、欠けたテストの指摘、読み取り専用、Driverだけの編集、最終確認を照合する。
- GitHub Copilot CLIで評価する場合、複数回の確認が必要なNavigatorは `mode: "background"` で起動し、初回応答後も同じ `agent_id` への `write_agent` が処理されることを確認する。`mode: "sync"` と `idle` 表示だけから後続連絡が可能だと判断しない。
- 起動機能がない環境または実際の起動失敗を確認できる環境では同じ依頼を用い、Driverがペア未実施の制約を報告し、役割演技や独立確認済みの主張をしないことを確認する。安全にその状態を用意できない場合は再現したと扱わず、未確認として記録する。

### ルール: 同じNavigatorを実装前から最終確認まで使う

#### シナリオ: 対応環境で一つの振る舞いを変更する

- 前提: コード変更を依頼され、独立したサブエージェントを起動して継続的に連絡できる
- もし: Driverが実装を始める
- ならば: Driverは元の要件、受け入れ条件、作業範囲、適用指示、関連コードを一体のNavigatorに共有する
- かつ: Navigatorは実装前に次の振る舞い、対応テスト、境界条件を確認する
- かつ: Driverだけがファイルを編集し、Navigatorは実際の要件・コード・差分・テスト結果を読み取り専用で確認する
- かつ: 両者は共有ToDoから理由とともに一項目を選び、同じNavigatorが各段階と最終差分にフィードバックする

#### シナリオ: Copilot CLIで継続確認をするNavigatorを起動する

- 前提: 同じNavigatorに初回応答後も複数回確認を依頼するコード変更である。[^issue-87] [^github-copilot-cli-changelog]
- もし: DriverがGitHub Copilot CLIの `task` でNavigatorを起動する
- ならば: Driverは `mode: "background"` で起動する
- かつ: 初回応答後の `write_agent` が同じ `agent_id` に処理され、そのNavigatorから応答が返る
- かつ: `mode: "sync"` の応答や `list_agents` の `idle` 表示だけから継続連絡できると判断しない

### ルール: 共有ToDoを共同で育て、一度に一項目を進める

#### シナリオ: Driverが次の境界条件に気づく

- 前提: 一つのToDoが進行中であり、別の境界条件が必要だとDriverが気づく
- もし: その境界条件が現在の段階を成立させるためには不要である
- ならば: Driverは何を確認する項目か分かる形で共有ToDoへ追加する
- かつ: DriverとNavigatorは現在の項目を無条件に広げず、完了後に次の項目として選ぶか相談する

#### シナリオ: Navigatorがテスト不足を見つける

- 前提: 次の振る舞いを確認するテストに境界条件が欠けている
- もし: Navigatorが要件と実際のテストを確認する
- ならば: Navigatorは欠けている条件と理由を示し、Driverは共有ToDoへ反映する
- かつ: Navigatorは反映と、未合意の要件があれば要確認として区別されたことを確認する

#### シナリオ: 現在の回帰はToDoへ移すだけで先送りしない

- 前提: Red、Green、またはRefactorの確認で既存の振るまいへの回帰が見つかる
- もし: DriverとNavigatorが共有ToDoへ記録する
- ならば: 現在の段階を成立させる修正と検証を先送りせずに行う
- かつ: Driverはテストを通すために受け入れ条件や期待値を弱めない

### ルール: 各TDD段階を同じNavigatorが確認してから次へ進める

#### シナリオ: 意図したRedを確認する

- 前提: 両者が共有ToDoから一つの小さな振る舞いを選んでいる
- もし: Driverがアサーションから最小限のテストを書き、対象の振るまいが未充足のために失敗する
- ならば: Navigatorは要件、テスト差分、失敗理由を照合する
- かつ: Navigatorが要対応指摘を再確認して解消するまでDriverはGreenを実装しない

#### シナリオ: Greenの一時的な重複をRefactorへ引き継ぐ

- 前提: Redの確認後に、Driverの最小実装が新規・関連テストを成功させ、一時的な重複が残っている
- もし: NavigatorがGreenの差分と結果を確認する
- ならば: Navigatorは要件との一致と回帰がないことを確認する
- かつ: DriverとNavigatorは重複の改善を同じサイクルのRefactorとして共有ToDoへ追跡する
- かつ: Navigatorの確認前に別のToDoや未要求の一般化を先行させない

#### シナリオ: Refactorが不要と判断する

- 前提: Greenの確認後に引き継いだ改善事項がなく、振るまい不変の整理も必要ない
- もし: DriverとNavigatorがRefactorの必要性を確認する
- ならば: Driverは形式のための変更や人工的なRedを作らない
- かつ: Navigatorは改善不要の判断とGreen維持を確認してToDoを完了にする

#### シナリオ: 確認後に差分を変える

- 前提: Navigatorがある段階の差分とテスト結果を確認済みである
- もし: Driverが未コミット変更を含む確認対象を変更する
- ならば: Driverは影響するテストとNavigatorの確認をやり直す
- かつ: 同じHEADのSHAだけで過去の差分確認を変更後の根拠にしない

#### シナリオ: Navigatorに共通指示が適用されても再帰的なペアを作らない

- 前提: Navigatorの実行コンテキストにも共通の作業原則が適用される
- もし: Navigatorが対象コードを読み取り専用で確認する
- ならば: 新しいサブエージェントを起動せず、再委譲もしない
- かつ: ペア作業に参加するエージェントはDriverとNavigatorの2体のままである

### ルール: 独立したNavigatorを起動できない場合は、ペア作業の未実施を報告する

#### シナリオ: 対応環境にサブエージェント起動機能がない

- 前提: コード変更の依頼はあるが、独立したサブエージェントを起動する機能がない
- もし: Driverが適用可能な協働方法を確認する
- ならば: ペア作業と独立した確認を実施していないことをユーザーに報告する
- かつ: 一つのエージェントによるDriver/Navigatorの役割演技を独立確認として扱わない

#### シナリオ: Navigatorの起動に失敗する

- 前提: 独立したサブエージェントを起動できる環境だが、起動要求が失敗する
- もし: Driverが結果を確認する
- ならば: ペア作業や独立確認を実施済みと扱わず、失敗と制約を報告する

#### シナリオ: 同じNavigatorを継続できなくなる

- 前提: 同じNavigatorとの連絡が途中で再開不能になり、必要な履歴も失われた
- もし: Driverが継続可能性を確認する
- ならば: Driverは確認済み範囲と未確認範囲を報告する
- かつ: 確認を必要とする後続のコード変更を止め、新しいNavigatorを継続扱いにしない

### ルール: 解消しない指摘では作業を止める

#### シナリオ: 同じ指摘が二往復後も残る

- 前提: Navigatorの同じ指摘について修正と再確認を二往復しても合意できない
- もし: さらに同じ内容を修正・再確認しようとする
- ならば: 作業を止め、未解決点、根拠、選択肢をユーザーに報告する
- かつ: 未解決のまま完了や承認済みとしない

### ルール: ペア内の確認は通常のレビューを代替しない

#### シナリオ: ペア内で最終差分を確認する

- 前提: Navigatorが最終差分を読み取り専用で確認している
- もし: ペア内確認が終わる
- ならば: PRレビュー、必須CI、承認、マージ条件を別に満たす

[^issue-76]: [Issue #76](https://github.com/daiksud/agents/issues/76) に記録された目的、受け入れ条件、検証計画。
[^issue-80]: [Issue #80](https://github.com/daiksud/agents/issues/80) に記録された共有ToDoと段階別レビューの受け入れ条件、検証計画。
[^issue-87]: [Issue #87](https://github.com/daiksud/agents/issues/87) に記録されたCopilot CLIの `sync` taskを初回応答後の継続先にできない問題。
[^github-copilot-cli-changelog]: [Copilot CLI changelog v1.0.88](https://github.com/github/copilot-cli/blob/v1.0.88/changelog.md#L1710)。`sync` taskは再利用可能な `agent_id` を返さず、後続連絡には `mode: "background"` を使うと記載している。
