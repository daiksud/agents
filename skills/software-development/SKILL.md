---
name: software-development
description: Use to implement code additions or changes, bug fixes, and refactoring. Implement and validate through TDD, Simple Design, and small feedback cycles. Do not use for specification work, consultation, investigation, or document creation alone.
---

# Develop software through small feedback cycles

For code additions, changes, or fixes, also use `issue-management` for Issue plans, publication permission, and execution scope, and `change-delivery` for approved changes through branches, PRs, CI, and post-integration main verification. If `issue-management` is unavailable, do not post Issues or substitute another Skill; show unsaved drafts and restrictions. If `change-delivery` is unavailable, do not begin code changes or substitute another Skill; show incomplete scope. `docs/` below refers to the working repository.
Read material corresponding to the stage. Do not add unrelated UI/performance validation or design patterns.

- For responsibility, dependency, or comment design decisions: [Responsibilities, contracts, and comments](references/design.md).
- For discovering or specifying domain rules, shared external contracts, or acceptance conditions: the dependency [behavior-specification](../behavior-specification/SKILL.md). Reuse agreed specifications.
- For tests starting from assertions, test layers, reproducibility, UI, or performance validation design: [Change units and reproducible validation](references/testing.md).
- For checking definitions or adoption reasons: [Primary sources and adoption decisions](references/sources.md).
- Before the first Navigator request for code changes: [Internal Driver/Navigator communication](references/agent-communication.md). Follow common application/stop conditions and share the contents with the Navigator.
- When continuation with a launched Navigator is impossible: pause subsequent code changes under common instructions, read [Handoff and rechecking](references/navigator-recovery.md), and transfer as much context as possible to a new Navigator without waiting for user confirmation. Not needed for ordinary initial launch.
- For continued checking requests to the same Navigator in GitHub Copilot CLI: [Runtime-specific implementation](references/copilot-cli-pairing.md). Do not require the same tools or arguments in other runtimes.

## Start with a story

Build systems and features story-first: before design, describe who can do what, in which situation, after completion. If stories or acceptance conditions are unsettled, organize concrete examples and unanswered questions through `behavior-specification`. Reuse existing agreed stories; connect technical fixes or cleanup to existing purposes and expected results.

## Evolve design from current requirements

Make XP's five values concrete in shared ToDos, short tests, and pair feedback through the [Mapping in the bundled design material](references/design.md#xpの5価値を実装の判断へ使う). For Simple Design, check that current contracts and tests are satisfied, intent is clear, duplication of the same rules decreases, and unnecessary elements are not added. Follow YAGNI; do not preemptively add interfaces, extension points, or configuration for hypothetical future features. Introduce structure needed by actual requirements or feedback in small Refactor steps. See [Design material](references/design.md#simple-designとyagni) for evidence and the adopted scope in this environment.

## Starting XP alone

For learning or practice by one human, propose beginning with this Skill's small TDD cycles, design evolving from current requirements, and short feedback from existing automated builds and tests. This is an adoption proposal for this environment, not a fixed sequence in the original sources. Check [Sources and adoption decisions](references/sources.md#一人でのxp導入の採用判断). Distinguish human numbers from AI Driver/Navigator roles, and preserve existing staged checks, ordinary review, required CI, and integration conditions.

- Follow “Start with a story,” dividing work by small meaningful user outcomes and completion conditions. Do not use commit counts or one TDD iteration as outcome units.
- Run existing fast automated checks for each change, and slower overall checks at necessary stages. CI is frequent integration and validation of shared code; small commits or pushes alone do not achieve it. Follow `change-delivery` for execution, integration, and main checks. Releases deliver something users can actually use; distinguish integration, deployment, and release, and follow existing publication permission.
- For ongoing personal work or planning consultation, propose choosing small outcomes and completion conditions to deliver at the week's start, and briefly reflecting on results, difficulties, and one next change at week's end. Reuse existing Issues and ToDos; do not require weekly rituals or dedicated documents for every short code task. Follow existing procedures for reassessing plans between integration units.
- Separate required outcomes from work to do if time allows. If time is insufficient, adjust scope without cutting quality, tests, or review. Consult through `issue-management` before reducing agreed outcomes or acceptance conditions; do not arbitrarily move them to optional.
- Humans should choose sustainable work including rest rather than push through fatigue. Agents do not infer fatigue; when users request rest or interruption, respond by preserving confirmed results, incomplete items, and the next step. Do not create unrequested reminders or weekly automations.

## Design scope and change decomposition

When judging design policy, impact, change size, or decomposition into Sub-issues or small integration units, read [Responsibilities, contracts, and comments](references/design.md#変更の範囲と分割). Follow `issue-management` execution scope for changes requiring confirmation; if scope grows during implementation, reassess decomposition and execution scope before exceeding approval.

## Shared understanding and acceptance conditions

Before implementation, organize purposes, rules, representative examples, and unanswered questions, and define corresponding acceptance conditions. Distinguish existing agreements from assumptions; do not settle unagreed business decisions through agreement between AIs.

When adding or changing domain rules, even agreed ones, follow [Shared understanding and feature documents](../behavior-specification/references/behavior.md) in `behavior-specification`, also using `document-authoring` to save `docs/behavior/<feature-name>.feature.md` before implementation. Do not unnecessarily rewrite correct existing specifications; keep mappings to tests traceable.

## Test-driven development (TDD)

Follow [Incremental design](../../.apm/instructions/development.instructions.md#incremental-design), first listing representative normal paths in a ToDo list including test items. Include variants, boundaries, and failure conditions only as needed for explicit requirements, existing contracts, confirmed defects, or minimal protection against concrete risks, without covering imaginary cases. Begin bug fixes with reproduction tests, without using incremental design to omit existing behavior protection or necessary design improvements.
Do not implement all tests at once; repeat the following one item at a time from the list. In pair work, follow common instructions: Driver and Navigator evolve the same shared ToDo list and discuss the next single item and its selection reasons. This skill defines TDD targets and validation; common instructions govern roles, edit authority, between-stage review, and stop conditions.
For changes only to internal technical processing, do not create feature documents; write necessary specifications in tests.

1. **Red**: As test-first work, express expected post-implementation behavior in executable tests before the corresponding implementation code. Use assert-first: write the assertion that must ultimately pass first, then add necessary target operations and setup. Confirm failure because the specification is unmet.
2. **Green**: Implement the minimum that passes the new test and existing related tests. Do not anticipate unrequired features or generalization.
3. **Refactor**: Improve implementation and test design while keeping Green. If no improvement is needed, do not add changes; proceed to the next test.

- Prefer fast unit tests, choosing contract, integration, or acceptance tests according to the defect's nature. If actual DB or communication boundaries cause the problem, do not substitute only mocks unable to detect it.
- Do not treat environment deficiencies or test errors as confirmed Red.
- For behavior-preserving cleanup, first confirm existing test coverage and success. Reuse sufficient tests; if insufficient, supplement them from assertions of existing specifications and confirm success before cleanup. Keep Green; do not create additional tests or intentional failures for formality.
- Do not achieve success by weakening assertions or copying implementation output directly into expectations. Compare newly discovered cases with current scope, adding only those needed for current requirements and contracts to the ToDo list. Do not make future improvements mandatory now, or substitute another recorded item for fixes establishing the current stage or regressions.

## Validation and reporting

Read [Change units and reproducible validation](references/testing.md#欠陥の再現と報告) for reproduction tests, specification mappings, test layers, and exploratory/acceptance validation. Report executed tests, Red / Green, other validation, and unverified scope, without treating unexecuted checks or environment deficiencies as success.
