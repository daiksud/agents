---
type: Guide
title: daiksud/agents
description: Prerequisites for shared Instructions and Skills, and installation through APM.
---

This repository shares [development policy Instructions](.apm/instructions/) and [task-specific Skills](skills/) through APM.

## Artifact language

These shared guidance files use English. Artifacts created with them follow [Repository artifact language](.apm/instructions/language.instructions.md): commits, code comments, and Issue/PR titles always use English; bodies, discussions, reviews, and documentation use the target repository's English or Japanese conventions.

## Prerequisites

The distribution targets are Codex and GitHub Copilot, as specified in [apm.yml](apm.yml). Use an environment with APM CLI available, and install the complete set of Instructions and Skills globally. Because Skills depend on one another, copying only an individual `SKILL.md` is not a supported usage assumption.

Under the [collaboration instructions](.apm/instructions/collaboration.instructions.md), code changes require a Navigator with an independent execution context. Before the first code edit, confirm actual initial and follow-up responses from the same Navigator. If unavailable, do not begin code edits, including test code or refactoring; read-only investigation and planning within the approved scope may continue. Pair work is not required for consultation, explanation, planning alone, or documentation-only changes.

## Installation

```bash
apm install --global --target codex,copilot daiksud/agents
apm compile --global
```

## Instructions and GitHub protection settings

The checking procedures defined by Instructions and Skills are separate from protection conditions mechanically enforced by GitHub. Each repository manages its own Rulesets and required status checks; installing this package alone does not apply the same protection settings.

[github-repo](skills/github-repo/SKILL.md) diagnoses immutable releases, squash-only merges, the main Ruleset, full-SHA requirements for external Actions, and free security features for the specified repository, and applies only the explicitly requested scope. “Diagnose the settings” ends with a report, “record the plan in an Issue” ends with a record, and “apply the settings” includes applying the differences and diagnosing again. It coordinates workflow content changes with [github-actions](skills/github-actions/SKILL.md), and does not create empty commits or PRs solely for GitHub-side settings changes.

This repository requires `ci`. [PR validation](.github/workflows/ci-pr.yml) follows `draft → commit-stage → ready → acceptance-stage → check`: eligible same-repository PRs return to Draft for Markdown lint, become Ready after that succeeds on the current HEAD, and then undergo local file-link validation. Fork and Dependabot PRs receive validation without state changes. [Main-push validation](.github/workflows/ci.yml) retains Markdown lint.

CI does not wait for reviews or merge PRs. This repository does not wait for CodeQL scans or results before merging PRs. Check the [Ruleset](https://github.com/daiksud/agents/rules/22615823) for the latest enforced conditions, and [Review and merge](skills/change-delivery/references/review-and-merge.md) for procedures from ordinary review through post-integration verification.
