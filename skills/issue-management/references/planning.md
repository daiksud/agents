---
type: Instruction
title: Planning and execution scope
description: Determine execution scope from requests and connect impact, uncertainty, and validation environments to plans.
sources:
  - id: github-instructions-spec-driven-workflow-v1-instructions-md
    resource: https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/instructions/spec-driven-workflow-v1.instructions.md
  - id: github-agents-research-technical-spike-agent-md
    resource: https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/agents/research-technical-spike.agent.md
  - id: github-context-map-skill-md
    resource: https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/skills/context-map/SKILL.md
  - id: context-engineering
    resource: https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/instructions/context-engineering.instructions.md
  - id: taming-copilot
    resource: https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/instructions/taming-copilot.instructions.md
---

## Planning and execution scope

### Starting and planning

Determine execution scope from user requests and conversation approval under the following conditions. Plans, Issues, Sub-issues, or silence alone are not execution requests.

| Situation | Judgment |
| --- | --- |
| Change/implementation request with clear purpose and scope | Treat the request as execution approval; implement after saving, verifying, and presenting the plan below |
| “Implement it” for presented plans, instructions to address a specified Issue or start its goal | Read targets and retain conversation approval. Do not ask the same approval before/after saving |
| Consultation, investigation, or planning only | Stop at the requested deliverable without implementation, including individual change plans |
| Adjustments to procedures, files, prototypes, decomposition, or order meeting the same purpose/success conditions | Update reasons/plan and continue within the purpose |
| Changed purpose, outcomes, acceptance conditions, increased external impact, unagreed business decisions, additional permissions | Present concrete proposals/reasons, confirm, and wait for dependent execution |

1. Read target instructions and actual files, concretizing purpose, success conditions, changes, validation, and completion. Scale investigation to impact/uncertainty; do not add repository-wide structural investigation for spelling fixes.
2. Check targets, dependencies, referrers, existing tests, and similar evidence through [Impact investigation](#investigating-change-impact-context-map), including decision evidence in the plan. Ask about important unagreed matters and continue independent investigation.
3. Save plans under [Issue content](issue-recording.md#issue-content), recording request/approval grounds and scope/order. Preserve prior bodies/reasons for plan updates.
4. Through [Post-save procedures](issue-recording.md#opening-the-browser-after-saving-an-issue), verify retrieved body agreement/display and URL/body presentation. Explain inability to save/verify; implementation waits until saving is confirmed.
5. With execution approval above, hand off to the responsible skill after saved-plan verification. For Git-managed files use `change-delivery` through branch preparation, post-integration main verification, and cleanup. For GitHub-side settings only use `github-repo` through applying differences, retrieval, and diagnosis, without empty commits/PRs. Apply ordinary delivery to prerequisite file changes. Do not recreate saved plans; honor explicit stops such as “through PR.” Implementation, commits, pushes, or PRs are not default endpoints; do not ask again whether to execute the next stage.
6. For changes needing confirmation, record/retrieve/present concrete proposals and reasons in Issues and ask. Continue within approval afterward and continue independent existing work. Reduced outcomes or relaxed acceptance conditions also require this.

Retain approval across continuation/resumption. Do not confuse quoted goal instructions or Issue-viewing requests with execution instructions, or extend them to another purpose, other sessions' responsibilities, or environment permissions. Confirm when execution intent cannot be established and affects outcomes.

Prioritize execution-environment/user restrictions such as Plan Mode or read-only access. If posting is prohibited, present unsaved plans without changing branches, files, evaluation data, or generated artifacts. Do not add formulaic implementation-approval questions for planning-only requests.

### Investigating change impact (context map)

Before saving Issue plans, organize the following from actual files/evidence. Show relationships with changes, not only filenames, so users understand targets, dependencies, validation, and risks.

- Search targets and check each file's role and needed changes.
- Investigate direct dependencies and referrers, needed updates, and impact. Documents include link targets, incoming links, and related-instruction consistency.
- Read related tests and organize behavior they check and validation to add, update, or run. Test presence is not validation success.
- Identify authoritative specifications, contracts, and configuration; find analogous implementation/descriptions. Show concrete reference patterns and reasons fitting the current boundaries/requirements.[^context-engineering]
- For version-dependent judgments, check versions from configuration, locks, and implementation against corresponding official material. Latest material or memory alone does not establish target-version evidence; retain unconfirmed comparisons.[^taming-copilot]
- Check evidence-based risks relevant to changes, such as public API compatibility, data migration, or configuration changes.

Integrate results and referenced files/scope into existing Issue plans, validation, and risks. Small changes may use short descriptions without fixed tables, empty fields, or dedicated files. Missing/inaccessible matters do not prove “no impact”; retain unverified scope/checking methods, connecting important matters to [Validation of important uncertainties](#validation-of-important-uncertainties).

Include maps in [Starting and planning](#starting-and-planning) records without another approval wait. Changes needing confirmation follow the same procedures.

If branch switches or related changes alter investigation assumptions, reread needed files/reference versions and update plan evidence. Open tabs or past summaries alone do not establish current state. Divide changes into verifiable related contracts, implementation, and tests rather than by file counts.[^context-engineering]

### Reassessing the remaining plan

For multiple independent integration units, after integrating each unit and confirming main validation, briefly reassess remaining plans before starting the next. Do not aim solely to follow the initial plan; reflect new implementation/test/review/integration facts in next decisions.

- Check whether new facts change remaining assumptions, scope, order, decomposition, dependencies, ownership boundaries, or validation methods.
- If unchanged, retain confirmed facts without formally rewriting plans and proceed.
- If changes are needed within the same purpose/success conditions, record reasons and updated plans without extra approval. For changes to purpose, outcomes, acceptance conditions, external impact, or permissions, confirm through [Starting and planning](#starting-and-planning).
- Do not redo completed units differently without new evidence. If later improvements suffice, update remaining plans rather than defaulting to rollback for quality.
- Do not add comprehensive reinvestigation or formulaic documents for reassessment. Check only decision-relevant scope against latest main and current validation results.

### Validation of important uncertainties

For uncertainties affecting outcomes/feasibility, include affected judgments, checking methods, and results allowing subsequent decisions in plans. Separate facts from hypotheses and connect them to agreed success conditions to clarify investigation/prototype purposes/endpoints.

- Investigate technical questions through existing code/official material; plan minimal prototypes only when insufficient. Define observable outcomes/judgment criteria first; if unmet/unconfirmed, record and reassess. Prototype success does not validate entire implementations.
- Retain unsettled business rules/acceptance conditions as questions to authorized users. Technical investigation, prototypes, or assumed figures do not establish agreement; continue independent read-only investigation.
- Prototype edits/execution also follow [Starting and planning](#starting-and-planning) approval scope. Without approval, record only; within approval, do not reconfirm each operation. Changes to purpose, outcomes, acceptance conditions, or external impact require the same reapproval.
- Do not add prototypes/formal fields for spelling fixes with no decision-relevant uncertainty. Judge sufficiency of existing plans/validation from impact.

### Preparing the validation environment

Known necessary tools/pinned dependencies may be installed in temporary/project-specific environments after checking existing environments. Temporary download-based execution such as `uvx` follows the same criteria. Record targets, versions, locations, and reasons without overwriting global environments.

For global settings, additional permissions, costs, or installations with unverifiable provenance/execution, show necessary targets/reasons and confirm. Do not bypass refusals/restrictions; check authorized alternatives and do not treat inability to validate as success. Execution approval does not increase sandbox/network permissions.

### Execution permissions and tool calls

- Git-managed-file plans include commits, pushes, PRs, review requests/replies, fixes, squash merges, main switch and git pull, and deletion of merged branches. Do not split them into individual additional requests within the same purpose/success conditions; proceed after preceding success is verified.
- Do not replace them with optional suggestions such as “create a PR if needed” or “confirm whether to merge.” Without stop conditions, PR creation onward is default scope for Git-managed-file work.
- During planning check commands, write destinations, network access, and current permission; state missing permissions.
- Plan approval is not environment permission; confirm reasons/targets for additional permissions or conditions above.
- Batch related reading/independent checks in one tool call without repeatedly fetching unchanged information.
- Do not combine commands requiring elevation with ordinary-permission commands in the same shell sequence; execute each with appropriate permissions.
- Execute dependent operations after preceding success is confirmed.
- Use completion waits or spaced checks for review/CI, avoiding excessive polling.
- Distinguish fewer tool calls from hiding execution display; do not promise unavailable display controls.

### Sources and application decisions

Checked GitHub awesome-copilot Spec Driven Workflow v1[^github-instructions-spec-driven-workflow-v1-instructions-md] and Technical spike research mode[^github-agents-research-technical-spike-agent-md] on 2026-09-11, summarizing/restructuring uncertainty-scaled investigation/prototypes, pre-experiment success conditions, and evidence-based decision updates.

This environment limits them to important outcome/feasibility uncertainties, distinguishes business agreement from technical validation, and integrates existing Issues/approval. It does not require the sources' fixed three documents, confidence scores, uniform six stages, complete operation logs, comprehensive investigation, or dedicated prototype documents. This is an application decision, not wholesale adoption.

Checked GitHub awesome-copilot context-map[^github-context-map-skill-md] on 2026-09-11, summarizing/restructuring target, dependency, test, pattern, and risk perspectives. Include document links, related instructions, and referrer impact in existing Issue planning here. Do not introduce fixed tables/checklists or separate map review waits; integrate checking into existing plan approval.

Checked Context Engineering[^context-engineering] and Taming Copilot[^taming-copilot] on 2026-09-13, integrating concrete reference patterns, target-version evidence, and rechecking changed assumptions. IDE tab/cursor operations, creating `COPILOT.md`, one-file-at-a-time changes, or announcements before every tool are not common requirements.

[^context-engineering]: [Context Engineering](https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/instructions/context-engineering.instructions.md). Apply related information, reference patterns, and context updates to investigation here.
[^taming-copilot]: [Taming Copilot](https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/instructions/taming-copilot.instructions.md). Apply tool checking of version-dependent information to target-version comparisons.
[^github-instructions-spec-driven-workflow-v1-instructions-md]: [GitHub awesome-copilot Spec Driven Workflow v1](https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/instructions/spec-driven-workflow-v1.instructions.md). Evidence for reference scope and adoption decisions stated in the text.
[^github-agents-research-technical-spike-agent-md]: [Technical spike research mode](https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/agents/research-technical-spike.agent.md). Evidence for reference scope and adoption decisions stated in the text.
[^github-context-map-skill-md]: [GitHub awesome-copilot context-map](https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/skills/context-map/SKILL.md). Evidence for reference scope and adoption decisions stated in the text.
