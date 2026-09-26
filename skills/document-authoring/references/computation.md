---
type: Guide
title: Attested Computationの契約と確認
description: 計算定義、許可されたパラメータ、定義確認と実行証明を区別して記述します。
sources:
  - id: okf-spec
    resource: https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/ad30107c31c06aec8a7d5636e0d1058118604e6f/SPEC.md
    title: Open Knowledge Format v0.2
  - id: rumdl-md025
    resource: https://github.com/rvben/rumdl/blob/993b5b10feca512e07d017ba4550fe690cd08c51/docs/md025.md
  - id: sample-attester
    resource: https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/ad30107c31c06aec8a7d5636e0d1058118604e6f/bundles/acme_retail/attesters/sql_equality.py
    title: 参考SQL attester
---

## 契約を書く場面

承認された計算方法で値を得たことを確認する必要がある場合に、`type: Attested Computation` の独立した概念を使う。指標の説明から通常のMarkdownリンクで参照し、複数の計算を一つのfrontmatterへ詰め込まない。OKFは定義と確認方法を記録する形式であり、実行基盤ではない。[^okf-spec]

| フィールド | 契約で明らかにすること |
| --- | --- |
| `runtime` | この型では必須。`bigquery`・`dbt`・`python` 等。パラメータの束縛方法を決める |
| `parameters` | 宣言する穴のリスト。各項目の `name`・`type`・`required`。値を渡す側が定義を改変しない |
| `computation` | 別ファイルに置く場合の参照先。省略する場合は本文の `# Computation` 配下の一つのコードフェンス |
| `executor.resource` | 実行手順またはコードの参照先 |
| `executor.receipt` | 実行から返す証拠のフィールド。何を確認に使うか |
| `attester.resource` | receiptを検査して判定する決定的コードの参照先。LLMの判断をattesterとしない |

フィールドの役割は仕様§10.2–10.3に従う。`runtime` 以外の省略を一律にBundle不適合とせず、契約を実際に使えるかは別途確認する。[^okf-spec]

次は契約の形式例であり、計算・実行手順・attesterが実装済みであることを示さない。対象の正本と実在する参照先が確定してから文書化する。

```yaml
type: Attested Computation
title: 年度別の承認済み集計
description: 承認された計算を年度パラメータで実行する。
runtime: bigquery
parameters:
  - { name: year, type: integer, required: true }
computation: ../references/computations/annual.sql
executor:
  resource: ../references/run-annual.md
  receipt: [job_id, executed_sql, result]
attester:
  resource: ../references/attesters/annual.py
```

パスは契約ファイルの位置から解決する。`computation` ファイルと本文の計算フェンスを両方の正本にしない。実行に必要な能力や実在しない参照先が不足していれば未実装と明記し、このスキルだけを根拠にクラウド接続やランタイムを導入しない。[^okf-spec]

## Markdownと契約を合わせて検証する

本文に計算定義を置く場合は `title` と本文の `# Computation` を併記する。rumdlの既定MD025はfrontmatterのtitleもH1と数えるため、計算文書だけ次の指定を追加する。`front-matter-title = ""` はfrontmatterを別扱いにし、本文のH1重複検査を維持する。rumdl 0.2.69の設定定義に基づく本環境の選択であり、通常概念やGitHub投稿には適用しない。[^rumdl-md025]

```sh
rumdl check --config /path/to/rumdl.toml --config 'MD025.front-matter-title = ""' --deny-config-warnings /path/to/computation.md
```

整形するときも同じ設定に `--fix` を追加する。複数ファイルは計算文書とその他を分けて実行する。本文H1の重複を直す際も仕様の `# Computation` を残し、その配下のコードフェンスを確認する。authoring検査も続けて実行し、H2への誤変更や計算定義の不整合を検出する。rumdlだけの成功を契約の検証としない。

## 値の指定と定義変更

計算を利用するエージェントが指定できるのは宣言済みパラメータの値だけであり、任意SQLの作成・書き換えではない。パラメータを束縛した実行成果物はconsumerが作り、attesterは同じ束縛を独立に再構成して実際の成果物と比較する。[^okf-spec]

計算定義自体を変更する依頼は、値を得る依頼とは別の変更である。既存の正本・承認・レビューに従い、定義変更を実行時の「調整」として混ぜない。実行の依頼だけを受けて定義を作り直さない。

## 定義確認と一回の実行証明

`verified` は定義が方針に一致することの文書単位の確認、attestationは一回の実行で指定の計算が行われたことの証明である。期限切れの定義でも実行証明だけは成功し得るし、定義の確認が新しくても各実行の証明は必要となる。[^okf-spec]

確認手順を記述する場合は次を明らかにする。

1. 計算定義の版、runtime、宣言パラメータと値を読み取る。
2. executorが返す証拠と、その証拠を取得する信頼できる実行先を定める。
3. attesterが束縛後の計算と実際の実行を比較する方法を確認する。
4. 表示値が権威ある実行結果と一致することを、エージェントが返した文章だけに依存せず確認する。
5. 失敗の判定を隠さず、期限・信頼の状態とともに利用者へ示す方針を定める。

この実行手順のモデルは§10.5の参考情報に基づく。receipt・verdictのwire format、attester ABI、sandbox、cacheはv0.2で未規定であり、本環境が共通ランタイムとして補完する範囲ではない。receiptと判定は実行時の成果物であり、Bundleのfrontmatterへ埋め込まない。[^okf-spec]

## 参考attesterの限界

同梱サンプルの `sql_equality.py` はネットワークを使わず、SQLの正規化比較とreceipt内の結果・表示値の一致を確認する。パラメータ値の検査はexecutorを信頼し、job IDから権威ある結果を再取得しない。コメント・空白・単語の正規化はSQLの完全な構文解析ではなく、文字列リテラル等の意味を保つ保証は読み取れない。[^sample-attester]

したがって、サンプルの成功だけでパラメータの正しさ・実際のジョブ実行・結果の真正性まで証明されたと主張しない。参考コードを本番attesterとして無条件に転用せず、必要な証拠の取得・束縛の再構成・比較対象・失敗条件を契約ごとに確認する。validatorの静的検査も実行証明の代わりにはならない。

[^okf-spec]: 固定版SPEC §§10–12。§10.5はinformativeであり、運用上の確認項目は本環境の適用判断。
[^rumdl-md025]: rumdl 0.2.69、MD025のFront Matter IntegrationとConfiguration examples。
[^sample-attester]: 固定SHAのサンプル実装のdocstringと `attest`・`_canonicalize` を読んだ結果。実行基盤での有効性を実測した結果ではない。
