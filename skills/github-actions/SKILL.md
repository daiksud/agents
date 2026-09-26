---
name: github-actions
description: GitHub Actionsのworkflow作成・変更、CI失敗の原因調査と修正、workflowレビュー、CI高速化・安全性改善、Action内部ランタイム更新を依頼されたときに使う。.github/workflowsやActions設定が対象。変更時のIssue計画・公開許可はissue-management、承認済み変更のmainまでのdeliveryはchange-delivery、アプリのコード修正はsoftware-development、レビューはcode-reviewと併用する。Issue・PR操作だけ、アプリ実装だけ、CI/CDの概念説明だけには使わない。
---

# GitHub Actionsを設計・検証する

開発者が必要な検証を待ち過ぎずに受け取り、信頼できる成果物を届けられるワークフローを扱う。以下のリポジトリ内パスは作業対象リポジトリを指す。

## 依頼と参照資料

最初に、依頼が設計・調査だけか、レビューか、変更まで含むかを確認する。変更でIssue計画・公開許可・実行範囲を扱うときは `issue-management`、承認済み変更をbranch・PR・必須CI・統合後mainの確認まで届けるときは `change-delivery` を併用する。Issue計画だけなら `issue-management` で `change-delivery` や `software-development` が未導入でも保存・再取得・本文と表示・URLの提示で停止できる。

アプリコードの修正では `software-development` のTDDで回帰を再現して修正する。workflow設定のみの修正ではアプリコード用TDDを始めないが、設定の失敗に応じた最小の検証を先に定める。文書作成は `document-authoring`、読み取り専用レビューの進め方と指摘は `code-review` に従う。`issue-management` を利用できなければIssueへ投稿せず、他のSkillで代用せずに未保存案と制約を示す。`change-delivery` を利用できなければworkflowを編集せず、他のSkillで代用せずに未完了の検証・main確認を示す。`software-development` を利用できなければアプリコードを編集せず、再現情報と未完了範囲を示す。該当する依存が未導入なら利用環境で導入方法を確認する。相談・監査だけから編集・Issue投稿・PR作成・実行トリガーへ進まない。

作業に該当する資料だけを読む。複数の分野に関わる場合は組み合わせる。

| 作業・読む条件 | 資料 |
| --- | --- |
| 新規作成、トリガー・ジョブ依存・再利用・配備構成の変更 | [ワークフロー設計](references/workflow-design.md) |
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
6. ワークフローの設計・変更・レビューでは、runnerとshellを次の方針で確認する。
   - runnerを選ぶ前に、対象環境がその`runs-on` labelを提供しているか、labelに一致する候補のprovider（GitHub-hosted / self-hosted）、runner group、repository accessを確認する。label名だけでproviderを推測しない。同じcustom labelを持つself-hosted runnerが候補に入る場合は、特にPR由来codeの実行について[安全性](references/hardening.md)の共有状態・network・host credentialの境界を確認し、GitHub-hosted runnerだと確認できるまでlabelだけで選定を確定しない。
   - `ubuntu-slim` が利用可能でも、必要な処理を実現できないと確認した場合に限り恒久的に別のrunnerを使う。慣習、既存例の踏襲、高性能への単なる希望は例外理由にしない。
   - 実行時間が要件になる場合は、対象runner上の実測と判断時点の公式資料に記載されたjob timeoutを照合し、別runnerでの時間だけを根拠に適合を断定しない。未計測なら既存の必須jobがあれば維持し、新候補は非必須のtrialで代表的なjobを試す。これは適合確認までの暫定運用で、恒久的なrunner例外として説明しない。
   - 例外時はGitHub.comかGHESか、repositoryの公開状態とplanを確認する。GitHub.comでは該当する[public repository向けrunner一覧](https://docs.github.com/en/actions/reference/runners/github-hosted-runners#standard-github-hosted-runners-for-public-repositories)または[private repository向けrunner一覧](https://docs.github.com/en/actions/reference/runners/github-hosted-runners#standard-github-hosted-runners-for-private-repositories)を参照し、GHESではGitHub.comの一覧を適用せず対象環境のrunner inventoryを確認する。
   - `ubuntu-slim` の制約を照合し、満たせない要件と具体的な制約をワークフローのコメントか変更説明に記録する。[公式の制約](https://docs.github.com/en/actions/reference/runners/github-hosted-runners#single-cpu-runners)は判断時点で確認する。
   - runnerの選定理由を回答・記録するときは、`ubuntu-slim` 優先がこのスキル独自の方針で、GitHub共通の必須要件ではないことを明示し、runnerの提供条件・制約などのGitHub公式仕様と分けて説明する。日付付きの仕様確認値は[出典と適用判断](references/sources.md)に記録する。
   - 新規workflow、またはworkflow-level shell移行が承認範囲に含まれる設計・変更では、workflowトップレベルに `defaults.run.shell: bash` を必ず指定する。stepごとの `shell: bash` だけでこの要件を満たした扱いにしない。既存workflowの限定的な修正でshell移行が承認範囲に含まれない場合は、既存shellを変更せず、shell方針の適用を別変更として報告・提案する。
   - Bash既定値が適用される各jobの実行環境にBashがあるか、各commandがBashと互換かを確認する。Bashがないself-hosted runnerやjob containerでは、可能ならBash入りrunner・imageを用意する。既存のshellからpackageを導入するstepを使う場合は、そのstepに導入前から利用できるshell（例: `sh`）を明示する。workflow-levelの`bash`既定値は導入stepにも適用される。
   - Bashを用意できずjobのcommandがPOSIX互換なら、workflowトップレベルのBash既定値を残したうえで、そのjobだけ`defaults.run.shell: sh`を明示し、不在を理由として記録する。PowerShellなど別shellを契約とするjobやstepでは、トップレベルの既定値を残し、そのjobの`defaults.run.shell`または該当stepの`shell`を契約に合う利用可能なshellへ上書きし、具体的な要件を記録する。これらは実行環境またはcommandの互換性から必要となる場合の局所例外とする。Bash固有のcommandが必要でBashを提供できない場合は、shell方針とjob要件のどちらを優先するかユーザーに確認する。
   - 明示した`bash`とshell未指定では実行commandが異なる。fallbackを含む詳細は[Workflow syntax: `defaults.run.shell`](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#defaultsrun)と[出典と適用判断](references/sources.md)で確認する。
   - 既存workflowの未指定shellを明示的なBashへ変える場合、`pipefail`によるpipeline statusと既存handler・出力契約への影響を確認する。Bashの`errexit`条件文脈、pipelineのlist内位置、statusの詳細は[出典と適用判断](references/sources.md)で照合し、回答でこれらの仕様を根拠として述べる場合は同資料の該当する公式出典へのリンクを示す。意図した非0だけを局所的に扱い、他の失敗は維持する。job・step単位のshell上書きを使う場合は、既存のjob契約から必要となる理由を記録する。

   ```yaml
   defaults:
     run:
       shell: bash

   jobs:
     check:
       # Confirm provider, runner group, and repository access before selecting this label.
       # Label availability alone does not identify a GitHub-hosted runner.
       runs-on: ubuntu-slim
       steps:
         - name: Check shell
           run: printf '%s\n' "$BASH_VERSION"
   ```

## 成果と確認

設計・調査なら根拠と提案、レビューなら再現条件・影響を伴う指摘、変更なら差分と検証結果を示す。報告形式は依頼や既存スキルに合わせる。

- YAML構文、Actionsの式・参照・依存関係、必須チェックへの影響を静的に検査する。利用可能な既存lintやactionlintを使い、通常のYAMLパーサーだけでActions仕様まで検証済みとしない。
- ローカルのテストとGitHub上の実行を分ける。承認済みの変更では対象SHA・イベント・runner・run URLを照合し、実行結果だけでなく必要な成果物や配備後の状態を確認する。
- 失敗・キャンセル・未実行・取得不能を成功扱いしない。実行検証できない場合は未確認範囲と確認方法を示す。
- 効果は期待値と実測値を分ける。CI成功を安全性全体や性能改善の証明にしない。
