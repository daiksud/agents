---
type: Instruction
title: 無料セキュリティ機能の診断と有効化
description: 対象リポジトリで無料かつ適用可能な機能を棚卸しし、前提条件と費用を確認して実現します。
sources:
  - id: security-features
    resource: https://docs.github.com/en/code-security/getting-started/github-security-features
  - id: advanced-security
    resource: https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security
  - id: repository-api
    resource: https://docs.github.com/en/rest/repos/repos
  - id: code-scanning-api
    resource: https://docs.github.com/en/rest/code-scanning/code-scanning
---

## 無料範囲を機能ごとに決める

期待値は「対象リポジトリで無料かつ適用可能なセキュリティ機能がすべて有効」である。標準の無料機能とGitHub Code Security・GitHub Secret Protectionの無料対象を調べ、`advanced_security` の一括有効化で代用しない。publicで無料の機能をprivateにも無料と仮定せず、所有者・契約・対象言語・依存エコシステム・上位ポリシーを確認する。[^security-features][^advanced-security]

公式一覧と対象UIを実行時に照合し、下表を出発点に追加機能も棚卸しする。各機能の提供形態を「設定で有効化可能・既定で有効・workflow等の準備が必要・適用外・無料範囲外・未確認」に分け、[共通の判定](operations.md)へ反映する。既定で有効でも対象の状態が取得不能なら適合と断定しない。有効化スイッチがない機能に架空のAPIやworkflowを作らない。[^security-features]

| 棚卸し対象 | 取得・適用・再確認 |
| --- | --- |
| Dependency graph | 対象のsecurity設定とdependency graphで状態・対応manifestを確認し、設定可能なら有効化後に再確認する。依存が0件であることと無効を区別する |
| Dependabot alerts | `GET /repos/{owner}/{repo}/vulnerability-alerts` または対象UIで確認し、適用は同endpointへの `PUT`。権限・対象の存在を確認してHTTP結果を解釈し、再取得する |
| Dependabot security updates | `GET /repos/{owner}/{repo}/automated-security-fixes` の `enabled`・`paused` と対応依存を確認し、適用は同endpointへの `PUT`。有効だがpausedなら実行可能と断定せず原因と残件を示す |
| Secret scanning / repository-level push protection | repositoryの `security_and_analysis.secret_scanning`・`secret_scanning_push_protection` または対象UIを確認。無料条件と依存するsecret scanningを確認し、必要なフィールドだけを `PATCH /repos/{owner}/{repo}` で有効化して再取得する |
| Code scanning / CodeQL | `GET /repos/{owner}/{repo}/code-scanning/default-setup`、既存workflow、解析状態からdefault/advanced setupと対象言語を確認。default setupが適切な場合だけ同endpointへの `PATCH` で `state=configured` とするかUIで設定し、構成と実際の解析結果を確認する |
| Copilot Autofix / AIによるコード検出 | 対象の提供条件・設定・既存スキャンとの依存を確認し、無料かつ設定可能なら有効化後に再確認する。ライセンスやスキャン結果だけから有効化済みと推測しない |
| Dependency review | 提供条件とPRの依存差分表示を確認する。有効化スイッチがなければ提供状態を記録する。dependency-review-actionによるマージ阻止は別のworkflow変更・方針として扱う |
| Secret scanningの追加機能 | non-provider patterns、validity checks、AIによるsecret検出、custom patterns、delegated bypass等について対象UIと公式提供条件を確認する。無料性・設定可否・必要な運用判断を記録し、利用できる項目を落とさない |
| その他の無料機能 | private vulnerability reporting、dependency submission、artifact attestations等も公式一覧と対象の提供機能に照らす。リポジトリ設定、既定機能、ファイル変更、アカウント/Organizationの機能を区別する |

標準機能・製品境界は公式一覧、HTTP操作と応答・権限は各API仕様を根拠にする。表だけで無料性や実効性が証明されたとは扱わない。[^security-features][^advanced-security][^repository-api][^code-scanning-api]

## 有効化の前提と順序

- 機能ライセンスの無料性と、Actions・runner・ストレージ等の実行費用を分ける。課金や試用を開始せず、追加費用が未確認なら該当変更を保留する。既存の有料機能を「無料範囲外」という理由で無効化しない。
- Dependency graphやsecret scanning等の前提を先に満たし、機能ごとに取得・差分適用・再取得する。設定APIは原子的な一括適用と仮定しない。security updatesから作られるPRは勝手にマージしない。
- CodeQLの既存advanced setupをdefault setupで置き換えない。対応言語・build方式・利用できる実行環境を確認し、必要なworkflow変更は `github-actions` と `change-delivery` へ渡す。対応言語がない場合はダミーコードを追加せず理由付き適用外とする。設定済みと解析成功、アラート0件を区別する。[^code-scanning-api]
- アカウント単位のpush protectionだけではリポジトリ単位の設定を証明できない。アカウント・Organization全体の変更は行わず、必要なら範囲外の依存として記録する。[^security-features]
- 追加機能で例外承認者、custom pattern、外部への情報送信等の未合意な判断が必要なら具体案を示し、回答に依存しない無料機能の適用は続ける。判断が必要な機能を無言で一覧から除外しない。
- SECURITY.mdの連絡先や受付体制を捏造しない。SBOM表示・Advisory Database等の利用機能に空の設定を作らない。Dependabot version updatesの頻度、アラートの自動dismiss、全スキャンのマージ必須化は初期基準に自動追加しない。

## 完了の確認

取得できた設定、必要な解析・workflowの結果、既定提供の根拠を機能ごとに示す。追加スキャン・テスト用secretのpush・疑似脆弱性の追加を、読み取り診断の一部として実行しない。失敗や取得不能な設定を、既存アラートの有無から推定しない。

設定確認に `security_and_analysis` を使うには適切な権限が必要で、欠落やnullは無効の証拠にならない。アラート本文・secret値・非公開依存情報は公開Issueやログへ転載せず、対象・機能名・状態・権限付きの参照先だけを必要な範囲で記録する。[^repository-api]

[^security-features]: 標準無料機能と製品機能の一覧。実行時に追加・変更を確認する。
[^advanced-security]: Code Security・Secret Protectionの製品境界と可用性。
[^repository-api]: security_and_analysis、Dependabot設定等の取得・適用条件。
[^code-scanning-api]: default setupの取得・更新とコードスキャンの実行結果。
