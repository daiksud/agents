# daiksud/agents

[APM](https://microsoft.github.io/apm/)で、共通の作業原則と作業スキルをグローバル配布するパッケージです。

## 構成と編集先

| 原本 | 役割 |
| --- | --- |
| `.apm/instructions/core.instructions.md` | 常時適用する設計原則、変更保護、スキルの読み込み条件と完了条件 |
| `skills/task-workflow/` | Issue・計画からレビュー・スカッシュマージまでの作業手順 |
| `skills/bdd-tdd/` | 設計確認、シナリオ分割、BDD・TDD、検証 |
| `skills/code-review/` | 欠陥・回帰を根拠から評価する読み取り専用レビュー |
| `skills/okf-docs/` | OKF v0.2に従う文書の作成・更新・検証 |

変更・成果物作成には作業スキルを適用します。文書のみ・小さな修正も、読み取り調査で計画をIssue本文に保存し、再取得したURLと本文をユーザーが確認・明示的に承認してから、作業ブランチの準備と実行に進みます。関連する範囲追加・方針変更はIssue更新と本文提示を経て再承認を得ます。現在の目的・成功条件と関連の薄い追加依頼は例外として、計画・実装承認を求めず「後続対応・計画未作成」の独立したIssueへ記録し、現在のタスクを承認済み範囲で継続します。重複を確認してURLを案内し、関連性が不明なら確認します。後続Issueへの着手時または明示的な計画作成依頼時に通常形式で計画を作り、計画のみの依頼を実装承認とは扱いません。詳細は[追加依頼の記録手順](skills/task-workflow/references/planning.md#関連の薄い追加依頼の記録)に従います。相談・比較・説明・読み取りのみの調査にはIssue・PR・マージを要求しません。
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

このコマンドは、このリポジトリの4スキルと同梱資料を導入します。APMの外部依存である `skill-creator` と共通指示のAGENTS.mdは導入しません。共通指示と外部依存もまとめて導入する場合は、以下のAPM手順を使います。

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

Issueの新規作成（Sub-issue・計画なしの後続Issueを含む）と計画の保存・更新では、投稿前整形と保存後の本文一致確認を経てOSの既定ブラウザで一度開きます。起動の都度確認は求めません。参照・重複案内、コメント、進捗・検証結果だけの更新、PR操作は対象外です。起動失敗時は保存成功と区別して理由とURLを伝え、承認済み作業を継続します。表示確認・本文とURLの提示・計画承認の手順は維持し、後続Issueの起動をその計画・実装開始承認にはしません。詳細は[Issue保存後のブラウザ起動](skills/task-workflow/references/planning.md#issue保存後のブラウザ起動)を参照します。

## Markdownの整形と投稿

Issue・PR本文・コメントはEmoji付き見出し、対応関係の表、制約のAlertsで構成し、投稿・更新前に本文全体をrumdlで整形・チェックします。GitHub投稿本文にはOKFを付けません。

共通設定は `task-workflow` に同梱され、本リポジトリの `.rumdl.toml` も同じ設定を継承します。MD013・MD033・MD034・MD041のみを無効化し、MD060をcompact、MD076をtightにします。その他のルールは既定のままです。

リポジトリ直下で、継承設定を明示して実行します。

```bash
rumdl check --config .rumdl.toml --deny-config-warnings --fix <変更したMarkdownファイル>
rumdl check --config .rumdl.toml --deny-config-warnings <変更したMarkdownファイル>
```

投稿用の一時本文や配布先での実行は[GitHub向けMarkdownの品質](skills/task-workflow/references/markdown-quality.md)に従って設定を明示指定します。`okf-docs` は既存の依存スキル `task-workflow` に同梱された設定・資料を参照するため、両スキルを導入します。

rumdlは自動インストールしません。未導入・旧版の場合は導入方法を示して事前許可を得ます。ダウンロードを伴う一時実行も同様です。未検証の投稿は保留します。

## 検証

原本のYAML・JSON、ルールの移行漏れ、参照先、rumdlと `git diff --check` を確認します。
配布は隔離したユーザースコープで、新規・再導入・旧構成からの更新、手書きAGENTS.md保護を確認します。
各スキルの `evals/evals.json` は外部書き込みを行わず適用判断を確認する例です。時間・トークンの新旧比較結果ではありません。

- [APM: グローバルコンパイル](https://microsoft.github.io/apm/producer/compile/#global-compilation--g)
- [APM: スキルの作成と配布](https://microsoft.github.io/apm/producer/author-primitives/skills/)

### ローカルとCIで同じ検査を実行

Python 3.12、GitHub CLI 2.100.0を使います。依存ツールの導入を承認した環境で、リポジトリ直下から実行します。

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-ci.txt
source .venv/bin/activate
python -m unittest discover -s tests -v
python scripts/check_repository.py
python scripts/skill_smoke.py
```

静的検査は隠しディレクトリを含む原本のMarkdown・相対リンク・YAML・JSON・必須メタデータ・評価データを確認します。導入検証は一時ディレクトリで `gh skill` の列挙、新規導入、強制再導入と原本との内容一致を確認し、終了時に削除します。探索的に内容を読む場合は、次のコマンドで検証用ディレクトリを作れます。

```bash
exploration_dir=$(mktemp -d)
gh skill install . --from-local --all --dir "$exploration_dir"
```

表示された導入先で各SKILL.mdと同梱リンクを読み、使いにくい指示や不足を確認します。終了後はその検証用ディレクトリだけを削除します。エージェントによる読み取り専用模擬評価は別途行い、形式検査や導入成功をスキルの判断品質の証明とは扱いません。

GitHub Actionsは全ブランチへのpush、main向けPR、mainへの統合後、手動実行で検査します。`static-checks` 成功後に `skill-install` を実行し、失敗をマージで持ち越しません。必須チェックの定義は [.github/required-checks.json](.github/required-checks.json) です。初回の実行成功後、管理者が既存ルールを保持してmainの必須チェックに反映し、ジョブ名の変更時も両方を更新します。

[CIの実践](https://continuousdelivery.com/foundations/continuous-integration/)と[継続的テスト](https://continuousdelivery.com/foundations/test-automation/)に基づく最小基盤です。APMの更新・復旧経路と日常の統合運用の整備は後続段階で行います。

## GitHub上のレビュー用配置

ローカル導入とGitHub上の配置は別です。個人環境への導入だけでGitHubのレビューがスキルを利用できるとは扱いません。

| 利用先 | 配置・読み込み |
| --- | --- |
| ローカル | `gh skill` またはAPMで導入した `code-review` をレビュー実行時に読む |
| Copilot GitHubレビュー | 原本 `skills/code-review/` の実行時ファイルを `.github/skills/code-review/` へ同期する。`evals/` はコピーしない |
| Codex GitHubレビュー | root `AGENTS.md` の条件付き参照に加え、依頼にも原本パスと適用指示を含める。ネイティブなスキル自動探索の保証ではない |

```bash
python scripts/sync_review_skill.py
python scripts/sync_review_skill.py --check
gh skill install . --from-local code-review --dir /tmp/review-skill-install
```

同期先は生成専用です。原本を編集して同期し、両方をコミットします。CIで内容差分・欠落・余分なファイルを検出します。レビュー依頼・指摘対応・完了判定は[task-workflow](skills/task-workflow/references/review-and-merge.md#代替レビュー)が担当します。

[Copilot公式資料](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/request-a-code-review/use-code-review#mcp-servers-and-agent-skills)に従い、実PRの指摘の出典またはセッションログで使用したスキルを確認します。[Codex公式資料](https://learn.chatgpt.com/docs/third-party/github)によるAGENTS.mdの案内も、実PRで読み込みを検証します。通常の `@codex review`、確認できなければ原本パスを付けた依頼を順に試し、ログまたは固有手順の根拠付き適用を確認します。後者のみ成功ならパス指定を標準にし、いずれも未確認なら連携未完了とします。結果と未確認範囲はPRに記録し、パス復唱やリアクションだけを成功の証拠にしません。

標準の依頼は `@codex review` に「`skills/code-review/SKILL.md` を読んで適用してください」を添えます。[実PRの検証](https://github.com/daiksud/agents/pull/34#issuecomment-5627514742)では、明示パス指定時に[セッションログ](https://chatgpt.com/codex/cloud/tasks/task_e_6aa34c1893508327b2c83f674db370e8)で原本本文の読み取りを確認しました。ログの閲覧には権限が必要です。条件付き参照だけの通常依頼では読み取りの証拠を確認できていません。
