---
type: Instruction
title: 作業スキルの読み込み
description: 依頼と現在の工程に合う作業スキルを選びます。
---

## 作業スキルの読み込み

プロジェクト固有の指示も確認する。`docs/` は作業対象リポジトリ、`~` はユーザーのホームを指す。

該当するスキルを着手前に読み、詳細はその工程に対応する同梱資料を使う。複数に該当すれば併用する。

| 条件 | 配布先 |
| --- | --- |
| Issueの検索・作成・更新、計画・Sub-issue・後続依頼・共通スタンダード候補の記録 | `~/.agents/skills/issue-management/SKILL.md` |
| リポジトリの変更・成果物作成、PRの作成・更新、変更作業の完了 | `~/.agents/skills/task-workflow/SKILL.md` |
| コードの追加・変更・修正・リファクタリング | `~/.agents/skills/software-development/SKILL.md` |
| 利用者向けのふるまい・受け入れ条件の発見と仕様化 | `~/.agents/skills/behavior-specification/SKILL.md` |
| コードレビューの実行時だけ | `~/.agents/skills/code-review/SKILL.md` |
| 文書の作成・更新 | `~/.agents/skills/okf-docs/SKILL.md` |
| 開発実践の現状診断・導入計画を依頼されたとき | `~/.agents/skills/engineering-assessment/SKILL.md` |
| GitHub Actionsのworkflow設計・変更・失敗調査・レビュー・効率改善 | `~/.agents/skills/github-actions/SKILL.md` |

相談・比較・説明・読み取り調査だけにはIssue・PR・マージを要求しない。ただし、ユーザーが共通スタンダードとなり得るトレードオフを判断した場合は、相談・レビュー中でも候補Issueの記録に `issue-management` を使う。読み取り専用Reviewer/Navigatorは候補をDriverへ引き渡し、自身は投稿しない。読み取り専用のコードレビューは `code-review` を使い、GitHub Actions workflowのレビューでは `github-actions` も併用する。レビューだけの依頼に通常の変更作業として `task-workflow` を加えず、変更・投稿・マージを別途依頼された場合に担当スキルを併用する。調査から変更へ進む前に対応スキルを読む。文書は `okf-docs` に従い、OKF v0.2の通常概念・索引/履歴と固有形式を区別し、出典・未知メタデータ・確認履歴を保持する。
