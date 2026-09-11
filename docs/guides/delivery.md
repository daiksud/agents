---
type: Guide
title: 検証済みのスキルと共通指示を届ける
description: 同じ候補SHAの導入・更新・復旧を検証し、証跡から利用可能な版を選ぶ手順を説明します。
---

## 検証済みのスキルと共通指示を届ける

利用者が必要なときに導入できる状態を保つため、原本のGitコミットを配布候補として扱います。バイナリを再ビルドする製品ではないため、後段でも同じSHAのMarkdown・設定・同梱ファイルを検証します。[構成管理](https://continuousdelivery.com/foundations/configuration-management/)と[デプロイメントパイプライン](https://continuousdelivery.com/implementing/patterns/)に基づく構成です。

### 検証と証跡

| 工程 | 確認内容 |
| --- | --- |
| static-checks | 原本・リンク・形式と単体テスト。ローカルでも同じコマンドを実行 |
| acceptance（Ubuntu・macOS） | gh skillの隔離導入後、APMで候補SHAの新規導入・再導入、正常SHAから候補SHAへの更新、正常SHAへの復旧を実行 |
| 共通指示 | Codex・Copilot両方の生成本文、手書きAGENTS.mdの保護、再生成結果を確認 |
| 内容照合 | インストール済みパッケージのSHA、原本と配布内容、APMが書き換えたリンクの参照先を確認 |
| 証跡 | Actions artifactのdelivery-report.jsonとapm-delivery.logに候補・正常SHA、依存SHA、ツール版、OS、ファイルハッシュと所要時間を保存 |

PRではGitHubが作る統合候補SHAを一時Gitミラーから供給し、mainへのpushではマージ後SHAを公開GitHubの `daiksud/agents#<SHA>` 経路で導入します。APM 0.30.0が一時マージコミットを通常cloneで取得できないため、PRだけAPM子プロセスのGit URL解決をミラーへ向けます。ミラーのHEAD・内容はチェックアウト済み候補と同じで、元リポジトリやグローバルGit設定を書き換えません。可変のmainを後段で再取得して別の候補に置き換えません。`apm.yml` の外部skill-creator依存は完全SHAに固定し、[検証設定](../../.github/delivery.json)と合わせてPRで更新します。初回成功後に[必須チェック](../../.github/required-checks.json)を既存保護ルールへ反映します。

> [!IMPORTANT]
> APM検証は使い捨てのGitHub-hosted runnerだけで実行します。既存のAPM導入先・配布スキル・AGENTS.mdがあれば停止します。ローカルやself-hosted runnerで実ユーザーのグローバル配布先を検証用に変更しません。

Actionsの手動実行では対象ブランチを選択できます。失敗時もログと途中の証跡をartifactで確認し、実行されなかった工程を成功とは扱いません。探索的なスキル内容の確認は[READMEの隔離環境手順](../../README.md#ローカルとciで同じ検査を実行)で行い、指示の判断品質は読み取り専用模擬評価で別に確認します。

APM 0.30.0では、未固定依存を持つ旧版から更新すると、変更後の依存固定が `update` だけでは反映されないケースを実検証で検出しました。READMEの更新手順では `apm update --global` の後に `apm install --global` を実行して宣言された依存を再適用し、新規導入時と同じ内容になることを確認します。

### 導入する版を選ぶ

1. mainの対象コミットで両OSの受け入れ検証が成功していることをActionsで確認します。
2. artifactのcandidate、各phaseのsha、依存SHA、ハッシュと成功状態を確認します。チェック成功だけで公開後の判断品質まで保証しません。
3. 同じ候補を導入する場合は、READMEのAPM導入コマンドのパッケージ指定を `daiksud/agents#<確認した完全SHA>` にします。導入後にdry-run、compileと生成結果を確認します。

APM 0.30.0・GitHub CLI 2.100.0と固定Python依存を使用します。runnerのOSイメージとPython 3.12のパッチ版は更新されるため、実際の環境・版を証跡で追跡します。検証済みSHAを保持し、依存更新も同じパイプラインを通します。

### 不具合から復旧する

mainを正常な状態へ戻す変更は、原因変更のrevertなど最小のPRにします。通常の計画承認・レビュー・必須チェックを維持し、失敗した検証の無効化で復旧を代用しません。

すでに導入した利用者は、過去の成功した証跡で確認した正常SHAを指定し直して再生成できます。

```bash
known_good_sha='<証跡で確認した正常な完全SHA>'
apm install --global --target codex,copilot "daiksud/agents#$known_good_sha"
apm compile --global --dry-run
apm compile --global
```

既存設定と手書き指示を先に保持し、復旧後の本文・スキル・依存を証跡と照合します。検証では設定中のbaseline_shaへ実際に戻し、更新前後の配布ハッシュ一致と復旧時間を確認します。正常SHAの更新も、実測済みの成功したコミットを選んでPRに記録します。高速検証5分・受け入れ10分・復旧10分は初期目標です。長時間化や失敗では原因を調べ、未達を達成済みとしません。

自動リリースと実ユーザー環境への自動配布は行いません。artifactの保存期限後も再検証できるよう、コミット・依存固定・検査コマンドを版管理します。
