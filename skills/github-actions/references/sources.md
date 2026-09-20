---
type: Reference
title: GitHub Actionsスキルの出典と適用判断
description: 取り込み元の固定版、帰属、確認範囲と統合時に修正した判断を記録します。
sources:
  - id: copilot-cicd
    resource: https://github.com/github/awesome-copilot/blob/4f4796f0bf30e105700f97ed8408c12b6aa95e06/instructions/github-actions-ci-cd-best-practices.instructions.md
  - id: copilot-efficiency
    resource: https://github.com/github/awesome-copilot/tree/4f4796f0bf30e105700f97ed8408c12b6aa95e06/skills/github-actions-efficiency
  - id: copilot-hardening
    resource: https://github.com/github/awesome-copilot/tree/4f4796f0bf30e105700f97ed8408c12b6aa95e06/skills/github-actions-hardening
  - id: copilot-runtime
    resource: https://github.com/github/awesome-copilot/blob/4f4796f0bf30e105700f97ed8408c12b6aa95e06/skills/github-actions-runtime-upgrade-conventions/SKILL.md
  - id: copilot-license
    resource: https://github.com/github/awesome-copilot/blob/4f4796f0bf30e105700f97ed8408c12b6aa95e06/LICENSE
---

## 取り込み元と帰属

2026-09-20にawesome-copilotの以下4資料と関連資料を確認し、日本語で要約・再構成した。固定コミットは `4f4796f0bf30e105700f97ed8408c12b6aa95e06`。確認は資料と公式仕様の照合であり、各サンプルの実ワークフロー実行や人間による承認を示すものではない。

| 原典 | 取り込んだ範囲と配置 |
| --- | --- |
| CI/CD Best Practices[^copilot-cicd] | トリガー、ジョブ、再利用、テスト、成果物、配備・復旧を設計資料へ、安全性と効率の観点を対応資料へ統合 |
| Efficiency[^copilot-efficiency] | SKILL.md、actions.md、reporting.md、patterns.md、review-rubric.mdの測定・候補選択・検証を効率資料へ統合 |
| Hardening[^copilot-hardening] | SKILL.mdと同梱referencesの入力・トリガー・権限・実行経路の点検を安全性資料へ統合 |
| Runtime Upgrade Conventions[^copilot-runtime] | 警告の調査、互換性、SHA固定、小さい更新、成果物検証を更新資料へ統合 |

原典はMIT License、Copyright GitHub, Inc.。著作権表示・許諾・免責の全文を [LICENSE.txt](../LICENSE.txt) に保持する。[^copilot-license]

## 採用・修正・不採用

| 論点 | 統合した判断 |
| --- | --- |
| 4資料の重複 | 入口と共通の安全・検証条件を1スキルにまとめ、詳細は作業別に読む |
| 作業の境界 | 原典hardeningの編集禁止は監査・レビューだけに適用。修正依頼は既存task-workflowへ接続する。独自の重要度・報告形式・Issue手順を増やさない |
| 権限 | 「tokenは既定で常にwrite」「イベント名だけで全Secretへアクセス」「fork PRは無条件に安全」を採用しない。実効権限・渡すSecret・実行元・runnerを確認する |
| 未信頼出力 | 非特権buildのartifactをtrustedと呼ばない。特権のworkflow_runへ渡しても未信頼として検証し、コードとして実行しない |
| Actionの固定 | 完全SHAとリリース・コメントの一致を採用。原典の可変タグ例やSHAと版コメントが一致しない例は転記しない |
| 設計 | develop/releaseブランチ、手動承認、Canary、特定サービスや全検査ツールの導入を一律に要求しない |
| 効率 | 少数の根拠ある改善と実測の区別を採用。固定3件や待ち時間1.25倍を成功基準にしない |
| マトリクス | 未文書化の対応環境を削除せず、契約・実際の利用を確認する |
| スキップとキャンセル | pathフィルターで必須チェックを壊さず、全workflowへのcancelを要求しない。pending置換とqueueの対象環境での仕様を確認する |
| キャッシュ | 毎回変わるrun IDのキーやnode_modules保存を定番にしない。互換性・保存費用・信頼境界を確認する |
| 更新と検証 | Action内部とアプリ用ランタイムを区別する。ローカル成功をActionの実実行成功の代用にしない |

この表は本スキルへの適用判断であり、原典全体の採用を意味しない。

## 公式仕様の確認と見直し条件

2026-09-20にGitHub公式のworkflow syntax、reusable workflows、cache、secure use、events、workflow commands、OIDC、Action metadata、およびcheckout・setup-nodeの現行資料と照合した。主張とURLは各参照資料の `sources` と脚注へ結んでいる。仕様の転記を増やさず、版に依存する判断を行う時点で対象環境に対応する正本を読み直す。

- フィルター、必須チェック、concurrencyを変えるときは[効率改善](efficiency.md)の公式仕様を確認する。`queue: max` の利用可否や制約を旧環境にも適用できるとは仮定しない。
- 権限、fork、runner、OIDCを変えるときは[安全性](hardening.md)の公式仕様と実際の設定・claimsを確認する。subject形式やcredential保存場所を固定の前提にしない。
- Action更新時は[ランタイム更新](runtime-upgrades.md)に従い、そのリリースのmetadata・release notes・完全SHAを照合する。確認日だけを最新版・互換性の証明にしない。

[^copilot-cicd]: GitHub awesome-copilotのCI/CD Best Practices Instructions、上記固定版。
[^copilot-efficiency]: GitHub Actions Efficiencyと同梱4資料、上記固定版。
[^copilot-hardening]: GitHub Actions Hardeningと同梱参照資料、上記固定版。
[^copilot-runtime]: GitHub Actions Runtime Upgrade Conventions、上記固定版。
[^copilot-license]: GitHub awesome-copilotのMIT License、上記固定版。
