---
type: Instruction
title: GitHub Actionsの効率改善
description: 実行履歴から待ち時間と使用量の原因を選び、必要な検証と信頼境界を保って改善します。
sources:
  - id: copilot-efficiency
    resource: https://github.com/github/awesome-copilot/tree/4f4796f0bf30e105700f97ed8408c12b6aa95e06/skills/github-actions-efficiency
  - id: github-syntax
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
  - id: github-cache
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/dependency-caching
---

## 原因を測って少数の改善を選ぶ

ワークフロー、必須チェック、対応環境の文書、run/job/stepの履歴を確認する。新規なら[設計](workflow-design.md)で基準となる検証を定める。既存ならキャッシュ、重複トリガー、不要な実行、長い依存経路を調べ、根拠があり目的に効く少数の変更を選ぶ。設定がないだけでは無駄と断定しない。[^copilot-efficiency]

作業対象リポジトリで使う読み取り例:

```bash
gh run list --limit 20 --json databaseId,workflowName,event,headSha,status,conclusion,createdAt,updatedAt,url
gh run view RUN_ID --json jobs,event,headSha,conclusion,url
gh run view RUN_ID --log-failed
```

`RUN_ID` は対象の実在するIDに置き換える。取得できない場合は提供ファイルに基づく静的分析として扱う。

### 効果を分ける

| 観測する値 | 判断すること |
| --- | --- |
| PRで必要な結果が揃うまでの経過時間 | 待ち行列、直列の依存、長いジョブが利用者を待たせていないか |
| 各ジョブの実行時間の合計 | ランナー総使用時間が減るか。OS・課金条件を確認せず料金へ換算しない |
| 回避したrun・job・matrixの実行数 | 必要な検証を保ったまま処理を省けたか |

変更前後でイベント・変更内容・runner・マトリクス・キャッシュ状態・サンプル期間を揃え、交絡要因を残す。期待効果と実測を分け、データがない値をゼロや改善済みにしない。

### 変更ごとの確認

- **キャッシュ**: ダウンロード・保存・展開の費用とヒット率を調べる。lockfile、OS、アーキテクチャ、ツール版など互換性に関わる値をキーへ含め、部分一致の復元後も依存を検証する。setup Actionの組み込みキャッシュと二重化しない。Secretや認証済み設定を保存せず、作成元・読み手の信頼境界は[安全性](hardening.md)で確認する。PRからbase/default branchのキャッシュを読める場合がある。[^github-cache]
- **重複実行**: 同じ変更のpush/PR実行を比較する。ブランチ保護、release、schema、migration、共有ライブラリの必要な検証を失わない。
- **path判定**: workflow全体をスキップすると必須チェックがPendingになる場合がある。ジョブ判定・集約へ移しても、必要な検証の失敗が最終結果へ届くようにする。依存、lockfile、設定、workflow自身の変更を含め、変更ファイル取得の比較元・上限・取得失敗時の動作を点検する。workflow変更で全検査が走ることを、それだけで無駄とはしない。[^github-syntax]
- **同時実行**: 古いPR検証を中止できるか確認し、groupにworkflowとPR/ref等の識別を含める。本番配備の途中キャンセルを一律に有効化しない。`cancel-in-progress: false` でも既定のpending枠は置換されるため、全配備を保持する要件は別途キュー仕様を確認する。利用先が対応するなら `queue: max` を検討するが、上限と `cancel-in-progress: true` との非互換性を確認する。
- **マトリクス**: 各組み合わせが保証する契約を調べる。対応要件が未文書化という理由だけで削らず、利用者・依存・既存履歴から確認する。削減する場合は残る保証と失う保証を明示する。
- **並列化とジョブ統合**: クリティカルパス、起動・セットアップ費用、成果物の受け渡しを比較する。並列化で経過時間が短くても総使用時間が増えることがある。許容する待ち時間と費用の判断を固定倍率で代用しない。
- **書き戻しジョブ**: 自動整形等の公開条件と権限を確認する。ラベル・手動操作等へ変える場合はイベント再評価も検証し、既存の合意を無断で変えない。

### 挙動と効果の検証

承認済みの変更では、安全な既存の作業ブランチ上で関連変更・無関係な変更・workflow変更、連続更新時のキャンセルを確かめる。新規ブランチの最初のpushだけでpath判定を検証済みとしない。監査依頼だけならテストpushやdispatchをせず、検証案を示す。

キャッシュのcold/warm両方と必要なチェック・成果物を確認する。予想外のスキップや実行は、YAMLが妥当に見えても不具合として追う。改善内容、保持した保証、検証したrun、実測と未確認を報告する。

[^copilot-efficiency]: SKILL.mdとactions・reporting・patterns・review-rubricの測定・選択・検証観点を再構成。
[^github-cache]: Dependency caching reference。復元の互換性とブランチ間のアクセス範囲を確認する。
[^github-syntax]: Workflow syntax。フィルター、concurrencyとqueueの対象環境での仕様を確認する。
