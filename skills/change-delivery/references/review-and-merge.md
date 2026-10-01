---
type: Instruction
title: レビューとマージ
description: PR作成、レビュー対応、CI確認、リベース、スカッシュマージと作業環境の整理の手順を定めます。
sources:
  - id: docs-request-a-code-review-use-code-review
    resource: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/request-a-code-review/use-code-review
  - id: github-graphql-pulls
    resource: https://docs.github.com/en/graphql/reference/pulls
  - id: github-installed-apps
    resource: https://docs.github.com/en/apps/using-github-apps/reviewing-and-modifying-installed-github-apps
  - id: github-app-installation-api
    resource: https://docs.github.com/en/rest/apps/apps#get-a-repository-installation-for-the-authenticated-app
  - id: github-app-user-installations
    resource: https://docs.github.com/en/rest/apps/installations#list-app-installations-accessible-to-the-user-access-token
  - id: codex-github-review
    resource: https://developers.openai.com/codex/integrations/github
  - id: github-app-user-access
    resource: https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/generating-a-user-access-token-for-a-github-app
  - id: ruleset-rules
    resource: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets
  - id: code-owners
    resource: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners
  - id: approval-code-owner-exception
    resource: https://github.com/daiksud/agents/issues/165
---

## レビューとマージ

### PRとレビュー

- 明示された停止条件がなく、変更作業の実行承認とプッシュ済み差分がある場合、PR作成は任意の追加作業ではなく直後の既定工程とする。PR作成の可否を再質問せずドラフトPRを作成する。
- PR作成後もレビュー、指摘修正、再検証、CI・競合確認、マージ、統合後確認まで継続する。レビュー待ちやCI待ちを完了報告にせず、利用可能な待機・再取得手段で状態を確認する。
- プッシュ後にドラフトPRを作成し、対象のIssueまたはSub-issueに紐づける。
- PRのAssigneeには、Issueで確認したタスク指示者を設定する。特定できない場合はユーザーに確認し、認証ユーザーを無条件に指示者とみなさない。
- PR作成時はリポジトリのラベル一覧と説明を確認し、変更内容に合うラベルを設定する。
- PR本文には最終的な変更内容、変更が必要な理由、検証結果と未確認範囲を書く。重要な制約・対象外も明示する。導入先の指定テンプレートに従い、指定がなければ必要な構成を選ぶ。固定見出し・不要な表やAlerts・空の節・「なし」の埋め草を要求しない。
- 投稿・更新・レビュー返信は依存スキル `issue-management` の「GitHub向けMarkdownの品質」に従い、本文全体を整形・チェックし、保存後に本文一致と表示を確認する。
- レビュー対応で目的・成果・受け入れ条件や外部影響を変える場合は、縮小も含め依存スキル `issue-management` の「計画と実行範囲」に従って具体案を保存・提示して確認する。同じ成功条件を満たすファイル・手順の調整は記録して継続する。
- 承認済み範囲でレビューとその対応により変更内容・理由・検証結果・重要な制約に変化があった場合は、対応と同時にPR本文を更新する。
- 変更内容が変わった場合はPRのラベルも見直す。
- ドラフトPRでは [レビュー候補の高速判定](#レビュー候補の高速判定)でCopilot Code Review[^docs-request-a-code-review-use-code-review]を優先して選ぶ。Codexを選ぶ場合は「代替レビュー」に従う。
- Copilotへの依頼にはこの文書の「Copilot Code Reviewの依頼」を使用する。
- 外部レビュアーへ適用するレビュー方針は、対象リポジトリ自身のInstructions・レビューガイド・Skill・テンプレート等を優先する。APMでローカルに導入された `daiksud/agents` の `code-review` を、別リポジトリのCopilot Code ReviewやCodex Reviewへ追加指示として渡さない。対象リポジトリ自身にレビュアー向け資料がある場合だけ、そのリポジトリ内の原本を案内できる。`daiksud/agents` 自身のレビューでは、このリポジトリ内の `skills/code-review/SKILL.md` を対象リポジトリ自身の方針として案内できる。
- 初回・再レビューの依頼後は、レビュー完了までセルフレビューを行う。
- セルフレビューで修正すべき点を見つけたら、修正・検証・コミット・プッシュしてPRを更新する。
- レビュー待ちの間に、CIの結果とコンフリクトの有無を確認する。
- CIが未設定の場合は、既存のマージ例外としてCI条件を満たしたと扱う。[CI未設定の場合](#ci未設定の場合)に従い、実行成功とは区別する。
- CIの失敗やコンフリクトがあれば、修正・検証・コミット・プッシュしてPRを更新する。
- レビュー指摘は、現在の要求・契約との不一致、根拠の確かさ、発生条件、具体的な影響を確認し、正式な修正指摘、任意提案、追加調査、対応不要を判断する。重要度・緊急度・発生可能性・対応コストは優先順位や修正方法の判断に使い、レビュアーの分類や承認状態だけで採否を決めない。
- 再現に必要な前提条件の多さ、再現頻度の低さ、再現の難しさだけを対応不要の理由にしない。現行契約との不一致と具体的な影響を根拠から説明できる指摘は、発生条件が限定的でも正式な修正指摘として扱う。成立条件や根拠が不足する場合は追加調査とし、推測だけで修正もしない。
- レビュー結果で「Suppressed comments」などと分類された指摘も同じ基準で内容を評価する。抑制という分類やCopilotのApprove有無だけで修正要否を決めない。Approve未取得時の扱いは次の「抑制指摘とApprove未取得時の扱い」に従う。
- レビューへの返信は次の「返信の記載先と公開手順」に従い、個別指摘への回答とレビュー全体への説明を分ける。
- 修正する指摘は、修正・検証・コミット・プッシュした後に再レビューを依頼する。
- セルフレビューやCI対応、リベースでレビュー対象のコミットが変わった場合も、最新コミットへの再レビューを依頼する。
- 対応が必要な指摘がゼロになるまでレビューと修正を繰り返す。
- Copilotを選んだ場合は最新コミットのApproveを得るまで完了としない。「レビュー候補の高速判定」でCodexを選んだ場合はCodexの完了条件を適用する。候補判定をレビュー完了の代わりにしない。

### レビュー候補の高速判定

ここで判断するのは依頼先の候補であり、利用枠・実行成功・レビュー完了の保証ではない。Codexも導入確認だけでレビュー完了とはせず、依頼後の実行結果を確認する。[^codex-github-review]

| 状態 | 意味 |
| --- | --- |
| `available` | Copilotのレビュー候補・依頼受理、または対象repoへのCodex Connector導入を確認できた。依頼先として選べる |
| `unavailable` | Copilotの候補なし、対象repoへのConnector未導入・対象外、またはサービス固有の明示的な利用不能を確認した。この選択では候補から除外する |
| `unknown` | 権限不足、取得失敗、不完全な一覧、確認手段の非対応などで候補を判定できない。未導入・利用不能と断定しない |

事前確認は下記の手順を各サービスにつき最大1回実施する。Copilotを先に確認し、選べるならCodexを調べない。判定・対象repo・認証条件・根拠・確認日時をタスク内で保持し、同じ条件で設定画面・契約・利用枠・別APIを探し直さない。対象PRが変わればCopilot、対象repoや認証・導入設定が変われば関連する判定を更新する。HEAD更新だけでConnectorの導入確認を繰り返さない。永続キャッシュや専用設定は追加しない。

同じHEADへの依頼が既にある場合は、先に依頼履歴・Botの実行状態・完了済みレビューを確認する。Copilotは [依頼後の実行状態を確認する](#copilot依頼後の実行状態を確認する) に従い、進行中なら通常の完了待ちを続ける。受理されたか不明なら状態を1回取得し、それでも不明なら再依頼や切替を止め、未確認範囲と再開条件を記録する。候補探索の上限を、受理済みレビューやCIの通常の進捗確認に適用しない。

- 未依頼でCopilotが `available` ならCopilotへ依頼する。
- Copilotが `unavailable` または `unknown` で、Codexが `available` ならCodexを選ぶ。前者の理由は「候補なし」「利用不能」、後者は「候補確認不能」と区別し、恒久的な利用不能を証明する追加調査や切替の再承認を要求しない。依頼済みの進行中・受理不明をこの条件で迂回しない。
- 両方とも `available` でなければ探索を打ち切る。セルフレビュー・CI確認は継続できるが、外部レビュー完了やマージ可とは扱わない。必要な導入・権限・確認手段をブロッカーとして報告し、保護設定を緩めない。

#### Copilotの候補を1回取得する

対象PRの `suggestedReviewerActors` を照会する。これはレビュー候補のAPIであり、Issue担当者用の `suggestedActors` を代用しない。[^github-graphql-pulls]

`OWNER`・`REPO`・`PR_NUMBER` を対象に置き換える。以下は読み取りだけで、レビューを依頼しない。

```bash
OWNER=daiksud
REPO=agents
PR_NUMBER=123

gh api graphql \
  -f owner="$OWNER" -f name="$REPO" -F number="$PR_NUMBER" \
  -f query='
    query($owner: String!, $name: String!, $number: Int!) {
      repository(owner: $owner, name: $name) {
        pullRequest(number: $number) {
          suggestedReviewerActors(first: 100, query: "copilot") {
            nodes {
              reviewer {
                __typename
                ... on Bot { login }
              }
            }
            pageInfo { hasNextPage }
          }
        }
      }
    }
  ' \
  --jq '
    if ((.errors // []) | length) > 0
       or .data.repository.pullRequest == null then "unknown"
    else
      .data.repository.pullRequest.suggestedReviewerActors
      | if (.nodes | type) != "array" then "unknown"
        elif any(.nodes[]?.reviewer;
          .__typename == "Bot"
          and .login == "copilot-pull-request-reviewer") then "available"
        elif .pageInfo.hasNextPage == false then "unavailable"
        else "unknown"
        end
    end
  '
```

コマンド失敗・GraphQLエラーは `unknown` とする。候補なしはこの選択での除外根拠であり、契約全体の利用不能の証明ではない。ページが残るのに見つからない場合も `unknown` とし、探索のための追加ページ取得は行わない。

候補照会を提供しない実行環境では、未依頼を確認したうえで「Copilot Code Reviewの依頼」の正式APIを1回だけ判定兼依頼として使ってよい。成功は依頼受理として記録して完了待ちへ進み、確認目的で再送しない。利用枠上限・無効化などの明示的な利用不能だけを `unavailable` とし、汎用的な403・422・通信失敗だけでサービス利用不能を断定しない。失敗後に別の候補APIを探索しない。

#### Codex Connectorの対象repoへの導入を確認する

`ChatGPT Codex Connector`（slug: `chatgpt-codex-connector`）が対象repoのインストール済みGitHub Appに含まれるかを確認する。既に対象repoについて確認済みの導入結果、または下記の同一タスクの成功イベントがあれば先に再利用する。どちらもなければ、利用可能な認証済みGitHub設定画面のGitHub Apps、または対象repoの導入情報を返す既存ツールのいずれか1つを使う。対応する確認手段がなければ呼び出しを試行錯誤せず `unknown` とする。[^github-installed-apps]

上記の既存ツールには、同一タスク・同じ認証条件で対象repoへの既存操作が成功した際の、GitHubの返却データや既知のイベントを読む方法も含む。`performed_via_github_app.slug` が `chatgpt-codex-connector` と一致し、対象repo・操作時刻・今回の成功操作との対応を確認できれば `available` の根拠として再利用する。Appとユーザーの双方がアクセスできるリソースに限定される仕組みに基づく運用上の判定であり、導入一覧の直接取得やレビュー成功の保証とは区別する。コメント本文の自己申告や過去タスクの記録は代用せず、確認だけのためのラベル変更・コメント投稿などの書き込みは行わない。[^github-app-user-access]

対象repoへの導入を確認できれば `available`、完全な対象一覧で未導入・対象外と確認できれば `unavailable` とする。アカウント単位の情報を使う場合はownerの一致と、All repositoriesまたはSelected repositoriesに対象repoが含まれることまで確認できなければ `unknown` とする。明示的に停止・無効化されていれば `unavailable` とする。公開Appページの存在、過去のBotコメント、ローカルの `codex login status` は現在の対象repoへの導入証拠にしない。

通常の `gh` ユーザートークンで `GET /repos/{owner}/{repo}/installation` を汎用のApp一覧APIとして使わない。このAPIは確認対象App自身のJWTを必要とする。`GET /user/installations` も認証したGitHub Appの導入情報であり、無関係なAppを横断する確認には使わない。これらの認証条件を満たさない環境で、別トークン・別API・ブラウザ内部APIの探索を続けない。[^github-app-installation-api][^github-app-user-installations]

### 代替レビュー

レビュー依頼と完了判定は本手順が担当する。差分をレビューするときだけ `code-review` を読み、そのスキルから依頼・修正・マージを開始しない。

1. 「レビュー候補の高速判定」でCodexを選んだ理由、CopilotとCodexの判定、証拠URLまたは取得結果、確認日時をPRに記録する。Copilotへの依頼後に明示的な利用不能が判明した場合も、その結果を保持して同じ選択手順へ進む。利用不能と候補確認不能を混同せず、切替の都度ユーザー承認を求めない。
2. 指摘への不同意、Approve未取得、単なる待機時間、一時的な結果取得失敗だけを切替理由にしない。依頼済みのレビューは「レビュー候補の高速判定」の進行中・受理不明の手順に従い、同じHEADへの依頼を重複させない。
3. PRコメントで `@codex review` を依頼する。対象リポジトリ自身にレビュアー向けInstructions・ガイド・Skill等があり、外部レビュアーから読める場合だけ、そのリポジトリ内の原本パスと適用指示を添える。APMでローカルに導入された共通 `code-review` や、その原本が別リポジトリにあるという理由だけで追加指示しない。対象リポジトリに固有のレビュー資料がなければ、Codex自身の通常レビューに委ねる。送信前後に依頼コメントを確認し、タイムアウト時も保存済みの可能性を調べてから再送する。新しい依頼が必要なのは未送信の確認、HEAD変更、または失敗原因を解消して再実行するとき。

### Codexの完了判定

以下のすべてを満たすまでレビューは未完了とする。修正・リベースでHEADが変われば再レビューする。

| 確認対象 | 必要な根拠 |
| --- | --- |
| 投稿者・実行結果 | Codex Bot本人のサマリー・レビュー本文・指摘・依頼コメントと紐づくセッションを突き合わせ、正常完了を明示的に確認する。失敗・中断・実行中は除外する |
| 対象コミット | レビューの対象SHAが現在の完全HEAD SHAに一致する。短縮SHAはリポジトリのコミットで一意に完全SHAへ解決する。依頼時HEADだけから対象SHAを推測しない |
| 残る指摘 | 今回だけでなく過去の通常指摘・レビュー本文の指摘も確認する。Copilotから引き継いだ要対応指摘も修正・公開返信・Resolveまで追跡する |
| マージ条件 | CI、競合、公開返信、スレッド解決、リポジトリ側の必須承認を確認する。Codex切り替えを理由に保護設定を緩めない |

👀、👍、コメント件数、第三者の「完了」という記述だけでは正常完了・対象SHA・指摘解消を判定しない。SHA不明や結果取得失敗は未完了として、未確認範囲と再開条件を記録する。

Codexの「重大な問題なし」はそのレビュー範囲の結果であり、公式に案内されるP0・P1中心のレビューを全品質の保証とは扱わない。CopilotのApproveとCodexの正常完了を同じ承認イベントと表現しない。

### Copilotが人手確認を求めた場合

Copilot Code Reviewのサマリー・レビュー本文・指摘で「人手の確認が必要」「human review required」など、人間による確認・判断へのエスカレーションが明示された場合は、通常のApprove未取得やCopilotの利用不能と区別する。

- 人手確認要求を `unavailable` と扱わず、Codex Reviewへの切り替えや別Botのレビューで代替しない。
- 任意のユーザー・チーム・第三者へレビュー依頼を追加しない。Issue・PRで確認したタスク指示者を原則の人手レビュー先とし、GitHub上で本人を特定でき、レビュー依頼可能な場合はその本人にだけ依頼する。認証ユーザーやリポジトリ所有者を無条件に指示者とみなさない。
- タスク指示者を特定できない、本人へレビュー依頼できない、または別の人間の判断が必要な場合は、代わりのレビュアーを推測せず、必要な判断と理由を示して指示者またはユーザーへ戻す。
- 必要な人手確認が未解決の間はマージしない。指示者レビューによる修正でHEADが変わった場合は、通常の最新HEADレビュー手順へ戻る。

### 必須ApproveとCODEOWNERSの判定

Rulesetの `required_approving_review_count` と `require_code_owner_review` を別の条件として確認する。前者はPR全体で必要なApprove数、後者は変更パスに適用されるCode Ownerレビュー要件である。Code Ownerが複数いる場合はいずれか1人のApproveでCode Owner要件を満たす。設定値だけでブロック状態を推測せず、PR author、変更パスに適用されるCODEOWNERS、最新review state、GitHubのmergeabilityを照合する。[^ruleset-rules][^code-owners]

変更パスに適用されるCode Ownerが1人だけで、その本人がPR authorの場合は、本人の自己Approveや存在しない別Code Ownerを待たない。このケースではGitHubの実効判定上、Code Owner以外の有効なApproveで必須Approve数を満たせるため、別の有効なApproveとGitHubのマージ可否を確認して先へ進む。Copilot Approvalsが有効で、最新HEADに対するCopilotレビューが `APPROVED` として必須承認に数えられている場合は、そのApproveで問題ない。既定のコメントだけのCopilotレビューはApproveとして扱わない。[^approval-code-owner-exception][^docs-request-a-code-review-use-code-review]

この例外は、Copilotが明示的にhuman reviewを要求した場合、未解決のRequest changes、最新pushを別主体が承認する要件、その他GitHubが未充足としている保護条件を迂回しない。満たせない保護条件が残る場合は、CODEOWNERS設定を緩めたり任意の人間へレビュー依頼したりせず、実際に未充足の条件を特定する。

### 抑制指摘とApprove未取得時の扱い

「Suppressed comments」などの抑制指摘は、Approveの有無にかかわらず通常のレビュー指摘と同じ基準で採否を判断する。この節は、最新コミットのCopilotレビューが完了してもApproveが得られていない場合のマージ条件の扱いだけを定める。CopilotのApprove必須というマージ条件は維持し、Approve取得を指摘の妥当性の根拠にしない。

1. レビュー対象のコミットと完了状態、Approveの有無を確認し、過去の通常指摘と抑制指摘を含めて未対応の正式な修正指摘がないことを確認する。「新規コメント0件」だけでは判定しない。レビュー未完了・取得失敗は承認済みとも、指摘なしとも扱わない。
2. 抑制指摘を、現在の要求・契約との不一致、根拠、発生条件、具体的な影響から評価する。正式な修正指摘なら通常のレビュー対応へ戻し、根拠不足なら追加調査する。追加調査に必要な証拠を取得できない場合は、不足する証拠と未確認範囲を示してユーザー判断に戻し、Approve再取得のための再レビューへ進まない。現状が契約を満たす任意提案や対応不要の指摘は、Approve取得だけを目的に必須修正へ引き上げない。
3. 正式な修正指摘が承認済み範囲に収まる場合は、追加確認なしで修正・検証・コミット・プッシュする。目的・成果・受け入れ条件や外部影響・権限を変える場合は、依存スキル `issue-management` の「計画と実行範囲」に従って確認する。
4. 未対応の正式な修正指摘と未解決の追加調査がなくてもApproveが得られていない場合は、修正内容・検証結果、または任意提案・対応不要と判断した根拠を、対象レビューへのリンク付きレビュー全体コメントに記録する。次の「返信の記載先と公開手順」に従って公開を確認してから再レビューを1回依頼する。公開未確認なら依頼せず、再開時は公開済みコメントと依頼履歴を確認して重複を避ける。
5. この再レビューでも同じ任意提案または対応不要の指摘を理由にApproveが得られない場合は、承認目的だけの修正や自動再依頼を繰り返さない。指摘の採否判断は維持したまま、判断根拠・実施済み対応と残る選択肢を提示してユーザー判断に戻す。新しい指摘は同じ基準で改めて評価するが、同じ論点への反復制限はリセットしない。

### 返信の記載先と公開手順

レビュアーが各指摘の対応とレビュー全体の説明を適切な場所で確認できるよう、返信を次のように分ける。

| 対象 | 記載先と内容 |
| --- | --- |
| 個別スレッドの指摘 | 対象スレッドに、その指摘の対応内容・変更コミット・検証結果、または対応しない判断理由を書く |
| `Suppressed comments`などレビュー本文にだけ存在する指摘 | レビュー全体コメントに、対象レビューへのリンクと、正式な修正指摘として対応した場合の修正内容・変更コミット・検証結果、または任意提案・対応不要と判断した根拠を書く。Approveの有無で記載要否を変えず、返信先のスレッドを代用しない |
| レビュー全体に関わる説明 | レビュー全体コメントに、対象レビューへのリンクと全体の説明を書く。個別スレッドに混在させない |

1. 指摘を確認し、既存の修正判断基準に従って対応する。修正した指摘では検証・コミット・プッシュまで完了させ、返信の根拠を揃える。
2. 個別返信を保留中のレビューにまとめ、必要なレビュー全体コメントを用意する。全体コメントが不要なら作成を強制せず、個別返信がない場合は全体コメントだけを用意する。
3. 一連の返信をsubmitする。レビュー全体コメントが必要な場合はともにsubmitし、不要な場合は個別返信だけをsubmitする。全体コメントだけの場合もレビューとしてsubmitする。
4. submit後に公開済みの個別返信とレビュー全体コメントを再取得し、対象と内容が正しいことを確認する。保留中の返信やsubmit要求の成功だけを公開確認の代わりにしない。
5. 公開済みの対応内容または対応しない理由を確認できたスレッドだけをResolveする。投稿に失敗した、または公開を確認できないスレッドはResolveしない。再開時は公開済みの返信を確認し、成功済みの投稿を重複させない。

使用するAPIやUIで個別返信を保留中のレビューにまとめてsubmitできない場合は、その制約を報告する。個別返信は対象スレッドに投稿し、全体説明は対象レビューへのリンクを付けたレビュー全体コメントとして別に記録する。全体説明を個別スレッドで代用せず、公開確認後にResolveする順序を守る。レビュー全体コメントも投稿できない場合は未完了として報告し、投稿できた範囲と再開に必要な手段を明記する。

### リベースとマージ

- マージ先の更新を作業ブランチに取り込むときはリベースし、Git履歴をLinear historyに保つ。
- リベース後は関連する検証を再実行し、リモートへプッシュする。
- プッシュ済みの履歴をリベースした場合は `git push --force-with-lease` を使い、リモートに未知の更新があれば上書きせず確認する。
- マージ直前に、最新コミットのレビューが完了し、対応が必要な指摘がゼロ、CIがパス、コンフリクトがゼロであることを確認する。必須ApproveとCODEOWNERSは「必須ApproveとCODEOWNERSの判定」に従い、唯一のCode OwnerがPR authorであることだけを理由に自己Approve待ちへ入らない。
- マージ直前に最新mainのSHAとそのpushで動いた必要チェック・配布検証を再確認する。開始時の確認だけで代用せず、実行中・未確認なら待ち、失敗していれば復旧を優先して通常PRをマージしない。当該失敗を解消する承認済み復旧PRはこのmain成功条件の対象外とし、復旧PR自体のレビュー・必要チェック・必須承認を満たして進める。CIが存在しない場合だけ既存の未設定例外に従う。
- すべての条件を満たしたらドラフトPRをReady for reviewに変更し、スカッシュマージする。
- スカッシュコミットのメッセージも[コミットメッセージの指示](conventional-commits.md)に従う。
- PRがマージ済みで、マージ先の履歴が直線状であることを確認する。

### 統合後mainの確認と復旧

変更担当者はマージ後の確認まで担当する。PRの統合候補とマージ後mainのSHAは異なるため、PRのCI成功だけでmainを検証済みにしない。

1. スカッシュマージのコミットSHAと、そのmainへのpushで動いた必要チェックを照合する。配布検証があるプロジェクトでは公開された同じSHAの導入経路も確認する。
2. 実行中なら完了を待つ。失敗・キャンセル・未実行・結果取得不能は成功にせず、理由と未確認範囲を記録する。必要なCIが起動していない状態を「CI未設定」の例外にしない。
3. 失敗を検出したら通常作業を止め、影響と検知時刻、最後に正常だったSHA、失敗したチェック・ログを記録する。原因変更がある場合は、そのrevertまたは最小修正を独立した復旧PRにする。外部サービス・runnerの一時障害でリポジトリ変更が不要と確認できた場合は、根拠と再試行理由を記録し、障害解消後に同じmain SHAの必要チェック・配布経路を再検証する。空の復旧PRは作らず、成功確認までは後続作業を止める。原因不明なら調査を続け、外部障害と推測で決めつけない。変更不要の場合は手順4〜6を行わず、再検証後の手順7へ進む。
4. リポジトリ変更が必要な復旧計画はIssueへ保存・再取得・提示し、依存スキル `issue-management` の「計画と実行範囲」で実行範囲を判断する。自身の依頼範囲内の回帰修正や明確な復旧依頼では同じ承認を再要求しない。別の目的・受け入れ条件・外部影響・権限を変える復旧は確認し、無関係な障害の実装へ承認を広げない。実行範囲を確認後は差分とworktreeの使用状況を確認して保護し、`git switch main` でmainへ切り替え、`git pull --ff-only` で更新して、そのmainから専用の復旧ブランチを作成する。mainが他worktreeで使用中なら、そこを変更せず `git fetch origin` で取得した `origin/main` のSHAを失敗対象と照合し、現在の作業場所でそのSHAから専用復旧ブランチを作る。未知のmain更新があれば先に確認し、checkoutの保護を強制回避したりマージ済みの旧作業ブランチへ復旧変更を追加したりしない。
5. 欠陥が原因なら再現可能な最も小さい検証を追加し、修正前の失敗と修正後の成功を確認する。コードは `software-development`、スキルの判断は模擬評価を使う。外部障害など再現できない場合は証拠と未検証範囲を記録し、失敗テストを作ったと偽らない。
6. 通常の最新HEADレビュー・公開返信・Resolve・必須承認・必要チェックを通して復旧PRをマージする。保護設定や検査を弱めて正常に見せない。
7. 復旧コミット（変更不要なら再検証した同じmain SHA）の必要チェックと配布経路が成功した時刻を記録し、正常化を確認してから後続作業を再開する。検証できない間は復旧済み・作業全体完了としない。

main復旧時間は失敗検知から復旧コミットの必要チェック（必須の配布検証を含む）がすべて成功するまでとして、APMなどの導入済み環境を正常SHAへ戻す工程時間と分ける。外部障害で変更不要なら同じmain SHAで同じ必要チェックがすべて成功した時刻を終点と明記する。新しい合否閾値を共通スキルで設けず、プロジェクトで決めた目標と実測を記録する。

障害記録には、影響、発生・検知・復旧時刻、確認できた原因、検出できなかった理由、追加した検証、残る改善を短く残す。分からない原因や時刻を推測で確定せず、担当者を責める記録にしない。

### CI未設定の場合

- CIが存在しないプロジェクトでは、マージ条件上の既存例外を維持する。ローカルで行った検証と結果、CIが未設定である事実、例外として扱う旨、CI設定を強く推奨する旨をPRに記録する。
- 例外は「CIを実行して成功した」「CDを達成した」という意味ではない。マージ後もローカル検証など確認できた範囲と限界を示す。
- 既存の必須CI、失敗・キャンセル・未実行のジョブ、取得不能な結果には適用しない。保護ルールを緩めず、設定変更が必要なら承認済み範囲を確認する。

### マージ後の作業環境の整理

- PRのマージを確認したら、作業ツリーに未コミットの変更がないことを確認して `git switch main` を実行する。
- `main` で `git pull --ff-only` を実行する。失敗した場合は原因を確認し、ローカルの変更や履歴を強制的に上書きしない。
- mainが他worktreeで使用中なら、上記の切り替え・pullの代わりに `git fetch origin` 後の `origin/main` とマージSHA・main検証結果を照合し、現在の作業場所を `git switch --detach origin/main` で切り離して下記の削除へ進む。他worktreeやそのローカルmainは変更せず、checkout保護を回避しない。この場合はリモートmainと現在の作業場所の同期を確認して整理完了とし、他worktreeのローカルmainは未更新として区別して報告する。
- マージ済みのリモート・ローカルブランチを確認し、削除する。削除前に対応PRのマージ状態、ブランチ先端とPRの最終コミットの一致、`git worktree list` で使用状況を確認する。
- マージ後に追加コミットがあるブランチや、他のworktreeで使用中のブランチは削除せず、残した理由を報告する。`main` とマージ先ブランチは削除対象に含めない。
- リモートブランチは `git push origin --delete <branch>`、ローカルブランチは `git branch -d <branch>` で削除する。既に削除済みの場合は再実行しない。
- スカッシュマージにより `git branch -d` が拒否された場合は、対応PRのマージと先端の一致を再確認したうえで `git branch -D <branch>` を使う。
- `git fetch --prune origin` の後、`git status --short --branch`、`git branch -vv`、`git ls-remote --heads origin` でmainの同期、作業ツリー、削除対象ブランチが残っていないことを確認する。
- mainの更新やブランチ削除が完了していない場合は、マージ完了と区別して未完了の操作と理由を報告する。

### Copilot依頼後の実行状態を確認する

Copilotへのレビュー依頼後は、`requested_reviewers` と完了済みreviewだけで実行状態を判定しない。レビュー依頼が受理された後、`requested_reviewers` が空になり、まだreview submissionが存在しない期間でもCopilotが実行中であることがある。空配列を「未依頼」「停止」「利用不能」の根拠にしない。

状態は次の順に確認する。

1. `GET /repos/{owner}/{repo}/pulls/{pull_number}/reviews` でCopilotのreview submissionを確認する。対象reviewの `commit_id` が現在のHEAD SHAに一致すれば、そのHEADに対する完了結果として扱う。`APPROVED`・`COMMENTED` 等のstateはそのまま扱い、本文の「Approval recommended」を `APPROVED` に読み替えない。
2. 最新HEADに対する完了reviewがなければ、PRのIssue eventsまたはtimelineを確認する。`requested_reviewer.login` がCopilotの `review_requested` は依頼済み、`performed_via_github_app.slug == "copilot-pull-request-reviewer"` の `copilot_work_started` は実行開始済みのシグナルとして扱う。
3. `copilot_work_started` を確認できたら実行中として待機を継続し、同じHEADへの再依頼やCodexへの切り替えを行わない。
4. `copilot_work_started` が見つからないことだけで未実行とは断定しない。イベント取得権限・ページング・反映遅延などで観測できない可能性があるため、依頼APIの成功、`review_requested`、既存の進行表示など利用可能な証拠を合わせて受理済み・不明を判断する。
5. HEADが更新された場合は、旧HEADの `copilot_work_started` やreview submissionを最新HEADの完了根拠にしない。最新HEADへのレビュー依頼履歴と `commit_id` を改めて確認する。

例として、現在の実行状態を確認するときは次を使える。

```bash
gh api "repos/$OWNER/$REPO/issues/$PR_NUMBER/events?per_page=100" --paginate \
  --jq '.[] |
    select(
      .event == "review_requested"
      or .event == "copilot_work_started"
    ) |
    {
      event,
      created_at,
      requested_reviewer: .requested_reviewer.login,
      app: .performed_via_github_app.slug
    }'

gh api "repos/$OWNER/$REPO/pulls/$PR_NUMBER/reviews" \
  --jq '.[] |
    select(.user.login == "copilot-pull-request-reviewer[bot]") |
    {state, submitted_at, commit_id, html_url}'
```

Issue eventsに現れる `copilot_work_started` は進行確認の運用シグナルとして使い、永続的な公開API契約とはみなさない。取得できない環境では未実行と断定せず、上記の他の証拠で状態を判断する。PR #166 では `requested_reviewers=[]` かつreview未提出の期間にも `copilot_work_started` が記録され、その後reviewが正常完了した。

### Copilot Code Reviewの依頼

「レビュー候補の高速判定」と同じ `OWNER`・`REPO`・`PR_NUMBER` を設定し、次のREST APIを1回呼ぶ。固定Bot IDやPRのNode IDの取得は不要。既存の他のレビュアーを削除しない。[^docs-request-a-code-review-use-code-review]

```bash
gh api --method POST \
  "repos/$OWNER/$REPO/pulls/$PR_NUMBER/requested_reviewers" \
  -f 'reviewers[]=copilot-pull-request-reviewer[bot]'
```

成功応答は依頼受理であり、レビュー完了ではない。依頼後は「Copilot依頼後の実行状態を確認する」に従う。`requested_reviewers` やreviewsが空であることだけを失敗根拠にせず、タイムアウト等で受理が不明でも無条件に再送しない。

[^docs-request-a-code-review-use-code-review]: [Copilot Code Review](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/request-a-code-review/use-code-review)。本文に記した参照範囲と採用判断の根拠。
[^codex-github-review]: [CodexのGitHubレビュー](https://developers.openai.com/codex/integrations/github)。レビューの設定・依頼・結果確認と、導入だけで完了としない判断の根拠。
[^github-graphql-pulls]: [GitHub GraphQL Pull requests](https://docs.github.com/en/graphql/reference/pulls)。PRのレビュー候補取得フィールドと引数の根拠。
[^github-installed-apps]: [Installed GitHub Appsの確認](https://docs.github.com/en/apps/using-github-apps/reviewing-and-modifying-installed-github-apps)。導入済みAppとリポジトリアクセス範囲の確認方法。
[^github-app-user-access]: [GitHub App user access tokenのアクセス範囲](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/generating-a-user-access-token-for-a-github-app)。Appとユーザー双方のアクセス範囲に限定される仕組みと、同一タスクの成功操作を候補判定に使う根拠。
[^github-app-installation-api]: [Repository installation API](https://docs.github.com/en/rest/apps/apps#get-a-repository-installation-for-the-authenticated-app)。確認対象App自身のJWTが必要なAPIの認証条件。
[^github-app-user-installations]: [User access tokenで参照できるinstallations](https://docs.github.com/en/rest/apps/installations#list-app-installations-accessible-to-the-user-access-token)。認証したGitHub Appに限定された導入情報の範囲。
[^ruleset-rules]: [Rulesetで利用できるルール](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets)。必須Approve数とCode Ownerレビュー要件の根拠。
[^code-owners]: [Code Ownersについて](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)。CODEOWNERSの適用と複数owner時の承認条件。
[^approval-code-owner-exception]: Issue #165 で採用した、唯一のCode OwnerがPR authorの場合の実効承認条件。
