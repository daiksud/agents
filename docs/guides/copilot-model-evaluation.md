---
type: Guide
title: GitHub Copilot複数モデル評価
description: 共通InstructionsとSkillsを同じ条件で複数モデルに適用し、品質・効率・失敗原因を分離して記録する手順です。
sources:
  - id: issue-124
    resource: https://github.com/daiksud/agents/issues/124
  - id: issue-122
    resource: https://github.com/daiksud/agents/issues/122
  - id: issue-123
    resource: https://github.com/daiksud/agents/issues/123
  - id: github-supported-models
    resource: https://docs.github.com/en/copilot/reference/ai-models/supported-models
  - id: github-copilot-cli-programmatic
    resource: https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-programmatic-reference
  - id: github-copilot-cli-auth
    resource: https://docs.github.com/en/copilot/how-tos/copilot-cli/set-up-copilot-cli/authenticate-copilot-cli
---

## 目的

GPT-6 Sol、GPT-6 Luna、Claude Opus 5.5、Claude Sonnet 5に、同じInstructions・Skills・prompt・成功基準を適用し、モデル固有の補正が本当に必要かを調べる。4モデルはいずれも2026-09-27時点でGitHub Copilotのサポート対象として掲載されている。Copilot CLIは非対話実行、モデル固定、tool制限、専用の `COPILOT_HOME` をサポートする。[^github-supported-models] [^github-copilot-cli-programmatic]

この評価はモデルの総合ランキングを作らない。品質と効率を分け、少数回の差を一般化しない。

## 正本と非公開境界

- 共通ケースとgrader基準: `evals/copilot-models/cases.json`
- 実行: `scripts/run_copilot_model_eval.py`
- 実測raw evidence: repo外の出力ディレクトリ。選択したrepository内suite自体も `suite.json` としてここへ保存する
- リポジトリに残す基準記録: `evals/copilot-models/results/` 直下のレビュー済みJSON
- #122のモデル非依存契約と#123のrouting / Progressive Disclosureを変更せずに評価する。[^issue-122] [^issue-123]

`cases.json` の `criteria` はgrader専用で、評価対象モデルへ渡さない。runnerは各run用workspaceをGitのclean HEADから作り、`evals/copilot-models`、`docs/behavior`、このガイド、runner本体、専用testをworkspaceから除外する。`docs/behavior` はA–Gの期待結果と重なる受け入れ仕様を含むため、評価対象モデルのanswer keyとして使わせない。`--cases` で別suiteを選ぶ場合も、commitから再現できるrepository内ファイルに限定し、その選択済みsuite自体をmodel-visible workspace、APM cache、必要ならinstalled Skill treeから除外する。repository外suiteは実評価・dry-runとも受け付けない。promptにもcriteriaを埋め込まない。

評価対象モデルがgrader、別モデルの出力、過去attemptを読める状態では比較しない。

## 実行前提

同じ比較バッチでは次を固定する。

- repository SHA
- clean checkout
- 選択suiteがそのrepository SHAでGit追跡され、working tree内容とHEAD blobが一致すること
- Copilot CLI version
- `cases.json` の内容hash
- prompt
- APMから隔離HOMEへ配布したInstructions / Skillsのhash
- taskの開始状態
- tool / permission境界
- 明示的に変更するreasoning等のモデル設定
- 1ケースあたりの反復回数
- per-run model invocation timeout（正の有限値のみ）。APM install / compile等のdelivery setup timeoutとは独立させる

モデルごとに成功条件を変えない。モデルが利用できない、CLIがない、認証・policyで拒否された場合は品質失敗ではなく `runtime` または `tool_or_permission` として記録する。

### clean checkout

実測では tracked / untracked の評価入力がHEADとずれないよう、runnerが `git status --porcelain --untracked-files=all` を確認する。差分があれば実行しない。

これによりmanifestの `repo_sha` と、モデルへ届く候補Instructions / Skills、grader側のsuiteを同じcommitted stateへ結びつける。suiteは最初に1回だけbytesとしてcaptureし、その同じbytesからparse、hash、repo外snapshot、記録SHAのGit blobとの一致確認を行う。途中でworking treeのsuiteが変化しても、別のbytesを混ぜない。suiteは単にrepository内にあるだけでは足りず、記録したSHAでGit追跡されていることを確認する。ignored/untracked suiteは実行しない。

### 隔離したInstructions / Skills配布

runnerはbase用の一時HOMEへ候補SHAをAPMで導入・compileし、既存のAPM smoke verifierで次を確認する。model-visible workspaceもmoving `HEAD` ではなく、clean-checkで取得した同じimmutable SHAを直接 `git archive` して作る。

- APM cacheの候補SHA
- `~/.copilot/AGENTS.md` に候補Instructionsが生成されていること
- `~/.agents/skills/` が候補Skillsと対応していること
- candidateのInstructions / Skillsと配布物のhash

各モデルrunは、この検証済みbase workspace / HOMEを新しい一時ディレクトリへコピーする。run間でHOME、Copilot state、workspaceを共有しない。

APM配布検証の完了後、隔離HOMEのpackage cacheからgrader専用パスも削除してからbaseを複製する。選択したrepository内suiteが `skills/<name>/...` にある場合は、APMが生成した `~/.agents/skills/<name>/...` 側の対応ファイルも削除する。さらに、source workspace、APM cache、`~/.agents/skills/` の各Skill配下にある `evals/` も評価時だけ除外する。Skill本文とreferencesは保持し、過去のSkill評価fixtureやexpected outputをanswer keyとして参照させない。

### 認証と権限

隔離HOMEでは既存のkeychain / Copilot設定を評価入力として再利用しない。非対話評価は `COPILOT_GITHUB_TOKEN`、`GH_TOKEN`、`GITHUB_TOKEN` のいずれかを環境変数として明示する。Copilot CLIはこの順序でtokenを使用でき、headless環境では環境変数認証が公式に案内されている。[^github-copilot-cli-programmatic] [^github-copilot-cli-auth]

BYOKの `COPILOT_PROVIDER_*` がある環境ではGitHub Copilotモデル比較として実行しない。

評価ケースは判断契約を見るためのread-only taskとし、`shell`、`write`、`url`、`memory` toolを明示的にdenyする。現在workspace外を追加のallowed pathにしない。[^github-copilot-cli-programmatic]

## 共通ケース

A–Gを全モデルで同じ順序・基準で使う。

| ID | 対象 |
| --- | --- |
| A | 小さな不具合修正: 小さいshared Todo、Red / Green / Refactor、Navigator gate、scope |
| B | 計画だけ: issue-managementで止まり、実装・deliveryへ広げない |
| C | 大きくなったTodo: 独立したRedを分割して再選択する |
| D | CI失敗 / review changes requested: 未完了として修正・再検証・最新HEADレビュー・deliveryを続ける |
| E | 権限不足: 制約を回避せず、完了範囲・未完了・blocker・再開条件を分ける |
| F | モデル引き継ぎ: self-reportではなく現在の差分・証拠を再確認する |
| G | Skill routing: github-actions + code-reviewと必要referenceだけを使う |

具体promptとgrader criteriaは `cases.json` を正本とし、モデルにはprompt部分だけを渡す。runnerはsuiteのモデル名・CLI ID、A–GのID・title・非空prompt・非空criteria、共通rules、failure taxonomyを実行前に検証し、malformed suiteを開始しない。

## 実行

まず評価計画だけを確認する。dry-runはAPM配布を行わず、PyYAMLなどdelivery専用の依存をimportしない。

```bash
python3 scripts/run_copilot_model_eval.py --dry-run --repeat 3
```

認証済みCopilot CLIがあり、clean checkoutである環境から最低3回ずつ実行する。raw evidenceはrepo外へ出す。

```bash
export COPILOT_GITHUB_TOKEN='...'
python3 scripts/run_copilot_model_eval.py \
  --repeat 3 \
  --timeout-seconds 600 \
  --output-dir /tmp/copilot-model-eval/<run-id>
```

一部モデルだけを再現確認するときはCLI model IDを明示する。`--models` を明示した場合は少なくとも1つの有効なIDを必要とし、空文字や区切り文字だけの指定はエラーとする。

```bash
python3 scripts/run_copilot_model_eval.py \
  --models gpt-6-sol,claude-opus-5.5 \
  --repeat 3 \
  --output-dir /tmp/copilot-model-eval/<run-id>
```

repo内の出力先は拒否する。repo外のevidence directoryは `0700`、suite / manifest / stdout / stderrは `0600` とし、共有machineの他ユーザーからgrader基準やraw responseを読めないようにする。runnerは各runの開始時に、graderを含まないworkspaceと新しいHOMEを検証済みbaseから作る。stdout / stderrはCopilot終了後にrunner側がrepo外へ保存するため、後続runのworkspaceから先行モデル出力を読ませない。

実測開始時は、選択モデルとmodel / case / attemptの全planned matrixをmanifestへ先に保存する。CLI不足、BYOK設定、token不足、dirty checkout、Copilot version probe失敗などのpreflight失敗でもこの初期manifestを残し、候補配布前のCLI・環境失敗を `runtime`、認証不足を `tool_or_permission` として記録する。`copilot --version` が非0終了またはtimeoutした場合は、取得できたstdout / stderrを同じprivate evidence directoryへ保存し、manifestからその診断が残ったことを確認できるようにする。APM verifierのPyYAMLなどdelivery専用依存が不足した場合はtracebackのまま終了せず、`setup: failed` と `instruction_delivery` の未完了証拠をmanifestへ残す。

1 runがtimeoutしても、それまでのmanifestを保存し、当該attemptを `runtime` として記録して次のrunへ進む。model invocationの `--timeout-seconds` はAPM install / compileへ流用せず、delivery setupは独立した上限で実行する。setup側のtimeoutもmodelの失敗ではなく `runtime` として記録する。Copilotが例外ではなく非0 exit codeを返した場合も成功候補にせず、`runtime` と診断メモを記録してraw stderrと区別する。exit code 0でもstdoutが空なら採点可能なmodel responseが存在しないため `runtime` failureとして扱う。

APM配布の検証済み状態とrun側の失敗を混同しない。配布完了後のworkspace copy、Copilot起動、evidence保存等が失敗した場合は、`setup: verified` を維持したまま当該attemptまたはbatchの `runtime` failureとして記録する。

## 記録

manifestには少なくとも次を残す。

- suite version / suite hash / repo外へ保存した `suite.json` snapshot
- repository SHA
- Copilot CLI version
- 認証に使った環境変数名だけ（値は保存しない）
- workspace / compiled Copilot Instructions / installed Skillsのhash
- 選択したmodel一覧と、開始前に確定したmodel / case / attemptの全planned matrix
- model / case / attempt
- prompt hash
- model invocation elapsed time（workspace/HOME複製時間を含めない）
- per-run setup time
- return code / timeout
- raw evidenceのファイル名
- 品質判定欄
- 効率判定欄
- failure class / notes

manifest更新は同じ出力ディレクトリの `0600` 一時ファイルへ完全な標準JSON（NaN / Infinityを許可しない）を書き、flush / fsync後にatomic replaceする。中断時に最後の正常manifestを不用意にtruncateしない。

未評価フィールドは `null` のままにし、未知を0へ変換しない。選択したrepository内suiteは再現・再採点用のgrader evidenceとして、raw出力と同じ保護されたrepo外ディレクトリへ `suite.json` としてコピーする。repository外suiteは受け付けない。raw JSONLやstderr、suite snapshotにはコード・ログ・モデル応答・grader基準等が含まれ得るため、そのままGitへ追加しない。共有が必要なら公開範囲を確認し、必要な集計・判定だけをレビュー済み記録へ転記する。

`evals/copilot-models/results/.gitignore` は日時等のrun subdirectoryを既定でGit管理対象から外す。直下のレビュー済み基準JSONは保持できる。

### 品質

各ケースのcriteriaをモデル実行後にgrader側で出力へ照合し、少なくとも次を記録する。

- criteria達成
- TDD / Navigator gateの欠落
- 完了条件前の途中停止
- 不要なscope expansion
- 不具合・要件違反・回帰の見逃し
- evidenceなしの成功判定
- 正当なstop boundary違反

criteriaを評価対象モデル自身へ見せて自己採点させない。

### 効率

取得できる場合だけ次を記録する。

- elapsed time
- turn count
- tool call count
- token usage
- loaded Skills / references
- 不要な再読

`elapsed_seconds` はCopilot invocation直前からsubprocessのreturn / timeout直後までだけを測り、TemporaryDirectoryのcleanupやworkspace/HOME複製時間を含めない。複製等は `setup_seconds` へ分ける。CopilotのJSONLや利用環境から取得できない値は `null` とする。品質とコストを一つの総合scoreへ合成しない。

## 原因分類

失敗は次の順序で原因を切り分け、一つの便利な「モデル差」へまとめない。

1. `instruction_delivery`: APM配布検証、Instructions / Skills hash、実行ログから必要な内容が届いていない。
2. `ambiguity`: 共通指示が曖昧、重複、矛盾している。
3. `tool_or_permission`: 必要な認証、policy、permissionがない。
4. `task_granularity`: Todoやケース自体が大きすぎる。
5. `runtime`: Copilot client、CLI、session、transport、timeout固有の制約。
6. `model_specific`: 上記を除外しても同じモデルだけで再現する。
7. `none`: 受け入れ条件を満たす。

原因を判断できない場合は `notes` に未確認事項を残し、`model_specific` に推測で分類しない。

## モデル固有補正のゲート

モデル固有の補正は次のすべてを満たす場合だけ候補にする。

- 同じ失敗が同じモデルで複数回再現する。
- 同一SHA / suite / 配布hash / tool境界で再現する。
- instruction deliveryの欠落ではない。
- 共通Instructions / Skillsの曖昧さ・矛盾ではない。
- tool / permission / runtime / timeoutでは説明できない。
- task粒度では説明できない。
- grader leakageや先行run leakageがない。
- 共通ルールを直すと、既に正しく動くモデルへ不要な制約を追加する。
- 補正の根拠、適用範囲、削除条件を説明できる。

補正はモデル別Skillの複製を第一選択にせず、最小のoverlayにする。追加後はA–Gを全モデルで再評価し、#122 / #123の契約を壊していないことを確認する。

## 現在の基準記録

`evals/copilot-models/results/2026-09-27-runtime-unavailable.json` は、このIssueを実装したChatGPT実行環境では `copilot` と `gh` CLIが利用できなかった事実だけを記録する。4モデルの品質・速度・token効率を評価した記録ではない。

この記録を「4モデルに差がなかった」という証拠に使わない。実機結果が得られるまでモデル固有overlayを追加しない。

[^github-supported-models]: [Supported AI models in GitHub Copilot](https://docs.github.com/en/copilot/reference/ai-models/supported-models)。対象モデルの対応状況。
[^github-copilot-cli-programmatic]: [GitHub Copilot CLI programmatic reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-programmatic-reference)。非対話実行、モデル固定、tool制限、`COPILOT_HOME` とtoken環境変数。
[^issue-122]: [Issue #122](https://github.com/daiksud/agents/issues/122) のモデル非依存契約。
[^issue-123]: [Issue #123](https://github.com/daiksud/agents/issues/123) のSkill routingとProgressive Disclosure。
[^github-copilot-cli-auth]: [Authenticating GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/set-up-copilot-cli/authenticate-copilot-cli)。非対話環境でのtoken認証と優先順位。
