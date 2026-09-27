---
type: Instruction
title: スキルの作成・更新
description: このリポジトリのスキルを作成・更新するときの形式、内容、評価と配布の確認方法を定めます。
sources:
  - id: agentskills-specification
    resource: https://agentskills.io/specification
  - id: github-copilot-add-skills
    resource: https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills
  - id: github-copilot-cli-reference
    resource: https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference
---

## スキルの作成・更新

このディレクトリ以下のスキルと同梱資料を作成・更新するときに適用する。
このファイルはリポジトリの編集指示であり、個々のスキルが実行時に読む前提にはしない。編集前に[記入の指針](../docs/templates/instructions.md#記入の指針)を読み、条件と行動、必要な理由と例を明確にする。形式と配布の規則は以下を使う。

### 作成前の確認

- 利用者が実現したい状態、スキルを使う場面、期待する成果物と成功条件を明確にする。
- 既存スキルの目的と適用範囲を確認し、新規作成と既存スキルの改善のどちらが必要か判断する。
- 作成・改善の手順には、利用可能な `skill-creator` の `SKILL.md` を読んで適用する。APMの外部依存として導入する方法は[README](../README.md)を参照する。
- 成果物や適用範囲を左右する不明点は、既存の指示と会話を確認したうえでユーザーに確認する。
- Issue計画・公開許可は `issue-management`、承認済み変更・PR・レビュー・main確認は `change-delivery`、文書の形式は `document-authoring`、実行コードの追加・変更は `software-development` に従う。

### 配置と形式

- 原本は `skills/<name>/SKILL.md` に置く。`gh skill` の標準探索を維持するため、隠しディレクトリに移さない。
- `SKILL.md` は Agent Skills仕様[^agentskills-specification]に従い、YAML frontmatterに `name` と `description` を記載する。
- `name` はディレクトリ名と一致させ、小文字英数字とハイフンで1〜64文字とする。先頭・末尾のハイフンと連続するハイフンは使わない。
- `description` は1〜1024文字とし、CopilotがSkillを選ぶ際の判断材料として使う。GitHub公式資料では、Copilotはユーザーのpromptとdescriptionを基に利用を判断し、選んだ後に `SKILL.md` 本文を読み込む。CLIのfrontmatter仕様はdescriptionを「何をするか・いつ使うか」と定義し、1024文字を上限とする[^github-copilot-add-skills] [^github-copilot-cli-reference]。
- descriptionには、担当する内容（What）だけでなく、どのような依頼で使うか（When）を実際のユーザー依頼に近い言葉で書く。似ていて誤選択しやすい対象外（Exclusions）も短く示し、適用判断に必要な条件を本文だけへ置かない。
- 機能一覧や工程説明を詰め込むより、選択判断に役立つ依頼表現と境界を優先する。話題語に触れただけで発火させず、過剰な強調や工程の説明を入れない。
- What / When / Exclusionsをdescriptionで明確にすること、APM経由の配布を維持することはこのリポジトリの運用方針であり、GitHub公式仕様の要件とは区別する。descriptionや一覧の確認はrouting判断の実動作確認とは区別する。
- Copilot CLIでは `copilot skill list --json` で登録Skillとdescriptionを確認できる。対話CLIでは `/skills list` と `/skills info <name>` で一覧と個別情報を確認する[^github-copilot-cli-reference]。
- 既存スキルの更新では、依頼に必要な変更がない限り名前と適用範囲を保持する。
- 本文と説明は日本語を基本とし、コマンド・識別子・固有名詞は元の表記を保つ。
- このAGENTS.mdと同梱する通常概念はOKF v0.2に従う。仕様必須の `type` に加え、自作時の追加条件として `title`・`description` を記載する。`index.md`・`log.md` は予約形式とし、`SKILL.md` のfrontmatterはAgent Skills仕様を用いる。
- Bundleの境界、出典・確認履歴の保持と更新、検証の判断は [document-authoring](document-authoring/SKILL.md) に従う。原本のBundleはリポジトリルートとし、固有形式と通常概念を区別する。

### 内容と同梱資料

- 配布本文には利用先で必要な判断・手順だけを置く。agentsの原本配置・同期・導入検証履歴はローカルAGENTS.mdまたは保守ガイドへ置き、共通本文から管理手順に依存させない。
- 本文には利用先の判断基準、手順、成果物と確認方法を書く。
- 共通指示や他スキルの手順を複製せず、必要な場面と参照先を示す。利用環境にそのスキルがあることを前提にする場合は依存関係を明記する。
- `SKILL.md` は適用境界・重要な判断・完了条件と工程別の参照導線を中心にする。詳細・例・コマンドは読む条件を付けて `references/` 等へ分ける。500行未満だけを簡潔さの証明にせず、通常タスクが無関係な工程まで読まないか確認する。
- 繰り返し実行する処理は `scripts/`、成果物に使うひな形などは `assets/` に置く。必要な資源だけを同梱する。
- 同梱資料は参照元ファイルからの相対リンクで結ぶ。スキル外の資料は導入先に存在する前提にせず、公開URLや明示した依存先を使う。
- 指示中の `docs/` などが作業対象リポジトリを指す場合は、その基準を明記する。原本・配布先・作業対象のパスを混同しない。
- 一時ファイルや実測していない評価結果をスキル本文に残さない。

### 変更内容の確認

- 現時点では、このパッケージ自身のテスト・eval・導入smoke検証を管理対象としない。配布するスキル・共通インストラクションのテスト方針や、スキルが提供する検証機能は維持する。
- 変更した目的・適用範囲・手順と実差分を読み合わせ、参照を分割・移動した場合はリンク元も更新する。配布本文から保守専用の手順へ依存させない。
- 評価資産の追加・再生成を、現時点のこのパッケージの保守作業の完了条件にしない。これは原本リポジトリだけの扱いであり、配布先の開発・評価方針を変更しない。
- スキルの構成や導入方法を変更した場合はREADMEの案内を更新する。確認した範囲・レビュー結果・未確認事項をIssue・PRに記録する。

[^agentskills-specification]: [Agent Skills仕様](https://agentskills.io/specification)。本文に記した参照範囲と採用判断の根拠。
[^github-copilot-add-skills]: [GitHub CopilotのAgent Skills](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills)。promptとdescriptionによる選択、選択後の本文読み込みに関する公式説明。
[^github-copilot-cli-reference]: [GitHub Copilot CLI command reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference)。Skill descriptionの要件・上限とCLIでの一覧・情報確認方法。
