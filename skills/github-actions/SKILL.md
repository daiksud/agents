---
name: github-actions
description: GitHub Actions workflowの作成・変更、失敗調査、レビュー、効率・安全性改善、Action内部ランタイム更新で使う。変更時はissue-managementとchange-deliveryを併用する。Issue・PR操作だけ、アプリ実装だけ、CI/CDの概念説明だけには使わない。
---

# GitHub Actionsを設計・検証する

開発者が必要な検証を待ち過ぎずに受け取り、信頼できる成果物を届けられるワークフローを扱う。以下のリポジトリ内パスは作業対象リポジトリを指す。

## 依頼と参照資料

最初に、依頼が設計・調査だけか、レビューか、変更まで含むかを確認する。変更でIssue計画・公開許可・実行範囲を扱うときは `issue-management`、承認済み変更をbranch・PR・必須CI・統合後mainの確認まで届けるときは `change-delivery` を併用する。Issue計画だけなら `issue-management` で `change-delivery` や `software-development` が未導入でも保存・再取得・本文と表示・URLの提示で停止できる。

アプリコードの修正では `software-development` のTDDで回帰を再現して修正する。workflow設定のみの修正ではアプリコード用TDDを始めないが、設定の失敗に応じた最小の検証を先に定める。文書作成は `document-authoring`、読み取り専用レビューの進め方と指摘は `code-review` に従う。`issue-management` を利用できなければIssueへ投稿せず、他のSkillで代用せずに未保存案と制約を示す。`change-delivery` を利用できなければworkflowを編集せず、他のSkillで代用せずに未完了の検証・main確認を示す。`software-development` を利用できなければアプリコードを編集せず、再現情報と未完了範囲を示す。該当する依存が未導入なら利用環境で導入方法を確認する。相談・監査だけから編集・Issue投稿・PR作成・実行トリガーへ進まない。

作業に該当する資料だけを読む。複数の分野に関わる場合は組み合わせる。

| 作業・読む条件 | 資料 |
| --- | --- |
| 新規作成、トリガー・ジョブ依存・再利用・配備構成、runner・shellの選定や変更 | [ワークフロー設計](references/workflow-design.md) |
| セキュリティ監査、権限・外部入力・認証・未信頼コード・成果物やキャッシュの信頼境界に関わる変更 | [安全性](references/hardening.md) |
| 遅いCI、重複実行、キャッシュ、スキップ条件、並列化、マトリクス改善 | [効率改善](references/efficiency.md) |
| Actionの版更新、内部ランタイムの非推奨警告、runner互換性 | [ランタイム更新](references/runtime-upgrades.md) |
| 由来・採用理由・版依存の主張の確認 | [出典と適用判断](references/sources.md) |

## 共通の判断

1. `.github/workflows/`、呼び出すローカルAction・再利用ワークフロー・スクリプト、lockファイル、必須チェックと対応環境を調べる。実行履歴・設定にアクセスできなければ、静的に分かることと未確認事項を分ける。
2. 依頼の目的と観測する成功条件を定める。既存の必須検証・対応環境・公開条件を保ち、更新に無関係なジョブ再設計や最適化を混ぜない。
3. 変更のたびに、実効的な `permissions`、Secretの渡し先、実行コードの出所、runner、外部入力、参照するAction・成果物・キャッシュを確認する。トリガー名やforkであることだけで安全と判断しない。境界に触れる場合は安全性資料を読む。
4. 外部Actionと外部再利用ワークフローは、対象リポジトリのリリースと照合した完全コミットSHAへ固定し、コメントの版との一致を確認する。例のSHAを推奨版として流用しない。コンテナ参照には検証済みdigestを使い、同一リポジトリの相対参照は対象checkoutの出所を確認する。
5. 目的を満たす最小の変更と検証を選ぶ。手動承認、特定のブランチ戦略、大規模マトリクス、Canaryを一律に要求しない。
6. runner・shellの選定や変更では[ワークフロー設計のrunnerとshell](references/workflow-design.md#runnerとshell)を読み、対象環境の実在するrunner、provider・repository access、shell互換性と既存契約を確認する。

## 成果と確認

設計・調査なら根拠と提案、レビューなら再現条件・影響を伴う指摘、変更なら差分と検証結果を示す。報告形式は依頼や既存スキルに合わせる。

- YAML構文、Actionsの式・参照・依存関係、必須チェックへの影響を静的に検査する。利用可能な既存lintやactionlintを使い、通常のYAMLパーサーだけでActions仕様まで検証済みとしない。
- ローカルのテストとGitHub上の実行を分ける。承認済みの変更では対象SHA・イベント・runner・run URLを照合し、実行結果だけでなく必要な成果物や配備後の状態を確認する。
- 失敗・キャンセル・未実行・取得不能を成功扱いしない。実行検証できない場合は未確認範囲と確認方法を示す。
- 効果は期待値と実測値を分ける。CI成功を安全性全体や性能改善の証明にしない。
