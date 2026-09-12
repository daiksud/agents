---
type: Instruction
title: GitHub向けMarkdownの品質
description: 共通rumdl設定、導入許可、GFMの構成、投稿前整形と投稿後確認の手順を定めます。
sources:
  - id: rumdl-getting-started-installation
    resource: https://rumdl.dev/getting-started/installation/
  - id: rumdl-md060
    resource: https://rumdl.dev/md060/
  - id: rumdl-md076
    resource: https://rumdl.dev/md076/
  - id: github-docs-global-settings-md
    resource: https://github.com/rvben/rumdl/blob/main/docs/global-settings.md
---

## GitHub向けMarkdownの品質

Issue・PR番号やコミットSHAを日本語・句読点に続ける場合は、前後に半角スペースを入れ、コード記法で囲まず、投稿後に自動リンクを確認する。

Issue・PR本文・コメントを新規投稿・更新するとき、およびリポジトリのMarkdownを作成・更新するときに適用する。読み取りのみの相談・説明には整形や導入を要求しない。

### 構成と表示

- GitHub投稿にOKFやYAML frontmatterを付けない。リポジトリ文書には対象のOKF・Agent Skills形式を適用する。
- 導入先の指定テンプレートに従う。指定がなければ、内容を理解するために必要な段落・見出し・リストを選ぶ。固定見出し、不要な表・Alerts、空の節、「なし」の埋め草を要求しない。
- Emoji・表・Alertsは識別・比較・重要な制約の理解に役立つ場合に使う。装飾がなくても承認待ち・対象外・未検証などの重要情報は明示する。
- 単純リストの不要な項目間空行を除き、複数段落・コードブロック・入れ子の意味のある構造と空行は保つ。
- rumdlは内容の構成を決めない。意味が伝わる本文を用意してから機械整形する。

### 共通設定

[共通rumdl設定](../assets/rumdl.toml)を利用する。読み込んだ本スキルの `assets/rumdl.toml` を基準とする。

| 設定 | 内容 |
| --- | --- |
| 無効化 | MD013・MD033・MD034・MD041のみ。長い行、HTML、裸URL、先頭H1なしを許容する |
| MD060 | 明示的に有効化し、compactで余分な列幅の空白を除去する |
| MD076 | tightで単純な項目間空行を除去し、allow-loose-continuationで複数段落の構造を保持する |
| その他 | MD003などは既定値を維持する。MD025は有効に保ち、以下の計算文書だけtitleの数え方を調整する |

GitHub投稿本文には共通設定を明示指定する。リポジトリ文書では既存設定を確認し、プロジェクト固有の設定を無断で上書きしない。既存設定と共通方針に衝突がある場合は解消方法を計画へ記録し、目的・受け入れ条件や権限を変える場合は着手と計画の条件で確認する。

### rumdlの利用可否と導入許可

1. インストール済みの `rumdl --version` と `rumdl config --config <設定ファイル> --output json` を確認する。設定警告や必要なルールの欠落を無視しない。
2. 未導入・旧版なら、[検証環境の準備](planning.md#検証環境の準備)に従い、既知の必要版を隔離環境へ準備する。対象・版・配置先と理由を記録する。
3. ダウンロードを伴う一時実行も同じ基準を使う。グローバル設定変更・追加権限・費用発生や出所不明の導入は確認する。
4. 導入後にバージョンと設定を確認して検証する。拒否・環境制約で実行できなければ理由と未検証範囲を示し、必要な検証を通せない投稿は保留する。

### 整形から投稿後確認まで

1. 既存本文を更新する場合は再取得して元の本文を保持する。構成・検証結果・リンクを維持して本文全体を一時Markdownファイルに保存する。追記時も追記部分だけでなく本文全体を対象にする。
2. 共通設定を絶対パスで指定し、次の順で実行する。`<本文ファイル>` と `<共通設定>` は実在するパスに置き換える。

   ```bash
   rumdl check --config <共通設定> --deny-config-warnings --fix <本文ファイル>
   rumdl check --config <共通設定> --deny-config-warnings <本文ファイル>
   ```

3. 修正後の差分を確認し、もう一度整形して差分が出ないことを確認する。指摘が残る場合は意味を維持して修正し、チェックに合格するまで投稿しない。必要な段落やコードが変形した場合はその構造を直し、再検証する。
4. 整形済みファイルを `gh issue create --body-file`、`gh issue edit --body-file`、`gh pr create --body-file`、`gh pr edit --body-file`、`gh issue comment --body-file`、`gh pr comment --body-file`、または対応するAPIで投稿する。整形後の文字列を手で再構築しない。
5. 保存済み本文を再取得して整形済みファイルと一致することを確認する。Issueでは[Issue保存後のブラウザ起動](issue-recording.md#issue保存後のブラウザ起動)に従い、要求時だけ一度開く。GitHubのレンダリングで使用した見出し・表・Alerts・リンク・リストの表示を確認し、単純リストの不要な `li > p` と意図した複数段落を区別する。起動の有無によらず本文・表示を確認し、起動成功だけで目視確認済みとしない。
6. 表示が不自然なら元ファイルを修正し、整形・チェック・投稿・再取得を繰り返す。APIのHTML確認だけの場合は画面を目視確認したと報告しない。

リポジトリ文書も保存前に同じ整形・チェックを行い、frontmatter・見出し階層・相対リンク・feature文書のステップを確認する。通常概念のtitleとH1がMD025で重複と判定される場合は本文の見出し階層を調整する。`type: Attested Computation` で本文に計算定義を置く場合は仕様が `# Computation` を要求するため、その文書だけ `--config 'MD025.front-matter-title = ""'` を既存設定に追加する。MD025自体と本文H1の重複検査は維持する。計算のH1をH2へ変えて回避しない。固有契約と検証手順は依存する [okf-docsの計算資料](../../okf-docs/references/computation.md) を確認する。

### 参考

- rumdlの導入方法[^rumdl-getting-started-installation]
- MD060: compact形式[^rumdl-md060]
- MD076: リスト項目間隔[^rumdl-md076]
- 共通設定の継承[^github-docs-global-settings-md]

[^rumdl-getting-started-installation]: [rumdlの導入方法](https://rumdl.dev/getting-started/installation/)。本文に記した参照範囲と採用判断の根拠。
[^rumdl-md060]: [MD060: compact形式](https://rumdl.dev/md060/)。本文に記した参照範囲と採用判断の根拠。
[^rumdl-md076]: [MD076: リスト項目間隔](https://rumdl.dev/md076/)。本文に記した参照範囲と採用判断の根拠。
[^github-docs-global-settings-md]: [共通設定の継承](https://github.com/rvben/rumdl/blob/main/docs/global-settings.md)。本文に記した参照範囲と採用判断の根拠。
