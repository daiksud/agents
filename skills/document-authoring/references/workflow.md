---
type: Guide
title: 文書作業の依存と引き渡し
description: Issue、PR、リポジトリ文書、外部Bundle検査を区別し、必要な依存Skillと停止条件を示します。
---

## 依頼に応じた引き渡し


- 外部Bundleのconformanceだけなら `issue-management`・`change-delivery` が未導入でも読み取り検査を扱い、自作のauthoring条件を課さない。
- Issue計画だけなら `issue-management` で保存・再取得して本文・表示・URLを確認し、`change-delivery` は不要として停止する。
- Issue本文・コメントだけなら `issue-management` の投稿とMarkdown品質を使い、`change-delivery` は不要とする。
- PR本文・リポジトリ文書の変更では、計画承認済みでもIssue計画を保存・確認済みと推測しない。保存・確認済みなら再記録せず、未保存なら公開許可を確認し、未許可の未公開情報だけ投稿先・本文案への許可を得て `issue-management` で計画を保存・再取得し本文・表示・URLを確認する。既存の実行承認を取り直さない。
- PR本文だけの更新は `issue-management` で投稿範囲とMarkdown品質を確認し `change-delivery` でPR本文を更新するが、それだけでリポジトリ編集・マージを始めない。
- 承認済みのリポジトリ文書変更は、Issue計画と実行承認を保持して `change-delivery` で公開mainの確認・整理まで進める。文書だけの変更にコードのTDDを要求しない。
- `issue-management` を利用できなければIssue投稿や文書・PRの変更を始めず、文案と未保存の計画を示す。`change-delivery` を利用できなければリポジトリ文書・PRの変更を始めず、保存済みのIssue計画を作り直さないが、Issue本文・コメントだけの更新は妨げない。どちらも旧スキルで代用しない。
