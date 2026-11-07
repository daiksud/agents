---
name: continuous-delivery
description: GitHubで継続的デリバリーを実践するために、Actionsの設定、ワークフロー、アクション、ツールを整備するときに使う。PR検証、mainへのpush、手動リリース、検証済み成果物の再利用を設計・改善する。
---

# GitHubで継続的デリバリーを実践する

変更を継続的に検証し、検証済みの成果物を必要なタイミングでリリースできる状態にする。ワークフローとアクション、対応するGitHubの設定、実行に必要なツールを整える。

## 構成の基本

| レイヤー | 例 | 責務 |
| --- | --- | --- |
| ワークフロー | `pr.yml`、`push.yml`、`release.yml` | イベント、入力、ジョブの構成 |
| ジョブ | `screening`、`inspection`、`delivery` | ランナー、権限、依存関係、マトリクス、環境、実行条件、タイムアウト |
| アクション | `.github/actions/screening/action.yml` など | フェーズの共通処理と入出力 |
| ステップ | `build`、`lint`、`test` など | `run` によるコマンド実行、`uses` によるアクション呼び出し |

ジョブ内のステップからフェーズのComposite Actionを呼び、その内部に基本操作のステップを置く。ジョブは実行条件、アクションは処理内容を持つ。OS・権限・並列実行・承認条件が異なる処理はジョブを分ける。

## 基本ワークフローとフェーズ

| ワークフロー | トリガー | ジョブ |
| --- | --- | --- |
| `pr.yml` | `pull_request` | `screening` |
| `push.yml` | `push`、`branches: [main]` | `screening` → `inspection` |
| `release.yml` | `workflow_dispatch` | 再利用判定 → `screening`・`inspection`（再利用時は省略）→ `delivery` |

- `screening`: lint、単体テスト、型検査、ビルドなど、プロジェクトに必要な基本検証と候補成果物の生成。
- `inspection`: 候補成果物に対する統合・受け入れ・動作確認。
- `delivery`: 検証済み成果物の公開・配備。
- `prlint`、`settings-pr`、`settings-apply`、`labeler`、`codex-review` などの補助ワークフローは目的と権限に応じて必要なものを用意する。

`push.yml` で検証済み成果物を保存し、`release.yml` で再利用する。再利用できない場合の生成・検証と停止条件は[ワークフロー設計](references/workflow-design.md)に従う。手動でリリースを開始し、開始後の検証・公開を自動化する。

## 再利用の単位

- 共通フェーズの処理は一つのComposite Actionにまとめる。各ワークフローには呼び出しを置く。
- 一つのコマンドだけの処理はステップに直接書く。ビルド、lint、テスト、パッケージングは別ステップにする。
- アクションの入力は必要な値に絞る。イベントの判別や多数のスキップフラグで処理を切り替えない。
- 複数ジョブの構成自体を共有する場合は `workflow_call` を使う。

## 設定と実装の詳細

- [ワークフロー設計](references/workflow-design.md): 入出力、実行環境、成果物の受け渡し・再利用、公開条件、必須チェック。
- [安全性と設定](references/hardening.md): Actionsの実行許可、権限、配備先の環境、信頼境界、外部入力、依存先の固定。
- [効率化](references/efficiency.md): キャッシュ、並列化、マトリクス、同時実行、重複実行の抑制。
- [ツールと実行環境](references/tooling.md): 検査・更新・公開ツールの選定、バージョン固定、ランタイムとランナーの互換性。
