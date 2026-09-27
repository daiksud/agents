---
type: Reference
title: 開発実践と作業スキルの用語
description: このパッケージで用いる開発実践と診断の用語、適用範囲、対応する名称を定義します。
sources:
  - id: engineering-model
    resource: engineering/model.md
  - id: architecture-organization-lens
    resource: ../skills/engineering-assessment/references/architecture-and-organization.md
  - id: dora-lens
    resource: ../skills/engineering-assessment/references/dora.md
  - id: xp-lens
    resource: ../skills/engineering-assessment/references/xp.md
  - id: xp-principles
    resource: ../skills/software-development/references/sources.md
  - id: okf-v02
    resource: https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/ad30107c31c06aec8a7d5636e0d1058118604e6f/SPEC.md
  - id: issue-100
    resource: https://github.com/daiksud/agents/issues/100
---

## 開発実践と作業スキルの用語

ここでの境界は、agentsパッケージの「開発実践の指示・診断」の文脈である。導入先の業務ドメインや組織を定義しない。実行コードの識別子がない概念には、対応する指示・スキル上の名称を示す。[概念と出典](../skills/engineering-assessment/references/principles.md)も参照する。

| 用語 | この文脈での定義 | 適用境界 | コード・指示上の名称 |
| --- | --- | --- | --- |
| Engineering model | 開発実践をValues / Principles、Practices、Capabilities、Architectural / Organizational Choicesに分類し、相互の多対多の関係と配置境界を示す概念モデル | agentsパッケージの保守・診断知識。成熟度の一方向階層やruntime必須ルールにはしない | `docs/engineering/model.md` |
| Values / Principles | 判断時に何を優先するかを示す価値・原則。具体的な作業手順や能力の達成状態とは区別する | 開発判断・診断 | engineering model、各Instruction |
| Practice | 価値・原則を具体化する、繰り返し実行する行動。別体系ではCapabilityとして扱われる場合がある | 開発実践・診断 | TDD、Pair Programming、CI、Small Batches等 |
| Capability | チーム・システムが実際に持つ観測可能な能力。設定やPracticeの存在だけで達成済みと判定しない | engineering modelの分類とDORA / Architecture診断 | `engineering-assessment` のfocused lens |
| Architectural / Organizational Choice | 現在の要求・制約・能力から選ぶ構造、配置、責任境界。上位成熟状態や既定解とは扱わない | 設計・組織の判断・診断 | Microservices、module / deployment / team boundaries等 |
| XP | Communication・Simplicity・Feedback・Courage・Respectを軸に、小さなテストと協働から設計を進化させる開発思想 | 開発判断・実装・診断 | `development`、`software-development`、`engineering-assessment` |
| XP Value | XPで判断時に重視する5つの価値。Practiceの実施数や成熟度スコアとは区別する | 日常の開発判断・XP診断 | `development`、`engineering-assessment/references/xp.md` |
| XP Principle | XPのValueと具体的Practiceの間をつなぐ判断原則。独立した共通Instruction一覧へ平坦化しない | XP診断 | `engineering-assessment/references/xp.md` |
| XP Primary Practice | XP第2版でPrimaryに分類された具体的Practice。13項目すべての一律導入を要求しない | XPの実践・診断 | `engineering-assessment/references/xp.md`、該当する実行Skill |
| XP Corollary Practice | XP第2版でCorollaryに分類された具体的Practice。11項目の採用数を成熟度としない | XPの実践・診断 | `engineering-assessment/references/xp.md`、該当する実行Skill |
| Simple Design | 現在の契約を満たし、意図を伝え、同じルールの重複と不要な要素を減らす設計の判断基準 | 開発判断と設計・実装 | `software-development` の設計資料 |
| YAGNI | 仮想の将来機能を先取りせず、現在必要な検証・設計改善を保つ判断 | 開発判断と設計・実装 | `software-development` の設計資料 |
| DevOps | 開発から運用まで、利用者の成果と品質に対する責任・学習を共有する実践 | 開発実践の指示・診断 | deliveryのDevOps、`engineering-assessment` |
| Lean | 利用者価値を起点に流れ・仕掛かり・待ち・手戻りを改善し、人を尊重して学ぶ考え方 | 開発実践の指示・診断 | deliveryのLean、`engineering-assessment` |
| 継続的インテグレーション | 小さな変更の頻繁なmain統合、速い自動検証、失敗修復を続ける実践。XP / CD文脈ではPractice、DORAではCapabilityとしても扱う | 開発実践の指示・診断 | CI、`change-delivery` |
| 継続的デリバリー | 検証済みの変更を必要なときに安全に配布できる状態として維持するCapability / system of work。複数のPracticeに支えられる | 開発実践の指示・診断 | CD、`engineering-assessment` |
| 継続的デプロイメント | 検証を通った変更を自動的に本番へ配備する実践 | 開発実践の指示・診断 | Continuous Deployment（CDと区別） |
| BDD | 具体例を使う共同の発見・定式化・自動化を通じて期待するふるまいの理解を深める実践 | 開発実践の指示・診断 | `behavior-specification`、`*.feature.md` |
| ATDD | 対応する実装に先立ち、受け入れ条件・テストを具体化する実践 | 開発実践の指示・診断 | `behavior-specification` |
| TDD | テスト項目を含むToDoから一つずつRed・最小のGreen・必要なRefactorを反復する設計・検証の実践 | 開発実践の指示・診断 | `software-development` |
| 共有ToDo | TDDの対象となる小さな振る舞い、境界・異常系、既存ふるまいの保護、設計改善を記録し、未着手・進行中・完了・要確認を区別するリスト | 各ペア内で同じNavigatorと継続して協働するDriver/Navigatorのコード変更。専用ツール・固定ファイル名は要求しない | 共通インストラクションの共有ToDoリスト |
| Driver | 2エージェントでのコード変更を進めるメインエージェント。共有ToDoをNavigatorと共同で選び、テスト・実装・統合を担い、作業対象を編集する唯一の役割 | 独立コンテキストを持つそのペアのNavigatorと継続的にフィードバックを交換できる環境でのコード変更 | 共通インストラクションのDriver |
| Navigator | Driverと独立した実行コンテキストを持つ1体の読み取り専用サブエージェント。共有ToDo、要件・コード・差分・テスト結果を確認し、Red・Green・Refactorごとにフィードバックする | 各ペア内では同じNavigatorを使い、交代する場合も同時に有効なNavigatorは1体とするコード変更 | 共通インストラクションのNavigator |
| 再ペア | Navigatorを復旧できないときに停止・報告し、その喪失への明示承認を受けて元Navigatorを担当から外し、新しいNavigatorと別のペアを始めること。未確認段階と未解決指摘を引き継ぐ。[^issue-100] | 継続不能になったDriver/Navigatorのコード変更。作業全体や過去の再ペア承認では再開しない | 共通インストラクションの承認付き再ペア |
| ストーリーファースト | 設計より先に、誰が、どの状況で、完成後に何をできるかを語り、受け入れ条件へつなぐ本環境の方針 | システム・機能の構築。技術修正・整理では既存の目的・期待結果へ結ぶ | decision-makingの目的・目標・手段・スタンダード、`behavior-specification` |
| スタンダード | 複数のプロジェクトで目標を満たす手段を選ぶ際に繰り返し使う判断基準・優先順位。ユーザーの判断から抽出した候補はIssueへの記録だけでは採用されない | 共通作業原則の設計判断・候補Issueの記録 | decision-makingのスタンダード、`issue-management` の共通スタンダード候補 |
| テストファースト | 実装後の期待するふるまいを、対応する実装コードより先にテストで表現する本環境の方針 | コード変更。ふるまい不変の整理では十分な既存テストの成功を先に確認し、不足時は先に補う | developmentの共有理解と検証、`software-development` |
| アサートファースト | 最後にパスすべきアサーションを最初に書き、必要な対象操作と準備を補う本環境の方針。実行順とは区別する | テストの作成 | `software-development` のレッド、テスト資料 |
| DDD | 業務の知識、モデル、境界、共有された言語を軸に複雑さを扱う設計 | 開発実践の指示・診断 | domain-modelingのDDD、`software-development` |
| OOP | 状態とふるまいをオブジェクトにまとめる設計手段。DDDの必須形式ではない | 設計・実装の指示 | Object-Oriented Programming、`software-development` |
| SOLID | 責務・拡張・置換可能性・インターフェース・依存方向を点検する設計原則。抽象型やクラス数を目標にしない | 設計・実装の指示 | `software-development` の設計判断 |
| GoFパターン | 繰り返し現れるオブジェクト設計の問題と解決形を共有する語彙。実際の要求に応じて選択する | 設計・実装の指示 | Strategy、Adapter、Builder等、`software-development` |
| 外部契約 | モデルやシステムの境界を越えて利用者に約束する入出力・失敗・副作用等の条件 | 仕様記述・検証の指示 | feature、API仕様、スキーマ、`document-authoring` |
| 仕様の正本 | ある要求・契約を変更するときに基準として更新する記録。情報ごとに特定し他文書から参照する | 仕様記述の指示 | feature、ADR、API仕様、`document-authoring` |
| 不安定なテスト | 同じ条件で結果が揺れるテスト。再試行成功と原因の解消を区別する | テスト・検証の指示 | flaky test、`software-development` |
| サブドメイン | 業務上の問題領域の一部分 | 開発実践の指示・診断 | Subdomain |
| Domain boundary | 業務上の問題・知識の範囲を区切る境界。Bounded Contextのsemantic boundaryやtechnical boundaryとは区別する | Architecture / Organization診断 | `engineering-assessment` のarchitecture lens |
| 境界づけられたコンテキスト | 一つのモデルの意味が通用する明示的な範囲 | 開発実践の指示・診断 | Bounded Context |
| Change boundary | 独立して理解・変更・検証できる変更単位の境界。semantic / runtime / deployment / repository boundaryとは区別する | Architecture / Organization診断 | `engineering-assessment` のarchitecture lens |
| Runtime boundary | 別process・componentとして実行され、runtime failureや通信の境界となる単位 | Architecture / Organization診断 | `engineering-assessment` のarchitecture lens |
| Deployment boundary | 独立してdeploy・release・rollbackできる配布単位の境界。build依存は関連する制約として別に確認する | Architecture / Organization診断 | `engineering-assessment` のarchitecture lens |
| Repository boundary | source・history・automationを同じ管理単位として扱う境界。service / Bounded Context / teamとの1対1を要求しない | Architecture / Organization診断 | `engineering-assessment` のarchitecture lens |
| Team ownership boundary | 継続的な意思決定・運用・改善責任を持つ範囲。CODEOWNERSだけで確定しない | Architecture / Organization診断 | `engineering-assessment` のarchitecture lens |
| Microservices | 独立change・deploy・scale・ownership等の必要性に応じて選び得るArchitecture choice。DDDやteam数から自動採用しない | Architecture / Organizationの選択・診断 | `engineering-assessment` のarchitecture lens |
| ユビキタス言語 | 同じモデルの境界内で、会話・文書・コードを通じて使う共通の言語 | 開発実践の指示・診断 | Ubiquitous Language、導入先の `docs/glossary.md` |
| チームトポロジー | 価値の流れと認知負荷を軸に、チームの責任と相互作用を進化させる考え方 | 開発実践の指示・診断 | Team Topologies |
| Team API | チームの責任、サービス、期待、関わり方を示す資料 | 開発実践の指示・診断 | Team API（HTTP APIではない） |
| DORA Core Model | DORA研究で繰り返し支持されたCapability・Performance・Outcomeの関係を保守的にまとめるmodel | DORA診断。Capability Catalogや最新metrics guideと区別する | `engineering-assessment/references/dora.md` |
| DORA Capability Catalog | Core項目に加えてCore外・AI関連等も含むCapability catalog。掲載自体を必須導入条件にしない | DORA診断 | `engineering-assessment/references/dora.md` |
| DORA指標 | 対象serviceのsoftware delivery performanceを観測し改善feedbackに使う指標。Core v2.1.0のFour key metricsと現行5 metrics guideを区別する | 開発実践の診断 | `engineering-assessment/references/dora.md` |
| 導入診断 | 証拠・不足・未確認・適用外を区別し、改善の優先順位を決める調査 | 診断スキル | `engineering-assessment` |
| 導入計画 | 最初の小さな実験、依存・順序、期待する変化と検証・見直し条件を示す成果物 | 診断スキルとIssue記録 | `engineering-assessment`、`issue-management` |
| 導入未実施 | 診断・計画を記録したが、その変更は実行していない状態 | 診断スキルとIssue記録 | Issue本文の状態。自動で閉じない |

Simple Design・YAGNIの定義と本環境への適用範囲は、一次資料と採用判断に従う。[^xp-principles]

### OKF文書検査の用語

この境界は配布スキルによる文書検査であり、利用先の業務モデルとは別である。OKFの語義は固定版の仕様に基づく。[^okf-v02]

| 用語 | この文脈での定義 | 適用境界 | コード・指示上の名称 |
| --- | --- | --- | --- |
| Bundle | 検査対象として指定した文書ツリーのルートと配布単位 | OKF文書検査 | `bundle` |
| Concept ID | Bundle内の概念ファイルパスから.mdを除いた識別子 | OKF文書検査 | Concept ID |
| 適合検査 | OKF §11の受け入れ条件の検査 | OKF文書検査 | `conformance` |
| 自作時の検査 | 適合条件に自作文書の記述品質の条件を加える検査 | OKF文書検査 | `authoring` |
| 出典ID | 個別主張の脚注とsourcesを順序に依存せず結ぶキー | OKF文書検査 | `sources[].id` |
| 確認記録 | 文書の内容や計算定義を確認したActorと日時 | OKF文書検査 | `verified` |
| 実行証明 | 許可された計算による単一実行の結果をreceiptから確認すること。静的検査の対象外 | OKF計算契約 | Attestation |

[^issue-100]: [Issue #100](https://github.com/daiksud/agents/issues/100) のNavigator喪失と承認付き再ペアの条件。
[^xp-principles]: Simple Design・YAGNIの一次資料と本環境のテスト・設計改善への適用判断。
[^okf-v02]: OKF v0.2 §§2、5、10–11。profile名は本パッケージの検査契約。
