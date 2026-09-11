---
type: Guide
title: OKFの基本形式と参照
description: 通常概念、索引、履歴の違いとBundle境界に基づくリンク解決を説明します。
sources:
  - id: okf-spec
    resource: https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/ad30107c31c06aec8a7d5636e0d1058118604e6f/SPEC.md
    title: Open Knowledge Format v0.2
---

## 通常概念とBundle

Knowledge Bundleは配布単位となるディレクトリツリー、Conceptはその中の一つの知識文書である。Concept IDはBundle内のファイルパスから末尾の `.md` を除いたもの。例えばBundleが `docs/` なら `docs/behavior/order.feature.md` のIDは `behavior/order.feature` となる。リポジトリ・ドメインの境界・Bundleは同じものとは限らない。[^okf-spec]

通常概念はUTF-8のMarkdown本文と先頭のYAML frontmatterで構成する。開始・終了はそれぞれ独立した行の `---`。必須キーは非空文字列の `type` だけで、型の登録簿はない。未知の型や追加キーを拒否しない。`title`・`description`・`resource`・`tags` は推奨であり、以下も適合する。[^okf-spec]

```markdown
---
type: Local Idea
---

検討中の概念。
```

本環境の自作概念には `title`・`description` も記載する。`resource` は概念が表す資産の識別先であり、根拠資料を記録する `sources[].resource` とは区別する。抽象概念に資産URLを捏造しない。本文の固定章構成は要求しない。[^okf-spec]

## 索引と履歴の例外

`index.md` と `log.md` は階層のどこでも予約名であり、通常概念に使わない。どちらも任意なので、不在だけを理由に新設しない。予約ファイルへ `type`・`title`・`description` を付けない。[^okf-spec]

`index.md` は見出しで分類したリンク項目のリストにする。説明はリンク先の `description` を使うことが推奨される。frontmatterは原則持たず、Bundleルートに限って版宣言を置ける。既存のroot版宣言は更新時に保持する。[^okf-spec]

```markdown
---
okf_version: "0.2"
---

# ガイド

- [注文の扱い](behavior/order.feature.md) - 注文の受け入れ条件。
- [設計判断](adr/) - 判断と理由。
```

`log.md` は日付ごとの平坦な更新項目を新しい順に並べる。日付見出しは実在する `YYYY-MM-DD`。先頭の太字ラベルは慣例であり必須ではない。ログの日付はイベントのグループ化であり、UTC offset付き日時を記録するメタデータとは別である。[^okf-spec]

```markdown
# 更新履歴

## 2026-09-11

- 注文の受け入れ条件を更新した。

## 2026-09-10

- 最初のガイドを追加した。
```

見本のコードブロック内にある見出しや脚注は、外側の文書の構造として解釈しない。

## 参照の解決

Markdownリンクと `resource`・`sources[].resource`・`computation`・`executor.resource`・`attester.resource` は以下の基準で解釈する。`sources[].resource` には「プロジェクトX内の全クエリ」のような取得先を持たない範囲記述も認められるため、すべてをファイルパスとみなさない。[^okf-spec]

| 表記 | 解決基準 | `docs/guide/page.md` からの例（Bundleは `docs/`） |
| --- | --- | --- |
| `/tables/orders.md` | Bundleルート | `docs/tables/orders.md` |
| `../tables/orders.md` | 現在のファイルのディレクトリ | `docs/tables/orders.md` |
| `https://example.com/policy` | 外部URL | ローカルファイルへ変換しない |

仕様は先頭 `/` のBundle基準リンクを推奨する。本環境ではGitHub・APMの通常のMarkdown閲覧に合わせ、ファイル相対リンクを選ぶ。仕様例の `references/...` をサブディレクトリの文書へコピーする際は、実際の位置から `../references/...` 等へ解決し直す。[^okf-spec]

関連の種類はリンク周辺の本文に書く。主張の根拠には[出典の手順](provenance.md)を使う。`references/` は外部資料・手順・コードの置き場所の慣例で、必須ディレクトリではない。[^okf-spec]

リンク切れは未記述の知識を表す場合があり、OKF適合を失わせない。本環境の自作文書では公開品質としてローカル参照先を修正するか、未作成・取得不能の状態を明示して扱う。Bundle境界外のファイルやシンボリックリンクを辿って勝手に検査・修正しない。[^okf-spec]

[^okf-spec]: 固定版SPEC §§2–4、6、8–9、11–12。本環境の追加条件は本文で区別した。
