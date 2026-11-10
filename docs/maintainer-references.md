---
type: Guide
title: Maintainer references for Skills
description: Find sources, adoption decisions, and supplementary records without adding them to ordinary agent task context.
sources:
  - id: guidance-separation
    resource: https://github.com/daiksud/agents/issues/231
    title: Separate execution guidance from maintainer references
  - id: skill-independence
    resource: https://github.com/daiksud/agents/issues/285
---

## How the documentation is divided

Skill entry points state what the agent must do. Operational references bundled with each skill provide the definitions, examples, and detailed procedures needed at a specific stage. The notes linked below preserve origins, adoption decisions, and maintenance history for people maintaining that guidance.[^guidance-separation]

The authoring policy lives in [Separate execution guidance from maintainer notes](../archived-skills/document-authoring/references/agent-documents.md). Source notes link back to the guidance they explain; ordinary tasks do not require reading this catalog. Historical checking dates remain historical, and file reorganization does not establish renewed verification.

Skill entry points, references, and assets contain no referrals to other skills. Keep the rules needed for the task locally, with concise shared concepts where necessary; describe skill selection and responsibilities in the repository README. Catalog links below map related guidance for maintainers without creating execution dependencies.[^skill-independence]

[^guidance-separation]: [Issue #231](https://github.com/daiksud/agents/issues/231) records the requested separation, preserved execution boundaries, and migration scope, following the Sakura Miko split in [PR #230](https://github.com/daiksud/agents/pull/230).

## Current Engineering Policies

- [Change records](engineering-policies/change-records.md): current choice, applicability, rationale, alternatives, and trade-offs; historical judgments remain in PRs/commits.

## Skills

| Skill | Maintainer material |
| --- | --- |
| Behavior specification | [Sources and adoption notes](skill-sources/behavior-specification.md) |
| Change delivery | [Sources and adoption notes](skill-sources/change-delivery.md) |
| Code review | [Sources and adoption notes](skill-sources/code-review.md) |
| Document authoring | [Sources and adoption notes](skill-sources/document-authoring.md); [OKF specification audit](okf-specification-audit.md) |
| Engineering assessment | [Sources and adoption notes](skill-sources/engineering-assessment.md) |
| Story-point estimation | [Sources and maintenance scenarios](skill-sources/estimate-story-points.md) |
| Continuous delivery | [Sources and adoption notes](skill-sources/continuous-delivery.md) |
| Versioning | [Sources and adoption notes](skill-sources/versioning.md) |
| GitHub repository settings | [Sources and adoption notes](skill-sources/github-repo.md) |
| Issue management | [Sources and adoption notes](skill-sources/issue-management.md) |
| Software development | [Sources and adoption notes](skill-sources/software-development.md) |

The external `yomiyasu` skill is maintained upstream and is not included as a package dependency or rewritten here. Required attribution and licenses remain with the affected skill.

[^skill-independence]: [Independent skill guidance and versioning responsibilities](https://github.com/daiksud/agents/issues/285).
