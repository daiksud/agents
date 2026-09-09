# daiksud/agents

[APM](https://microsoft.github.io/apm/)で、共通の作業原則と作業スキルをグローバル配布するパッケージです。

## 構成と編集先

| 原本 | 役割 |
| --- | --- |
| `.apm/instructions/core.instructions.md` | 常時適用する設計原則、変更保護、スキルの読み込み条件と完了条件 |
| `skills/task-workflow/` | Issue・計画からレビュー・スカッシュマージまでの作業手順 |
| `skills/bdd-tdd/` | 設計確認、シナリオ分割、BDD・TDD、検証 |
| `skills/okf-docs/` | OKF v0.2に従う文書の作成・更新・検証 |

変更・成果物作成には作業スキルを適用します。文書のみ・小さな修正も、読み取り調査で計画をIssue本文に保存し、再取得したURLと本文をユーザーが確認・明示的に承認してから、作業ブランチの準備と実行に進みます。範囲追加・方針変更はIssue更新と本文提示を経て再承認を得ます。相談・比較・説明・読み取りのみの調査にはIssue・PR・マージを要求しません。
外部依存の `anthropics/skills/skills/skill-creator` は、スキルの作成・改善に使います。

共通指示には `applyTo` を付けません。詳細な手順はスキルに置き、必要な段階で `references/` を読みます。
[インストラクションのテンプレート](docs/templates/instructions.md)は、常時必要なルールを編集するためのひな形です。
スキルの作成・更新時は[スキルの編集指示](skills/AGENTS.md)に従います。
スキルは `name`・`description` を持つ `SKILL.md` と、同梱資料・`evals/evals.json` で管理します。

## gh skillでスキルを導入

スキルだけを導入する場合は、GitHub CLIの `gh skill` を利用できます。ルートの `skills/` は標準探索対象なので、追加の探索オプションは不要です。

```bash
gh skill install daiksud/agents --all --agent codex --scope user
```

このコマンドは、このリポジトリの3スキルと同梱資料を導入します。APMの外部依存である `skill-creator` と共通指示のAGENTS.mdは導入しません。共通指示と外部依存もまとめて導入する場合は、以下のAPM手順を使います。

## グローバル導入

APM 0.30.0で検証済みです。Codex・Copilot向けの標準手順は次です。

```bash
apm install --global --target codex,copilot daiksud/agents
apm compile --global --dry-run
apm compile --global
```

`install --global` はパッケージ・依存関係とスキルを配布します。AGENTS.mdの生成は `compile --global` が担当します。
グローバルコンパイルは作業ディレクトリの原本ではなく、`~/.apm/apm_modules/` のインストール済み指示を読みます。

| 配布先 | 内容 |
| --- | --- |
| `~/.apm/apm.yml` | ユーザースコープの依存関係・対象設定 |
| `~/.apm/apm_modules/` | インストール済みパッケージ |
| `~/.agents/skills/` | 作業スキルと同梱資料 |
| `~/.codex/AGENTS.md` | Codex向け共通指示 |
| `~/.copilot/AGENTS.md` | Copilot向け共通指示 |

`compile --global` に `--target` は付けません。対象は `~/.apm/apm.yml` の `targets` で管理し、既存の依存関係・対象設定を確認してから変更します。対象が未指定の場合は他の対応ツールにも生成されるため、コンパイル前にdry-runの出力を確認します。

グローバルコンパイルは本文の相対リンクを書き換えません。共通指示は `~/.agents/skills/<name>/SKILL.md` を明示し、スキル内の資料は同梱相対リンクで参照します。
プロジェクトの `docs/` などのパスは、スキルの配布先ではなく作業対象リポジトリを基準にします。

## 更新

原本を編集しただけではグローバル配布先に反映されません。公開済みパッケージを更新してから再生成します。

```bash
apm update --global daiksud/agents
apm compile --global --dry-run
apm compile --global
```

生成されたAGENTS.mdを直接編集せず、共通ルールはこのパッケージの原本へ反映します。
プロジェクト固有のルールは各リポジトリのAGENTS.mdに残します。

## 既存構成からの移行

1. 現在のグローバル・プロジェクト側のAGENTS.md、APM設定、配布ファイルを確認し、変更前の内容を保持します。
2. 上記のグローバル導入・更新を行い、スキルと共通指示の参照先が存在することを確認します。
3. 手書きのグローバルAGENTS.mdはAPMが上書きしません。スキップされた場合は既存内容と新しい共通指示を比較し、必要な個人設定を保持する移行を別途行います。生成成功とは扱いません。
4. 旧ローカル配布があるリポジトリでは、パッケージの依存関係とAPM管理の共通指示を確認し、グローバル配布と重複する部分だけを整理します。他の依存パッケージや手書きのプロジェクト固有指示は保持します。
5. 更新後に旧6指示が残っていないことと、新しい共通指示が適用されることを確認します。他リポジトリを一括変更しません。

Codexの実行権限を準備する場合は[コマンド事前許可のガイド](docs/guides/codex-command-approvals.md)を参照します。計画承認は環境の権限付与を意味しません。

## 検証

原本のYAML・JSON、ルールの移行漏れ、参照先、rumdlと `git diff --check` を確認します。
配布は隔離したユーザースコープで、新規・再導入・旧構成からの更新、手書きAGENTS.md保護を確認します。
各スキルの `evals/evals.json` は外部書き込みを行わず適用判断を確認する例です。時間・トークンの新旧比較結果ではありません。

- [APM: グローバルコンパイル](https://microsoft.github.io/apm/producer/compile/#global-compilation--g)
- [APM: スキルの作成と配布](https://microsoft.github.io/apm/producer/author-primitives/skills/)
