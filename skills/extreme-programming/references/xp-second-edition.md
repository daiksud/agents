# XP第2版の価値・原則・プラクティス

開発中の問いを手掛かりに、該当する項目を開く。たとえばテストの結果を待つ間にほかの作業が増えるなら、変更を分割できるかを Baby Steps で考え、ビルド自体に時間がかかっていれば Ten-Minute Build を参照する。

項目の名称と分類は Kent Beck、Cynthia Andres 著『Extreme Programming Explained: Embrace Change』第2版の第4・5・7・9章に基づく。各ページの開発例は、そこで扱う考え方を具体化したもの。[原著の目次](https://www.informit.com/store/extreme-programming-explained-embrace-change-9780134051987)・[日本語版の詳細目次](https://www.ohmsha.co.jp/book/9784274217623.html)

## 価値

何を大切にして判断するか。目的は合っているのに意見が割れるときは、それぞれの案が守ろうとしているものを確かめる。

| 項目 | こんなときに読む |
| --- | --- |
| [Communication（コミュニケーション）](values/communication.md) | 同じ用語から異なる結果を想像している |
| [Simplicity（シンプリシティ）](values/simplicity.md) | いま設計に加える仕組みの範囲を決めたい |
| [Feedback（フィードバック）](values/feedback.md) | 実装や利用者についての予想を確かめたい |
| [Courage（勇気）](values/courage.md) | 途中で前提が崩れ、進め方を変える必要がある |
| [Respect（リスペクト）](values/respect.md) | 影響を受ける人の知識や制約を設計に生かしたい |

## 原則

その状況で価値をどう行動に結びつけるか。たとえばフィードバックを早く得たいなら、まず結果を観測できる大きさまで変更を小さくする。

| 項目 | こんなときに読む |
| --- | --- |
| [Humanity（人間性）](principles/humanity.md) | 特定の人に負担が集中している |
| [Economics（経済性）](principles/economics.md) | 今決める費用と、判断を後に延ばす費用を比べたい |
| [Mutual Benefit（相互利益）](principles/mutual-benefit.md) | 今の作業と将来の保守の両方に役立つ手があるか |
| [Self-Similarity（自己相似性）](principles/self-similarity.md) | 小さな範囲で役立った方法を別の規模でも試したい |
| [Improvement（改善）](principles/improvement.md) | 全体を作り直す前に一つ良くしたい |
| [Diversity（多様性）](principles/diversity.md) | 一つの視点で見落とした条件を探したい |
| [Reflection（ふりかえり）](principles/reflection.md) | 実際に起きたことから次の試みを決めたい |
| [Flow（流れ）](principles/flow.md) | 着手した仕事が途中で滞っている |
| [Opportunity（機会）](principles/opportunity.md) | 繰り返す困りごとを改善のきっかけにしたい |
| [Redundancy（冗長性）](principles/redundancy.md) | 一つの対策をすり抜ける失敗に備えたい |
| [Failure（失敗）](principles/failure.md) | 安全な範囲で未知の条件を試したい |
| [Quality（品質）](principles/quality.md) | 納期が迫るなかで品質を保ちたい |
| [Baby Steps（ベイビーステップ）](principles/baby-steps.md) | 次の変更を試して戻せる大きさにしたい |
| [Accepted Responsibility（責任の引き受け）](principles/accepted-responsibility.md) | 誰が何を判断し、どこまで引き受けられるか |

## 基本プラクティス

日々の作業で何を試すか。結果を知るのが遅いときは、対話、テスト、統合のどこで待ちが生まれているかを見て選ぶ。日本語版の第7章では「主要プラクティス」と呼ぶ。

| 項目 | こんなときに読む |
| --- | --- |
| [Sit Together（全員同席）](primary-practices/sit-together.md) | 小さな疑問が長い返事待ちになる |
| [Whole Team（チーム全体）](primary-practices/whole-team.md) | 成果を届けるのに必要な知識がチームに足りない |
| [Informative Workspace（情報満載のワークスペース）](primary-practices/informative-workspace.md) | 進捗や失敗を問い合わせずに知りたい |
| [Energized Work（いきいきとした仕事）](primary-practices/energized-work.md) | 集中して良い判断を続けられる働き方を選びたい |
| [Pair Programming（ペアプログラミング）](primary-practices/pair-programming.md) | 二者が同じ変更を一緒に考える進め方を知りたい |
| [Stories（ストーリー）](primary-practices/stories.md) | 利用者が価値を得られる単位で範囲を切りたい |
| [Weekly Cycle（週次サイクル）](primary-practices/weekly-cycle.md) | 今週届ける成果を選びたい |
| [Quarterly Cycle（四半期サイクル）](primary-practices/quarterly-cycle.md) | 投資先と複数週にまたがるテーマを見直したい |
| [Slack（ゆとり）](primary-practices/slack.md) | 急な仕事を引き受ける余地を計画に持たせたい |
| [Ten-Minute Build（10分ビルド）](primary-practices/ten-minute-build.md) | 変更を確かめるビルドとテストを速くしたい |
| [Continuous Integration（継続的インテグレーション）](primary-practices/continuous-integration.md) | 他の変更と組み合わせた結果を早く知りたい |
| [Test-First Programming（テストファーストプログラミング）](primary-practices/test-first-programming.md) | 次に実装する振る舞いを一つ決めたい |
| [Incremental Design（インクリメンタルな設計）](primary-practices/incremental-design.md) | 増えた要求に合わせて設計を育てたい |

## 導出プラクティス

基本プラクティスで培った協働や技術を前提に、どこまで進めるか。項目ごとに、始める条件と、効果を判断できる人を確かめる。

| 項目 | こんなときに読む |
| --- | --- |
| [Real Customer Involvement（本物の顧客参加）](corollary-practices/real-customer-involvement.md) | 実際に使う人の経験を優先順位に反映したい |
| [Incremental Deployment（インクリメンタルなデプロイ）](corollary-practices/incremental-deployment.md) | 稼働中の仕組みを少しずつ入れ替えたい |
| [Team Continuity（チームの継続）](corollary-practices/team-continuity.md) | 案件が変わっても協働してきた知識を生かしたい |
| [Shrinking Teams（チームの縮小）](corollary-practices/shrinking-teams.md) | 生まれた余力を別の仕事にも生かしたい |
| [Root-Cause Analysis（根本原因分析）](corollary-practices/root-cause-analysis.md) | 不具合が繰り返される仕組みを変えたい |
| [Shared Code（コードの共有）](corollary-practices/shared-code.md) | 担当範囲を越えて必要なコードを直せるようにしたい |
| [Code and Tests（コードとテスト）](corollary-practices/code-and-tests.md) | 維持すべき振る舞いを実行できる形で伝えたい |
| [Single Code Base（単一のコードベース）](corollary-practices/single-code-base.md) | 同じ製品の修正を複数系統に繰り返している |
| [Daily Deployment（デイリーデプロイ）](corollary-practices/daily-deployment.md) | 日々の変更を本番で確かめたい |
| [Negotiated Scope Contract（交渉によるスコープ契約）](corollary-practices/negotiated-scope-contract.md) | 期限や費用の枠内で価値の高い仕事を選び直したい |
| [Pay-Per-Use（利用都度課金）](corollary-practices/pay-per-use.md) | 実際の利用と対価を結びつけたい |
