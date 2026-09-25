---
type: Reference
title: Copilot CLIでNavigatorを継続利用する
description: 共通の協働契約をCopilot CLIで実現する起動・後続連絡の方法を示します。
sources:
  - id: github-copilot-cli-changelog
    resource: https://github.com/github/copilot-cli/blob/v1.0.88/changelog.md#L1710
  - id: issue-87
    resource: https://github.com/daiksud/agents/issues/87
---

## Copilot CLIでNavigatorを継続利用する

Driver / Navigatorの役割、編集権限、共有ToDo、段階確認、起動できない場合と継続不能になった場合の停止・報告は共通の協働指示に従う。この資料はCopilot CLI固有の実現方法を扱う。

GitHub Copilot CLIで後続の連絡が必要なNavigatorは、最初の `task` を `mode: "background"` で起動する。`mode: "sync"` は一度の応答で完了する依頼に限り、応答後に `idle` と表示されても `write_agent` の送信先にできるとは判断しない。[^github-copilot-cli-changelog]

返された `agent_id` を保持し、後続の確認・フィードバックを同じIDへ `write_agent` で送る。依頼が同じNavigatorに処理され、そのNavigatorから応答が返ることを確認する。起動や状態表示だけを継続性の証拠にせず、再開不能・履歴喪失等は共通の停止条件に従う。[^issue-87]

### CLIでの確認例

- 前提: 同じNavigatorに初回応答後も複数回確認を依頼するコード変更である。[^issue-87] [^github-copilot-cli-changelog]
- もし: DriverがGitHub Copilot CLIの `task` でNavigatorを起動する
- ならば: Driverは `mode: "background"` で起動する
- かつ: 初回応答後の `write_agent` が同じ `agent_id` に処理され、そのNavigatorから応答が返る
- かつ: `mode: "sync"` の応答や `list_agents` の `idle` 表示だけから継続連絡できると判断しない

[^github-copilot-cli-changelog]: [Copilot CLI changelog v1.0.88](https://github.com/github/copilot-cli/blob/v1.0.88/changelog.md#L1710)。`sync` taskは再利用可能な `agent_id` を返さず、後続連絡には `mode: "background"` を使うと記載している。
[^issue-87]: [Issue #87](https://github.com/daiksud/agents/issues/87) の継続連絡と実際の応答確認。
