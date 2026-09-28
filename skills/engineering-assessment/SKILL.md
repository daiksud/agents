---
name: engineering-assessment
description: XP、Lean、DevOps、CI/CD、DORA、DDD、architecture、Team Topologies等の開発実践を現状診断し、改善提案・導入計画を作るときに使う。通常の修正、個別コードレビュー、概念説明、導入実装には使わない。
---

# 開発実践を診断し、導入を計画する

利用者へ価値を安全に届ける流れを調べ、最初に試す改善を具体化する。診断という話題だけで終了点を決めず、依頼された終端成果物に応じて回答・Issue記録・実装への引き渡しを選ぶ。Issueへの診断・導入計画の記録だけが終端成果物なら、依存スキル `issue-management` の[診断・計画専用経路](../issue-management/references/issue-recording.md#診断計画専用のissue記録)を使う。Issue記録と実装の両方が依頼されている場合は診断専用経路で停止せず、`issue-management` の通常経路で計画を保存・確認して実装へ引き渡す。以下のリポジトリ・`docs/` は診断対象を指す。

## 範囲と参照資料

対象の指示、利用者の成果、サービス・価値の流れ、制約、既存の診断Issueを確認する。診断範囲・優先順位を左右する目的が不明なら人に確認し、回答に依存しない資料調査を進める。

[証拠から導入計画を作る](references/assessment.md)は診断・計画で読む共通手順とする。そのうえで、依頼されたproblemに必要なlensだけを選ぶ。

| 条件 | 追加で読むreference | 読まないもの |
| --- | --- | --- |
| XPそのもの、XP第2版、Values / Principles / Practices、またはXPを主対象として診断する | [XP taxonomy](references/xp.md) | 無関係なDORA / Architecture全文 |
| Architecture / DORA / Lean等の診断で個別のXP Value / Principle / Practiceだけを補助lensとして使う | [XP個別項目の軽量lookup](references/xp-auxiliary.md) | `xp.md` 全taxonomy |
| Domain / Bounded Context、service・repository・teamの対応、cross-team dependency、Microservices、Conway | [ArchitectureとOrganization](references/architecture-and-organization.md) | 無関係なDORA Catalog全件 |
| DORA Core / Capability Catalog / delivery metrics、DORA Capability | [DORA capability lens](references/dora.md) | 無関係なXP全taxonomy / Architecture全文 |
| BDD / ATDD / TDD / DDD / Lean / DevOps / CI / CDで、定義・相互関係・compact guardrailの確認が必要な診断 | [原則の関係](references/principles.md) | 条件に該当しないfocused reference |
| 出典・版差・採用判断を確認する | [一次資料と適用判断](references/sources.md) | 全資料の無条件な再読 |

複数lensが実際のproblemへ関係する場合だけ組み合わせる。Architecture / DORA / Lean等の診断でXPの個別項目を補助判断に使うだけなら、`xp.md` 全taxonomyを読まず軽量lookupから必要な項目だけ使う。XP自体が診断対象へ広がった場合だけ `xp.md` へ切り替える。たとえばMicroservices採否ではArchitecture / Organizationを中心にDDDとXP SimplicityまたはEconomics等を補助できる。release承認待ちだけならLean / CDと関連DORA Capabilityへ絞る。

定義・版差・compact guardrailが関係者と確認済みで、現在の実践の証拠収集だけが必要な限定診断では、`assessment.md` だけで進めて `principles.md` / `sources.md` を必須にしない。たとえばCIの定義が確認済みなら、main統合・feedback・失敗修復等の実証拠へ直接進める。

限定診断は依頼された概念・困りごとに絞り、関連するlensだけを選ぶ。包括診断ではXPを含む各観点を対象の流れへ照らすが、全referenceを順番に読み込まず、実際に関係するlensを選ぶ。話題語が出ただけで無関係な観点を未確認一覧へ追加せず、依頼範囲を変える場合は確認する。

## 判断と完了の境界

設定や成果物の存在と実際の実践を区別し、観測した実践・根拠のある不足・未確認・理由付き適用外を分ける。責任分担・文化・認知負荷は担当者の経験と照合する。欠測をゼロや改善効果にせず、個人評価・固定Elite判定に使わない。

最も影響する制約から小さい実験を選び、証拠・順序と依存・役割・受け入れ条件・検証・見直しを整理する。担当者の合意・実施日を推測で確定せず、単独開発・レガシー・複数チーム等の条件に合わせる。4チーム新設や一律のリポジトリ分割を導入条件にしない。

依頼された成果物で終了条件を決める。

| 依頼された成果物 | 終了条件 |
| --- | --- |
| 診断、改善ポイント、比較、提案の回答 | 証拠・判断・未確認事項・提案を回答として提示して終了する。Issue作成、文書保存、実装を暗黙に開始しない |
| 診断・導入計画のIssue記録だけ | `issue-management` の診断・計画専用経路で保存・再取得・表示確認し、URLと本文を提示して終了する。診断完了と導入未実施を区別してIssueを開いたまま残す |
| 診断レポート・計画文書の保存 | 診断内容を `document-authoring` へ引き渡す。リポジトリ内文書なら通常のIssue計画を補助成果物として扱い、`change-delivery` で要求された文書を届けて終了する。改善施策の実装へ暗黙に進まない |
| 導入・改善の実装 | `issue-management` の通常経路で実装範囲・受け入れ条件・検証・承認を確認し、承認済み範囲だけを `change-delivery` と担当Skillへ引き渡す |

回答だけを依頼された診断でmain失敗などを見つけても、証拠・影響・復旧優先度を回答へ含めるだけで復旧を開始しない。Issue記録だけを終端成果物として依頼された場合は同じ内容を計画へ記録して停止する。診断レポート等の文書成果物が終端成果物なら、必要な補助Issue計画を経て文書を届けた時点で停止する。Issue記録と実装を同時に依頼された場合は通常の実装計画として扱い、計画保存を補助成果物として完了した後も承認済み実装へ進む。投稿禁止・保存不能・未確認ではIssue記録を成功扱いせず、回答可能な診断結果と未完了の保存範囲を分けて示す。後日の実装で `change-delivery` を利用できなければ実装を開始せず、未完了範囲と導入条件を示す。
