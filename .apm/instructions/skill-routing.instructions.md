---
type: Instruction
title: Loading task skills
description: Choose task skills appropriate to the request and current stage.
---

## Loading task skills

Also check project-specific instructions. `docs/` refers to the working repository, and `~` to the user's home directory.

Before starting, read only skills directly applicable to the request and current stage; use the bundled material for that stage for details. Treat descriptions as the initial selection boundary; do not load related Skills in bulk merely because a topic word appears. Combine Skills only when multiple Skills actually own stages of the work.

Separate skill selection from the conditions for ending work. Finish when the user's requested terminal deliverable, such as an answer, diagnosis, Issue record, document, or implementation, is complete, rather than based on the topic or selected Skill. Supporting artifacts such as Issues, PRs, and validation records required by existing workflows to reach the terminal deliverable may be created as means, but do not reinterpret them as the requested deliverable or a new endpoint. Do not implicitly begin a subsequent stage beyond the requested terminal deliverable.

At the end of work using a skill, add a short KPT to the free-form report of outcomes, validation, and incomplete scope. Do not add unpermitted sections or fields to fixed output contracts such as JSON or findings-only formats. If an approved tracking destination for KPT exists, record it there; for read-only work, hand it to the Driver or user through a permitted route. If no route exists, honor the output contract without expanding posting permissions or artifacts solely for KPT. Keep states practices that actually helped and their evidence; Problem states observed friction or failures with concrete evidence; Try states a small experiment to resolve that Problem and how to check improvement in the next related task. Do not invent unconfirmed problems to fill a heading; briefly state when none were observed. Do not unconditionally turn a single experience into a common rule.

Separate completion of the current artifact from later skill improvements in KPT. When reflecting improvements in `daiksud/agents`, follow [Recording improvements and checking next time](../../skills/issue-management/references/issue-recording.md#recording-improvements-and-checking-next-time) in `issue-management`, preserving execution scope, publication permission, ordinary review, and CI. At the start of the next related task, search the inherited tracking destination, or open Issue bodies in `daiksud/agents`, for `"KPT Try"` and the skill name, and read records and checking methods for relevant adopted Try items. At completion, judge continuation, revision, or closure from actual results. Do not start dedicated retrospective meetings, recurring runs, or recursive changes that continually improve improvement work.

| Condition | Distribution path |
| --- | --- |
| Searching, creating, or updating Issues; recording plans, Sub-issues, follow-up requests, or common standard candidates | `~/.agents/skills/issue-management/SKILL.md` |
| Changes to Git-managed files, artifact creation, PR creation or updates, post-integration verification | `~/.agents/skills/change-delivery/SKILL.md` |
| Adding, changing, fixing, or refactoring code | `~/.agents/skills/software-development/SKILL.md` |
| Discovering and specifying user-facing behavior and acceptance conditions | `~/.agents/skills/behavior-specification/SKILL.md` |
| Only when performing code review | `~/.agents/skills/code-review/SKILL.md` |
| Creating or updating documents | `~/.agents/skills/document-authoring/SKILL.md` |
| When asked to diagnose current development practices or plan their adoption | `~/.agents/skills/engineering-assessment/SKILL.md` |
| Diagnosing, maintaining, or applying GitHub repository settings, Rulesets, merge methods, release protection, or security settings | `~/.agents/skills/github-repo/SKILL.md` |
| GitHub Actions workflow design, changes, failure investigation, review, or efficiency improvements | `~/.agents/skills/github-actions/SKILL.md` |

Do not require Issues, PRs, or merges for consultation, comparison, explanation, or read-only investigation alone. However, when the user decides a tradeoff that may become a common standard, use `issue-management` to record a candidate Issue even during consultation or review. Read-only Reviewers/Navigators hand candidates to the Driver and do not post themselves. Use `code-review` for read-only code review, also using `github-actions` for GitHub Actions workflow review. Do not add `change-delivery` as ordinary change work to review-only requests; combine the responsible skills when changes, posting, or merging are separately requested. Read the corresponding skill before moving from investigation to changes. Follow `document-authoring` for documents, distinguishing ordinary concepts and index/history files in OKF v0.2 from specific formats, and preserving sources, unknown metadata, and checking history.

For applying only GitHub-side repository settings, use `github-repo` through applying differences and diagnosing again after plan recording and approval checks. If no Git-managed files change, do not require `change-delivery` or empty commits or PRs. If prerequisite workflows or other files change, apply ordinary delivery to those file changes.
