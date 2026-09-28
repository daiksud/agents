---
type: Instruction
title: GitHubリポジトリの設定基準
description: リリース・マージ・main保護・Actionsポリシーの期待値と診断方法を定めます。
sources:
  - id: personal-policy
    resource: https://github.com/daiksud/agents/issues/152
  - id: release-setting
    resource: https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/establish-provenance-and-integrity/prevent-release-changes
  - id: immutable-release
    resource: https://docs.github.com/en/code-security/concepts/supply-chain-security/immutable-releases
  - id: repository-api
    resource: https://docs.github.com/en/rest/repos/repos
  - id: ruleset-rules
    resource: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets
  - id: rules-api
    resource: https://docs.github.com/en/rest/repos/rules
  - id: actions-settings
    resource: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository
  - id: actions-permissions-api
    resource: https://docs.github.com/en/rest/actions/permissions
---

## 基準の適用

次の期待値は個人の採用方針であり、GitHub全利用者に対する必須仕様ではない。診断は期待値と観測値を分け、書き込みは[操作と判定](operations.md)に従う。無料セキュリティ機能は[別資料](security.md)で機能単位に診断する。[^personal-policy]

## イミュータブルリリース

期待値はリポジトリのrelease immutabilityが有効であること。リリース未作成でも設定を調べる。公式UIの `Settings` → `General` の `Releases` → `Enable release immutability` で現在値を確認し、承認済みなら有効化後に再表示して確認する。APIを使う場合は実行時の公式仕様で設定取得・更新のサポートを確認し、架空のendpointやフィールドを作らない。[^release-setting]

適用されるのは今後のリリースであり、既存リリースの非遡及性を報告する。公開後のタグ・アセット更新を前提とする運用を調べ、必要ならdraft作成・全アセット添付・公開の順へ先に変更する。設定の検証名目でリリースを勝手に公開しない。承認済みの次回公開がある場合だけ、そのreleaseのimmutable表示も確認する。[^release-setting][^immutable-release]

タグ・アセットを削除・再作成して移行せず、設定を戻すことと既に公開したimmutable releaseの制約を取り消すことを混同しない。リリース本文やタイトルの編集まで禁止されたとは説明しない。[^immutable-release]

## SquashのみのPRマージ

`GET /repos/{owner}/{repo}` または `Settings` → `General` の `Pull Requests` で、次の3値を確認する。[^repository-api]

| 設定 | 期待値 |
| --- | --- |
| `allow_squash_merge` | `true` |
| `allow_merge_commit` | `false` |
| `allow_rebase_merge` | `false` |

承認済みなら同じrepository endpointの `PATCH` で差分の3値だけを送るか、対応するUIを変更し、再取得して全3値を確認する。返却されない値を既定値で補完しない。Rulesetやmerge queue等との整合を先に確認し、既存制約と両立しなければ該当変更を保留する。auto-merge、自動ブランチ削除、コミットメッセージ形式を同時に変更しない。[^repository-api][^ruleset-rules]

## mainのRuleset保護

期待値は `refs/heads/main` にactiveなbranch Rulesetが適用され、PR経由の変更・削除防止・force push防止が実効的に成立すること。継承されたRulesetで満たす場合も適合とし、重複するリポジトリRulesetは作らない。従来のbranch protectionだけでは、この個人基準のRuleset要件を満たさない。[^personal-policy][^ruleset-rules]

1. `GET /repos/{owner}/{repo}/branches/main` 等でmainの実在とdefault branchを確認する。別名・空リポジトリ・main不在を、暗黙の改名・作成・対象変更で解決しない。
2. `GET /repos/{owner}/{repo}/rulesets?includes_parents=true` を全ページ取得し、関連するRulesetの詳細でtarget、enforcement、include/exclude、source、bypassを確認する。
3. `GET /repos/{owner}/{repo}/rules/branches/main` を全ページ取得し、activeな実効ルールを照合する。このAPIは存在しないブランチにもルールを返すため、mainの実在確認の代わりにしない。[^rules-api]
4. `pull_request`、`deletion`、`non_fast_forward` と既存の追加制約を確認する。evaluate/disabled、main除外、不要なbypassは見逃さない。bypass情報を閲覧できない場合は「例外なし」と断定しない。
5. 不足を対象リポジトリ自身のRulesetへ追加する。UIは `Settings` → `Rules` → `Rulesets`、APIは既存IDへの `PUT /repos/{owner}/{repo}/rulesets/{ruleset_id}`。新規 `POST /repos/{owner}/{repo}/rulesets` は必要な場合だけ使う。今回の承認済み変更の対象外である条件・ルール・パラメーター・例外を保持し、上位Rulesetを変更しない。[^rules-api]
6. 詳細と実効ルールを再取得する。従来保護の削除は初版の適用に含めず、保護に空白を作らない。検証目的のmain直接push・削除・force pushを行わない。

既存の必須チェック、承認人数、CODEOWNERS等は維持する。新しい必須チェックは対象側の方針、実際のチェック名・発行元・実行条件・成功履歴を確認して選び、存在しないチェックでマージを止めない。CodeQL有効化をCodeQL必須化に読み替えず、単独開発で満たせない承認人数、署名必須、線形履歴を一律追加しない。不要なbypassを新設せず、既存例外の廃止にも影響と承認を確認する。非対応プランは利用不可として理由を残し、有料プランへ変更しない。[^personal-policy][^ruleset-rules]

## 外部ActionのフルSHA必須化

期待値はネイティブの `Require actions to be pinned to a full-length commit SHA` が有効で、対象workflowが適合していること。公式Action・同じ所有者の別リポジトリも対象とする。`GET /repos/{owner}/{repo}/actions/permissions` の `sha_pinning_required` または `Settings` → `Actions` → `General` で確認する。[^actions-settings][^actions-permissions-api]

先にworkflow・ローカルcomposite action・呼び出し先の依存を調べ、必要な修正を `github-actions` へ渡す。参照は対象リリースと照合した完全コミットSHAへ固定し、承認済みの必要なファイル変更をPR・CI・統合後確認まで完了してからポリシーを強制する。mainだけでなく有効な他ブランチ・リリース経路への影響も確認し、未確認の実行経路を安全とみなさない。

APIの適用は `PUT /repos/{owner}/{repo}/actions/permissions`。必須の `enabled` と既存 `allowed_actions` を直前の取得値から保持し、`sha_pinning_required=true` を送る。Actionsが無効なら有効化を黙って追加せず、無効理由と対象範囲を確認する。許可リストや上位ポリシーを緩めない。適用後は同じ設定と対象workflowを再確認する。[^actions-permissions-api]

ネイティブ設定は再利用workflowのタグ参照を禁止しないため、設定が有効でも外部再利用workflowは別途フルSHA固定を診断する。同一リポジトリの相対参照をGitのSHAに置換せず、コンテナのdigest固定をGit参照と混同しない。これらの実装基準は `github-actions` を正本として使う。[^actions-settings]

[^personal-policy]: Issue #152 の初期5項目と既存保護・適用範囲の制約。
[^release-setting]: リポジトリでの有効化と将来のリリースへの適用。
[^immutable-release]: 保護対象、draft公開手順、既存immutable releaseの制約。
[^repository-api]: repositoryの取得・更新とマージ方式のフィールド。
[^ruleset-rules]: Rulesetの提供条件、branch保護、マージ関連ルール。
[^rules-api]: Rulesetの取得・更新、継承とbranchの実効ルール。
[^actions-settings]: ネイティブSHA必須設定の対象と再利用workflowへの制約。
[^actions-permissions-api]: Actions permissionsの取得・更新と必須パラメーター。
