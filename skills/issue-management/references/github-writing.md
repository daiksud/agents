---
type: Instruction
title: IssueとPRの書き方
description: GitHub IssueとPull Requestのタイトル・本文に残す情報と役割の違いを定めます。
sources:
  - id: conventional-commits
    resource: https://www.conventionalcommits.org/en/v1.0.0/
  - id: github-issue-quickstart
    resource: https://docs.github.com/en/issues/tracking-your-work-with-issues/learning-about-issues/quickstart
  - id: github-review-changes
    resource: https://docs.github.com/en/pull-requests/concepts/helping-others-review-your-changes
  - id: github-link-pr-issue
    resource: https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue
  - id: google-cl-descriptions
    resource: https://google.github.io/eng-practices/review/developer/cl-descriptions.html
---

## IssueとPRの書き方

Issueは実現したい状態と完了条件を、Pull Requestは実際に行った変更とその検証を記録する。両者を同じテンプレートの複製にせず、将来の読み手がタイトルと本文から「何を変える・変えたのか」と「なぜ必要なのか」を追えるようにする。GitHubはIssueに一目で内容が分かるタイトルと目的・解決に必要な情報を、PRに問題・アプローチ・結果を理解できる文脈を勧めている。Googleの変更説明ガイドも、変更内容と理由を将来の履歴に残すことを重視する。[^github-issue-quickstart] [^github-review-changes] [^google-cl-descriptions]

### タイトル

IssueとPRのタイトルは、次のConventional Commits形式で記述する。

```text
<type>[(scope)][!]: <description>
```

Conventional Commits 1.0.0が規定する対象はコミットメッセージであり、Issue・PRタイトルへの適用は、作業項目・変更・スカッシュコミットで同じ語彙を使うための本環境のローカル規約とする。標準仕様そのものがIssue・PRタイトルを要求しているとは扱わない。[^conventional-commits]

- `feat`、`fix`、`docs`、`refactor`、`test`、`chore` など、対象リポジトリのコミット規約と変更の意図に合うtypeを使う。リポジトリ固有の許可typeがあればそれを優先する。
- scopeは安定したドメイン・コンポーネント・責務を短い名詞で示せる場合だけ付ける。意味のないscopeを埋めるために追加しない。
- descriptionは英語の命令形で、対象と変化が分かるよう具体的かつ簡潔に書き、末尾にピリオドを付けない。「fix bug」「update docs」「phase 1」のように、対象や変化が分からない表現だけで済ませない。[^google-cl-descriptions]
- `!` は対象リポジトリのコミット規約が破壊的変更を許可するtypeに限り、互換性を壊す変更であることを確認できる場合だけ使う。本環境の既定規約では `feat` または `fix` に限る。Issueの段階で未確認の破壊的変更を推測して付けない。

### 共通の本文原則

- 本文だけで目的・変更理由・重要な文脈が分かるようにする。Issue、設計文書、外部資料へのリンクは根拠や詳細への導線として使い、リンク先を読まなければ理由が分からない本文にしない。[^google-cl-descriptions]
- 対象リポジトリにIssue Form、Issue template、PR templateがある場合はその構造を優先する。指定がなければ内容に合う構成を選び、固定見出し、空の節、「なし」の埋め草を共通要件にしない。
- 確認済みの事実、計画、実施済みの結果、未確認事項を区別する。予定を実施済みの変更や検証結果として書かず、分からない原因・効果を推測で補わない。
- 短いIssue・PRは短く書いてよい。情報量ではなく、現在の判断と将来の検索・理解に必要な文脈が残っているかで判断する。

### Issue本文

Issueは「どう実装したか」ではなく「どの状態を実現したいか」を中心に書く。GitHubもIssue本文には目的と解決に役立つ情報を求め、バグでは再現手順・期待結果・実際の結果を例示している。[^github-issue-quickstart]

- 目的・問題・現在との差分を示す。
- 完了を判定できる成功条件と、守る必要がある制約を示す。
- 実装計画が決まっている場合は、作業範囲・順序・検証方法を記録する。未決定の実装方法、変更ファイル、設計を推測して成功条件へ固定しない。
- バグでは必要に応じて再現条件、期待する結果、実際の結果を記録する。
- 承認待ち、未実行の検証、依存関係など、完了判断に影響する状態を明示する。

### PR本文

PRはレビュー対象となる「実際の変更」を記録する。GitHubは明確なタイトルと説明によって、問題、アプローチ、結果、レビューで注目すべき点を理解できるようにすることを勧めている。[^github-review-changes]

- 何を変更したかと、なぜその変更が必要だったかを書く。
- 実行した検証と結果を示し、未確認の範囲があれば区別する。
- 重要な制約、既知の限界、意図的な対象外、レビューで特に確認してほしい点は、判断に必要な場合だけ記載する。
- Issue本文をそのまま複製せず、Issueが目標を、PRが実際の差分を説明するように役割を分ける。
- レビュー対応で変更内容・理由・検証結果・重要な制約が変わった場合は、PR本文も現在のHEADに合わせて更新する。

PRがIssueを完全に解決する場合は、対象リポジトリの既定ブランチへ向けたPR本文で `Closes #123`、`Fixes #123`、`Resolves #123` などのclosing keywordを使える。部分対応や後続作業が残る場合は自動closeを使わず、通常の参照として関連付ける。GitHubではclosing keywordでリンクしたPRが既定ブランチへマージされると、関連Issueが自動的にcloseされる。[^github-link-pr-issue]

### 参照元と適用判断

Conventional Commitsの構文とtype・scope・破壊的変更の表現をタイトル形式の基礎にするが、Issue・PRへの適用自体は本環境の規約である。GitHubのIssue・PRガイドから、目的が分かるタイトル、解決・レビューに必要な文脈、問題・アプローチ・結果の説明、Issue連携を採用する。Google Engineering Practicesから、変更内容と理由を将来の履歴に残し、短い要約だけでなく必要な文脈を本文へ残す考え方を採用する。固定テンプレート、必須の本文長、全Issue・PRへの同一見出しは導入しない。

[^github-issue-quickstart]: GitHub Docs「Quickstart for GitHub Issues」。Issueの説明的なタイトル、目的、バグ報告での再現・期待・実際の結果の例。
[^github-review-changes]: GitHub Docs「Helping others review your changes」。PRを小さく明確にし、問題・アプローチ・結果とレビューに必要な文脈を示す指針。
[^google-cl-descriptions]: Google Engineering Practices「Writing good CL descriptions」。変更内容と理由を将来の履歴へ残し、短い要約と必要な文脈を記述する指針。
[^conventional-commits]: Conventional Commits 1.0.0。コミットメッセージの構文、type・scope・破壊的変更の仕様。
[^github-link-pr-issue]: GitHub Docs「Linking a pull request to an issue」。closing keywordによるIssue連携と既定ブランチへのマージ時の自動close。
