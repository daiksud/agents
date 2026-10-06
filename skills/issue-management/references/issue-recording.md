---
type: Instruction
title: Recording and presenting Issues
description: Define Issue content, save/display verification, and recording paths for diagnosis-only or follow-up requests.
---

## Recording and presenting Issues

### Issue content

Associate changes and artifact creation with Issues, search existing Issues, and identify numbers and URLs. If none corresponds, record a plan before implementation. Assign Issues/Sub-issues to the task requester; ask if unidentified. Do not unconditionally equate the authenticated user with the requester.

- Follow [Writing Issues and PRs](github-writing.md) for titles and bodies. Plan Issues state whose desired state this is (purpose), specifications/constraints judging achievement (success conditions), scope/files/order (plan), checking methods/results (validation), and completion conditions. Do not confuse purposes, goals, and means.
- Follow destination templates. If none is specified, choose content-appropriate structure without requiring fixed headings, unnecessary tables/Alerts, empty sections, or “none” filler. Explicitly state important restrictions such as unexecuted validation or pending approval.
- Check repository label names/descriptions at creation and set appropriate labels; reassess when scope changes.
- Follow [Markdown quality for GitHub](markdown-quality.md) for pre-post formatting/checks and post-save body agreement/display. Do not add OKF to Issue bodies.

### Parent Issues and Sub-issues

When splitting work meeting the parent's purpose and success conditions into independently plannable/verifiable units, create linked Sub-issues rather than unrelated follow-up Issues.

1. Preserve decomposition reasons/order in the parent plan, and record each child's scope, validation/completion conditions, and dependencies. Connect parent success conditions to child completion conditions; do not guess child numbers/URLs before creation.
2. Format/check the updated parent and each complete child body with common rumdl configuration before posting/updating. Record dependencies using actual numbers from created children, and link them as parent Sub-issues on GitHub. Retrieve parent and children, and check **agreement with final formatted bodies, GitHub rendering, and saved parent/child relationships** before presenting verified bodies and retrieved URLs. If saving, agreement, or relationships are unconfirmed, work is incomplete; follow [Post-save procedures](#opening-the-browser-after-saving-an-issue) for browsers.
3. Child creation alone does not approve or start implementation. With retained parent execution approval and decomposition within the same success conditions, hand off approved scope after plan saving/verification without reapproval solely for decomposition. For planning-only requests, stop at recording/presentation.

Judge parent completion after every Sub-issue completes and the parent's own success conditions are confirmed. Child creation or plan saving alone does not complete the parent.

### Opening the browser after saving an Issue

These common procedures apply to new Issues (including Sub-issues and follow-up Issues without plans) and saved/updated plans. Regardless of browser opening, verify saving, body agreement, and display before each path's presentation and approval.

1. Retrieve the saved Issue and compare its body with the formatted/checked body from [Posting quality procedures](markdown-quality.md). Do not open while saving failed or body is unverified.
2. If the user requests opening, open the retrieved URL once through the OS-standard URL launcher. On macOS use `open <URL>`, passing the URL as one argument. Repeated launch permission, settings changes, or dedicated scripts are unnecessary.
3. Do not open twice for one save operation. During recovery, check saved/opened state and resume only incomplete parts. Without a request, do not open; proceed.
4. Check GitHub rendering and present the URL. Also present saved bodies at completion of ordinary/updated plans and diagnosis/planning. Follow each path's approval requirements; saving verification alone is not approval.

Separate opening failure from saving success, explaining reasons and URL without recreating/resaving. State unverified rendering scope; opening failure alone does not stop approved work. Opening success is neither visual verification nor implementation approval.

### Recording common standard candidates

Apply when the user chooses an implementation policy with tradeoffs and a criterion reusable across projects emerges, including consultation/read-only review. Do not create candidates solely for one-time implementation instructions, project-specific decisions, unchosen proposals, or review-material statements.

1. Organize the chosen option, alternatives, tradeoffs, reasons/history, applicability, and exceptions. Ask the user if reasons or scope are unclear. If unresolved, separate confirmed decisions from unanswered questions without treating inferred criteria as agreed.
2. Check visibility of the posting destination `daiksud/agents`. If grounds include private repositories/material or user statements absent from published material and the destination is public, show draft and publication scope and do not save before explicit posting permission. Verify sources of published statements. Do not ask again when explicit permission exists for the same draft/destination, or infer permission to publish unpublished statements from general Issue-creation requests. Even after permission, exclude project-specific private information; separately confirm permission for content needing transcription.
3. Search both open and closed `daiksud/agents` Issues. For open candidates on the same judgment, preserve original bodies/reasons and add new evidence/unresolved matters without duplicates. For closed Issues, check closure reasons, adoption/rejection, and replacements; show URLs if the same criterion is current. If revision is needed, create a new candidate referencing current authoritative material and the closed Issue, without rewriting historical decision bodies. New independent Issues state “standard candidate,” judgment, alternatives/tradeoffs, confirmed reasons/history, applicability, and unresolved questions. Explicitly mark candidates with unsettled reasons as provisional.
4. Apply requester, labels, and posting format from “Issue content,” then verify/present body agreement, rendering, and URL through [Common post-save procedures](#opening-the-browser-after-saving-an-issue). Candidate saving alone does not approve standard adoption or implementation. Continue current work except parts depending on answers.

Do not post when explicitly prohibited, in Plan Mode, without permission to publish unpublished content, or under connection/permission restrictions; show unsaved drafts and reasons. During consultation/review, do not expand candidate records into change plans, branches, PRs, or merges. Later standard adoption/change follows separate approval scope and ordinary Issue planning.

### Recording improvements and checking next time

When connecting post-skill KPT to improvements in `daiksud/agents`, use related existing Issues/PRs and briefly record observed Problem evidence, corresponding Try, experimental scope, checking method in the next related task, adoption/rejection, and implementation status. Search open and closed records to avoid duplicates. If current work records are in another repository, connect only necessary improvements to existing agents candidates or small follow-up Issues; do not copy confidential information or task data without publication permission. Apply existing posting/save verification procedures.

- Distinguish observed Problems from unverified hypotheses; describe Try as a small experiment addressing one Problem. Retain Keep's useful scope; do not formally create improvement Issues without problems.
- With requests or continuing execution approval to reflect improvements in agents, hand small in-scope changes to ordinary planning/delivery. KPT or candidate existence alone does not approve implementation, or expand into unrelated repositories, authentication/security, cost, or global settings. Leave out-of-scope Try items proposed/unimplemented.
- For adopted Try items awaiting later checks, put `KPT Try`, target skill names, applicability, checking methods, and tracking links in existing or small follow-up `daiksud/agents` Issue bodies. Hand off those URLs so later work can find related records by searching open Issue bodies. Link implementation PRs and outcome tracking. Separate implemented from confirmed improvement effects; if later checking remains, keep records open or transfer checking methods to existing follow-up Issues before closing implementation Issues. No dedicated DB, script, or automatic schedule is required.
- At the next related task's start, read the Try and checking method; at completion judge continuation, revision, or closure from observed results/evidence. Record to the same destination only in work approved to post; read-only Reviewers or posting-prohibited work hand results and tracking destinations to Driver/user through permitted routes. If handoff is impossible, recording is incomplete; do not break publication permission or output contracts. If no opportunity arose or validation was impossible, state unverified; do not infer success/effects. Do not repeat instruction additions without new evidence or rerun closed Try items.

### Recording loosely related additional requests

To preserve additional requests while continuing current work, recording loosely related requests alone is an exception to ordinary Issue planning format and the planning/approval flow in [Starting and planning](planning.md#starting-and-planning).

| Relationship to current task | Action |
| --- | --- |
| Needed for current purpose/success conditions | Reflect within approved scope; for changes to purpose, outcomes, acceptance conditions, or external impact, apply plan update/reapproval in [Starting and planning](planning.md#starting-and-planning) |
| Independent purpose, loosely related to current purpose/success conditions | Explain separate handling and record in an independent follow-up Issue below. Continue current approved work |
| Relationship unclear | Ask the user and classify after the answer. Continue current work not depending on the answer |

1. Search existing Issues; if recorded, provide its URL without duplication.
2. New records contain a concise request title, request content, and “follow-up work; plan not yet created” status. Do not infer specifications, implementation methods, or validation plans. Treat as an independent Issue, not a current-task Sub-issue.
3. Apply requester, assignment, labels, and posting format from “Issue content,” and [Common post-save procedures](#opening-the-browser-after-saving-an-issue) through saved-state checking and URL presentation. Do not ask implementation-plan approval merely to record.
4. Recording alone does not start planning/implementation; continue current approved work.

Do not claim creation after posting failure or unverified saving. Even with confirmed saving, unverified requested opening/rendering leaves the overall recording procedure incomplete; separately explain saving success and failed/unverified scope. On resumption check saved state without repeating successful operations. Continue current work independent of answers/recovery.

Before implementing follow-up Issues, preserve original requests and create/save/retrieve/present ordinary plans under “Issue content” and [Starting and planning](planning.md#starting-and-planning). Follow “Issue recording for diagnosis and planning only” for development-practice diagnosis/adoption planning alone, and [Starting and planning](planning.md#starting-and-planning) for individual change implementation plans. Planning-only requests do not approve implementation. Start implementation through ordinary approval procedures, including the same conditions for approval by instructions to start a specified Issue goal.

### Issue recording for diagnosis and planning only

Use this path for terminal deliverables limited to Issue records of diagnosis/adoption plans, rather than based on the topic of diagnosis. Do not create Issues for requests merely seeking answers with diagnosis, proposals, comparisons, or draft plans. For both Issue recording and implementation, do not stop here; use ordinary [Starting and planning](planning.md#starting-and-planning).

For requests only to create/update development-practice diagnosis/adoption-plan Issues, deliver through this path without introducing a wait for implementation-plan approval. If individual change/incident implementation plans or post-diagnosis implementation are also requested, prioritize [Starting and planning](planning.md#starting-and-planning) even when cause diagnosis is included.

1. Check target repository, purpose, and scope, and search existing Issues. For repeated diagnosis, preserve original evidence/bodies and record changed judgments/reasons in history.
2. Summarize diagnosis evidence, uncertainties, priorities, the first small adoption unit, order/dependencies, expected changes, validation, and reassessment conditions in the body. Use the dependency `engineering-assessment` for development-practice adoption diagnosis.
3. Save with requester, labels, and posting format from “Issue content.” Do not require implementation-start approval for requested diagnosis/plan records.
4. Apply [Common post-save procedures](#opening-the-browser-after-saving-an-issue) through saved-state verification and presenting URL/saved body.
5. Distinguish completed diagnosis from unimplemented adoption and leave the Issue open. Do not proceed to Sub-issues, code/settings/organization changes, branches, PRs, or merge.

Do not save in posting-prohibited Plan Mode or explicitly read-only work; show unsaved drafts and restrictions. Saving failure or inability to verify is not success; show resumption conditions. On resumption check saved state and avoid duplicates.

If diagnosis discovers failing main, record evidence and recovery priority in the plan; diagnosis alone does not start recovery implementation. If implementation is requested later, inherit the existing Issue through ordinary [Starting and planning](planning.md#starting-and-planning). If explicit approval for that plan already exists, do not ask again; check scope and execute.
