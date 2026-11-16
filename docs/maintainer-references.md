---
type: Guide
title: Maintainer references for Skills
description: Find current authoring guidance and existing source and maintenance material for Skills.
sources:
  - id: guidance-separation
    resource: https://github.com/daiksud/agents/issues/231
    title: Separate execution guidance from maintainer references
  - id: skill-independence
    resource: https://github.com/daiksud/agents/issues/285
---

## How the documentation is divided

Skill entry points state what the agent must do. Operational references bundled with each skill provide the definitions, examples, and detailed procedures needed at a specific stage. Existing source and maintenance notes remain available below.[^guidance-separation]

Current authoring guidance lives in [documentation](../skills/documentation/SKILL.md), with bundled [placement](../skills/documentation/references/placement.md) and [writing](../skills/documentation/references/writing.md) guidance. Keep effective rules and necessary citations with the explanation that uses them; keep adoption comparisons and history in PRs/commits. A separate source catalog is not required for each skill. When consolidating existing notes, preserve unique current guidance and required attribution before removing redundant material. Historical checking dates remain historical, and file reorganization does not establish renewed verification.

Skill entry points, references, and assets contain no referrals to other skills. Keep the rules needed for the task locally, with concise shared concepts where necessary; describe skill selection and responsibilities in the repository README. Catalog links below map related guidance for maintainers without creating execution dependencies.[^skill-independence]

[^guidance-separation]: [Issue #231](https://github.com/daiksud/agents/issues/231) records the requested separation, preserved execution boundaries, and migration scope, following the Sakura Miko split in [PR #230](https://github.com/daiksud/agents/pull/230).

## Current policies

- [Change records](engineering-policies/change-records.md): current recording rules and validation requirements; historical judgments remain in PRs/commits.

## Skills

| Skill | Maintainer material |
| --- | --- |
| Documentation | [Bundled writing guidance and sources](../skills/documentation/references/writing.md) |
| Behavior specification | [Sources and adoption notes](skill-sources/behavior-specification.md) |
| Change delivery | [Sources and adoption notes](skill-sources/change-delivery.md) |
| Code review | [Sources and adoption notes](skill-sources/code-review.md) |
| Archived document authoring | [Sources and adoption notes](skill-sources/document-authoring.md); [OKF specification audit](okf-specification-audit.md) |
| Engineering assessment | [Sources and adoption notes](skill-sources/engineering-assessment.md) |
| Story-point estimation | [Sources and maintenance scenarios](skill-sources/estimate-story-points.md) |
| Continuous delivery | [Sources and adoption notes](skill-sources/continuous-delivery.md) |
| Versioning | [Sources and adoption notes](skill-sources/versioning.md) |
| GitHub repository settings | [Sources and adoption notes](skill-sources/github-repo.md) |
| Issue management | [Sources and adoption notes](skill-sources/issue-management.md) |
| Software development | [Sources and adoption notes](skill-sources/software-development.md) |

The external `yomiyasu` skill is maintained upstream and is not included as a package dependency or rewritten here. Required attribution and licenses remain with the affected skill.

[^skill-independence]: [Independent skill guidance and versioning responsibilities](https://github.com/daiksud/agents/issues/285).
