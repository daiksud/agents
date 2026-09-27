---
type: Guide
title: スキルと共通指示の原本を保守する
description: 配布する指示と機能を保持し、原本の編集・同期・レビュー・統合を進める手順を説明します。
sources:
  - id: continuousdelivery-foundations-configuration-management
    resource: https://continuousdelivery.com/foundations/configuration-management/
  - id: continuousdelivery-implementing-patterns
    resource: https://continuousdelivery.com/implementing/patterns/
  - id: continuousdelivery-foundations-test-automation
    resource: https://continuousdelivery.com/foundations/test-automation/
  - id: microsoft-producer-compile
    resource: https://microsoft.github.io/apm/producer/compile/#global-compilation--g
  - id: microsoft-author-primitives-skills
    resource: https://microsoft.github.io/apm/producer/author-primitives/skills/
  - id: continuousdelivery-foundations-continuous-integration
    resource: https://continuousdelivery.com/foundations/continuous-integration/
  - id: docs-request-a-code-review-use-code-review
    resource: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/request-a-code-review/use-code-review#mcp-servers-and-agent-skills
  - id: learn-third-party-github
    resource: https://learn.chatgpt.com/docs/third-party/github
  - id: github-pull-34
    resource: https://github.com/daiksud/agents/pull/34#issuecomment-5627514742
  - id: chatgpt-tasks-task-e-6aa34c1893508327b2c83f674db370e8
    resource: https://chatgpt.com/codex/cloud/tasks/task_e_6aa34c1893508327b2c83f674db370e8
---

## スキルと共通指示の原本を保守する

このパッケージの原本はGitで版管理し、配布する版をコミットSHAで識別します。構成管理[^continuousdelivery-foundations-configuration-management]と配布経路[^continuousdelivery-implementing-patterns]を区別し、実ユーザー環境の更新は[README](../../README.md)の導入・更新手順に従います。

### パッケージ保守の範囲

現時点では、このリポジトリ自身の単体テスト・スキル評価・モデル比較・導入smoke検証と専用CIを管理対象としていません。保守作業では、目的・仕様・実差分・参照先を読み合わせ、実際に確認した範囲と未確認事項をIssue・PRに記録します。これらの追加・再生成を現在の保守作業の完了条件に含めません。将来の再導入を禁止するものではなく、必要性を別途判断します。

配布するスキルと共通インストラクションのTDD・テスト・評価指示は維持します。`document-authoring` のOKF検証CLI・依存・利用手順、`issue-management` の配布用rumdl設定、レビュー用スキルの同期機能も提供機能として保持します。外部Bundleの検証は[検証手順](../../skills/document-authoring/references/validation.md)に従います。

専用CIの撤去は、GitHub側のCodeQL・Code Quality・レビュー保護の解除を意味しません。既存の必須チェックを変更するときは承認された範囲を確認し、実際の設定とマージ条件を照合します。

### 導入する版を選ぶ

1. 導入するコミットSHAと、その変更内容・レビュー状態を確認します。
2. 同じ版を導入する場合は、READMEのAPM導入コマンドのパッケージ指定を `daiksud/agents#<確認した完全SHA>` にします。
3. APMのグローバルコンパイル[^microsoft-producer-compile]とSkill配布[^microsoft-author-primitives-skills]の役割を区別し、READMEの導入・更新手順を使います。

### 不具合から復旧する

mainの不具合を見つけたら、影響・確認できた原因・対象SHAを記録し、[統合後mainの確認と復旧](../../skills/change-delivery/references/review-and-merge.md#統合後mainの確認と復旧)に従って認可された復旧を進めます。必要なレビューとGitHub側の保護条件を維持し、確認できない状態を復旧済みとしません。

すでに導入した利用者は、正常だったことを確認したコミットSHAを指定し直して再生成できます。

```bash
known_good_sha='<正常だったことを確認した完全SHA>'
apm install --global --target codex,copilot "daiksud/agents#$known_good_sha"
apm compile --global --dry-run
apm compile --global
```

既存設定と手書き指示を先に保持し、復旧対象と結果を確認します。未確認のコミットを正常版と呼ばず、実ユーザー環境をパッケージの試験に使いません。

### 小さく統合しmainまで確認する

[小さな統合単位と活動日](../../skills/change-delivery/references/branches.md#小さな統合単位と活動日)に従い、目的にまとまった変更をレビュー・統合します。CIの実践[^continuousdelivery-foundations-continuous-integration]と継続的テスト[^continuousdelivery-foundations-test-automation]について配布本文が定める指針と、本リポジトリで管理する検証基盤の有無を区別します。

マージ前には最新HEADのレビュー、要対応指摘、競合、GitHub側に残る保護条件を確認します。マージ後は[main確認](../../skills/change-delivery/references/review-and-merge.md#統合後mainの確認と復旧)と[作業環境整理](../../skills/change-delivery/references/review-and-merge.md#マージ後の作業環境の整理)まで担当し、公開mainのSHA・対象ファイル・保護設定と結果を記録します。専用CIがないことを、テストや配布検証の成功として報告しません。

### 原本の編集と保守

| 原本 | 役割 |
| --- | --- |
| `.apm/instructions/skill-routing.instructions.md` | 作業に合うスキルの読み込み条件 |
| `.apm/instructions/decision-making.instructions.md` | 目的・目標・手段・スタンダードと判断の前提 |
| `.apm/instructions/development.instructions.md` | XPの価値、共有理解、テスト先行と小さな反復 |
| `.apm/instructions/domain-modeling.instructions.md` | 用語、モデルの境界と依存 |
| `.apm/instructions/collaboration.instructions.md` | 継続Navigator、共有ToDo、段階確認と承認付き再ペア |
| `.apm/instructions/delivery.instructions.md` | 価値の流れ、小さな統合とmainの健全性 |
| `.apm/instructions/change-safety.instructions.md` | 承認・権限・変更保護 |
| `.apm/instructions/quality.instructions.md` | 成果物と検証の品質、未確認範囲の報告 |
| `skills/issue-management/` | Issue計画・記録、公開許可、Markdown投稿・整形の手順 |
| `skills/change-delivery/` | 承認済み変更のbranch、レビュー・CI・マージと統合後mainの確認・整理 |
| `skills/engineering-assessment/` | 開発実践の証拠に基づく診断と段階的な導入計画。Issue記録で完了 |
| `skills/behavior-specification/` | ストーリー、BDD・ATDD、具体例・受け入れ仕様の発見と整理 |
| `skills/software-development/` | Shared ToDo、TDD、Simple Design・YAGNIと小さな実装・検証 |
| `skills/code-review/` | 現在の要求を満たす最もシンプルな設計と実際の変更への安全性を軸に、欠陥・回帰も根拠から評価する読み取り専用レビュー |
| `skills/document-authoring/` | OKF v0.2に従う文書の作成・更新・検証 |
| `skills/github-actions/` | GitHub Actionsの設計・安全性・効率改善・Action内部ランタイム更新の判断と検証 |

共通指示には `applyTo` を付けません。詳細手順はスキルと同梱資料に置きます。各SKILL.mdを工程別の入口にし、issue-managementは計画・Issue記録・Markdown品質、change-deliveryはbranch・レビュー・main確認、behavior-specificationは共有仕様、software-developmentは設計・実装・テスト、document-authoringは形式・出典・検証へ分けます。参照を移した場合はリンク元と導入後の同梱資料も確認します。[インストラクションのテンプレート](../templates/instructions.md)と[スキルの編集指示](../../skills/AGENTS.md)を参照します。スキルの作成・改善には外部依存の `skill-creator` を使います。

原本を編集しても公開版やユーザースコープは更新されません。編集中の原本を適用するための自己更新は行わず、公開後の導入・更新は[README](../../README.md)の利用者向け操作として扱います。生成されたAGENTS.mdは直接編集しません。

### Markdownの整形と投稿

Issue・PR等の投稿は[GitHub向けMarkdownの品質](../../skills/issue-management/references/markdown-quality.md)に従い、保存した本文と表示を確認します。配布用の `skills/issue-management/assets/rumdl.toml` は同スキルの機能として保持します。現時点では、パッケージ全体を検査する専用設定やCIへの接続は備えていません。

### GitHub上のレビュー用配置

ローカル導入とGitHub上の配置は別です。個人環境への導入だけでGitHubのレビューがスキルを利用できるとは扱いません。

| 利用先 | 配置・読み込み |
| --- | --- |
| ローカル | `gh skill` またはAPMで導入した `code-review` をレビュー実行時に読む |
| Copilot GitHubレビュー | 原本 `skills/code-review/` の実行時ファイルを `.github/skills/code-review/` へ同期する |
| Codex GitHubレビュー | root `AGENTS.md` の条件付き参照に加え、依頼にも原本パスと適用指示を含める。ネイティブなスキル自動探索の保証ではない |

```bash
python scripts/sync_review_skill.py
```

同期先は生成専用です。原本を編集して同期し、両方をコミットします。同期結果の実差分を確認します。レビュー依頼・指摘対応・完了判定は[代替レビュー](../../skills/change-delivery/references/review-and-merge.md#代替レビュー)を含む `change-delivery` が担当します。

Copilot公式資料[^docs-request-a-code-review-use-code-review]とCodex公式資料[^learn-third-party-github]を参照し、各実行環境の読み込み方法を区別します。個人環境への導入やパスの復唱だけで、GitHub上のレビューにスキルが適用されたとは扱いません。

標準の依頼は `@codex review` に「`skills/code-review/SKILL.md` を読んで適用してください」を添えます。実PRの検証[^github-pull-34]では、明示パス指定時にセッションログ[^chatgpt-tasks-task-e-6aa34c1893508327b2c83f674db370e8]で原本本文の読み取りを確認しました。ログの閲覧には権限が必要です。条件付き参照だけの通常依頼では読み取りの証拠を確認できていません。

APMのパッケージキャッシュにルートやディレクトリ別のAGENTS.mdが保存されることと、共通指示として実行時に適用されることを区別します。配布スキルをローカル編集指示へ依存させません。

[^continuousdelivery-foundations-configuration-management]: [構成管理](https://continuousdelivery.com/foundations/configuration-management/)。本文に記した参照範囲と採用判断の根拠。
[^continuousdelivery-implementing-patterns]: [デプロイメントパイプライン](https://continuousdelivery.com/implementing/patterns/)。本文に記した参照範囲と採用判断の根拠。
[^microsoft-producer-compile]: [APM: グローバルコンパイル](https://microsoft.github.io/apm/producer/compile/#global-compilation--g)。本文に記した参照範囲と採用判断の根拠。
[^microsoft-author-primitives-skills]: [APM: スキルの作成と配布](https://microsoft.github.io/apm/producer/author-primitives/skills/)。本文に記した参照範囲と採用判断の根拠。
[^continuousdelivery-foundations-continuous-integration]: [CIの実践](https://continuousdelivery.com/foundations/continuous-integration/)。本文に記した参照範囲と採用判断の根拠。
[^continuousdelivery-foundations-test-automation]: [継続的テストの原則](https://continuousdelivery.com/foundations/test-automation/)。本文に記した参照範囲と採用判断の根拠。
[^docs-request-a-code-review-use-code-review]: [Copilot公式資料](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/request-a-code-review/use-code-review#mcp-servers-and-agent-skills)。本文に記した参照範囲と採用判断の根拠。
[^learn-third-party-github]: [Codex公式資料](https://learn.chatgpt.com/docs/third-party/github)。本文に記した参照範囲と採用判断の根拠。
[^github-pull-34]: [実PRの検証](https://github.com/daiksud/agents/pull/34#issuecomment-5627514742)。本文に記した参照範囲と採用判断の根拠。
[^chatgpt-tasks-task-e-6aa34c1893508327b2c83f674db370e8]: [セッションログ](https://chatgpt.com/codex/cloud/tasks/task_e_6aa34c1893508327b2c83f674db370e8)。本文に記した参照範囲と採用判断の根拠。
