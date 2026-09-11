---
type: Guide
title: 検証済みのスキルと共通指示を届ける
description: 同じ候補SHAの配布検証、小さな統合、mainの復旧責任、計測と学習の手順を説明します。
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

Actionsの手動実行では対象ブランチを選択できます。失敗時もログと途中の証跡をartifactで確認し、実行されなかった工程を成功とは扱いません。探索的なスキル内容の確認は[隔離環境手順](#ローカルとciで同じ検査を実行)で行い、指示の判断品質は読み取り専用模擬評価で別に確認します。

APM 0.30.0では、未固定依存を持つ旧版から更新すると、変更後の依存固定が `update` だけでは反映されないケースを実検証で検出しました。READMEの更新手順では `apm update --global` の後に `apm install --global` を実行して宣言された依存を再適用し、新規導入時と同じ内容になることを確認します。

### 導入する版を選ぶ

1. mainの対象コミットで両OSの受け入れ検証が成功していることをActionsで確認します。
2. artifactのcandidate、各phaseのsha、依存SHA、ハッシュと成功状態を確認します。チェック成功だけで公開後の判断品質まで保証しません。
3. 同じ候補を導入する場合は、READMEのAPM導入コマンドのパッケージ指定を `daiksud/agents#<確認した完全SHA>` にします。導入後にdry-run、compileと生成結果を確認します。

APM 0.30.0・GitHub CLI 2.100.0と固定Python依存を使用します。runnerのOSイメージとPython 3.12のパッチ版は更新されるため、実際の環境・版を証跡で追跡します。検証済みSHAを保持し、依存更新も同じパイプラインを通します。

### 不具合から復旧する

mainを正常な状態へ戻す変更は、原因変更のrevertまたは最小修正のPRにします。変更担当者は通常作業より復旧を優先し、復旧計画の承認・最新HEADのレビュー・必須チェックを維持します。元の計画を復旧計画の承認に流用せず、失敗した検証の無効化で復旧を代用しません。復旧コミットのmainで必要チェックと公開配布検証が成功するまで後続作業を進めません。詳細は[統合後mainの確認と復旧](../../skills/task-workflow/references/review-and-merge.md#統合後mainの確認と復旧)に従います。

外部サービスやrunnerの一時障害でリポジトリ変更が不要と確認できた場合は、根拠・再試行理由を記録し、障害解消後に同じmain SHAを再検証します。空のPRや不要なrevertを作らず、必要チェックと公開配布検証の成功まで後続作業を止めます。

すでに導入した利用者は、過去の成功した証跡で確認した正常SHAを指定し直して再生成できます。

```bash
known_good_sha='<証跡で確認した正常な完全SHA>'
apm install --global --target codex,copilot "daiksud/agents#$known_good_sha"
apm compile --global --dry-run
apm compile --global
```

既存設定と手書き指示を先に保持し、復旧後の本文・スキル・依存を証跡と照合します。検証では設定中のbaseline_shaへ実際に戻し、更新前後の配布ハッシュ一致と復旧時間を確認します。正常SHAの更新も、実測済みの成功したコミットを選んでPRに記録します。高速検証5分・受け入れ10分・APM復旧工程10分は初期目標です。長時間化や失敗では原因を調べ、未達を達成済みとしません。main復旧時間とは区別します。

自動リリースと実ユーザー環境への自動配布は行いません。artifactの保存期限後も再検証できるよう、コミット・依存固定・検査コマンドを版管理します。

### 小さく統合しmainまで確認する

利用者が検証済みのmainを選べるよう、変更担当者はPRのマージ後も必要チェックと公開配布経路を確認します。[CIの原則](https://continuousdelivery.com/foundations/continuous-integration/)に従い、独立して検証・レビューできる小さな変更、活動日の毎日の統合、原則1活動日以内のブランチを目安にします。承認・レビュー・CIを省略して目安を達成しません。

1. Issueに作業開始日時、次の統合単位、検証・完了条件を記録します。分割と順序の承認は[計画手順](../../skills/task-workflow/references/planning.md#小さな統合単位と活動日)に従います。
2. ブランチが1活動日を超えたら、レビュー待ちなど確認できた原因と次の統合単位を更新します。休日や欠測を遅延と決めつけません。
3. マージ後mainのSHAと必要チェックを照合し、両OSartifactの候補・依存・配布ハッシュを確認します。失敗なら復旧を優先し、未実行・キャンセル・取得不能も成功とはしません。
4. 正常なmain、ローカル同期、対象ブランチ整理を確認して完了を記録し、承認済みの次のIssueへ進みます。

他プロジェクトでCIが未設定の場合は、[既存のマージ例外](../../skills/task-workflow/references/review-and-merge.md#ci未設定の場合)を維持します。ローカル検証結果と未設定をPRに記録し、「CI実行成功」「CD達成」と区別します。本リポジトリの必須CIにこの例外を適用しません。

### 計測の定義

新しい集計サービスやCIジョブを作らず、PR・Issue・Actionsと既存artifactの日時・SHA・URLを根拠に記録します。時刻はタイムゾーンを明記し、活動日の集計はJSTで行います。

| 項目 | 起点・終点と記録方法 |
| --- | --- |
| 統合頻度 | 変更作業を記録した活動日ごとのmainマージ件数。ブランチへのpushは数えない。活動記録が欠ける日は欠測とする |
| 作業の滞留 | Issueに記録した作業開始からPRマージまで。開始不明ならPR作成時刻を代用したと明記する |
| レビュー待ち | 各依頼から対応するレビューの正常完了まで。対象SHAと依頼・結果URLを結び、未完了・利用不能は別記する |
| 検証時間 | Actions各ジョブのstarted_at〜completed_at。created_at〜started_atの待ち行列時間と分ける。依存ジョブの待ちを実行時間へ加算しない |
| main復旧時間 | main失敗検知から復旧コミットの必要チェック（必須の配布検証を含む）がすべて成功するまで。外部障害で変更不要なら同じmain SHAで同じ必要チェックがすべて成功した時刻を終点と明記。失敗発生時刻と検知時刻を混同しない |
| APM復旧工程 | delivery-report.jsonのrestore_seconds。正常SHAへ戻すCLI工程の所要時間で、main復旧時間ではない |

高速検証5分、受け入れ10分、APM復旧工程10分の初期目標を維持します。main復旧時間に新しい合否閾値は設けず実測します。失敗がなければ「該当なし」、時刻がなければ「欠測」、終わっていなければ「未完了」とし、ゼロ秒へ置き換えません。

実測値は該当PR・Issueへ記録し、共通スキル本文には個別実績を埋め込みません。単発比較から改善効果を断定せず、個人評価・指摘数・Approve速度の競争にも使いません。

### 欠陥から検証を改善する

[継続的テストの原則](https://continuousdelivery.com/foundations/test-automation/)に従い、探索・受け入れ検証で見つかった欠陥を、再現可能な最も小さい検証に反映します。ドメイン判断はfeatureと単体テスト、技術的処理は単体テスト、スキル判断は模擬評価で検証します。必要な統合検証は保持し、単体に落とせない場合は理由を残します。

スキルの模擬評価では、同じ入力・採点基準を使って変更前後を新しい独立した実行コンテキストで比較し、原回答・採点根拠・比較HTMLを保存します。形式検査・導入成功と判断品質を区別し、欠測を成功扱いしません。

障害が起きたIssue・PRには次を記録します。責任追及ではなく、次回の検出を早めるための記録です。

| 記録項目 | 内容 |
| --- | --- |
| 影響・時刻 | 影響を受けた利用経路、発生・検知・復旧時刻。不明な時刻は欠測 |
| 原因と検出 | ログ・再現で確認できた原因、既存検証で検出できなかった理由。仮説は仮説と明記 |
| 復旧と検証 | 復旧PR・SHA、追加した再現検証、修正前後の結果、mainの必要チェック成功URL |
| 残る改善 | 未確認範囲と次に検証すべきこと。範囲外の改善は通常の後続Issue手順へ |

### 原本の編集と保守

| 原本 | 役割 |
| --- | --- |
| `.apm/instructions/core.instructions.md` | 常時適用する設計原則、変更保護、スキルの読み込み条件と完了条件 |
| `skills/task-workflow/` | Issue・計画からレビュー・スカッシュマージまでの作業手順 |
| `skills/bdd-tdd/` | 設計確認、シナリオ分割、BDD・TDD、検証 |
| `skills/code-review/` | 欠陥・回帰を根拠から評価する読み取り専用レビュー |
| `skills/okf-docs/` | OKF v0.2に従う文書の作成・更新・検証 |

共通指示には `applyTo` を付けません。詳細手順はスキルと同梱資料に置きます。[インストラクションのテンプレート](../templates/instructions.md)と[スキルの編集指示](../../skills/AGENTS.md)を参照します。スキルの作成・改善には外部依存の `skill-creator` を使います。

原本を編集しても公開版やユーザースコープは更新されません。編集中の原本を適用するための自己更新は行わず、公開後の導入・更新は[README](../../README.md)の利用者向け操作として扱います。生成されたAGENTS.mdは直接編集しません。

### Markdownの整形と投稿

Issue・PR本文・コメントはEmoji付き見出し、対応関係の表、制約のAlertsで構成し、投稿・更新前に本文全体をrumdlで整形・チェックします。GitHub投稿本文にはOKFを付けません。

共通設定は `task-workflow` に同梱され、本リポジトリの `.rumdl.toml` も同じ設定を継承します。MD013・MD033・MD034・MD041のみを無効化し、MD060をcompact、MD076をtightにします。その他のルールは既定のままです。

リポジトリ直下で、継承設定を明示して実行します。

```bash
rumdl check --config .rumdl.toml --deny-config-warnings --fix <変更したMarkdownファイル>
rumdl check --config .rumdl.toml --deny-config-warnings <変更したMarkdownファイル>
```

投稿用の一時本文や配布先での実行は[GitHub向けMarkdownの品質](../../skills/task-workflow/references/markdown-quality.md)に従って設定を明示指定します。`okf-docs` は既存の依存スキル `task-workflow` に同梱された設定・資料を参照するため、両スキルを導入します。

rumdlは自動インストールしません。未導入・旧版の場合は導入方法を示して事前許可を得ます。ダウンロードを伴う一時実行も同様です。未検証の投稿は保留します。

### 原本と配布の検証

原本のYAML・JSON、ルールの移行漏れ、参照先、rumdlと `git diff --check` を確認します。
配布は隔離したユーザースコープで、新規・再導入・旧構成からの更新、手書きAGENTS.md保護を確認します。
各スキルの `evals/evals.json` は外部書き込みを行わず適用判断を確認する例です。時間・トークンの新旧比較結果ではありません。

- [APM: グローバルコンパイル](https://microsoft.github.io/apm/producer/compile/#global-compilation--g)
- [APM: スキルの作成と配布](https://microsoft.github.io/apm/producer/author-primitives/skills/)

### ローカルとCIで同じ検査を実行

Python 3.12、GitHub CLI 2.100.0を使います。依存ツールの導入を承認した環境で、リポジトリ直下から実行します。

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-ci.txt
source .venv/bin/activate
python -m unittest discover -s tests -v
python scripts/check_repository.py
python scripts/skill_smoke.py
```

静的検査は隠しディレクトリを含む原本のMarkdown・相対リンク・YAML・JSON・必須メタデータ・評価データを確認します。導入検証は一時ディレクトリで `gh skill` の列挙、新規導入、強制再導入と原本との内容一致を確認し、終了時に削除します。探索的に内容を読む場合は、次のコマンドで検証用ディレクトリを作れます。

```bash
exploration_dir=$(mktemp -d)
gh skill install . --from-local --all --dir "$exploration_dir"
```

表示された導入先で各SKILL.mdと同梱リンクを読み、使いにくい指示や不足を確認します。終了後はその検証用ディレクトリだけを削除します。エージェントによる読み取り専用模擬評価は別途行い、形式検査や導入成功をスキルの判断品質の証明とは扱いません。

GitHub Actionsは全ブランチへのpush、main向けPR、mainへの統合後、手動実行で検査します。`static-checks` 成功後にUbuntu・macOSの `acceptance` を並列実行し、失敗をマージで持ち越しません。必須チェックの定義は [.github/required-checks.json](../../.github/required-checks.json) です。初回の実行成功後、管理者が既存ルールを保持してmainの必須チェックに反映し、ジョブ名の変更時も両方を更新します。

[CIの実践](https://continuousdelivery.com/foundations/continuous-integration/)と[継続的テスト](https://continuousdelivery.com/foundations/test-automation/)に基づく基盤です。APMの導入・更新・復旧と固定候補の選び方は[配布ガイド](#検証と証跡)を参照します。

### GitHub上のレビュー用配置

ローカル導入とGitHub上の配置は別です。個人環境への導入だけでGitHubのレビューがスキルを利用できるとは扱いません。

| 利用先 | 配置・読み込み |
| --- | --- |
| ローカル | `gh skill` またはAPMで導入した `code-review` をレビュー実行時に読む |
| Copilot GitHubレビュー | 原本 `skills/code-review/` の実行時ファイルを `.github/skills/code-review/` へ同期する。`evals/` はコピーしない |
| Codex GitHubレビュー | root `AGENTS.md` の条件付き参照に加え、依頼にも原本パスと適用指示を含める。ネイティブなスキル自動探索の保証ではない |

```bash
python scripts/sync_review_skill.py
python scripts/sync_review_skill.py --check
gh skill install . --from-local code-review --dir /tmp/review-skill-install
```

同期先は生成専用です。原本を編集して同期し、両方をコミットします。CIで内容差分・欠落・余分なファイルを検出します。レビュー依頼・指摘対応・完了判定は[task-workflow](../../skills/task-workflow/references/review-and-merge.md#代替レビュー)が担当します。

[Copilot公式資料](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/request-a-code-review/use-code-review#mcp-servers-and-agent-skills)に従い、実PRの指摘の出典またはセッションログで使用したスキルを確認します。[Codex公式資料](https://learn.chatgpt.com/docs/third-party/github)によるAGENTS.mdの案内も、実PRで読み込みを検証します。通常の `@codex review`、確認できなければ原本パスを付けた依頼を順に試し、ログまたは固有手順の根拠付き適用を確認します。後者のみ成功ならパス指定を標準にし、いずれも未確認なら連携未完了とします。結果と未確認範囲はPRに記録し、パス復唱やリアクションだけを成功の証拠にしません。

標準の依頼は `@codex review` に「`skills/code-review/SKILL.md` を読んで適用してください」を添えます。[実PRの検証](https://github.com/daiksud/agents/pull/34#issuecomment-5627514742)では、明示パス指定時に[セッションログ](https://chatgpt.com/codex/cloud/tasks/task_e_6aa34c1893508327b2c83f674db370e8)で原本本文の読み取りを確認しました。ログの閲覧には権限が必要です。条件付き参照だけの通常依頼では読み取りの証拠を確認できていません。

レビュー連携を設定・変更した場合だけ、通常依頼と原本パス付き依頼の読み込みを検証します。先行レビューの終了を確認してから次を依頼し、ログのファイル読み取り、または固有の判断手順が具体的根拠に適用された結果を確認します。通常レビューに証明用の定型報告を要求しません。両方未確認なら連携未完了として記録します。

APMのパッケージキャッシュにルートやディレクトリ別のAGENTS.mdが保存されることと、共通指示として実行時に適用されることを区別します。生成されたCodex・Copilotの本文は共通指示の原本と照合し、配布スキルにはローカル編集指示への依存がないことを確認します。
