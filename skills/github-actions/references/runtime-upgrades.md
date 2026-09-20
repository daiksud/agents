---
type: Instruction
title: Actionの内部ランタイム更新
description: 非推奨警告の発生元と互換性を確認し、アプリ用ランタイムを混同せずActionを更新・検証します。
sources:
  - id: copilot-runtime
    resource: https://github.com/github/awesome-copilot/blob/4f4796f0bf30e105700f97ed8408c12b6aa95e06/skills/github-actions-runtime-upgrade-conventions/SKILL.md
  - id: github-metadata
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/metadata-syntax
  - id: actions-checkout
    resource: https://github.com/actions/checkout
  - id: actions-setup-node
    resource: https://github.com/actions/setup-node
---

## 警告の発生元を特定する

runの警告、対象SHA、イベント、runner、該当ステップを取得し、直接・間接に使うActionを追う。JavaScript Actionの `action.yml` / `action.yaml` にある `runs.using` はAction自身の内部ランタイムであり、`setup-node` の `node-version` やアプリの `engines` とは別である。composite Actionと再利用ワークフローでは内側のActionまで確認する。[^github-metadata]

警告の解消だけが目的なら、アプリ用Node.js、依存lock、ビルド設定、ジョブ構成を無関係に更新しない。環境変数で警告を隠すことや、Action本体の対応なしにランタイム指定だけを置き換えることを恒久対応にしない。互換リリースが見つからない場合は、制約、上流の対応状況、代替案と未確認を示す。[^copilot-runtime]

## 互換性と参照先を照合する

1. 現行の完全SHA・版コメント・metadata、更新先の安定リリースとrelease notesを確認する。Actionの公式リポジトリでタグが指す完全コミットを解決する。annotated tagならtag objectからcommitまで辿り、短縮SHA・タグ名だけを固定値にしない。
2. 必要なrunner版、OS・architecture、GitHub.com/GHESの対応を対象版で確認する。self-hosted runnerが古い場合に、runner更新権限があるとは仮定しない。
3. 入力・廃止項目・デフォルト、outputs、checkoutの認証・fork条件、キャッシュ、artifactの名前・内容・保持・署名への影響を確認する。内部ランタイム更新という説明だけで動作不変と判断しない。checkoutやsetup-nodeにも版ごとの既定動作の変更がある。[^actions-checkout][^actions-setup-node]
4. 互換な版の完全SHAと正しい版コメントをセットで更新する。同じActionの参照が別workflow・composite・再利用先にあるか検索し、必要な呼び出し元を揃える。異なる互換性要件がある参照を一律置換しない。
5. 少数の関連Actionごとに更新・検証し、権限・入力・認証・キャッシュの境界が変わる場合は[安全性](hardening.md)も読む。古い例のSHAや固定の推奨メジャー版を転記しない。

更新先の根拠を読むコマンド例（対象リポジトリとタグを実値に置き換える）:

```bash
gh release view TAG --repo OWNER/ACTION
gh api repos/OWNER/ACTION/commits/TAG --jq .sha
```

リリースが存在しない、版コメントとcommitの関係を確認できない場合は検証済みとしない。

## 検証を分ける

| 確認 | 得られる根拠 |
| --- | --- |
| 静的検査 | YAML・式・完全SHA・版コメント・入力・runner要件の整合 |
| ローカル検査 | アプリのbuild/test等がそのローカル環境で動くこと |
| GitHub上の実行 | 対象SHA・イベント・runnerで更新Actionが実行され、警告・outputs・artifact等が期待どおりであること |

承認済みの変更では代表的な実行経路と変更の影響を受ける経路を選び、run URL・対象SHA・結論を記録する。artifactや署名は生成成功だけでなく利用側で必要な内容を確かめる。fork拒否等のデフォルト変更なら、その対象経路も確認する。ローカル成功だけで更新Actionの実行検証済みとせず、取得不能・未実行と残る確認方法を明示する。原典の小さな更新と動作保持を、この区別で適用する。

[^github-metadata]: Metadata syntax。Action内部の `runs.using` を確認する正本。
[^copilot-runtime]: Runtime Upgrade Conventionsの発生元調査・互換な更新・動作保持を要約。古いSHA/版の例やローカル検査と実実行の同一視は採用しない。
[^actions-checkout]: checkoutの対象リリース・metadata・READMEで認証、fork、runner要件を確認する。
[^actions-setup-node]: setup-nodeの対象リリース・metadata・READMEでキャッシュ・入力等の変更を確認する。
