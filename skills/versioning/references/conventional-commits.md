---
type: Guide
title: Conventional Commits
description: コミットの形式と変更の意味をそろえ、バージョン計算に必要な情報をマージ後も残す。
---

## 件名と本文

コミット件名は[Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)の形式にする。PRタイトルにも同じ形式を使う。

```text
<type>[optional scope][!]: <description>
```

- `type` は変更の目的で選ぶ。機能追加は `feat`、バグ修正は `fix` とし、ほかに `docs`、`refactor`、`test`、`ci` などを使う。
- `scope` は対象の領域やモジュールを示す。不要なら省く。
- `description` は実際の変更を簡潔に述べる。例は `fix(parser): reject empty input`。
- 本文には変更内容と理由を記録し、件名・本文・フッターを空行で区切る。

互換性を壊す変更は、任意のtypeに付けた `!`、または `BREAKING CHANGE: 説明`・`BREAKING-CHANGE: 説明` のフッターで示す。影響と必要な移行方法も説明する。

## マージ後に残す情報

スカッシュマージでは最終PRタイトルを件名、本文をコミット本文・フッターとして保存し、その組み合わせを検査する。タイトルだけを検査して、本文の破壊的変更情報を失わないようにする。

元のコミットが履歴に残るマージ方式では、それぞれのメッセージも検査する。マージ方式とメッセージ設定に合わせ、検査した内容が実際のコミットへ保存されることを確認する。

形式の検査方法は[commitlintの導入](commitlint.md)を使う。形式が正しくても、typeや破壊的変更の表記が変更内容に合うとは限らない。公開APIへの影響と記録内容の一致はレビューで確認する。
