---
type: Reference
title: Issue management sources and adoption notes
description: Preserve source mappings, adoption decisions, and historical checking scope for maintainers of the issue-management skill.
sources:
  - id: conventional-commits
    resource: https://www.conventionalcommits.org/en/v1.0.0/
  - id: github-issue-quickstart
    resource: https://docs.github.com/en/issues/tracking-your-work-with-issues/learning-about-issues/quickstart
  - id: github-review-changes
    resource: https://docs.github.com/en/pull-requests/concepts/helping-others-review-your-changes
  - id: github-link-pr-issue
    resource: https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue
  - id: google-cl-descriptions
    resource: https://google.github.io/eng-practices/review/developer/cl-descriptions.html
  - id: rumdl-getting-started-installation
    resource: https://rumdl.dev/getting-started/installation/
  - id: rumdl-md060
    resource: https://rumdl.dev/md060/
  - id: rumdl-md076
    resource: https://rumdl.dev/md076/
  - id: github-docs-global-settings-md
    resource: https://github.com/rvben/rumdl/blob/main/docs/global-settings.md
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

## Scope

Maintainer reference for [issue-management](../../skills/issue-management/SKILL.md). These records explain source provenance and adoption history. Execution procedures and decision-relevant details remain in the skill and its task-specific references; ordinary execution does not require this document.

Checking dates below are historical records retained from the original documents. Relocating them does not establish a new specification check, human review, successful execution, or current applicability.

## Source mapping

The following mapping preserves the original source IDs and annotation scope for each runtime document.

### Writing Issues and PRs

Runtime material: [github-writing.md](../../skills/issue-management/references/github-writing.md).

| Source | Original annotation scope |
| --- | --- |
| [^github-issue-quickstart] | GitHub Docs, “Quickstart for GitHub Issues.” Descriptive Issue titles, purpose, and bug reproduction/expected/actual result examples. |
| [^github-review-changes] | GitHub Docs, “Helping others review your changes.” Guidance on small clear PRs and context about problems, approaches, results, and review needs. |
| [^google-cl-descriptions] | Google Engineering Practices, “Writing good CL descriptions.” Guidance on preserving changes/reasons in future history, with short summaries and needed context. |
| [^conventional-commits] | Conventional Commits 1.0.0. Commit syntax, types, scopes, and breaking-change specifications. |
| [^github-link-pr-issue] | GitHub Docs, “Linking a pull request to an issue.” Issue links through closing keywords and automatic closure on default-branch merge. |

### Markdown quality for GitHub

Runtime material: [markdown-quality.md](../../skills/issue-management/references/markdown-quality.md).

| Source | Original annotation scope |
| --- | --- |
| [^rumdl-getting-started-installation] | [rumdl installation](https://rumdl.dev/getting-started/installation/). Evidence for the reference scope and adoption decisions stated in the text. |
| [^rumdl-md060] | [MD060: compact formatting](https://rumdl.dev/md060/). Evidence for the reference scope and adoption decisions stated in the text. |
| [^rumdl-md076] | [MD076: list-item spacing](https://rumdl.dev/md076/). Evidence for the reference scope and adoption decisions stated in the text. |
| [^github-docs-global-settings-md] | [Common configuration inheritance](https://github.com/rvben/rumdl/blob/main/docs/global-settings.md). Evidence for the reference scope and adoption decisions stated in the text. |

### Planning and execution scope

Runtime material: [planning.md](../../skills/issue-management/references/planning.md).

| Source | Original annotation scope |
| --- | --- |
| [^context-engineering] | [Context Engineering](https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/instructions/context-engineering.instructions.md). Apply related information, reference patterns, and context updates to investigation here. |
| [^taming-copilot] | [Taming Copilot](https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/instructions/taming-copilot.instructions.md). Apply tool checking of version-dependent information to target-version comparisons. |
| [^github-instructions-spec-driven-workflow-v1-instructions-md] | [GitHub awesome-copilot Spec Driven Workflow v1](https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/instructions/spec-driven-workflow-v1.instructions.md). Evidence for reference scope and adoption decisions stated in the text. |
| [^github-agents-research-technical-spike-agent-md] | [Technical spike research mode](https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/agents/research-technical-spike.agent.md). Evidence for reference scope and adoption decisions stated in the text. |
| [^github-context-map-skill-md] | [GitHub awesome-copilot context-map](https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/skills/context-map/SKILL.md). Evidence for reference scope and adoption decisions stated in the text. |

## Planning adoption notes

Checked GitHub awesome-copilot Spec Driven Workflow v1[^github-instructions-spec-driven-workflow-v1-instructions-md] and Technical spike research mode[^github-agents-research-technical-spike-agent-md] on 2026-09-11, summarizing/restructuring uncertainty-scaled investigation/prototypes, pre-experiment success conditions, and evidence-based decision updates.

This environment limits them to important outcome/feasibility uncertainties, distinguishes business agreement from technical validation, and integrates existing Issues/approval. It does not require the sources' fixed three documents, confidence scores, uniform six stages, complete operation logs, comprehensive investigation, or dedicated prototype documents. This is an application decision, not wholesale adoption.

Checked GitHub awesome-copilot context-map[^github-context-map-skill-md] on 2026-09-11, summarizing/restructuring target, dependency, test, pattern, and risk perspectives. Include document links, related instructions, and referrer impact in existing Issue planning here. Do not introduce fixed tables/checklists or separate map review waits; integrate checking into existing plan approval.

Checked Context Engineering[^context-engineering] and Taming Copilot[^taming-copilot] on 2026-09-13, integrating concrete reference patterns, target-version evidence, and rechecking changed assumptions. IDE tab/cursor operations, creating `COPILOT.md`, one-file-at-a-time changes, or announcements before every tool are not common requirements.

## GitHub writing adoption notes

Use Conventional Commits syntax, types, scopes, and breaking-change notation as the title-format basis; applying them to Issues/PRs is this environment's convention. Adopt purpose-expressive titles, resolution/review context, problem/approach/result explanations, and Issue linking from GitHub guides. Adopt preserving changes/reasons in future history and retaining needed body context beyond short summaries from Google Engineering Practices. Do not introduce fixed templates, mandatory body lengths, or identical headings for every Issue/PR.

## Markdown quality adoption notes

- rumdl installation[^rumdl-getting-started-installation]
- MD060: compact formatting[^rumdl-md060]
- MD076: list-item spacing[^rumdl-md076]
- Common configuration inheritance[^github-docs-global-settings-md]

## Writing guidance attribution

The original [GitHub writing guidance](../../skills/issue-management/references/github-writing.md) attributed immediately understandable Issue titles and purpose/resolution information to GitHub, and PR context about problems, approaches, results, and review needs to GitHub's review guide. It also attributed preserving changes and reasons for future history to Google's change-description guide.[^github-issue-quickstart][^github-review-changes][^google-cl-descriptions]

Applying Conventional Commits to Issue and PR titles is this environment's local convention; Conventional Commits 1.0.0 itself specifies commit messages.[^conventional-commits]

[^github-issue-quickstart]: [github-issue-quickstart](https://docs.github.com/en/issues/tracking-your-work-with-issues/learning-about-issues/quickstart).
[^github-review-changes]: [github-review-changes](https://docs.github.com/en/pull-requests/concepts/helping-others-review-your-changes).
[^google-cl-descriptions]: [google-cl-descriptions](https://google.github.io/eng-practices/review/developer/cl-descriptions.html).
[^conventional-commits]: [conventional-commits](https://www.conventionalcommits.org/en/v1.0.0/).
[^github-link-pr-issue]: [github-link-pr-issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue).
[^rumdl-getting-started-installation]: [rumdl-getting-started-installation](https://rumdl.dev/getting-started/installation/).
[^rumdl-md060]: [rumdl-md060](https://rumdl.dev/md060/).
[^rumdl-md076]: [rumdl-md076](https://rumdl.dev/md076/).
[^github-docs-global-settings-md]: [github-docs-global-settings-md](https://github.com/rvben/rumdl/blob/main/docs/global-settings.md).
[^context-engineering]: [context-engineering](https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/instructions/context-engineering.instructions.md).
[^taming-copilot]: [taming-copilot](https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/instructions/taming-copilot.instructions.md).
[^github-instructions-spec-driven-workflow-v1-instructions-md]: [github-instructions-spec-driven-workflow-v1-instructions-md](https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/instructions/spec-driven-workflow-v1.instructions.md).
[^github-agents-research-technical-spike-agent-md]: [github-agents-research-technical-spike-agent-md](https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/agents/research-technical-spike.agent.md).
[^github-context-map-skill-md]: [github-context-map-skill-md](https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/skills/context-map/SKILL.md).
