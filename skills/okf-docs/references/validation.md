---
type: Instruction
title: OKFとMarkdownの検証
description: 同梱validatorの環境準備・profile・結果判定と、公開前のMarkdown品質検査を定めます。
---

## OKFとMarkdownの検証

同梱の [validate_okf.py](../scripts/validate_okf.py) はPython 3.10以上を使用する。[requirements.txt](../scripts/requirements.txt)にPyYAML、markdown-it-py、mdit-py-pluginsとその依存mdurlの検証対象版を固定している。既存の実行環境を確認し、利用できるPythonコマンドを使う。検査は依存の自動インストール、ファイルの書き換え、ネットワーク取得を行わない。

依存が不足する場合は、task-workflowの[検証環境の準備](../../task-workflow/references/planning.md#検証環境の準備)に従い、必要な固定依存を隔離venvへ準備する。対象・配置先と理由を記録する。グローバル設定変更・追加権限・費用発生は確認し、実行できない検査を合格にしない。準備例は以下のとおり。

```sh
python3 -m venv /path/to/project/.venv-okf
/path/to/project/.venv-okf/bin/python -m pip install -r /path/to/okf-docs/scripts/requirements.txt
```

準備した環境のPythonで検査を実行する。以下の `python3` はそのコマンドに置き換える。

```sh
python3 /path/to/okf-docs/scripts/validate_okf.py /path/to/project/docs
python3 /path/to/okf-docs/scripts/validate_okf.py /path/to/project/docs adr/choice.md --profile authoring
```

対象ファイルはBundleルート基準で指定する。省略時はBundle内のMarkdownを検査する。固有形式を含むディレクトリ全体をOKF Bundleとして渡さず、OKF対象のファイルを指定する。シンボリックリンク経由で無関係な配布先へ検査を広げない。

| profile | 用途と判定 |
| --- | --- |
| `conformance`（既定） | 外部Bundleの受け入れ。YAML・非空文字列の `type`・予約ファイル構造を確認する。任意項目の欠落、未知の型・キー、索引不在、リンク切れだけでは不適合にしない |
| `authoring` | 自作文書の検査。上記に加え `title`・`description`、記載された既知メタデータの形式と対応、ローカル参照先を検査する。独自の公開品質条件を含む |

結果のファイル・フィールド・理由・規則区分を確認する。終了値は成功 `0`、検査エラー `1`、引数・依存・実行環境の問題 `2`。未検証・期限切れ自体は構文エラーにしない。検査成功は出典の真偽、人間の内容確認、計算の実行証明を意味しない。

- 依存スキル `task-workflow` の[GitHub向けMarkdownの品質](../../task-workflow/references/markdown-quality.md)に従い、Markdown全体をrumdlで整形・チェックする。既存プロジェクト設定を無断で上書きしない。
- rumdl未導入・旧版の場合の導入・更新やダウンロードを伴う一時実行は、同資料の権限確認手順に従う。実行不能を合格と扱わない。
- 分類、用語、リンク、記載したコマンド、差分を確認する。リンク検査とrumdlは本環境の公開品質検査であり、外部BundleのOKF適合判定に流用しない。
- feature文書は整形後も見出し・ステップを確認する。出典の内容や契約の意味は、validatorとは別に読んで確認する。
