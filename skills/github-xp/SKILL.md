---
name: github-xp
description: >-
  GitHubを活用してエクストリームプログラミングを実践するときに使う。
  機能要求と受け入れ条件の合意、Feature Issueの作成・更新、
  Task Issueへの分割とSub-issueの登録、Pull Requestの作成・統合、
  IssueステータスやGitHub Projectsを使った作業の選択、Stacked PRの活用、CI失敗時の復旧をガイドする。
---

# GitHubでエクストリームプログラミングを実践する

利用者と要求を合意し、人間同士のペアで小さな変更を積み重ね、継続的にメインラインへ統合する。得られたフィードバックをもとに要求、計画、設計を見直す。IssueやPRの作成、タスクの消化、進捗の記録そのものを目的とせず、管理の手間によってフィードバックや統合を遅らせない。

## 作業の単位

| 成果物 | 記録する内容 |
| --- | --- |
| Feature Issue | 利用者が得たい価値、要求仕様、受け入れ条件 |
| Task Issue | 次の小さな成果と完了条件 |
| Pull Request（PR） | 実際の変更、判断理由、検証結果、対象のTask Issue |

IssueとPRは既存のものを確認し、重複して作らない。FeatureとTaskはIssueの役割を表す。リポジトリで対応するIssue typeを使える場合は利用し、使えない場合は既存の規約に従う。

対象リポジトリ、メインライン、既存の運用、依頼の範囲を確認する。要求の整理だけを依頼された場合は実装へ進まない。実装・統合は依頼された範囲で行い、リポジトリの保護ルール、権限、マージ条件を守る。

## Feature Issueで要求を合意する

利用者に提供する機能の要求をFeature IssueとしてGitHubにオープンし、対話を通じて以下を明確にする。

- 背景と目的: 誰がどんな状況で何を達成したいか。
- 要求仕様: 必要な振る舞い、業務ルール、制約。
- 受け入れ条件: 具体的な状況、操作、観察できる結果。

要求が大きければ、利用者が試せる小さなストーリーに分ける。実装方法や全Taskの詳細を事前に確定させる必要はない。要求仕様と受け入れ条件を利用者または依頼者と合意してから、その範囲の実装に着手する。新しい知見が得られたら対話し、Feature Issueを更新する。合意した要求を凍結しない。

## 次のTask Issueを決める

Featureの受け入れ条件と先行する変更の結果をもとに、次に達成する小さな成果を人間のペアで決める。そのTask IssueをFeature Issueの[Sub-issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/adding-sub-issues)として登録し、親子関係を確認する。登録できない場合は未登録であることと理由を伝える。

Taskは一つの目的と検証可能な完了条件を持ち、短時間で実装、検証、統合できる大きさにする。技術レイヤーごとの分割よりも、振る舞いや意味のある成果による分割を優先する。既存の振る舞いを保つリファクタリングも一つのTaskにできる。Featureと独立した不具合修正やリファクタリングには、形式のためだけにFeature Issueを作らず、Task Issueで扱ってよい。

## Issueステータスで進捗を共有する

候補は `Backlog`、次に取り組むと合意したら `Todo`、着手したら `In progress`、成果がレビュー段階に入ったら `In review` を目安にする。GitHubの自動更新を活かし、表示と実際の進捗がずれたときに更新する。Featureは機能全体の進捗を示す。一つのTaskがレビュー中でも、ほかの実装が続くFeatureは `In progress` のままでよい。[Issueステータスの仕様](https://docs.github.com/en/issues/tracking-your-work-with-issues/learning-about-issues/about-issue-statuses)

Issueを完了として閉じると `Done` が反映される。取りやめる場合は理由を残して `Not planned` を選び、重複の場合は元のIssueを指定して `Duplicate` を選ぶ。

## GitHub Projectsで次の作業を選ぶ

複数のFeatureやリポジトリを見渡して作業を選ぶときは、目的に合う既存のProjectに対象のIssueを追加する。要求や完了条件はIssueに記録し、ProjectのビューでそのIssueを並べる。共有したい一覧を既存のProjectで作れなければ、新設を提案する。単一リポジトリの進捗を見るには、Issuesのボードも使える。

- 次のTaskを選ぶときは、`Parent issue` でTaskをFeatureごとにまとめ、残っている受け入れ条件を確認する。[親Issueを使うビュー](https://docs.github.com/en/issues/planning-and-tracking-with-projects/understanding-fields/about-parent-issue-and-sub-issue-progress-fields)
- `Status` 別のボードで `In review` のTaskがたまっていたら、新しいTaskを始める前に対象PRのCIと承認を確認し、レビューや統合を進める。

Projectとリポジトリの所有者が同じで、ステータスの同期が有効なら、Issueを完了として閉じるとProjectの同名の `Done` 列にも反映される。その列へ移す操作でもIssueが閉じる。移す前に、必要な変更が統合され、Taskの完了条件またはFeatureの受け入れ条件を満たしたことを確認する。[Projectとの同期](https://docs.github.com/en/issues/tracking-your-work-with-issues/learning-about-issues/about-issue-statuses#syncing-statuses-with-projects)

## 人間同士のペアで実装する

二人の人間がドライバーとナビゲーターを務め、AIへのプロンプト、次に試すテスト、重要な設計判断を対話して決める。AIは二人が共同で使う開発ツールとして、合意した範囲で作業し、結果と知見をペアに返す。AIをペアの代役にせず、事後のPRレビューでペアプログラミングを代替しない。TDDの一歩ごとにIssueやPRを作る必要はない。

## PRを小さく統合する

原則として一つのTask Issueにつき一つのPRを作成する。各PRは、必要なテストが通り、既存の振る舞いを壊さずに統合できる小さな変更とする。未完成の機能を公開すると利用者に不正な振る舞いを提供してしまう場合は、統合と公開を分けるか、変更の切り方を見直す。PRの本文にはTaskへの参照、実際の変更と判断理由、検証結果を書く。

1. 通常のPRでは最新のメインラインから作業ブランチを作り、Taskの目的に沿った小さな変更を実装する。
2. PRを作成し、CIで変更を検証する。必要なチェックと承認を満たしたら速やかにメインラインへマージする。Feature全体の完成を待つ長寿命のFeatureブランチは作らない。
3. 統合後のメインラインと必要な検証結果を確認する。共有のコードや先行するPRの検証に失敗したら、次の変更より復旧を優先する。
4. Taskの完了条件を満たしたことと、必要な変更がすべて統合されたことを確認してTask Issueをクローズする。結果をペアで確認し、Featureの残りの受け入れ条件から次のTaskを選ぶ。

Taskを完了させるPRでは、受け入れに必要な確認がマージ前に済み、デフォルトブランチを対象にしていれば、本文に `Closes #123` と書ける。GitHubはIssueにリンクされたドラフトPRをもとに `In progress`、レビュー可能なPRをもとに `In review` に自動更新することがある。[PRとIssueのリンク](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue)

途中のPRや統合後に検証が必要なPRでは、本文とコミットメッセージに `Refs #123` と書き、自動クローズにつながるリンクを避ける。この参照だけではIssueのステータスも自動更新されない。Task全体がレビュー段階に入ったら必要に応じて `In review` にし、完了条件を確認してから閉じる。

## 必要に応じてStacked PRを使う

一つのTaskをさらに小さく統合できる場合は、複数のPRに分けてよい。先行するPRのCIや承認を待つ間に、その変更に依存する次の変更を進める場合は[Stacked PR](https://docs.github.com/en/pull-requests/get-started/about-stacked-prs)を活用できる。依存関係のない変更や通常のPRで十分な場合はスタックを作らない。

- 最下段のPRはメインラインを、後続のPRは直下のPRの作業ブランチをベースにする。各PRで対象のTask Issueを参照し、そのPRで追加する変更を示す。
- GitHubのネイティブのStacked PRを利用できる場合は、[公式の手順](https://docs.github.com/en/pull-requests/get-started/stacked-prs-quickstart)に従って依存関係を登録する。利用できない場合は通常のPRを順に統合する。
- GitHubでは、選択したPRとその下にある未統合のPRがすべて一緒にマージされる。未統合のうち最下段のPRを選び、必須チェックと承認を満たしたら、その1件を速やかに統合する。[Stacked PRのマージ仕様](https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/merging-stacked-pull-requests)
- 先行PRの変更や統合後は、後続PRのベース、差分、CI、承認の状態を確認し、必要に応じて更新する。保護ルールを回避しない。
- 先行PRの失敗を放置して後続の変更を積み上げない。未統合の変更を増やす負担が待ち時間を減らす効果を上回るなら、通常のPRに戻す。

## Featureの受け入れ条件を検証する

各Taskを統合した結果としてFeatureの受け入れ条件を満たすかを、利用者または依頼者が確認できる形で検証する。合意した条件ごとに実際の結果と未確認の範囲を伝え、不足があれば次のTaskを決める。

必要な変更がすべてメインラインに統合され、受け入れ条件を満たしたことを確認してFeature Issueをクローズする。Sub-issueの進捗が100%になったことだけを完了の根拠にしない。統合と機能のリリースは区別し、リリースが受け入れ条件に含まれる場合はその結果も確認する。

## 進め方の例

窓口担当者が予約を確認できる機能をFeature Issueにし、予約一覧を表示できることと、予約番号で絞り込めることを受け入れ条件として合意する。

まず予約一覧を表示するTaskを作ってFeatureのSub-issueに登録し、人間のペアでテストと実装を進め、PRを統合する。その結果を確認してから、予約番号で絞り込むTaskへ進む。必要なら後者のTaskを小さなPRに分けて統合する。最後に窓口担当者が行う操作から両方の受け入れ条件を検証し、Featureを完了する。
