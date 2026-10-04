---
type: Instruction
title: 作業スキルの読み込み
description: 依頼と現在の工程に合う作業スキルを選びます。
---

## 作業スキルの読み込み

プロジェクト固有の指示も確認する。`docs/` は作業対象リポジトリ、`~` はユーザーのホームを指す。

依頼と現在の工程に直接該当するスキルだけを着手前に読み、詳細はその工程に対応する同梱資料を使う。descriptionは最初の選択境界として扱い、話題語が出ただけで関連Skillを一括して読み込まない。複数Skillが実際に担当する工程を持つ場合だけ併用する。

Skillの選択と作業の終了条件を分ける。扱う話題や選択したSkillではなく、回答、診断結果、Issue記録、文書成果物、実装など、ユーザーが依頼した終端成果物を完了した時点を終了点とする。終端成果物へ到達するために既存ワークフローが要求するIssue・PR・検証記録などの補助成果物は手段として作成できるが、それ自体をユーザーが依頼した成果物や新しい終了点に読み替えない。依頼された終端成果物を超える次工程は暗黙に開始しない。

スキルを使った作業の終了時は、成果・検証・未完了範囲の報告に短いKPTを添える。Keepは実際に役立った実践と根拠、Problemは観測した摩擦・失敗と具体的な証拠、TryはそのProblemを解消する小さな実験と、次の関連作業で改善を確かめる方法を示す。確認できない問題を見出しのために作らず、未観測ならその旨を短く述べる。単発の経験を無条件に共通規則へ広げない。

KPTは現在の成果物の完了と後続のスキル改善を分ける。改善を `daiksud/agents` へ反映するときは `issue-management` の[改善の記録と次回確認](../../skills/issue-management/references/issue-recording.md#改善の記録と次回確認)に従い、実行範囲・公開許可と通常のレビュー・CIを保持する。次の関連作業の着手時に採用済みTryの記録と確認方法を読み、終了時に実際の結果から継続・修正・終了を判断する。ふりかえりのための専用会議・定期実行や、改善作業をさらに改善し続ける再帰的な変更を開始しない。

| 条件 | 配布先 |
| --- | --- |
| Issueの検索・作成・更新、計画・Sub-issue・後続依頼・共通スタンダード候補の記録 | `~/.agents/skills/issue-management/SKILL.md` |
| Git管理ファイルの変更・成果物作成、PRの作成・更新、統合後確認 | `~/.agents/skills/change-delivery/SKILL.md` |
| コードの追加・変更・修正・リファクタリング | `~/.agents/skills/software-development/SKILL.md` |
| 利用者向けのふるまい・受け入れ条件の発見と仕様化 | `~/.agents/skills/behavior-specification/SKILL.md` |
| コードレビューの実行時だけ | `~/.agents/skills/code-review/SKILL.md` |
| 文書の作成・更新 | `~/.agents/skills/document-authoring/SKILL.md` |
| 開発実践の現状診断・導入計画を依頼されたとき | `~/.agents/skills/engineering-assessment/SKILL.md` |
| GitHubリポジトリ設定の診断・整備・適用、Ruleset・マージ方式・リリース保護・セキュリティ設定 | `~/.agents/skills/github-repo/SKILL.md` |
| GitHub Actionsのworkflow設計・変更・失敗調査・レビュー・効率改善 | `~/.agents/skills/github-actions/SKILL.md` |

相談・比較・説明・読み取り調査だけにはIssue・PR・マージを要求しない。ただし、ユーザーが共通スタンダードとなり得るトレードオフを判断した場合は、相談・レビュー中でも候補Issueの記録に `issue-management` を使う。読み取り専用Reviewer/Navigatorは候補をDriverへ引き渡し、自身は投稿しない。読み取り専用のコードレビューは `code-review` を使い、GitHub Actions workflowのレビューでは `github-actions` も併用する。レビューだけの依頼に通常の変更作業として `change-delivery` を加えず、変更・投稿・マージを別途依頼された場合に担当スキルを併用する。調査から変更へ進む前に対応スキルを読む。文書は `document-authoring` に従い、OKF v0.2の通常概念・索引/履歴と固有形式を区別し、出典・未知メタデータ・確認履歴を保持する。

GitHub側のリポジトリ設定のみを適用する場合は `github-repo` を使い、計画記録・承認確認後の差分適用と再診断まで進める。Git管理ファイルの変更がなければ `change-delivery` や空のcommit・PRを要求しない。前提となるworkflow等の変更がある場合は、そのファイル変更に通常のdeliveryを適用する。
