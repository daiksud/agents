# daiksud/agents

[APM](https://microsoft.github.io/apm/)で、共通の作業原則と作業スキルをグローバル配布するパッケージです。

共通Instructionは、スキル選択、判断、開発、ドメインモデル、協働、デリバリー、変更の安全性、品質の8つの関心事に分かれています。APMはこれらを共通AGENTS.mdへまとめて配布します。原本と担当責務は[保守ガイド](docs/guides/delivery.md#原本の編集と保守)に示します。

## gh skillでスキルを導入

スキルだけを導入する場合は、GitHub CLIの `gh skill` を利用できます。ルートの `skills/` は標準探索対象なので、追加の探索オプションは不要です。

```bash
gh skill install daiksud/agents --all --agent codex --scope user
```

このコマンドは、このリポジトリの作業スキルと同梱資料を導入します。APMの外部依存である `skill-creator` と共通指示のAGENTS.mdは導入しません。共通指示と外部依存もまとめて導入する場合は、以下のAPM手順を使います。

各スキルの `SKILL.md` から、計画・Issue記録・ブランチ準備、設計・共有仕様・テスト、文書検証など、現在の工程に対応する資料を参照します。feature文書だけの作成では形式資料を使い、コード実装のTDD工程は開始しません。

[behavior-specification](skills/behavior-specification/SKILL.md)は、コードを書かない場合もストーリー・具体例・受け入れ条件を整理します。[software-development](skills/software-development/SKILL.md)は、合意済みの仕様からTDD・ペア協働・Simple Designで実装します。Issue計画・公開許可・Markdown品質は `issue-management`、承認済み変更のbranch準備から公開main確認までは `change-delivery`、文書形式は `document-authoring` を条件に応じて併用します。Issue計画だけならdeliveryを始めません。兄弟Skillの資料を使う場合は、上記の `--all` で依存も導入してください。

[github-actions](skills/github-actions/SKILL.md)は、GitHub Actionsの設計・安全性・効率改善・Action内部ランタイム更新を扱います。依頼に該当する参照資料だけを読み、監査のみと修正依頼を区別します。Issue計画と公開許可は `issue-management`、承認済みworkflow変更とmain確認は `change-delivery`、アプリコードの変更は `software-development`、文書作成は `document-authoring`、読み取り専用レビューは `code-review` を併用します。これらの依存スキルは上記の `--all` で一緒に導入できます。

`document-authoring`の検査スクリプトにはPython 3.10以上と同梱requirements.txtの依存が必要です。スキルの配布はPython依存を自動導入しません。外部Bundleの読み取り専用の受け入れにはIssue計画やdeliveryを要求せず `conformance`、自作の公開前検査は `authoring` を使います。[検査環境の準備](skills/document-authoring/references/validation.md)に従って利用する環境を確認してください。

### gh skillの更新と廃止Skillの退避

`gh skill install --all --force` は既存Skillを上書きしますが、名前が変わった旧Skillは削除しません。APMが管理する導入先では、下記のAPM更新手順を使います。

1. `gh skill list --agent codex --scope user --json skillName,sourceURL,path` で実際の導入先と出所を確認します。他のagent・scope・`--dir` を使った場合はその導入先も確認します。
2. `daiksud/agents` 由来か、独自変更や追加ファイルがあるかを確認し、必要な内容をSkill探索先の外へバックアップします。所有元・独自変更を判断できないものを上書き・退避しません。
3. 上書きする対象を確認したうえで `gh skill install daiksud/agents --all --force --agent codex --scope user` を実行し、新しいSkillと同梱依存が揃うことを確認します。
4. 下表の旧Skillが残っている場合は、確認した出所のディレクトリだけを、すべてのSkill探索先の外へ丸ごと退避します。単に `SKILL.md` を書き換えたり、探索先の中で名前を変えたりせず、独自ファイルもバックアップへ保持します。他のSkillは移動しません。
5. 同じ `gh skill list` で旧名が発見されず、新しいSkillが利用できることを確認します。確認できない間は移行完了としません。

| 廃止した入口 | 移行先 |
| --- | --- |
| `bdd-tdd` | 仕様の発見は `behavior-specification`、コード変更は `software-development` |
| `task-workflow` | Issueの計画・記録は `issue-management`、承認済み変更の完了は `change-delivery` |
| `okf-docs` | 文書の作成・更新とOKF Bundleの検証は `document-authoring` |

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

## 開発実践の診断と導入計画

共通指示はXPの価値、DevOps・Lean・CI/CD・BDD/ATDD/TDD・DDD・チームトポロジーを日々の判断の軸にします。概念と本リポジトリでの名称は[用語集](docs/glossary.md)で確認できます。

既存リポジトリへの導入を検討するときは、[engineering-assessment](skills/engineering-assessment/SKILL.md)へ「現状を診断し、段階的な導入計画をIssueにまとめて」と依頼します。実際の作業の証拠から優先順位と最初の小さな実験を示し、保存したIssueを提示して終了します。実装・組織変更は行わず、導入未実施のIssueは開いたまま残します。通常の修正や概念説明では全面診断を起動しません。

診断計画は `issue-management` でIssueへ保存・確認・提示して終了します。別途の明確な変更依頼と承認がある場合だけ、確認済み計画を `change-delivery` へ引き渡します。

## 更新

原本を編集しただけではグローバル配布先に反映されません。公開済みパッケージを更新してから再生成します。

```bash
apm update --global daiksud/agents
apm install --global
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

Codexの実行権限を準備する場合は[コマンド事前許可のガイド](docs/guides/codex-command-approvals.md)を参照します。明確な変更依頼や計画への実行承認は、環境の権限付与を意味しません。

## 保守と検証

原本編集・同期・ローカル検査・CI・レビュー連携の設定検証は[配布ガイド](docs/guides/delivery.md#原本の編集と保守)を参照します。変更・保守前の準備は[AGENTS.md](AGENTS.md)、スキル編集は[skills/AGENTS.md](skills/AGENTS.md)に従います。

導入済み環境の復旧は[正常SHAへ戻す手順](docs/guides/delivery.md#不具合から復旧する)を参照します。共通ルールの使い方は導入済みの各スキルを読み、Issueの計画・記録は `issue-management`、承認済み変更とPR・main確認は `change-delivery`、文書の形式は `document-authoring` を適用します。
