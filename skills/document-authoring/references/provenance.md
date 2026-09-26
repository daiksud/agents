---
type: Guide
title: OKFの出典・信頼・ライフサイクル
description: 主張と出典の対応、生成と確認の区別、内容更新と鮮度の扱いを示します。
sources:
  - id: okf-spec
    resource: https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/ad30107c31c06aec8a7d5636e0d1058118604e6f/SPEC.md
    title: Open Knowledge Format v0.2
---

## 主張と出典を結ぶ

外部資料に依拠する文書では、その資料を `sources` のリストへ記録する。本環境では資料全体への関連リンクだけで済ませず、個別の主張を安定した `id` の脚注へ結ぶ。各sourceの `resource` は記載時に必須、`id`・`title` は任意だが、引用するsourceには `id` が推奨される。[^okf-spec]

```markdown
---
type: Guide
title: 注文の保存期間
description: 保存期間を確認する際の正本を示す。
sources:
  - id: retention-policy
    resource: https://example.com/policies/retention
    title: 保存方針
---

注文の保存期間は保存方針で定める。[^retention-policy]

[^retention-policy]: 保存方針。
```

上記は形式の例であり、実際の保存期間や取得結果を証明しない。作成時は読んだ資料と実在する主張に置き換える。

脚注ラベルが `sources[].id` への結合キーとなり、脚注の説明文を解析して出典を決めない。並べ替えても意味が変わらないIDを使い、位置番号 `sources[0]` に依存させない。本環境では重複ID、未定義の脚注、脚注に対応しないsourceを確認する。本文で引用しないsourceにまで脚注を新設させない。[^okf-spec]

出典の `resource` は外部URL、Bundle基準・ファイル相対パス、母集団・範囲の記述を取れる。範囲記述を存在しないファイルとして拒否しない。配布する資料の外部出典は完全URLで保持し、Gitの実装根拠は完全SHAで版を固定する。後者は本環境の再現性のための選択である。[^okf-spec]

## 客観的な信号を保持する

`sources` の `author`・`usage_count`・`last_modified` は任意の客観的な信号であり、信頼スコアではない。`last_modified` は資料自体の更新時刻であり、概念を作った時刻とは区別する。閲覧時刻を資料更新時刻として記録しない。[^okf-spec]

`usage_count` を記録する場合は観測した回数と観測期間を対応づける。`usage_window: { from, to }` は `sources` と同階層に置き、各sourceに置いた期間は共有期間を上書きする。スケジュール実行回数と人の閲覧回数を同じ精度のランキングとして比較しない。未知の回数をゼロにしない。[^okf-spec]

内部概念が出典なら、その `sources` を辿って根拠を追える。v0.2では外部データ系譜の専用フィールドを標準化していない。独自のキーを既存文書から削除したり、独自の評価値をOKF標準の信頼判定として追加したりしない。[^okf-spec]

## 生成と確認を分ける

`generated` は現在の内容の作成を、`verified` は出典・資産と照合した確認イベントを表す。すべて任意であり、値は根拠がある場合だけ記録する。`generated.by` は記載時に必須、`generated.at` は最後の意味ある変更の日時。整形しただけで事実を更新したように見せない。[^okf-spec]

`verified` は `{ by, at }` のリスト、または同じ意味の単一mappingを取る。単一mappingを不適合としない。最新の `at` が直近の確認を表すが、内容更新と再確認は独立している。[^okf-spec]

```yaml
verified: { by: 'human:reviewer-id', at: '2026-09-11T09:00:00+09:00' }
```

この例を実際の確認がない文書へコピーしない。確認者・時刻・対象の内容を実際の証拠で特定する。

| 記録 | 意味 |
| --- | --- |
| `verified` なし | 未検証。利用可能だが確認済みとは主張しない |
| 非 `human:` Actorだけによる確認 | machine-confirmed |
| `human:<id>` による確認あり | human-reviewed |

Actorはエージェント・ツールなら `<producer>/<version>`、人なら `human:<id>`、自動処理なら `process:<id>`。人が作成・確認した内容には `human:` を使う。CIの成功を人間の確認へ置き換えず、静的検査しかしていないCIを内容の照合として記録しない。信頼段階はアクセス制御ではない。[^okf-spec]

## 状態・日時・期限

`status` は `draft`（未レビュー・未完の場合あり）、`stable`（利用可能）、`deprecated`（履歴とリンク用に保持）のいずれか。省略時は `stable` であり、人間による確認済みを意味しない。[^okf-spec]

日時値にはISO 8601のUTC offset付きdatetimeを使う。例は `2026-09-11T09:00:00+09:00` または `2026-09-11T00:00:00Z`。対象は `generated.at`・`verified[].at`・`sources[].last_modified`・`usage_window.from/to`・`stale_after`。日付だけの古い値へタイムゾーンを推測で足さず、根拠を確認する。[^okf-spec]

`stale_after` は絶対時刻で、`now >= stale_after` のとき期限切れとなる。期限ちょうども含む。期限・未検証という状態自体は構文エラーではない。期限がない文書を鮮度が証明された文書とみなさず、期限を慣例だけで新設しない。[^okf-spec]

## 更新と移行

1. 既存の `sources`、未知キー、`generated`、`verified`、期限と本文を先に読む。引用IDは並べ替えで変更しない。
2. 変更する主張とその根拠を特定する。既存sourceは数が同じでも別資料への置換になっていないか確認する。
3. 軽微修正では生成日時・確認日時・期限を機械的に更新しない。意味が変わる場合は実際の生成事実を確認し、過去の確認履歴を保持したうえで、それが変更前の内容に対する確認であることを本文等で明示する。
4. 再確認を実施した場合だけ新しい `verified` イベントを追加する。確認対象・範囲を記録できない場合は、その不確実性を残し、最新内容が確認済みとは報告しない。
5. v0.1の本文 `Citations` は根拠を確認して `sources` と脚注へ移す。旧 `timestamp` だけではActorが分からないため、`generated.by` を捏造しない。外部v0.1資料を受け入れるだけなら無理に書き換えない。
6. 保存後の差分で出典・未知キー・履歴の消失がないか確認する。YAMLの読み書きで日時の表記や値が変わっていないかも確認する。

これらは仕様の保持推奨と生成・確認の意味に基づく本環境の更新手順である。仕様は履歴の版識別スキーマを規定していないため、既存の履歴管理を使い、独自キーを規範として要求しない。[^okf-spec]

[^okf-spec]: 固定版SPEC §§4.1、5、7、11、13。本環境の更新手順と追加検査は適用判断である。
