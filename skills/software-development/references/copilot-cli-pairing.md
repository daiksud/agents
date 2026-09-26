---
type: Reference
title: Copilot CLIでNavigatorを継続利用する
description: 共通の協働契約をCopilot CLIで実現する起動・後続連絡の方法を示します。
sources:
  - id: github-copilot-cli-changelog
    resource: https://github.com/github/copilot-cli/blob/v1.0.88/changelog.md#L1710
  - id: issue-87
    resource: https://github.com/daiksud/agents/issues/87
  - id: issue-100
    resource: https://github.com/daiksud/agents/issues/100
---

## Copilot CLIでNavigatorを継続利用する

Driver / Navigatorの役割、編集権限、共有ToDo、段階確認、起動できない場合と継続不能になった場合の停止・報告は共通の協働指示に従う。この資料はCopilot CLI固有の実現方法を扱う。

GitHub Copilot CLIで後続の連絡が必要なNavigatorは、最初の `task` を `mode: "background"` で起動する。`mode: "sync"` は一度の応答で完了する依頼に限り、応答後に `idle` と表示されても `write_agent` の送信先にできるとは判断しない。[^github-copilot-cli-changelog]

返された `agent_id` を保持し、後続の確認・フィードバックを同じIDへ `write_agent` で送る。依頼が同じNavigatorに処理され、そのNavigatorから応答が返ることを確認する。起動や状態表示だけを継続性の証拠にせず、再開不能・履歴喪失等は共通の停止条件に従う。[^issue-87]

元の `agent_id` に連絡できなくなったら、応答・利用可能なエージェント一覧・履歴から継続可能性を調べ、HEADと未コミット差分、テスト結果、共有ToDo、未解決指摘と段階の確認状況を保持して停止・報告する。その喪失について停止報告後に明示的な再ペア承認を得たら、旧IDを担当から外した記録を残し、旧IDへの新たな `write_agent` をやめる。後から届く旧IDの応答は段階確認の証拠にせず、必要なら未確認の資料として新Navigatorに渡す。新しい `task` を `mode: "background"` で起動し、別の `agent_id` として必要な初期コンテキストを渡す。後続の `write_agent` にそのIDから応答があることを確かめてから、共通指示の未確認段階の再検証へ進む。新IDを元IDの継続と呼ばず、旧IDが復旧しても戻さない。新IDも失われたら改めて停止・報告し、その喪失への明示承認を待つ。単なる起動成功や `idle` 表示で段階確認を代用しない。[^issue-100]

### CLIでの確認例

- 前提: 同じNavigatorに初回応答後も複数回確認を依頼するコード変更である。[^issue-87] [^github-copilot-cli-changelog]
- もし: DriverがGitHub Copilot CLIの `task` でNavigatorを起動する
- ならば: Driverは `mode: "background"` で起動する
- かつ: 初回応答後の `write_agent` が同じ `agent_id` に処理され、そのNavigatorから応答が返る
- かつ: `mode: "sync"` の応答や `list_agents` の `idle` 表示だけから継続連絡できると判断しない

[^github-copilot-cli-changelog]: [Copilot CLI changelog v1.0.88](https://github.com/github/copilot-cli/blob/v1.0.88/changelog.md#L1710)。`sync` taskは再利用可能な `agent_id` を返さず、後続連絡には `mode: "background"` を使うと記載している。
[^issue-87]: [Issue #87](https://github.com/daiksud/agents/issues/87) の継続連絡と実際の応答確認。
[^issue-100]: [Issue #100](https://github.com/daiksud/agents/issues/100) の停止・承認付き再ペアの境界。
