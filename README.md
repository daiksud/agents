---
type: Guide
title: daiksud/agents
description: 共有Instructions・Skillsの利用前提とAPMによる導入方法。
---

[開発方針のInstructions](.apm/instructions/)と[作業別のSkills](skills/)を、APMで共有するリポジトリです。

## 利用前提

配布対象は[apm.yml](apm.yml)で指定するCodexとGitHub Copilotです。APM CLIを利用できる環境で、Instructions・Skillsをグローバルに一式導入して使います。Skills間に依存関係があるため、個別の `SKILL.md` だけをコピーする利用は前提にしていません。

[協働指示](.apm/instructions/collaboration.instructions.md)に従い、コード変更には独立した実行コンテキストを持つNavigatorが必要です。最初のコード編集前に、同じNavigatorから初回・後続の実応答を確認します。利用できない場合はテストコードやリファクタリングを含むコード編集を開始せず、承認済み範囲の読み取り調査・計画整理は継続できます。相談・説明・計画のみ、および文書だけの変更にはペア作業を要求しません。

## 導入

```bash
apm install --global --target codex,copilot daiksud/agents
apm compile --global
```

## 指示とGitHubの保護設定

Instructions・Skillsが定める確認手順と、GitHubが機械的に強制する保護条件は別です。導入先のRulesets・必須ステータスチェックは各リポジトリで管理し、このパッケージの導入だけで同じ保護設定が適用されるとは扱いません。

[github-repo](skills/github-repo/SKILL.md) は、指定したリポジトリについて、イミュータブルリリース・Squash限定・mainのRuleset・外部ActionのフルSHA必須化・無料セキュリティ機能を診断し、明示的に依頼された範囲だけを適用します。「設定を診断して」は結果の回答、「計画をIssueにして」は記録、「設定を適用して」は差分適用と再診断までを担当します。workflow本文の変更は [github-actions](skills/github-actions/SKILL.md) と連携し、GitHub側の設定変更だけのために空のcommit・PRは作りません。

本リポジトリでは[ci](.github/workflows/ci.yml)を必須とし、CodeQLのスキャン・結果はPRマージの待機対象にしません。最新の強制条件は[Ruleset](https://github.com/daiksud/agents/rules/22615823)、通常レビューから統合後確認までの手順は[レビューとマージ](skills/change-delivery/references/review-and-merge.md)を確認してください。
