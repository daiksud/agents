---
type: Instruction
title: Code changes by two independent agents
description: Define ongoing Driver/Navigator collaboration, shared ToDos, staged checks, and automatic re-pairing.
sources:
  - id: issue-98
    resource: https://github.com/daiksud/agents/issues/98
  - id: issue-100
    resource: https://github.com/daiksud/agents/issues/100
  - id: issue-99
    resource: https://github.com/daiksud/agents/issues/99
  - id: issue-138
    resource: https://github.com/daiksud/agents/issues/138
  - id: issue-140
    resource: https://github.com/daiksud/agents/issues/140
  - id: issue-161
    resource: https://github.com/daiksud/agents/issues/161
---

## Code changes by two independent agents

This does not apply to consultation, explanation, or planning alone, or documentation-only changes. For code additions, changes, or fixes, launch a subagent with an independent execution context, and confirm that instructions, results, and additional feedback can be exchanged continuously with the same Navigator. Before the first code edit, confirm that the independent Navigator has launched and that actual initial and follow-up responses have arrived from that same Navigator, then jointly select the next single item from the shared ToDo list. Code edits here include adding or changing test code for Red and behavior-preserving refactoring.[^issue-138]

If subagent functionality is unavailable, permissions are missing, the initial launch explicitly fails, or continued availability cannot be confirmed, do not begin code edits. Do not claim pair work or independent checks were performed; report the confirmed restrictions, that code changes have not begun, and the conditions for resumption. Read-only work, cause investigation, plans, drafts, and shared ToDo candidates within the approved scope may continue, but do not treat their results as agreed by the pair. Do not reinterpret general execution approval or a request to “finish everything” as lifting this stop condition or approving solo implementation.[^issue-138]

If the initial launch explicitly failed and the Navigator's absence is confirmed, the initial launch may be retried after confirming that the cause is resolved or execution conditions have changed. Do not request approval again for the same purpose, but follow existing change protection for additional permissions, costs, or global configuration changes. If launch success is unknown, state after a timeout is unknown, or only an identifier was obtained, check the state; do not assume failure and launch a duplicate Navigator, or edit code until it is confirmed. If continued availability fails after an initial response, treat it as Navigator loss as described below, even before code editing. After confirming continued use is impossible, proceed to automatic re-pairing without waiting for additional user confirmation.[^issue-138] [^issue-161]

In an environment meeting these conditions, the following two agents perform code changes. Explicit invocation of the skill is not a prerequisite.

| Role | Responsibilities and authority |
| --- | --- |
| Driver (main agent) | Own tests, implementation, necessary documents, validation, and integration; be the only agent editing the working files. |
| Navigator (one subagent) | Read requirements, code, diffs, and test results from an execution context independent of the Driver, and return concrete concerns or next checks. |

In internal Driver/Navigator communication, use Controlled English, preserve original text, use lightweight semistructured formats containing only needed items, stable IDs within the task, and updates centered on differences after initial sharing, to reduce misunderstanding and unnecessary retransmission. Do not extend this to language rules for human-facing artifacts; when history is lost or context is insufficient, prioritize re-sharing and existing stop/re-pairing conditions.[^issue-99]

Before the first Navigator request for code changes, the Driver reads `~/.agents/skills/software-development/references/agent-communication.md`. If it cannot be read, do not proceed to the initial request or code editing. Do not assume automatic Navigator inheritance; share relevant collaboration contracts and that material in the initial request. If the Navigator cannot access it directly, share its contents, and do not edit code until the Navigator confirms them. Do not require this material for consultation, planning, or documentation-only work.[^issue-140]

Keep the same Navigator through every cycle of each pair. If responses, resumption, or necessary history are unavailable and continuation is impossible, pause subsequent code changes requiring confirmation and preserve the evidence of lost continuity and confirmed/unconfirmed scope. Do not treat a new agent as continuation of the same Navigator.[^issue-100]

Once the original Navigator cannot be recovered and continuation is confirmed impossible, a new Navigator may be launched as a replacement without waiting for additional user confirmation or approval to re-pair for this loss. Retire the former Navigator, do not treat delayed responses as evidence for the new pair, and do not switch back even if it recovers. Share as much retrievable and retained work context and evidence as possible with the new Navigator. Resumption requires confirmation of continued responses, revalidation from the first unconfirmed stage, and comparison of completed items with the final diff. Do not infer success from missing evidence; rerun affected validation when targets change. Retain the limit of two exchanges for the same finding or issue. If the new pair is also lost, repeat the same automatic recovery process without waiting for user confirmation.[^issue-100] [^issue-161]

After confirming Navigator loss, the Driver reads `~/.agents/skills/software-development/references/navigator-recovery.md` before proceeding to recovery or re-pairing. Before resuming, share the relevant contracts and that material with the new Navigator; provide contents if direct reading is impossible. Do not advance the affected stage until necessary content is confirmed, but do not require additional user confirmation for the Navigator replacement itself. This material is not required for ordinary initial launch, consultation, planning, or documentation-only work.[^issue-140] [^issue-161]

After sharing initial assumptions according to the communication material, follow [Incremental design](development.instructions.md#incremental-design) together, first recording representative normal paths and existing behavior to protect in a shared ToDo list both agents can inspect. Include boundary conditions, exceptional paths, and design improvements only where needed for explicit requirements, existing contracts, confirmed defects, or minimal protection against concrete risks. No dedicated tool or fixed filename is required. Distinguish unstarted, in-progress, and completed items from unagreed requirements needing confirmation. When either Driver or Navigator discovers cases, test gaps, or improvements through learning, compare them with current scope and immediately add only those needed for this change. Do not make future improvements mandatory for the current change. The Driver shares acceptance or rejection of Navigator proposals and reasons, reflects necessary items in the list, and the Navigator confirms that reflection. Adding ToDos or pair agreement does not approve changes to user requirements or expansion of scope.

At the start and after each ToDo is completed, both agents check the list and select the next single item with reasons. As a rule, keep only one item in progress, sized so one small behavior can be completed in one Red / Green / Refactor cycle. If learning before or during implementation shows it contains multiple independent behaviors, separate Reds, or independently completable changes, split it into small behaviors before continuing subsequent independent edits.[^issue-98] Share reasons for changes to selection or decomposition, update the shared ToDo list, and consult again. Keep other behaviors on the list rather than unconditionally packing them into the current implementation. However, do not postpone fixes needed to establish the current stage or regressions in existing behavior merely by recording another ToDo. The Navigator checks original requirements and targets rather than relying only on explanations, and returns candidate tests, boundary conditions, and design concerns. The Driver must not decide the next item alone and start implementation ahead of agreement.

For the selected ToDo, the Driver follows `software-development` through the stages below in order, advancing only after the same Navigator rechecks and resolves findings requiring action for each stage. Do not implement the next stage or another ToDo while waiting for review.

Within each Red / Green / Refactor stage, use the point at which one meaningful result enables the Navigator to change the next decision as a checking boundary. When new diffs and related validation results, unexpected failures or regressions, information affecting subsequent edits, expectations, design, or ToDo decomposition, or fixes and new evidence for findings requiring action become available, do not start subsequent independent edits that depend on that result. Share the actual current diff and validation results with the same Navigator, who checks the actual work and completes necessary fixes/rechecks before proceeding. In particular, do not batch multiple independent fixes until stage end and request only retrospective review.[^issue-98]

Do not define dialogue boundaries by tool calls. Continuous evidence gathering contributing to one decision may be batched: reading related code, tests, or configuration; grep/search; examining multiple files for an agreed step; local tests or related commands checking one change; and checks without state changes. Use a meaningful result the Navigator can apply to the next decision as the unit of dialogue, rather than fixed seconds, operation counts, or command counts.[^issue-98]

| Stage | Driver work | Navigator checks |
| --- | --- | --- |
| Red | Write a minimal test starting from assertions, and confirm it fails because the target behavior is unmet. | Compare requirements, actual test diff, and failure results; confirm expectations and failure reasons are correct rather than environment deficiencies or test errors. Do not treat intentional Red as a defect in the completed change. |
| Green | After Red is confirmed, write the smallest implementation passing that test and related tests. | Check requirements and regressions from actual diffs and success results, and check for unrequested generalization. Allow temporary duplication, but carry design improvements into Refactor in the same cycle. |
| Refactor | After Green is confirmed, make necessary improvements, centered on removing duplication, without changing behavior, and keep related tests Green. | Check the evidence that carried-over improvements were resolved or judged unnecessary, that unnecessary abstractions were not added, and that behavior and test effectiveness are preserved. If no improvement is needed, confirm the decision not to create a change. |

For ToDos consisting only of behavior-preserving cleanup, confirm sufficient existing tests and Green before cleanup/review, without creating formal Reds or unnecessary added tests. Mark only ToDos with required validation and staged review complete. Do not weaken acceptance conditions or test expectations merely to pass tests.

At each check, the Driver connects actual diffs, executed test results, and review results to the same code state. The same HEAD SHA alone does not prove uncommitted diffs are unchanged. If the target changes after requesting a check, rerun affected validation and review; do not use past results as evidence for the changed state. Do not mark findings resolved solely by Driver fixes or evidence-based answers; the Navigator rechecks them. Distinguish findings requiring action at that stage, optional suggestions, and items carried into Refactor in the same cycle. Have the same Navigator check the final diff as well.

Only two agents participate in pair work at once: the Driver and the active Navigator. Normally there is only one Navigator subagent, and original and replacement Navigators do not work concurrently during automatic re-pairing. Neither Driver nor Navigator launches additional implementation, coordination, or pair-review subagents. The Navigator does not delegate to other agents. Even if common instructions apply to the Navigator, do not have the child create another pair. Single-agent role-playing is not a substitute.

Count a Driver fix or evidence-based answer followed by Navigator rechecking as one exchange on the same issue. If it remains unresolved after two exchanges, stop work and report unresolved points, evidence, and options to the user. Do not reset the count by rewording or splitting findings, or claim completion or approval while unresolved. Pair checks do not replace existing PR review, required CI, approval, or merge conditions, or expand scope or execution authority.

[^issue-138]: [Issue #138](https://github.com/daiksud/agents/issues/138) records stopping code changes when the initial Navigator is unavailable, continued read-only work, and boundaries for initial retries and re-pairing.
[^issue-161]: [Issue #161](https://github.com/daiksud/agents/issues/161) records automatic re-pairing after Navigator loss without waiting for additional confirmation, preserving as much context as possible.
[^issue-99]: [Issue #99](https://github.com/daiksud/agents/issues/99) records internal communication in low-entropy Controlled English and its boundary with external artifacts.
[^issue-140]: [Issue #140](https://github.com/daiksud/agents/issues/140) records separating detail while retaining mandatory contracts at entry points, and boundaries for checking and sharing distributed material.
[^issue-100]: [Issue #100](https://github.com/daiksud/agents/issues/100) records preserving evidence after Navigator loss, retiring the former Navigator, and rechecking from the unconfirmed stage.
[^issue-98]: [Issue #98](https://github.com/daiksud/agents/issues/98) records the granularity of one ToDo, short dialogue boundaries within stages, and conditions for avoiding excessive sequential reporting.
