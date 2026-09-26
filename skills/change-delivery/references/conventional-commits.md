---
type: Instruction
title: コミットメッセージ
description: コミットメッセージは Conventional Commits の仕様に従います。
sources:
  - id: conventional-commits
    resource: https://www.conventionalcommits.org/en/v1.0.0/
  - id: commit-message-storyteller
    resource: https://github.com/github/awesome-copilot/blob/4f4796f0bf30e105700f97ed8408c12b6aa95e06/skills/commit-message-storyteller/SKILL.md
  - id: conventional-commit
    resource: https://github.com/github/awesome-copilot/blob/4f4796f0bf30e105700f97ed8408c12b6aa95e06/skills/conventional-commit/SKILL.md
  - id: git-commit
    resource: https://github.com/github/awesome-copilot/blob/4f4796f0bf30e105700f97ed8408c12b6aa95e06/skills/git-commit/SKILL.md
---

## コミットメッセージ

### 対象と根拠を確認する

- 文案は提示された差分・変更説明、または依頼対象の差分から作る。リポジトリを調べる場合は `git status`、`git diff --cached`、`git diff` でstagedとunstagedを区別し、対象外の変更を混ぜない。[^git-commit]
- type・scope・説明はファイル名だけで決めず、実際の変更の目的と既存の用語から選ぶ。本文には確認済みの背景を使い、原因・意図・代替案・性能値・検証結果・Issue番号を推測で補わない。[^commit-message-storyteller]
- 情報が不足する場合は既存のIssue・仕様・差分を確認し、それでも目的や対象を決められない点だけ質問する。単純な変更の文案に不要な背景の回答を必須にしない。

### 件名・本文・フッター

- タイトルの形式は `<type>[(scope)][!]: <description>`（`[]` 内は任意）。コロンの後にスペースを入れる。[^conventional-commits]
- 新機能は `feat`、バグ修正は `fix`。その他は `docs`、`refactor`、`test`、`chore` など、変更内容に合う型を使う。スコープは既存の領域・モジュールを表す名詞にし、不要なら省略する（例: `fix(parser): handle empty input`）。[^conventional-commits]
- 英語の命令形で具体的かつ簡潔に書き、件名末尾にピリオドを付けない。件名全体は72文字以内を目安とするが、機械的な切り詰めや新しい強制チェックを要求しない。[^commit-message-storyteller]
- 本文は件名や差分だけでは分からない問題・変更理由・影響・判断上の制約を補う場合に追加する。単純な変更は件名だけでよく、未置換の欄や応答文をメッセージへ残さない。[^commit-message-storyteller]
- 本文・フッターは必要な場合のみ追加し、前のセクションとの間に空行を入れる。フッターは `Token: 値` または `Token #値` の形式にし、トークン内の空白は `-` にする（`BREAKING CHANGE` は例外）。[^conventional-commits]
- 関連Issueへの参照は確認できた番号を使う。`Closes`・`Fixes` などの終了指定は、その変更でIssueを解決することを確認できる場合だけ使い、一部対応では `Refs` などの参照にする。
- 本環境では破壊的変更を `feat` または `fix` の場合のみ許可する。これは任意のtypeで破壊的変更を表せる標準仕様に対するローカル規約である。[^conventional-commits]
- 破壊的変更は `:` の直前に `!` を付けてタイトルで説明するか、フッターに `BREAKING CHANGE: <説明>` を書く。利用者への互換性の影響と既知の移行方法を説明し、Issue参照がないことを理由に必要な説明を削除しない。[^conventional-commits]

### コミットする場合

文案だけの依頼ではコピーできるメッセージを提示して終了する。Git操作を行う範囲は依存スキル `issue-management` の「計画と実行範囲」、他セッションの作業保護と変更単位は[ブランチと統合単位](branches.md)に従う。承認済みの同じ範囲について、コミットごとの再承認を要求しない。

1. 承認対象の関連する実装・テスト・文書を、同じ目的を検証できる変更単位として扱う。ファイル数や拡張子だけで分けず、無関係な整理は含めない。分割案の提示を対象外のコミットの承認とみなさない。[^git-commit]
2. stageが必要なら、対象ファイル・差分範囲を確認して承認対象だけを追加する。同じファイルに対象外のunstaged変更があれば、ファイル全体の追加で取り込まない。他者のstaged変更が混在していれば、勝手に解除・移動したり、そのままコミットしたりせず、必要な調整を確認する。
3. 文案を書いた後、コミット直前にstaged差分全体が承認対象と一致することを確認する。続けて文案の各主張を差分・確認済みの背景と照合し、対象外の変更や未確認の理由が含まれていないことを確かめてからコミットする。作成後も結果を確認し、指定された停止条件に従う。[^conventional-commit]
4. hook等で失敗した場合は成功と報告せず、HEAD・status・staged/unstaged差分を再確認する。hookによる変更も承認範囲と照合し、必要な修正・再検証と最終index確認後に通常のコミットを再試行する。自動的なhook回避やamendは行わない。[^git-commit]

### 参照元と適用判断

GitHub awesome-copilotの3資料を固定版で確認し、commit-message-storytellerの目的・理由を伝える文章作法[^commit-message-storyteller]、conventional-commitの差分確認と構造[^conventional-commit]、git-commitの目的に沿う変更単位と失敗時の扱い[^git-commit]を要約・再構成した。

本環境では既存の承認・変更保護へ統合する。固定XML、文案生成後の無条件コミット、毎回の「Story told」説明、Issueがなければフッターを全廃する指示は採用しない。72文字は読みやすさの目安とし、本文の一律文字数制限は設けない。

[^git-commit]: Git Commit。実際の差分・目的による変更単位とhook失敗時の扱いを採用し、stage例は既存の変更保護に従って適用する。
[^commit-message-storyteller]: Commit Message Storyteller。変更の目的・背景・影響と件名の文章作法を採用し、未確認の背景の推測と固定出力形式は採用しない。
[^conventional-commits]: Conventional Commits 1.0.0。形式・type・scope・本文・フッターと破壊的変更の標準仕様。
[^conventional-commit]: Conventional Commit。差分とメッセージの対応・構造を採用し、XMLと文案からの自動実行は採用しない。
