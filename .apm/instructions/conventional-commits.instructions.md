---
type: Instruction
title: コミットメッセージ
description: コミットメッセージは Conventional Commits の仕様に従います。
---

# コミットメッセージ

- 英語で簡潔に書く。
- タイトルの形式は `<type>[(scope)][!]: <description>`（`[]` 内は任意）。コロンの後にスペースを入れる。
- 新機能は `feat`、バグ修正は `fix`。その他は `docs`、`refactor`、`test`、`chore` など、変更内容に合う型を使う。
- スコープは変更対象を表す名詞にする（例: `fix(parser): handle empty input`）。
- 破壊的変更は `feat` または `fix` の場合のみ許可する。
- 破壊的変更は `:` の直前に `!` を付けてタイトルで説明するか、フッターに `BREAKING CHANGE: <説明>` を書く。
- 本文・フッターは必要な場合のみ追加し、前のセクションとの間に空行を入れる。
- フッターは `Token: 値` または `Token #値` の形式にする。トークン内の空白は `-` にする（`BREAKING CHANGE` は例外）。
