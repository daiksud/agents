---
type: Guide
title: Build an adoption plan from evidence
description: Evidence to inspect, treatment of unknowns, improvement priorities, and how to present the requested deliverable.
---

## Build an adoption plan from evidence

### Target and observation scope

First organize the user's difficulties and expected outcomes, target services, flow including delivery and operations, and constraints. If the target repository alone is insufficient, identify boundaries with other repositories, organizations, and external services. Treat evidence beyond your permissions as unavailable; do not change access rights or organizations to expand assessment scope on your own.

Find existing glossaries, specifications, design decisions, and assessment Issues first; decide the observation period and target SHA. Do not claim a short observation period represents general operation. When definitions or versions affect a judgment, check authoritative material for the selected lens and record the version and date actually checked. Distinguish checking dates from source publication dates.

### Perspectives and evidence

| Perspective | Evidence beyond diffs and configuration | Treatment when evidence is missing |
| --- | --- | --- |
| DevOps and Lean | Actual cases from request through publication and operations; waiting, rework, interruptions, incident learning, and stakeholder experience | Do not judge shared responsibility or culture from policy documents alone |
| CI | Actual integration history, branch lifetimes, checks executed on main, and failure-to-repair examples | Do not declare CI achieved from YAML or branch success alone |
| CD | Deployment records for the same artifact, configuration versions, on-demand execution, exploration, and recovery records | Deployment jobs alone do not prove delivery is possible at any time |
| BDD and ATDD | Rules, examples, questions, acceptance conditions, and with whom and when expectations were checked and mapped to implementation | Missing meeting minutes alone do not mean absence of practice; ask stakeholders |
| TDD | Evidence or practitioner explanations of tests first, failure, success, and cleanup in recent changes | Completed tests or squashed history alone do not establish whether tests came first |
| XP | Examples of design fitting current requirements, shared understanding, design improvement from small feedback, and sustainable work | Do not assess all XP from TDD/BDD artifacts, or infer absence from missing fixed meetings/roles. Ask stakeholders about actual work |
| DORA Capability | Actual change / test / deploy / feedback / learning records relevant to the problem and practitioner experience | Tools, configuration, or Catalog inclusion alone do not establish achievement or gaps. Use `dora.md` to distinguish Core / Catalog / metrics |
| DDD | Meaning of terminology and implementation, boundary contracts and translation, business decisions and technical processing, design reasons | Glossary presence is not model quality |
| Architecture and Organization boundaries | Co-changes, test/deploy dependencies, runtime topology, release units, ownership, cross-team coordination, and waiting in actual changes | Service counts, repository splits, Bounded Context documents, or CODEOWNERS alone do not establish loose coupling or independent delivery |
| Team Topologies | Actual responsibilities, handoffs, waiting, service use and blocking dependencies, interaction purposes/periods, and stakeholder cognitive load | CODEOWNERS or team counts do not establish team types, capabilities, or culture |

For Architecture / Organization difficulties, use [boundary and coupling assessment](architecture-and-organization.md) to observe semantic, change, runtime, deployment, repository, and team ownership boundaries separately. Before proposing Microservices or team restructuring, check the need for independent change/test/deploy and current evidence of distributed-system and coordination costs.

For DORA assessments, use the [DORA Capability lens](dora.md) to distinguish Core / Catalog / metrics / research and select only capabilities relevant to current constraints. Align metrics by service, period, and definition; do not make individual rankings or direct metric manipulation improvement targets.

Record each judgment as “observed practice,” “evidence-backed gap,” “unverified,” or “not applicable (with reasons).” Attach evidence, people, and questions needed to test hypotheses. Explicitly mark important perspectives within the requested scope that were not examined as unverified. Do not mechanically add out-of-scope concepts to the unknowns list in a focused assessment.

When operational detection and recovery concern the problem, trace one case of user impact: which signal enabled whom to detect it, and which observations, notifications, and procedures supported decisions and recovery. Logs, metrics, traces, or runbooks alone do not establish sufficiency; inspect records of actual use and practitioner experience. If only the author used a procedure, recovery by other operators remains unverified.

If you lack access to observability services, leave evidence unavailable; do not replace “unverified” with “no monitoring.” When repeated manual work or configuration differences constrain flow, inspect frequency, impact, failures, and maintenance cost before considering automation. Do not require full automation merely because of one-off work or manual approval.

### Choose the first experiment

Prioritize from value impact, actual waits/failures, dependencies, change risks, and validation costs. Do not derive adoption order from a tool list. Even with many candidates, first present a small group whose results can be observed.

| Example situation | Small experiment candidate | Change to verify |
| --- | --- | --- |
| Legacy system without a validation foothold | Agree on one important existing behavior, add a regression test and minimal automated validation path | Detect the target defect and execute on shared main |
| Long-lived branches obstruct integration | Independently verifiable change units and short feedback paths | Changes in actual integration intervals, waiting, and main health |
| Manual work required at every publication | Verify reproducibility and recovery of one delivery path | Redeliver and recover the same artifact with established approval |
| Users report incidents and recovery depends on experts | Confirm detection signals, notification recipients, decision and recovery procedures for one user impact with stakeholders; plan an exercise | Detect the target impact and enable intended operators to decide using necessary information and procedures |
| Cross-team waiting dominates | Confirm responsibilities and interaction purposes/periods at one boundary with stakeholders | Changes in inquiry/handoff waiting and load |

These examples are not prescriptions before assessment. Preserve confirmed rules and contracts. If decisions are unresolved, make confirming conditions with stakeholders a prerequisite to the first experiment. Do not make full legacy rewrites, Microservices, repository splitting, or particular products universal solutions.

Use the [DORA lens](dora.md) for Core / Catalog / metrics version differences.

Map each experiment to its target state, current evidence, participating roles, order/dependencies, acceptance conditions, observation method, and reassessment point. Propose rollback and stop conditions when changes pose operational risks. Do not invent numerical targets or schedules; distinguish provisional proposals from agreed conditions.

### Plan deliverables

Present findings according to the requested terminal deliverable. If only an answer is requested, directly present the following in a suitable structure; do not implicitly create an Issue. If only Issue recording is requested, save the same content to an Issue.

- Target users, purpose, success conditions, services, investigation scope, and constraints.
- Evidence locations and datetimes, SHAs, periods, observed practices, gaps, unknowns, and reasons for non-applicability.
- Priorities and grounds, the first small experiment, and dependencies/order of later candidates.
- Expected changes, responsible roles, acceptance conditions/validation, current measurements and missing data, and reassessment points.
- The state “assessment and planning only; adoption not implemented” and unresolved questions.

If a document such as an assessment report or plan is the terminal deliverable, save the above in the requested format and location. For repository documents, use the supporting Issue plan and delivery path below. Finish when the document is delivered; do not implement improvement measures unless separately requested.

#### Issue records

Search existing Issues in the confirmed target before creating a record. Preserve the original request, prior evidence, reasons, and relevant history when updating. State the requested outcome, success conditions, scope, proposed order, validation, unresolved decisions, and whether implementation is approved. Assign new Issues to the confirmed requester and select existing labels by their meaning. Use concise English Conventional Commits titles, the target's body language and template, and self-contained explanations with evidence links as supplements.

Keep publication within approved destinations and information scope. Save complete Markdown drafts without YAML frontmatter, format/check with rumdl using the applicable configuration, inspect the resulting diff, and confirm another formatting pass is unchanged. Publish the checked body, retrieve it, and compare the complete saved content with the draft. Check GitHub rendering of headings, tables, lists, and links; API HTML inspection is not visual screen inspection. Open a browser only when requested. Present the saved body and URL. Failed saves or unverified readback remain incomplete.

For diagnosis/planning-only records, leave the Issue open and stop after presenting it. Recording an Issue does not approve implementation, select Sub-issues for execution, or require a formulaic implementation-approval question.

#### Repository documents

Save and verify the supporting Issue plan before editing repository documents. Preserve the target's format, language, existing sources, and unknown metadata. Check document content and links, and report executed results separately from planned or unavailable validation.

Protect existing work and prepare a task branch. Deliver the document through commits, a draft PR, required CI and conflict resolution, ordinary current-HEAD review, and any necessary fixes with renewed checks/review. Preserve the target's approval and protection requirements. Before a permitted squash or merge-commit merge, confirm current-head review, passing required checks, resolved findings, no conflicts, and healthy main; preserve the final PR title/body verbatim. Verify required checks on the actual merged-main SHA, synchronize, and clean up the task branch. Do not claim completion while main is failing or unverified. Honor explicit stop conditions; document delivery does not authorize adopting its proposals.

#### Implementation scope

A clear implementation request authorizes its stated purpose and success conditions; retain that approval through plan saving and verification rather than asking again for each stage. Continue adjustments to procedures or files within that scope. Changes to purpose, outcomes, acceptance conditions, external impact, permissions, or costs require confirmation before the affected work. An Issue, proposal, or silence alone does not authorize execution.

When implementation is also requested, save and verify the plan above, then continue the approved changes through the same branch, review, CI, integration, and main-verification boundaries as repository documents. For settings-only changes, apply only approved differences, retrieve the effective settings, and check required behavior without creating empty commits or PRs. Report actual results, unresolved conditions, and unavailable operations; do not silently widen access or begin unapproved releases or deployments.
