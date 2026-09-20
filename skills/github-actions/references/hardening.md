---
type: Instruction
title: GitHub Actionsの安全性
description: 入力、実行コード、権限、ランナー、成果物の信頼境界を追ってリスクと修正を判断します。
sources:
  - id: copilot-hardening
    resource: https://github.com/github/awesome-copilot/tree/4f4796f0bf30e105700f97ed8408c12b6aa95e06/skills/github-actions-hardening
  - id: github-secure-use
    resource: https://docs.github.com/en/actions/reference/security/secure-use
  - id: github-syntax
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
  - id: github-events
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows
  - id: github-commands
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-commands
  - id: github-oidc
    resource: https://docs.github.com/en/actions/reference/security/oidc
---

## 入力から影響までを追う

監査では指定範囲を読み取り、修正依頼では承認済みの範囲を変更する。危険な構文の一致だけで重要度を決めず、入力を誰が制御でき、どのコードがどの権限で実行され、何へ到達できるかを確認する。トリガー別の点検という原典の観点を使い、実際の設定と経路で判断する。[^copilot-hardening]

### 権限・認証・runner

- 組織・リポジトリの既定値、workflow/jobの `permissions`、fork設定、再利用先を調べる。`GITHUB_TOKEN` の権限はトリガー名だけで確定しない。`permissions: {}` または必要なread権限を基準に、書き込みは必要なジョブへ限定する。明示時に未指定のscopeはnoneとなり、`id-token` はwrite/noneである。[^github-syntax]
- Secretは実際に渡しているジョブ・Action・再利用先まで追う。マスクを漏洩防止の保証にせず、context全体・認証済み設定・変換した秘密値をログやartifactへ出さない。不要なcheckout認証の永続化は `persist-credentials: false` を検討し、保存先や挙動は対象Action版で確認する。[^github-secure-use]
- クラウドが対応し信頼条件を管理できる場合はOIDCで長期鍵を減らす。必要ジョブだけ `id-token: write` とし、実際のclaims、audience・subject、repository、branch/environmentとクラウド側のrole権限を照合する。固定のsubject例を全リポジトリに当てはめない。[^github-oidc]
- fork PRでもself-hosted runnerの永続状態、ホスト資格情報、ネットワーク、共有ストレージは別のリスクとなる。Secretが渡らないことだけで安全としない。使い捨てrunner登録だけで実行ホストの清浄性を保証せず、隔離と消去の実態を確認する。

### 外部入力と実行コード

PRタイトル・本文・ブランチ名・コメント・dispatch入力等を `run` や `github-script` のスクリプトへ式展開しない。中間環境変数を引用付きで参照し、JavaScriptなら `process.env` 等からデータとして扱う。Actionの入力へ渡す場合も受け手がコードとして評価しないかを追う。

```yaml
- name: Print PR title as data
  env:
    PR_TITLE: ${{ github.event.pull_request.title }}
  run: printf '%s\n' "$PR_TITLE"
```

これはデータの受け渡し例であり、入力の信頼性を上げるものではない。`eval`、`bash -c`、生成したスクリプトへの連結で再解釈しない。改行を含む外部値を `GITHUB_ENV`・`GITHUB_OUTPUT` にそのまま書かない。複数行形式ではdelimiterが値の独立行に現れないことを保証し、任意のデータならファイルに保存して読み手で検証する。[^github-commands]

`pull_request_target` や `workflow_run` 等で特権を持つ処理は、PR由来のcheckout・ローカルAction・ビルド設定・依存インストールのlifecycle scriptを実行しない。見えるシェルだけでなく間接実行も追う。レビュー済みのworkflowから呼ぶだけで、呼び出されるPRコードまで信頼済みにはならない。[^github-events]

### Action・キャッシュ・成果物

外部Actionと再利用ワークフローは公式の対象リポジトリにあるリリースと完全SHAを照合する。SHA固定は参照の可変性を減らすもので、内容の安全性を証明しない。入力、依存コード、ネットワークやSecretの利用も必要な範囲で確認する。依存・Secret・静的セキュリティ検査は既存の検出範囲を確認して選び、全ツールを一律に増やさない。

非特権のbuildから特権の公開処理へ渡すartifactは未信頼のまま扱う。元run・repository・head SHA・イベント・conclusionとの対応を確かめ、ダウンロード先、展開パス、内容と期待する形式を検証する。特権側でスクリプトとして実行しない。`workflow_run` の完了や成功だけを成果物の信頼性の保証にしない。

キャッシュは誰がどのrefで作成し、どの権限のジョブが復元するかを調べる。広いrestoreキーや共有ディレクトリで未信頼コードが特権処理へ持ち込まれないようにする。Secret・token・認証設定を保存しない。署名やattestationを使う場合も、検証対象のdigestと許容する作成者・workflowの対応を確認する。

## 検証と報告

攻撃文字列は隔離したテストでデータのまま扱われることを確認し、実環境で漏洩・権限行使を試さない。監査では位置、入力源、実行経路、実効権限、影響と最小修正を `code-review` の判断に沿って示す。読めない設定、未実行の修正、到達可能性を確認できない点を区別する。

[^copilot-hardening]: Hardeningと同梱参照の調査観点を再構成。トリガーだけによる安全性・重要度の断定は採用しない。
[^github-syntax]: Workflow syntax。実効権限の計算とscopeの正本。
[^github-secure-use]: Secure use。入力処理、Secret、Action固定、runner隔離の根拠。
[^github-oidc]: OIDC reference。実際のclaimsとクラウド側の信頼条件を照合する。
[^github-commands]: Workflow commands。複数行データと環境ファイルの取り扱いを確認する。
[^github-events]: Events that trigger workflows。特権イベントと未信頼コード・artifactの境界を確認する。
