---
type: Policy
title: Change records and Engineering Policies
description: Current policy for PR decision history, validation reporting, and durable engineering guidance.
sources:
  - id: change-record-agreement
    resource: https://github.com/daiksud/agents/issues/253
  - id: repository-adoption
    resource: https://github.com/daiksud/agents/issues/254
---

## Current choice and applicability

This repository uses PR descriptions and squash commits to retain the judgment made in each change, and topical `docs/engineering-policies/` documents to explain current durable policy. The common guidance offers the same foundation to consuming repositories while respecting their existing conventions. Installing the package does not install templates or migrate ADRs.

The operational rules live in [Change records](../../.apm/instructions/change-records.instructions.md), [PR writing](../../skills/issue-management/references/github-writing.md), [delivery](../../skills/change-delivery/references/review-and-merge.md), and [policy authoring](../../skills/document-authoring/references/engineering-policies.md). This policy reflects the agreement in [Issue #253](https://github.com/daiksud/agents/issues/253).[^change-record-agreement]

For repositories adopting verbatim PR-body squash records, the default proposal is English PR bodies, consistent with English commit messages. The repository records its actual choice locally; existing adoption decisions and explicit exceptions remain effective, and conflicts with explicit local language rules require resolution before affected publication. Other artifact-language conventions remain unchanged. Equivalent arrangements and prior deferrals are respected without repeatedly blocking unrelated development. The [adoption guide](../../skills/change-delivery/references/repository-adoption.md) owns the procedure requested in [Issue #254](https://github.com/daiksud/agents/issues/254).[^repository-adoption]

## Rationale and trade-offs

A PR records the problem, actual result, relevant decisions, and actual validation status. Keeping that judgment self-contained preserves confirmed causes, constraints, and reasons even after linked living policies change. The supplied template uses Summary, Decisions, and Validation; Decisions can be omitted when unnecessary or already clear in Summary. This keeps ordinary fixes short without inventing analysis for every field.

Validation reporting is mandatory, but execution, method, scope, rigor, and timing are discretionary unless independently required. `Not run` is a complete status; partial checks and failures must be accurate. Checking after merge and correcting through a later PR is permitted. This favors honest evidence over ritual execution, accepting that unverified behavior can remain. It does not remove required CI, agreed acceptance conditions, or repository protections, including this repository's existing APM and independent-validation exclusions.

HTML comments help template authors but pollute squash messages if retained. Templates may contain them; actual descriptions must remove all comments at creation/update, review, and merge while retaining substantive validation status. The final title and description become the squash subject/body through GitHub's `squash_merge_commit_title: PR_TITLE` / `squash_merge_commit_message: PR_BODY` convention. Maintainers must therefore keep descriptions aligned with the final reviewed change.

Choosing PR-body language at adoption time makes verbatim squash records compatible with English commit conventions while retaining the reviewed reasoning and validation status. This can require contributors to write PR bodies in a different language from other repository prose; limiting the default to an explicit adoption proposal preserves local choices and avoids a blanket language change. Translating only at merge time would change the reviewed historical record and risks losing rationale, so it is not the chosen approach. Bundled assets do not change consumer files or live settings; settings diagnosis/application needs its own authorized scope and preserves unrelated merge, CI, security, and protection settings.

Engineering Policies describe current choices, applicability, rationale, alternatives, and trade-offs by topic. Revisions replace the same topical content and end with the introducing/revising PR link. This makes current guidance easy to find; readers seeking chronology follow PRs and commits instead. Ordinary feature and bug-fix decisions do not each require policy documents.

## Alternatives

- An append-only ADR log preserves chronology in documents but requires readers to trace supersession to find current guidance. Repositories using that convention can retain it; this repository keeps chronology in PRs/commits.
- Keeping every decision only in PRs avoids living-document maintenance but makes durable guidance harder to discover. Topical policies address decisions affecting future work.
- Mandatory validation execution or mandatory reasons for `Not run` provide more uniform process at the cost of discretion and boilerplate. Accurate status plus independently required checks is the chosen boundary.
- Retaining repository-language PR bodies can preserve contributor conventions and remains available through an explicit local choice or exception. The English adoption default instead aligns new verbatim PR-body squash records with English commits; it does not silently replace existing decisions.
- Separate automatically synchronized templates or new PR lint could enforce consistency but add machinery beyond the current need. The reusable and self-adoption templates are maintained together by ordinary review.

[^change-record-agreement]: Owner-agreed record policy and adoption boundaries in Issue #253.

[^repository-adoption]: Owner-requested consumer adoption guidance, scoped language choice, and settings boundaries in Issue #254.

Introducing/revising PR: [#258](https://github.com/daiksud/agents/pull/258).
