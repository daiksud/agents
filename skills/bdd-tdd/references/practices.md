---
type: Reference
title: ふるまいを共有しテストで育てる実践
description: BDD・ATDD・TDDとDDDの関係、具体例、テスト層の選択と一次資料を整理します。
---

## ふるまいを共有しテストで育てる実践

### 関係と適用判断

BDDは具体例による共有理解を育てる協働の実践で、CucumberはDiscovery・Formulation・Automationの反復として説明します。ATDDは実装前に受け入れテストを考え、要求と検証を結ぶ実践です。両者の対象は重なり、別々の必須会議や工程を増やす意味ではありません。TDDは期待するふるまいのテストリストから一つずつテストと実装を進めるプログラミングの反復です。

本スキルでは、目的とルールの確認、意味のある具体例、受け入れ条件、テスト先行の実装、探索とフィードバックをつなげます。これは資料を本環境へ適用した運用であり、全組織共通の唯一の手順という主張ではありません。

人が読む要求と自動テストの対応は必要ですが、同じファイルを直接実行することは必須にしません。Hendricksonの2024年の再評価は、自然言語自動化と全員同期協働が重くなった経験から、少数の例と必要な参加者を勧めています。一方、Cucumberは異なる専門性の間の対話を重視します。この違いを消さず、当事者の知識を得て共有理解を確かめる方法を選びます。

### 具体的で宣言的な例

次は「税込商品合計5,000円以上なら送料を無料にする」と合意済みの場合の例です。この金額や合計の定義を別の業務へ流用して確定事項にしません。

```markdown
## 機能: 注文の送料を決定する

### ルール: 税込商品合計が5,000円以上なら送料無料

#### シナリオ: 無料になる境界の金額

- 前提: 注文の税込商品合計が5,000円である
- もし: 注文の送料を決定する
- ならば: 送料は0円になる
```

同じルールの4,999円での例や異常系も、ルールの解釈を確認するために使えます。金額の具体性は保ち、カート画面のクリック列や内部関数名を露出させる必要はありません。未確定の送料・割引後金額の扱いなどは、期待値を推測せず質問として残します。

上の本文を保存するときは `okf-docs` に従うfrontmatterを付けます。ファイルパス・日本語形式は本環境の運用規約で、BDDの普遍的定義ではありません。

### 変更単位と検証

| 判断すること | 選び方 |
| --- | --- |
| Issueの分割 | 独立して価値・検証・統合を確認できる単位にする。一回のTDD反復や一つの具体例を、そのまま一つのIssueと同一視しない |
| 500行の目安 | レビュー負担の再検討に使う本環境の目安。BDD・TDD原典の規則ではなく、単なる行数で不可分な変更を分割しない |
| テスト層 | 速く原因を特定できる単体を優先し、実際の契約・接続・設定が原因なら最小の有効な統合テストを使う |
| 技術契約 | API応答、運用者への失敗通知など、読者に約束する観測可能な結果は共有仕様になり得る。内部の接続方式等の実装手順と区別する |
| 回帰修正 | 合意済み仕様が正しければ書き換えず、欠陥を再現する検証を足す。テストを通すために期待を変えない |

DDDのBounded Contextはモデルの意味の適用範囲、Subdomainは問題領域の区分、Gitリポジトリはコード管理単位です。用語・契約・所有・変更時の依存から対応を判断し、一律1対1をDDDの定義としません。テスト可能性と展開可能性を改善する際も、全体の書き直しではなく段階的な変更を選びます。

### 一次資料

参照日は2026-09-11です。日付なしは公開・更新日を確定できない資料です。以下は定義・提言の出典で、このスキル自体の効果測定ではありません。

| 著者・資料 | 日付・参照箇所 | 本スキルでの用途 |
| --- | --- | --- |
| Cucumber, [Behaviour-Driven Development](https://cucumber.io/docs/bdd/) | ページ更新表示2026-09-10。概念の成立日ではない | 共有理解とDiscovery・Formulation・Automation |
| Cucumber, [Examples](https://cucumber.io/docs/bdd/examples/)、[Writing better Gherkin](https://cucumber.io/docs/bdd/better-gherkin/) | 日付なし | 業務上意味のある具体性と宣言的な記述 |
| Cucumber, [Example Mapping](https://cucumber.io/docs/bdd/example-mapping/)、[Gherkin Reference](https://cucumber.io/docs/gherkin/reference/) | 日付なし | ルール・例・質問の区別、RuleとScenario |
| Kent Beck, [Canon TDD](https://newsletter.kentbeck.com/p/canon-tdd) | 2023-12-11 | テストリスト、一つずつの反復、期待値を弱めないこと |
| Agile Alliance, [Acceptance Test Driven Development](https://agilealliance.org/glossary/atdd/) | 日付なし | 実装前の受け入れテストと異なる観点の協働 |
| Elisabeth Hendrickson, [ATDD Revisited](https://curiousduck.io/posts/collections/2024-06-27-atdd/) | 2024-06-27 | 2008年の実践の再評価、参加方法と自動化形式の適応 |
| Liz Keogh, [Acceptance Criteria vs. Scenarios](https://lizkeogh.com/2011/06/20/acceptance-criteria-vs-scenarios/) | 2011-06-20 | 抽象的な条件と具体例の違い |
| Jez Humble, [Continuous Testing](https://continuousdelivery.com/foundations/test-automation/)、[Architecture](https://continuousdelivery.com/implementing/architecture/) | 日付なし | 速いフィードバック、探索、テスト可能性、段階的な設計改善 |
| Eric Evans, [DDD Reference](https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf) | 2015年3月、冊子39–41頁等 | Bounded Context、Ubiquitous Language、Context Map |
