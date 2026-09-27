---
type: Specification
title: 作業に必要なSkillだけを選ぶ
description: descriptionと現在の工程からSkillを選び、無関係なSkillやreferenceを一括読込しないrouting境界を定めます。
sources:
  - id: issue-123
    resource: https://github.com/daiksud/agents/issues/123
---

## 機能: 依頼と現在の工程に必要なSkillだけを使う

利用者は、複数モデルから同じSkillsを使うとき、話題語ではなく依頼の作業と現在の工程に基づいて必要なSkillだけを選びたい。[^issue-123]

### ルール: descriptionを最初の選択境界にする

#### シナリオ: Issue計画だけを作る

- 前提: ユーザーはGitHub Issueに計画を保存・確認することだけを依頼している
- もし: 使用するSkillを選ぶ
- ならば: `issue-management` を選ぶ
- かつ: 実装・PR・mergeを依頼されていないため `software-development` と `change-delivery` を開始しない

#### シナリオ: 合意済みの小さなコード変更を実装する

- 前提: 既存の受け入れ条件を変えないコード修正が承認されている
- もし: 実装工程へ進む
- ならば: コードの実装と検証に `software-development` を使う
- かつ: リポジトリ変更のdeliveryには `change-delivery`、保存済みIssue計画の確認には `issue-management` を必要な工程で併用する
- かつ: 新しい外部契約を発見しない限り `behavior-specification` を追加しない

#### シナリオ: 実装済み変更をmainまで届ける

- 前提: 実装と対象テストは完了し、PR以降のdeliveryが残っている
- もし: PR・通常レビュー・CI・merge・main確認を進める
- ならば: `change-delivery` を使う
- かつ: 新しいコード変更が不要なら `software-development` を再度読み込むことを必須にしない

#### シナリオ: コード差分だけをレビューする

- 前提: 読み取り専用のコードレビューだけが依頼されている
- もし: 差分を評価する
- ならば: `code-review` を使う
- かつ: 修正・PR操作・mergeが依頼されていないため `change-delivery` を追加しない

#### シナリオ: GitHub Actions workflowをレビューする

- 前提: `.github/workflows` の読み取り専用レビューが依頼されている
- もし: workflowの契約と差分を評価する
- ならば: Actions固有の判断に `github-actions`、レビュー手順に `code-review` を使う
- かつ: 編集やPR操作がないため `software-development` と `change-delivery` を追加しない

#### シナリオ: 受け入れ条件だけを整理する

- 前提: 利用者向けのふるまいと具体例を整理するが、文書保存やコード変更は依頼されていない
- もし: 仕様を整理する
- ならば: `behavior-specification` を使う
- かつ: `document-authoring`、`software-development`、`change-delivery` を開始しない

#### シナリオ: 文書だけを作成する

- 前提: MarkdownやADRの本文作成だけが依頼され、リポジトリへの保存は依頼されていない
- もし: 文書を作成する
- ならば: `document-authoring` を使う
- かつ: `software-development` と `change-delivery` を開始しない

#### シナリオ: 開発実践を診断する

- 前提: 現状の開発プロセスを証拠から診断し改善計画をIssueへ記録する依頼である
- もし: 診断と計画を作る
- ならば: `engineering-assessment` と計画記録の `issue-management` を使う
- かつ: 導入実装が依頼されていないため `software-development` と `change-delivery` を開始しない

### ルール: 選んだSkillでも必要なreferenceだけを読む

#### シナリオ: GitHub Actionsのrunnerだけを判断する

- 前提: runnerとshellの選定が現在の論点で、キャッシュやAction runtime更新は対象外である
- もし: `github-actions` を使う
- ならば: runnerとshellを扱う `workflow-design.md` と必要な出典だけを読む
- かつ: 無関係な `efficiency.md` や `runtime-upgrades.md` を一括して読むことを要求しない

#### シナリオ: NavigatorがGreenだけをレビューする

- 前提: Driver / NavigatorのGreen段階の確認だけが現在の工程である
- もし: `code-review` を使う
- ならば: `pair-review.md` のGreenに必要な観点を使う
- かつ: 11領域を毎回全面点検することを要求しない

[^issue-123]: [Issue #123](https://github.com/daiksud/agents/issues/123) に記録された、Skill routingとProgressive Disclosureの整理方針。
