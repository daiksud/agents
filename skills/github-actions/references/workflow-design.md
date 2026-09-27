---
type: Instruction
title: GitHub Actionsのワークフロー設計
description: 要件からトリガー、ジョブ、再利用、成果物と配備・復旧を選び、実行経路を検証します。
sources:
  - id: copilot-cicd
    resource: https://github.com/github/awesome-copilot/blob/4f4796f0bf30e105700f97ed8408c12b6aa95e06/instructions/github-actions-ci-cd-best-practices.instructions.md
  - id: github-syntax
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
  - id: github-reuse
    resource: https://docs.github.com/en/actions/how-tos/reuse-automations/reuse-workflows
---

## 要件から実行経路を決める

新規作成では、誰がどの変更に対して何の結果を必要とするかを確認する。既存構成では、その目的、必須チェック名、対応OS・ランタイム、Secret・公開権限、配備先と復旧方法を先に読む。原典の設計・テスト・配備の観点を使い、必要な検証を通す小さな構成から始める。[^copilot-cicd]

### イベントとジョブ

- `push`・`pull_request` は検証するコミットと重複実行を比較して選ぶ。merge queueを使う場合は `merge_group` など必要なイベントを確認する。`pull_request_target` をPRテストの権限不足の回避に使わない。
- `workflow_dispatch` は手動操作、`workflow_call` は再利用、`schedule` は定期処理という要件に合わせる。既定ブランチ上の定義が必要なイベントや、PRのheadとmerge refの違いを対象イベントの公式仕様で確認する。
- `needs` は実際の依存を表す。独立した検査を不要に直列化せず、前段の失敗・スキップ時に後段がどうなるかを確認する。後片付け・診断保存の条件と、必須検証を成功扱いにする条件を分ける。
- シェル・作業ディレクトリ・依存の固定方法・適切なtimeoutを明示する。OSごとのシェル差、サービス起動完了、テストの隔離と後片付けを確認する。無差別な再試行や `continue-on-error` で必須テストの失敗を隠さない。
- 必須チェックを伴うworkflow全体のpath/branchフィルターは、チェックがPendingのままになり得る。ジョブ単位の判定や集約を使う場合も、必要な検証の失敗・キャンセルが最終チェックへ伝わることを確かめる。[^github-syntax]

### 再利用とデータの受け渡し

同じステップの共有にはcomposite Action、ジョブやrunner構成の共有にはreusable workflowを検討する。既存の境界に合わせ、重複があるだけで分割しない。`workflow_call` では入力の型・必須性・デフォルト、outputs、渡すSecretを契約にし、呼び出し側との対応を確認する。入れ子の呼び出しで権限は増やせず、Secretの再転送も明示して点検する。`secrets: inherit` は必要な範囲を確認してから選ぶ。[^github-reuse]

小さい値はoutputs、ファイルはartifactとして渡す。別ジョブでファイルパスだけを渡してもファイル自体は移らない。生成したコミット、対象OS・版、内容の同一性、保持期間、機密情報の混入を確認する。ログ・テストレポートも必要な診断情報だけを保存し、Secretを含めない。キャッシュは再利用のための補助であり、配備成果物の正本にしない。

### 配備と復旧

検証した同じ成果物を環境間で昇格させる。配備ジョブの条件・権限・environment保護、同時実行の衝突、公開判断の責任を確認する。`environment:` を書くだけで手動承認が設定されるとは扱わない。手動承認・Canary・blue/green等はリスクと既存運用に合う場合に選ぶ。

配備後のヘルスチェック、観測する失敗、復旧する成果物と構成を決める。データ移行はコードのロールバックと同じ可逆性を仮定しない。既存の実行範囲で配備・復旧できるかを確認し、公開条件や権限の変更は `issue-management` で範囲と許可を確認する。承認済みの復旧変更と必要な検証は `change-delivery` へ引き渡す。

### 検証する経路

正常系だけでなく、必要なイベント、fork、無関係な変更、依存ジョブの失敗・スキップ、キャンセルを対象に選ぶ。静的確認と既存テストに加え、承認されたGitHub実行で必須チェック、outputs/artifact、配備後の状態を確かめる。取得できない保護設定や未実行の配備は未確認として示す。

[^copilot-cicd]: CI/CD Best Practicesの設計・テスト・成果物・配備観点を要約。固定構成や一律の公開方式は採用しない。
[^github-syntax]: Workflow syntax。イベントフィルター、ジョブ依存と条件式の実際の挙動を確認する正本。
[^github-reuse]: Reuse workflows。入力・Secret・権限の呼び出し契約の正本。

## runnerとshell

ワークフローの設計・変更・レビューでrunnerまたはshellが関係する場合だけ、次を確認する。

- runnerを選ぶ前に、対象環境がその`runs-on` labelを提供しているか、labelに一致する候補のprovider（GitHub-hosted / self-hosted）、runner group、repository accessを確認する。label名だけでproviderを推測しない。同じcustom labelを持つself-hosted runnerが候補に入る場合は、特にPR由来codeの実行について[安全性](hardening.md)の共有状態・network・host credentialの境界を確認し、GitHub-hosted runnerだと確認できるまでlabelだけで選定を確定しない。
- `ubuntu-slim` が利用可能でも、必要な処理を実現できないと確認した場合に限り恒久的に別のrunnerを使う。慣習、既存例の踏襲、高性能への単なる希望は例外理由にしない。
- 実行時間が要件になる場合は、対象runner上の実測と判断時点の公式資料に記載されたjob timeoutを照合し、別runnerでの時間だけを根拠に適合を断定しない。未計測なら既存の必須jobがあれば維持し、新候補は非必須のtrialで代表的なjobを試す。これは適合確認までの暫定運用で、恒久的なrunner例外として説明しない。
- 例外時はGitHub.comかGHESか、repositoryの公開状態とplanを確認する。GitHub.comでは該当する[public repository向けrunner一覧](https://docs.github.com/en/actions/reference/runners/github-hosted-runners#standard-github-hosted-runners-for-public-repositories)または[private repository向けrunner一覧](https://docs.github.com/en/actions/reference/runners/github-hosted-runners#standard-github-hosted-runners-for-private-repositories)を参照し、GHESではGitHub.comの一覧を適用せず対象環境のrunner inventoryを確認する。
- `ubuntu-slim` の制約を照合し、満たせない要件と具体的な制約をワークフローのコメントか変更説明に記録する。[公式の制約](https://docs.github.com/en/actions/reference/runners/github-hosted-runners#single-cpu-runners)は判断時点で確認する。
- runnerの選定理由を回答・記録するときは、`ubuntu-slim` 優先がこのスキル独自の方針で、GitHub共通の必須要件ではないことを明示し、runnerの提供条件・制約などのGitHub公式仕様と分けて説明する。日付付きの仕様確認値は[出典と適用判断](sources.md)に記録する。
- 新規workflow、またはworkflow-level shell移行が承認範囲に含まれる設計・変更では、workflowトップレベルに `defaults.run.shell: bash` を必ず指定する。stepごとの `shell: bash` だけでこの要件を満たした扱いにしない。既存workflowの限定的な修正でshell移行が承認範囲に含まれない場合は、既存shellを変更せず、shell方針の適用を別変更として報告・提案する。
- Bash既定値が適用される各jobの実行環境にBashがあるか、各commandがBashと互換かを確認する。Bashがないself-hosted runnerやjob containerでは、可能ならBash入りrunner・imageを用意する。既存のshellからpackageを導入するstepを使う場合は、そのstepに導入前から利用できるshell（例: `sh`）を明示する。workflow-levelの`bash`既定値は導入stepにも適用される。
- Bashを用意できずjobのcommandがPOSIX互換なら、workflowトップレベルのBash既定値を残したうえで、そのjobだけ`defaults.run.shell: sh`を明示し、不在を理由として記録する。PowerShellなど別shellを契約とするjobやstepでは、トップレベルの既定値を残し、そのjobの`defaults.run.shell`または該当stepの`shell`を契約に合う利用可能なshellへ上書きし、具体的な要件を記録する。これらは実行環境またはcommandの互換性から必要となる場合の局所例外とする。Bash固有のcommandが必要でBashを提供できない場合は、shell方針とjob要件のどちらを優先するかユーザーに確認する。
- 明示した`bash`とshell未指定では実行commandが異なる。fallbackを含む詳細は[Workflow syntax: `defaults.run.shell`](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#defaultsrun)と[出典と適用判断](sources.md)で確認する。
- 既存workflowの未指定shellを明示的なBashへ変える場合、`pipefail`によるpipeline statusと既存handler・出力契約への影響を確認する。Bashの`errexit`条件文脈、pipelineのlist内位置、statusの詳細は[出典と適用判断](sources.md)で照合し、回答でこれらの仕様を根拠として述べる場合は同資料の該当する公式出典へのリンクを示す。意図した非0だけを局所的に扱い、他の失敗は維持する。job・step単位のshell上書きを使う場合は、既存のjob契約から必要となる理由を記録する。

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
