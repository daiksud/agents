---
type: Instruction
title: ブランチと統合単位
description: 変更保護を確認してブランチを準備し、独立して検証・統合できる単位で進めます。
sources:
  - id: continuousdelivery-foundations-continuous-integration
    resource: https://continuousdelivery.com/foundations/continuous-integration/
  - id: github-src-index-ts
    resource: https://github.com/conventional-changelog/commitlint/blob/f4b108182e6d20eca52433135c7ba1675746318e/%40commitlint/config-conventional/src/index.ts#L24-L36
---

## ブランチと統合単位

### GitHub Issueとタスク分割

Issueの内容・指示者・保存確認は[Issueの記録](issue-recording.md)に従う。

- 現在のタスクを独立して計画・実行・検証できる作業に分割する場合は、親Issueに紐づくSub-issueとして作成する。
- 各Sub-issueに作業範囲、完了条件、依存関係を記載する。
- Sub-issueを作成しただけでは、そのタスクに着手しない。
- 依頼の目的・成功条件に含まれる分割タスクは、実施対象・順序を判断して計画へ記録し、現在のセッションで直列に実施する。別の目的や他セッションの担当を追加しない。
- 別セッションに割り当てたタスクは、そのセッションに委ねる。
- Sub-issueへの着手前に、Issue・PR・作業ツリーから他セッションの着手状況を確認する。
- 別セッションが着手済みのタスクには、重複して取り組まない。
- 他セッションの着手状況を判断できない場合は、ユーザーに確認してから着手する。
- 分割後はSub-issueごとに計画・実行・検証を行い、親Issueの計画や検証だけで代替しない。
- 親Issueの完了は、各Sub-issueの完了と親Issue全体の完了条件を確認して判断する。

### 小さな統合単位と活動日

変更を早く検証してmainへ統合し、長期ブランチによる前提のずれを小さくする。CIの原則[^continuousdelivery-foundations-continuous-integration]に基づき、次を計画に含める。

- 1つの変更を、独立して検証・レビュー・統合できる単位にする。ファイル数だけで分けず、利用者の目標と成功条件が確認できるまとまりにする。
- 変更作業を記録した日を活動日とし、活動日の毎日のmain統合、原則1活動日以内のブランチを目安にする。休日などの非活動日を作業遅延と決めつけない。
- Issueに作業開始日時、次の統合単位と検証方法を記録する。1活動日を超えた場合は、承認待ち・レビュー待ち・失敗調査など確認できた原因と次の統合単位を更新する。
- 承認・レビュー・CIを省略して目安を達成しない。期限だけを理由に未検証の変更をマージしない。
- 目的内の分割・順序・対象ファイルの調整は理由と計画を更新して継続する。確認が必要な変更は[着手と計画](planning.md#着手と計画)に従う。Sub-issueの存在だけを実行依頼にしない。
- 着手時に統合先mainの必要な検証を確認する。mainが失敗中なら[復旧手順](review-and-merge.md#統合後mainの確認と復旧)を優先し、正常化するまで後続作業を開始しない。

活動日・滞留・レビュー待ち・検証時間・main復旧時間はIssue・PRと既存Actionsの時刻・URLを根拠に記録する。欠測、代用した時刻、未完了、利用不能を明記し、個人評価や単発比較からの改善効果の断定には使わない。プロジェクトごとの定義と実測値はプロジェクトの文書・Issue・PRに置き、共通スキルに個別実績を埋め込まない。

### ブランチの確認と準備

- 着手時に現在のブランチと作業ツリーの差分を確認する。
- 実行承認がある場合、`main` の場合は、ファイル変更より先に `git switch -c <branch>` で作業ブランチを作成・切り替える。
- 実行承認がある場合も環境の制約でブランチを作成できない場合は、理由を伝え、準備できるまで編集を開始しない。
- `main` 以外で自セッションが作成したと確認できないブランチは、変更前に作業ツリーの差分、最近のコミット、関連Issue・PR、`git worktree list` の結果を読み取り、今回のタスクとの関係と他セッションとの衝突の可能性を検証する。
- ブランチ名や差分がないことだけで、既存ブランチを利用してよいと判断しない。
- 既存ブランチを利用してよい根拠が得られない場合はユーザーに確認し、確認までは編集・ブランチ切り替え・stash・コミットなど状態を変える操作を行わない。
- 現在の作業ディレクトリの作業ブランチで変更・コミット・検証を行う。
- ブランチ名のプリフィックスは次の表に従う。

| 変更内容 | プリフィックス |
| --- | --- |
| 破壊的変更を含む機能追加 | `breaking/feat/` |
| 破壊的変更を含むバグ修正 | `breaking/fix/` |
| 破壊的変更を含まない機能追加 | `feat/` |
| 破壊的変更を含まないバグ修正 | `fix/` |
| ドキュメントのみの変更 | `docs/` |
| その他 | `build/`・`chore/`・`ci/`・`perf/`・`refactor/`・`revert/`・`style/`・`test/` のうち変更内容に合うもの |

その他のプリフィックスは @commitlint/config-conventionalのtype定義[^github-src-index-ts] に従う。
破壊的変更に許可する型は、[コミットメッセージの指示](conventional-commits.md)に従う。

[^continuousdelivery-foundations-continuous-integration]: [CIの原則](https://continuousdelivery.com/foundations/continuous-integration/)。本文に記した参照範囲と採用判断の根拠。
[^github-src-index-ts]: [@commitlint/config-conventionalのtype定義](https://github.com/conventional-changelog/commitlint/blob/f4b108182e6d20eca52433135c7ba1675746318e/%40commitlint/config-conventional/src/index.ts#L24-L36)。本文に記した参照範囲と採用判断の根拠。
