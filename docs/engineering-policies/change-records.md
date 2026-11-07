---
type: Policy
title: Change records
description: Current working information in files and self-contained design judgments in commits.
---

## Current working guidance

Repository documents contain the effective technologies, specifications, rules, responsibilities, editable boundaries, and procedures that a contributor joining today needs. Update the relevant topic in place. Do not add adoption narratives, superseded-policy sections, comparison histories, or introducing/revising PR footers.

Use [decision-recording](../../skills/decision-recording/SKILL.md) to choose the recording destination and intended reader. Code expresses behavior and structure through simple names, types, and composition. Tests express observable behavior and contracts. Why-not comments explain beside the code why a plausible alternative fails a current constraint; public API documentation serves API users.

## PR and commit records

PR descriptions use Summary, optional Decisions, and Validation. State the problem, actual change, resulting behavior, and the facts, constraints, alternatives, reasons, and trade-offs needed to understand the judgment. Links may supplement this text but must not be necessary to understand it. Incorporate conclusions from discussion into the final body.

Every PR reports actual validation status. Execution remains discretionary unless required by the task or repository; `Not run` is valid for discretionary checks. Preserve required CI, agreed acceptance conditions, and the APM and independent-validation exclusions in [AGENTS.md](../../AGENTS.md).

Remove all HTML comments from actual descriptions. This repository uses English commit messages and PR titles/bodies. Preserve the final title/body verbatim in the commit created at merge, and verify the saved message. The repository's effective protections determine which permitted method is available; guidance for consumers does not apply live settings.

## Consumer adoption

The independent [decision-recording skill](../../skills/decision-recording/SKILL.md) provides a [PR template](../../skills/decision-recording/assets/pull_request_template.md) and [local instruction example](../../skills/decision-recording/assets/agents-decision-records.md). Accept equivalent arrangements and existing topical placement; no document directory or policy name is required.

The [settings guide](../../skills/decision-recording/references/github-settings.md) explains allowing squash and merge-commit merging, prohibiting rebase merging, and saving PR title/body with either method. The optional [versioning skill](../../skills/versioning/SKILL.md) provides the [commitlint guide](../../skills/versioning/references/commitlint.md) and [workflow](../../skills/versioning/assets/commitlint.yml), covering fixed Bun/commitlint versions, standard configuration discovery, the unchanged conventional default, and required-check adoption. Consumer workflow installation and live settings application are separate from distributing these assets.
