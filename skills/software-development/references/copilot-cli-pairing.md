---
type: Reference
title: Copilot CLIでNavigatorを継続利用する
description: 共通の協働契約をCopilot CLIで実現する起動・後続連絡の方法を示します。
sources:
  - id: github-copilot-cli-changelog
    resource: https://github.com/github/copilot-cli/blob/v1.0.88/changelog.md#L1710
  - id: issue-87
    resource: https://github.com/daiksud/agents/issues/87
  - id: issue-99
    resource: https://github.com/daiksud/agents/issues/99
  - id: issue-100
    resource: https://github.com/daiksud/agents/issues/100
  - id: issue-161
    resource: https://github.com/daiksud/agents/issues/161
---

## Copilot CLIでNavigatorを継続利用する

Driver / Navigatorの役割、編集権限、共有ToDo、段階確認、初回起動できない場合の停止と起動済みNavigator継続不能後の自動再ペアは共通の協働指示に従う。この資料はCopilot CLI固有の実現方法を扱う。

内部通信の詳細は最初のNavigator依頼より前に[DriverとNavigatorの内部通信](agent-communication.md)を読み、共通の協働契約に従って使う。Copilot CLIでは初回共有を `task` に、同じNavigatorへの後続メッセージを同じ `agent_id` の `write_agent` に載せる。この資料で通信形式や停止条件を再定義しない。[^issue-99]

GitHub Copilot CLIで後続の連絡が必要なNavigatorは、最初の `task` を `mode: "background"` で起動する。`mode: "sync"` は一度の応答で完了する依頼に限り、応答後に `idle` と表示されても `write_agent` の送信先にできるとは判断しない。[^github-copilot-cli-changelog]

返された `agent_id` を保持し、後続の確認・フィードバックを同じIDへ `write_agent` で送る。依頼が同じNavigatorに処理され、そのNavigatorから応答が返ることを確認する。起動や状態表示だけを継続性の証拠にせず、再開不能・履歴喪失等は共通の停止条件に従う。[^issue-87]

元の `agent_id` に連絡できなくなったら共通指示に従って確認が必要な後続コード変更を一時停止し、復旧・再ペア手順の前に[Navigator喪失後の引き継ぎと再確認](navigator-recovery.md)を読む。継続可能性は応答・利用可能なエージェント一覧・履歴から調べる。継続不能を確認したらユーザーの追加確認を待たず、旧IDへの新たな `write_agent` をやめて担当から外した記録を残す。新しい `task` を `mode: "background"` で起動し、別の `agent_id` へ取得・保持できる限りの作業コンテキストと証拠を渡す。後続の `write_agent` に同じ新IDから応答があることを確かめ、復旧資料の再確認を終えてから再開する。単なる起動成功や `idle` 表示を証拠にしない。旧IDへの切り戻し禁止や新ID喪失時の自動再ペアは共通指示に従う。[^issue-100] [^issue-161]

### CLIでの確認例

- 前提: 同じNavigatorに初回応答後も複数回確認を依頼するコード変更である。[^issue-87] [^github-copilot-cli-changelog]
- もし: DriverがGitHub Copilot CLIの `task` でNavigatorを起動する
- ならば: Driverは `mode: "background"` で起動する
- かつ: 初回応答後の `write_agent` が同じ `agent_id` に処理され、そのNavigatorから応答が返る
- かつ: `mode: "sync"` の応答や `list_agents` の `idle` 表示だけから継続連絡できると判断しない

[^issue-99]: [Issue #99](https://github.com/daiksud/agents/issues/99) の環境非依存な内部通信プロトコルとruntime固有transportの分離。
[^github-copilot-cli-changelog]: [Copilot CLI changelog v1.0.88](https://github.com/github/copilot-cli/blob/v1.0.88/changelog.md#L1710)。`sync` taskは再利用可能な `agent_id` を返さず、後続連絡には `mode: "background"` を使うと記載している。
[^issue-87]: [Issue #87](https://github.com/daiksud/agents/issues/87) の継続連絡と実際の応答確認。
[^issue-100]: [Issue #100](https://github.com/daiksud/agents/issues/100) の証拠保持・旧担当退役・再確認の境界。
[^issue-161]: [Issue #161](https://github.com/daiksud/agents/issues/161) のユーザー確認不要の自動再ペアとコンテキスト引き継ぎ。
