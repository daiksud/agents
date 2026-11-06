---
name: github-actions
description: GitHub Actionsをワークフロー・ジョブ・アクション・ステップの4レイヤーで設計・整理するときに使う。PR、mainへのpush、手動リリースと成果物再利用の方針を定める。
---

# GitHub Actionsの設計ポリシー

## 構成の基本

| レイヤー | 例 | 責務 |
| --- | --- | --- |
| ワークフロー | `pr.yml`、`push-main.yml`、`release.yml` | イベント、入力、ジョブの構成 |
| ジョブ | `screening`、`inspection`、`delivery` | ランナー、権限、依存関係、マトリクス、環境、実行条件、タイムアウト |
| アクション | `.github/actions/screening/action.yml` など | フェーズの共通処理と入出力 |
| ステップ | `build`、`lint`、`test` など | `run` によるコマンド実行、`uses` によるアクション呼び出し |

ジョブ内のステップからフェーズのComposite Actionを呼び、その内部に基本操作のステップを置く。ジョブは実行条件、アクションは処理内容を持つ。OS・権限・並列実行・承認条件が異なる処理はジョブを分ける。

## フェーズとイベント

| ワークフロー | トリガー | ジョブ |
| --- | --- | --- |
| `pr.yml` | `pull_request` | `screening` |
| `push-main.yml` | `push`、`branches: [main]` | `screening` → `inspection` |
| `release.yml` | `workflow_dispatch` | 再利用判定 → `screening`・`inspection`（再利用時は省略）→ `delivery` |

- `screening`: lint、単体テスト、型検査、ビルドなど、プロジェクトに必要な基本検証と候補成果物の生成。
- `inspection`: 候補成果物に対する統合・受け入れ・動作確認。
- `delivery`: 検証済み成果物の公開・配備。
- `prlint`、`settings-pr`、`settings-apply`、`labeler`、`codex-review` は、目的と権限に応じた別ワークフローにする。

## 再利用の単位

- 共通フェーズの処理は一つのComposite Actionにまとめる。各ワークフローには呼び出しを置く。
- 一つのコマンドだけの処理はステップに直接書く。ビルド、lint、テスト、パッケージングは別ステップにする。
- アクションの入力は必要な値に絞る。イベントの判別や多数のスキップフラグで処理を切り替えない。
- 複数ジョブの構成自体を共有する場合は `workflow_call` を使う。

## 技術的な詳細

- [ワークフロー設計](references/workflow-design.md): 入出力、実行環境、成果物の受け渡し・再利用、公開条件、必須チェック。
- [安全性](references/hardening.md): 権限、信頼境界、外部入力、依存アクションの固定。
- [効率化](references/efficiency.md): キャッシュ、並列化、マトリクス、同時実行、重複実行の抑制。
- [ランタイム更新](references/runtime-upgrades.md): アクション内部のランタイム、プロジェクトの実行環境、ランナーの互換性。
