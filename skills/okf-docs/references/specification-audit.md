---
type: Reference
title: OKF v0.2の仕様監査と採用判断
description: 固定した仕様の節ごとに規範、利用場面、採用判断、検証を対応づけ、参考実装との差を記録します。
sources:
  - id: spec
    resource: https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/ad30107c31c06aec8a7d5636e0d1058118604e6f/SPEC.md
    title: OKF v0.2正本
  - id: migration
    resource: https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/62651738dab0b497b0e3fd804c87bcd235f027b8/okf/README.md
    title: 移管と凍結コピーの案内
  - id: frozen-spec
    resource: https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/62651738dab0b497b0e3fd804c87bcd235f027b8/okf/SPEC.md
    title: 移管元の凍結仕様
  - id: timestamps
    resource: https://github.com/GoogleCloudPlatform/open-knowledge-format/commit/3dc3029168d2f98e331feeb4ca05c9178973a9b9
    title: UTC offset付き日時への変更
  - id: conformance-edit
    resource: https://github.com/GoogleCloudPlatform/open-knowledge-format/commit/0b87c52c6ef999286c745e19998fdfcd03d5dbee
    title: 重複した日時の適合条件の削除
  - id: document
    resource: https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/ad30107c31c06aec8a7d5636e0d1058118604e6f/src/reference_agent/bundle/document.py
    title: 参考パーサと信頼・鮮度処理
  - id: writer
    resource: https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/ad30107c31c06aec8a7d5636e0d1058118604e6f/src/reference_agent/tools/bundle_tools.py
    title: 参考書き込み処理
  - id: viewer
    resource: https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/ad30107c31c06aec8a7d5636e0d1058118604e6f/src/reference_agent/viewer/generator.py
    title: 参考viewerのリンクとメタデータ処理
  - id: attester
    resource: https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/ad30107c31c06aec8a7d5636e0d1058118604e6f/bundles/acme_retail/attesters/sql_equality.py
    title: 参考SQL attester
---

## 正本と読み方

採用する正本は移管先 `open-knowledge-format` の完全SHA `ad30107c31c06aec8a7d5636e0d1058118604e6f` のSPEC v0.2。移管元は凍結コピーで新規開発の基準にしないよう案内している。確認した凍結版のSPEC本文は固定した正本と一致した。[^migration][^frozen-spec][^spec]

以下の「必須・推奨・任意」は仕様における強さを示す。作成側の要件と§11の最小適合判定を混同しない。特に任意familyの形式は作成側で確認するが、記載の不備をすべて外部Bundle拒否の理由にはしない。[^spec]

## 節別の対応

| 節 | 要件・推奨・任意 | 利用場面 | 本環境の採用判断 | 検証方法 |
| --- | --- | --- | --- | --- |
| §1 Motivation | 目的と非目標。ランタイム・分類登録・ドメインスキーマの置換は対象外 | 適用判断 | 既存契約形式を維持 | SKILL・OpenAPI・投稿を変換しない模擬例 |
| §2 Terminology | Bundle・Concept・ID・Source・Actor等の定義 | 配置・参照 | IDはBundle内パスから `.md` を除く | 相対パスと境界の例 |
| §3 / §3.1 | 配布形態は任意。予約名を概念に使わない | 文書の配置 | `docs/` を既定Bundleとする | 概念と予約名を分けるテスト |
| §4.1 | `type` 必須。表示項目は推奨。未知型・キーの許容、未知キー保持推奨 | 通常概念 | 自作のみtitle・descriptionを追加要求 | typeのみ・未知拡張・不正YAML |
| §4.2 | 構造化Markdown推奨。固定本文節なし | 本文作成 | GFM、featureの固有記法を併用 | rumdlと意味の確認 |
| §4.3–4.4 | 資産あり・なしの例 | resourceの判断 | 抽象概念にURIを新設しない | 資産と出典の区別 |
| §5前文 | 各family任意。日時値はoffset付きISO datetime | 日時記録 | 不明日時を補完しない | offset欠落・日付だけの検査 |
| §5.1 | sourceのresourceは記載時必須。ID・信号は任意、引用時ID推奨 | 出典付き作成・更新 | sourcesと安定ID脚注を使用 | 並べ替え・重複・未定義のテスト |
| §5.2 | generated.byは記載時必須。verifiedはイベントリスト、単一mappingも可 | 作成・内容照合 | 作成と照合、履歴と現在内容を区別 | 単一mapping・履歴保持の例 |
| §5.3 | verifiedから信頼段階を導出。未検証を拒否しない | 信頼表示 | CI成功を人間確認に変換しない | 未検証・機械確認・人間確認 |
| §5.4 | statusはdraft / stable / deprecated、省略時stable | ライフサイクル | stableと検証済みを混同しない | 省略と不正状態 |
| §5.5 | stale_afterは任意、期限以上でstale | 鮮度判断 | 未設定を保証とせず、期限切れは注意 | 期限直前・ちょうど・後 |
| §6.1 | Bundle基準リンク推奨、相対可、リンク切れ許容必須 | 関連文書 | GitHub・APM向けにファイル相対を採用 | 両profileでリンク切れを区別 |
| §6.2–6.3 | URL・Bundle基準・相対パス。referencesは慣例 | パス項目 | 外部出典は完全URL。scope descriptorを許容 | 各基準と範囲記述の例 |
| §7 | Actorの慣例。人の作成・確認にはhuman:必須 | 主体記録 | 実在する主体だけ記録 | Actor形状と未確認主体の例 |
| §8 | indexは任意、見出しとリンク一覧。frontmatterはroot版宣言だけ | 索引 | 新設を強制しない | 正常索引・子索引の例外 |
| §9 | logは任意、日付見出しはYYYY-MM-DD、新しい順 | 履歴 | 実在日を検査。太字ラベルは必須にしない | 不正日付・逆順・コード内見出し |
| §10.1–10.2 | 計算を独立概念にする。runtime必須、契約fieldを定義 | 計算契約の作成 | runtime・parameters・参照をauthoring検査 | 正常契約・型と名前の不備 |
| §10.3–10.4 | 本文の一つの計算フェンスまたはファイル。利用者は宣言値のみ指定 | 計算の利用 | 定義変更と値の指定を分離 | 任意SQLに書き換えない模擬例 |
| §10.5 | informative。実行・証明・提示のモデル | 確認手順 | 実行基盤は追加せず、証跡をBundleへ格納しない | 手順と未実装範囲の確認 |
| §10.6 | verifiedは定義、attestationは一回の実行 | 証明の解釈 | 一方の成功を他方の証明としない | 定義が古く実行だけ成功する例 |
| §11 | 最小適合条件。任意family欠落・未知型/キー・リンク切れ・索引不在で拒否しない | 外部Bundle受け入れ | conformanceとauthoringを分離 | 両profileの回帰テスト |
| §12 | root版宣言任意、未知版もbest effort推奨。ABI等は保留 | 版の扱い | 版宣言保持、未採用提案を必須にしない | root索引・版の例 |
| §13.1–13.2 | timestampとCitationsを移行。旧形式fallbackは任意 | 既存文書更新 | 根拠を確認して移行、Actorを推測しない | 出典付き更新と未知キー保持 |
| Appendix A | 移行のworked example | 理解の補助 | 仮想Actor・日時・全familyをコピーしない | 完成した仮想入力で判断を評価 |

節ごとの仕様の要約は固定SPECに基づく。検査範囲と本環境の採用判断は独自の運用方針である。[^spec]

## 日時処理の変更

日時変更では、従来日付だけだった `stale_after`・source更新日時・利用期間もUTC offset付きdatetimeへ統一された。ログの日付見出しはその対象ではない。参考Python実装はPyYAMLのtimestamp暗黙変換を除き、日時表記を文字列として保持するよう変わった。[^timestamps][^document]

変更途中に存在した§11の日時に関するconsumer MUSTは、重複を除く後続コミットで削除された。採用する最終版には§5の日時形式の記述があるが、旧コミット本文の強い拒否・無視規則を現行の適合条件として引用しない。参考実装の `is_stale` はoffsetや `T` がない値を無視するが、これも実装上のふるまいと区別する。[^conformance-edit][^document]

## 参考実装を規範にしない

| 対象 | 読み取れたふるまい・限界 | 本環境での扱い |
| --- | --- | --- |
| document.py | validateはtypeのtruthinessのみ。未知キーをmappingで保持し、verified mappingを正規化する | 非空文字列や既知項目のauthoring検査を別途行う |
| bundle_tools.py | 渡されたfrontmatterを書き込み、generatedを補完する。既存内容を自動mergeしない。web passのBigQuery保護はsource件数の比較 | 同数のsource置換・未知キー消失を防ぐ一般保証とはみなさず差分を読む |
| viewer/generator.py | 先頭 `/` のリンクを無視し、本文の限定された `.md` リンクを抽出。表示データは既知キー中心。logを予約名として除外しない | viewer表示で参照・未知メタデータの完全性や予約ファイル適合を証明しない |
| sample sql_equality.py | 束縛値を検査せず、receiptのSQLと結果を比較。job結果の再取得なし | 完全な実行証明と呼ばず、契約ごとに必要な証拠を確認 |

これは固定SHAのコードを読んだ結果であり、上流の実行・クラウド接続を再現した結果ではない。[^document][^writer][^viewer][^attester]

仕様内のサンプルには `team:` のsource authorやインデントされた計算コード例など、本文規約と単純に一致しない表現もある。サンプルの値を独自の必須要件に昇格させず、作成時は規約本文を優先する。外部資料の拡張を自動削除・変換しない。将来のruntime protocol・ABI・cache・semantic-layer templateは§12で保留されており、未採用提案をv0.2の要件へ混ぜない。[^spec]

[^migration]: 移管元READMEの移管・凍結案内。
[^frozen-spec]: 確認対象の凍結SPEC。
[^spec]: 正本SPEC v0.2。規範とinformativeを本文に従って分類した。
[^timestamps]: 日時統一の変更とその理由。
[^document]: 参考パーサ・信頼段階・鮮度判定のコード。
[^conformance-edit]: 後続の重複した適合条件削除。
[^writer]: 参考書き込み処理のコード。
[^viewer]: 参考viewerのコード。
[^attester]: 参考SQL attesterのコード。
