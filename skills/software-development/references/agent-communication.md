---
type: Reference
title: Internal Driver/Navigator communication
description: Use communication fields, status words, IDs, and initial/follow-up messages under common collaboration contracts.
---

## Internal Driver/Navigator communication

Before the first Navigator request for code changes, the Driver reads this material and shares it with relevant collaboration contracts. If the Navigator cannot read directly, include content in the initial request; do not edit code until confirmed. Not required for consultation, planning, or documentation-only work. Common collaboration instructions remain authoritative for roles, edit permissions, application conditions, stopping, and re-pairing; this material does not change them.

Internal communication aims at efficient, low-entropy exchange resistant to misunderstanding, rather than English translation itself. Use concise Controlled English for requests, checks, and feedback: one meaning per sentence, stable terminology, avoiding unnecessary politeness, conversational filler, rhetoric, or ambiguous approval wording. Do not translate information needing exact originals, such as code, identifiers, commands, logs, errors, or specification content. Do not extend this internal rule to language rules for human-facing answers, Issues, PRs, documents, or commit messages; use [Repository artifact language](../../../.apm/instructions/language.instructions.md) for repository artifacts.

Prefer lightweight semistructured formats with only needed items over free conversation. Representative fields are `PHASE`, `TODO`, `STATUS`, `GOAL`, `CHANGES`, `EVIDENCE`, `FINDINGS`, `NEXT`, and `REQUEST`; do not fill all every time. As a rule, review/check `STATUS` uses `APPROVED`, `CHANGES_REQUIRED`, or `BLOCKED`; if classifications are needed, use short known vocabulary such as `REQUIREMENT`, `TEST`, `REGRESSION`, `DESIGN`, or `SCOPE`. Use Markdown or plain text without requiring JSON unless strict external parsing is necessary.

Give shared ToDos, findings, and unresolved matters referenced repeatedly short stable IDs within the same task and continuing session with the same Navigator. For example, `T-01` for ToDos and `F-01` for findings; refer by ID later rather than resending descriptions. No persistent global ID system is required.

At initial contact, share original requests, acceptance conditions, scope, applicable instructions, constraints, related code, and initial shared ToDos needed for judgment. After continuity is confirmed, as a rule do not resend long unchanged premises; send differences centered on current `PHASE` and `TODO`, `CHANGES` since last time, new `EVIDENCE`, added/resolved `FINDINGS`, and current `REQUEST`. If history loss, inability to resume, or insufficient context is suspected, stop delta-only updates, prioritize accuracy by re-sharing needed information, and prioritize common collaboration stopping/re-pairing conditions.
