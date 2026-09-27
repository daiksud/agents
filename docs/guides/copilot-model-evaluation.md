---
type: Guide
title: GitHub Copilot複数モデル評価
description: 共通InstructionsとSkillsを同じ条件で複数モデルに適用し、品質・効率・失敗原因を分離して記録する手順です。
sources:
  - id: issue-124
    resource: https://github.com/daiksud/agents/issues/124
  - id: issue-122
    resource: https://github.com/daiksud/agents/issues/122
  - id: issue-123
    resource: https://github.com/daiksud/agents/issues/123
  - id: github-supported-models
    resource: https://docs.github.com/en/copilot/reference/ai-models/supported-models
  - id: github-copilot-cli-programmatic
    resource: https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-programmatic-reference
---

## 目的

GPT-6 Sol、GPT-6 Luna、Claude Opus 5.5、Claude Sonnet 5に、同じInstructions・Skills・prompt・成功基準を適用し、モデル固有の補正が本当に必要かを調べる。4モデルはいずれも2026-09-27時点でGitHub Copilotのサポート対象として掲載されている。Copilot CLIは非対話実行と `--model` によるモデル固定をサポートする。[^github-supported-models] [^github-copilot-cli-programmatic]

この評価はモデルの総合ランキングを作らない。品質と効率を分け、少数回の差を一般化しない。

## 正本

- 共通ケース: `evals/copilot-models/cases.json`
- 実行: `scripts/run_copilot_model_eval.py`
- 実測記録: `evals/copilot-models/results/<run>/manifest.json`
- #122のモデル非依存契約と#123のrouting / Progressive Disclosureを変更せずに評価する。[^issue-122] [^issue-123]

## 実行条件

同じ比較バッチでは次を固定する。

- repository SHA
- Copilot CLI version
- `cases.json` のversion
- prompt
- 利用可能なInstructions / Skills
- taskの開始状態
- tool / permission境界
- reasoningやcontext windowなど、明示的に変更できるモデル設定
- 1ケースあたりの反復回数

モデルごとに成功条件を変えない。モデルが利用できない、CLIがない、認証・policyで拒否された場合は品質失敗ではなく `runtime` または `tool_or_permission` として記録する。

## 共通ケース

A–Gを全モデルで同じ順序・基準で使う。

| ID | 対象 |
| --- | --- |
| A | 小さな不具合修正: 小さいshared Todo、Red / Green / Refactor、Navigator gate、scope |
| B | 計画だけ: issue-managementで止まり、実装・deliveryへ広げない |
| C | 大きくなったTodo: 独立したRedを分割して再選択する |
| D | CI失敗 / review changes requested: 未完了として修正・再検証・最新HEADレビュー・deliveryを続ける |
| E | 権限不足: 制約を回避せず、完了範囲・未完了・blocker・再開条件を分ける |
| F | モデル引き継ぎ: self-reportではなく現在の差分・証拠を再確認する |
| G | Skill routing: github-actions + code-reviewと必要referenceだけを使う |

具体promptと判定項目は `cases.json` を正本とし、この表へ重複させない。

## 実行

まず、評価計画だけを確認する。

```bash
python3 scripts/run_copilot_model_eval.py --dry-run
```

認証済みCopilot CLIがある隔離環境で、同じSHAから最低3回ずつ実行する。

```bash
python3 scripts/run_copilot_model_eval.py \
  --repeat 3 \
  --output-dir evals/copilot-models/results/<run-id>
```

一部モデルだけを再現確認するときはCLI model IDを明示する。

```bash
python3 scripts/run_copilot_model_eval.py \
  --models gpt-6-sol,claude-opus-5.5 \
  --repeat 3 \
  --output-dir evals/copilot-models/results/<run-id>
```

runnerは `--mode=plan`、`--no-ask-user`、JSON出力を使い、ケース自体も外部writeを禁止する。実装能力ではなく共通契約の判断を比較するため、評価時にIssue・PR・mainを変更しない。

## 記録

runnerは各runについてraw JSONL、stderr、elapsed timeとmanifestを保存する。manifestの未評価フィールドは `null` のままにし、未知を0へ変換しない。

実測ディレクトリは `evals/copilot-models/results/.gitignore` で既定のGit管理対象から外す。raw JSONLやstderrにはコード・ログ・モデル応答等が含まれ得るため、共有・コミット前に内容と公開範囲を確認する。リポジトリへ残す場合は、必要な集計・判定だけをレビュー済みの記録へ転記し、秘密値や不要なraw transcriptを保存しない。

### 品質

各ケースのcriteriaを実際の出力へ照合し、少なくとも次を記録する。

- criteria達成
- TDD / Navigator gateの欠落
- 完了条件前の途中停止
- 不要なscope expansion
- 不具合・要件違反・回帰の見逃し
- evidenceなしの成功判定
- 正当なstop boundary違反

### 効率

取得できる場合だけ次を記録する。

- elapsed time
- turn count
- tool call count
- token usage
- loaded Skills / references
- 不要な再読

Copilotの出力形式・契約から取得できない値は `null` とする。品質とコストを一つの総合scoreへ合成しない。

## 原因分類

失敗は次の順序で原因を切り分け、一つの便利な「モデル差」へまとめない。

1. `instruction_delivery`: 必要なInstructions / Skillが実際に届いていない。
2. `ambiguity`: 共通指示が曖昧、重複、矛盾している。
3. `tool_or_permission`: 必要なtool、認証、policy、permissionがない。
4. `task_granularity`: Todoやケース自体が大きすぎる。
5. `runtime`: Copilot client、CLI、session、transport固有の制約。
6. `model_specific`: 上記を除外しても同じモデルだけで再現する。
7. `none`: 受け入れ条件を満たす。

原因を判断できない場合は `notes` に未確認事項を残し、`model_specific` に推測で分類しない。

## モデル固有補正のゲート

モデル固有の補正は次のすべてを満たす場合だけ候補にする。

- 同じ失敗が同じモデルで複数回再現する。
- instruction deliveryの欠落ではない。
- 共通Instructions / Skillsの曖昧さ・矛盾ではない。
- tool / permission / runtimeでは説明できない。
- task粒度では説明できない。
- 共通ルールを直すと、既に正しく動くモデルへ不要な制約を追加する。
- 補正の根拠、適用範囲、削除条件を説明できる。

補正はモデル別Skillの複製を第一選択にせず、最小のoverlayにする。追加後はA–Gを全モデルで再評価し、#122 / #123の契約を壊していないことを確認する。

## 現在の基準記録

`evals/copilot-models/results/2026-09-27-runtime-unavailable.json` は、このIssueを実装したChatGPT実行環境では `copilot` と `gh` CLIが利用できなかった事実だけを記録する。4モデルの品質・速度・token効率を評価した記録ではない。

この記録を「4モデルに差がなかった」という証拠に使わない。実機結果が得られるまでモデル固有overlayを追加しない。

[^github-supported-models]: [Supported AI models in GitHub Copilot](https://docs.github.com/en/copilot/reference/ai-models/supported-models)。対象モデルの対応状況。
[^github-copilot-cli-programmatic]: [GitHub Copilot CLI programmatic reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-programmatic-reference)。非対話実行とモデル固定。
[^issue-122]: [Issue #122](https://github.com/daiksud/agents/issues/122) のモデル非依存契約。
[^issue-123]: [Issue #123](https://github.com/daiksud/agents/issues/123) のSkill routingとProgressive Disclosure。
