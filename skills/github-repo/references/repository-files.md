---
type: Instruction
title: リポジトリの設定ファイル
description: GitHub側の前提条件を確認し、依存関係の更新、担当者、投稿用テンプレート、脆弱性の報告方法、任意の参加手順や問い合わせ先を整備する。
---

## 既存の設定を活かす

対象のデフォルトブランチ、既存ファイル、適用されるコミュニティ健全性ファイルの既定設定、有効な機能、保守担当者を確認する。同等の設定があれば活かし、導入先で使う言語を維持する。依頼された範囲で必要な不足ファイルだけを追加する。ファイルを変更しただけでは、そのファイルを前提とするGitHubの設定は有効にならない。

リポジトリ固有のファイルを追加する前に、継承されて実際に使われているテンプレートを確認する。リポジトリ固有の有効なIssueテンプレート、または `.github/ISSUE_TEMPLATE/config.yml` を置くと、継承元のIssueテンプレートディレクトリ全体が使われなくなる。意図した投稿の選択肢を維持する。

## Dependabotのバージョン更新

Dependabotが対応する依存関係を持つリポジトリでは、デフォルトブランチの `.github/dependabot.yml` にバージョン更新を設定することを推奨する（SHOULD）。各エコシステムとディレクトリを実際のマニフェストに合わせる。変更を依頼されていない限り、既存のスケジュール、グループ化、無視する条件、レジストリの選択を維持する。現在対応しているエコシステムは[オプションのリファレンス](https://docs.github.com/en/code-security/reference/supply-chain-security/dependabot-options-reference)で確認する。

GitHub Actionsでは、ワークフローが `.github/workflows` にあっても、`package-ecosystem: github-actions` と `directory: /` を指定する。次の例はActionsだけを対象とする。週次のスケジュールは導入時の一例であり、既存の更新頻度を置き換えるものではない。

```yaml
version: 2
updates:
  - package-ecosystem: github-actions
    directory: /
    schedule:
      interval: weekly
```

バージョン更新の設定と、Dependabotアラートやセキュリティ更新の有効化は別の操作である。保存された設定と認識されたマニフェストを確認し、取得できる場合は更新ジョブの結果と作成されたPRも確認する。ファイルが存在することや、更新PRがないことだけでは、必要な依存関係が正しく対象になっているとは判断できない。依存関係の更新にも通常のレビューと必須チェックを適用する。

## コードオーナー

保守の担当者を明示し、レビューを依頼するために、CODEOWNERSの利用を推奨する（SHOULD）。新しく配置する場合は `.github/CODEOWNERS` を優先し、有効な既存ファイルがある場合は尊重する。GitHubは `.github/`、リポジトリのルート、`docs/` の順に探し、最初に見つかったファイルを使う。PRではbase branchにあるファイルが使われる。

対象リポジトリへの明示的なwrite権限を持つ、実在するユーザーまたは表示可能なチームを指定する。CODEOWNERS自体の担当者も含める。次の `@OWNER` は保存前に確認済みの保守担当者へ置き換える。パスごとのルールは担当が異なる箇所にだけ追加する。

```text
* @OWNER
/.github/CODEOWNERS @OWNER
```

後に書かれた一致パターンが優先される。代表的なパスとCODEOWNERS自体に適用される担当者を確認し、GitHubが報告する構文エラーも確認する。担当者が存在しない、または権限が不足している場合は、担当者として割り当てられない。Draft PRでは、Ready for reviewにしたときにCode Ownerへレビューが自動で依頼される。

Code Ownerの承認をマージ条件にする場合は、承認できる担当者と機能の利用可否を確認してから、対応するRulesetまたはブランチ保護の条件を設定する。ファイルを置くだけでは承認は必須にならない。複数のCode Ownerがいる場合は、そのうち1人の承認で要件を満たせる。レビュアーを推測で補ったり、1人で管理するリポジトリに満たせない承認条件を課したりしない。ファイルの妥当性とは別に、有効なルールと実際のPRのマージ可否を確認する。

## IssueとPRのテンプレート

報告や提案にIssuesを使うリポジトリでは、簡潔なIssueテンプレートを用意することを推奨する（SHOULD）。PRを受け付けるリポジトリでは、簡潔なPRテンプレートを用意することを推奨する（SHOULD）。同等の既存テンプレートを維持し、不足している案内を補う場合にだけ、同梱のひな形を使う。

| 同梱ファイル | 導入先の配置場所 |
| --- | --- |
| [バグ報告](../assets/issue-templates/bug_report.yml) | `.github/ISSUE_TEMPLATE/bug_report.yml` |
| [機能提案](../assets/issue-templates/feature_request.yml) | `.github/ISSUE_TEMPLATE/feature_request.yml` |
| [テンプレート選択画面](../assets/issue-templates/config.yml) | `.github/ISSUE_TEMPLATE/config.yml` |
| [PRテンプレート](../assets/pull_request_template.md) | `.github/pull_request_template.md` |

テンプレートを表示するには、先にデフォルトブランチへマージする。Issue FormsはYAML形式で、PRには使えない。Issuesが無効な場合は、該当する依頼がない限り、テンプレートを配置するためだけにIssuesを有効にしない。

- 導入時に必須にするのは、問題または望む結果だけにする。導入先で必要とされない限り、再現の詳細、環境、解決案は任意にする。回答必須の質問票や長いチェックリストは避ける。
- 公開の投稿を意図的に制限している場合を除き、`blank_issues_enabled: true` にして空のIssueを作れる選択肢を残す。`false` にしても、write以上の権限を持つ保守担当者向けの空のIssue作成機能は残る。
- ラベル、担当者、プロジェクト、連絡先リンクは、存在、権限、用途を確認してから追加する。Issue Formsは存在しないラベルを作成しない。
- PRの案内は概要、任意の判断事項、実際の検証結果に絞る。提出する本文から執筆用のHTMLコメントを削除する。テンプレートは執筆を案内するものであり、レビュー、CI、本文が必要な内容を満たし続けることを強制しない。

YAMLとスキーマの妥当性、デフォルトブランチに保存されたファイルを確認する。利用できる場合はIssueの選択画面と、送信前のIssue／PR作成フォームを開き、意図した入力欄、空のIssueの選択肢、PR本文の初期入力を確認する。テンプレートの検証だけを目的に、ダミーのIssueやPRを送信しない。静的確認と、画面で確認した動作を区別する。

## 参加手順と問い合わせ先

**MAY:** 参加者に投稿や開発の進め方を案内したい場合、`.github/CONTRIBUTING.md` を用意してよい。Issue・PRの提出方法や必要な検証を、確認済みの運用に合わせて記載する。既存の文書にある手順はリンクで参照し、未確認のルールを作り上げない。[参加ガイドの公式仕様](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/setting-guidelines-for-repository-contributors)では、IssueとPRの作成時に案内へのリンクが表示される。

**MAY:** 問い合わせ先や利用者向けの支援情報を案内したい場合、`.github/SUPPORT.md` を用意してよい。確認済みの窓口、対応範囲、FAQや既存文書へのリンクを記載する。担当者や応答期限を作り上げず、脆弱性の報告は既存のセキュリティポリシーに従って案内する。[サポート情報の公式仕様](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-support-resources-to-your-project)では、Issueの作成時に案内へのリンクが表示される。

いずれも新規配置は `.github/` を優先する。ルートや `docs/` に有効な既存ファイルがある場合や、[既定のコミュニティ健全性ファイル](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file)が継承されている場合は活かし、重複するファイルを追加しない。採用する場合はデフォルトブランチに保存された内容とリンク先を確認する。利用できる作成画面で案内を確認し、検証のためだけにIssuesを有効にしたり、IssueやPRを送信したりしない。静的確認と、画面で確認した動作を区別する。

## セキュリティポリシー

保守しているプロジェクトでは、対応するバージョンまたはブランチと、実際に使える非公開の脆弱性報告先を示す `.github/SECURITY.md`、または同等の有効なセキュリティポリシーを用意することを推奨する（SHOULD）。保守担当者の対応範囲と、担当者が確認している報告先を確かめる。連絡先のメールアドレスや対応を約束する文言、脆弱性への対応手順を創作しない。

次のひな形は2か所のプレースホルダーを確認済みの情報に置き換えてから使う。

```markdown
# セキュリティポリシー

## 対応バージョン

<保守対象のバージョンまたはブランチ。>

## 脆弱性の報告

<確認済みの非公開報告先URL、または担当者が確認している連絡先。>
```

GitHubの非公開の脆弱性報告を使う場合は、報告先として案内する前に、利用可能で有効になっていることを確認する。Markdownファイルを置くだけでは、この機能は有効にならない。テスト用の脆弱性は送信せず、Securityページに表示される有効なポリシーと報告先を確認する。報告先が未定なら、使えないポリシーを公開せず、報告先を決める必要があることを伝える。
