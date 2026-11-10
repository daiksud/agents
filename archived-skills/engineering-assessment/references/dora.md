---
type: Reference
title: Assess DORA as a Capability lens
description: Distinguish DORA Core Model, Capability Catalog, software delivery metrics, and annual research, assessing only problem-relevant capabilities from evidence.
---

## Assess DORA as a Capability lens

Read for assessments using DORA, Capability Catalog, Core Model, delivery metrics, Quick Check, or similar resources. Do not use DORA as a complete adoption checklist or individual evaluation sheet. Select only Capability, performance, and outcome perspectives relevant to the user's difficulty.

### Separate four DORA artifacts

| Artifact | Role | Misuse to avoid |
| --- | --- | --- |
| Core Model | Conservative model of Capability, Performance, and Outcome relationships repeatedly supported by DORA research | Do not automatically add latest Catalog items or metrics definitions to Core |
| Capability Catalog | Catalog of capabilities and research themes useful for improvement. Items may carry labels such as `core` / `AI` | Do not equate the whole Catalog with Core or mandatory adoption |
| Software delivery performance metrics | Metrics observing delivery performance over time for an application/service | Do not equate them with capabilities or individual performance |
| Annual / ongoing research | Continuing research into new technologies, ways of working, and relationships | Do not immediately interpret one year's findings as fixed Core relationships |

DORA Core Model v2.1.0 organizes relatively established relationships within the research for practitioners and is intentionally updated more conservatively than ongoing research. Use the fixed [v2.1.0 material](https://dora.dev/research/core/assets/dora-core-v2.1.0-detail.pdf) as authoritative for Core structure.

### Core v2.1.0 has three Capability groups

Core v2.1.0 organizes capabilities into these three groups.

| Group | Capabilities listed in Core |
| --- | --- |
| Climate for learning | Code Maintainability, Documentation quality, Empowering teams to choose tools, Generative culture |
| Fast flow | Continuous delivery, Database change management, Deployment automation, Flexible infrastructure, Loosely coupled teams, Streamlining change approval, Version control, Working in small batches |
| Fast feedback | Continuous integration, Monitoring and observability, Reliability engineering, Pervasive security, Test automation, Test data management |

Do not convert these names into a questionnaire scored sequentially in every assessment. Use only groups and capabilities relevant to the current problem, value stream, and observed evidence.

Core shows relationships predicting Performance from Capability and outcomes such as Organizational performance / Well-being from Performance. It treats Software delivery through Four key metrics and Reliability through SLOs.

### Capability Catalog is broader than Core

The Capability Catalog includes AI-related and non-Core items as well as items labeled `core`. For example, Working in small batches displays both `core` and `AI` labels.

Therefore distinguish:

- Presence in the Catalog.
- Inclusion in the current Core Model.
- Relationship to specific research themes such as AI.
- Necessity for assessing this problem.

Do not judge every unadopted Catalog item a gap. Follow DORA Core updates when deciding whether new Catalog items belong in Core; this skill does not promote them independently.

### Do not confuse Core's Four key metrics with the current five metrics

Core v2.1.0's diagram shows Software delivery performance as Four key metrics, while the [DORA metrics guide](https://dora.dev/guides/dora-metrics/) uses five metrics in this skill's 2026-09-27 reference snapshot. Check the current guide when a version-sensitive assessment requires up-to-date definitions.

The five metrics in that snapshot:

| Factor | Metric | Target |
| --- | --- | --- |
| Throughput | Change lead time | Commit through production deployment |
| Throughput | Deployment frequency | Deployment count or interval over a period |
| Throughput | Failed deployment recovery time | Recovery from failed deployment |
| Instability | Change fail rate | Proportion of deployments requiring immediate intervention |
| Instability | Deployment rework rate | Proportion of unplanned deployments due to production incidents or similar causes |

This does not mean rewriting Core v2.1.0's Four key metrics diagram to five items. Core Model and the latest metrics guide differ in update cycles and roles; state the artifact, version, and verification date used.

### Practice and Capability classifications vary by perspective

Do not treat different classifications of the same concept across frameworks as contradictions.

| Concept | Other lens | DORA treatment |
| --- | --- | --- |
| Working in small batches | Practice consistent with Lean flow improvement and XP small feedback | Core Capability supporting short feedback loops and learning |
| Continuous integration | XP-origin practice and development practice supporting CD | Core / Fast feedback Capability |
| Continuous delivery | Delivery system/capability composed of multiple practices | Core / Fast flow Capability |
| Loosely coupled teams | Architectural/organizational property of independence | Core / Fast flow Capability |
| Documentation quality | State including usability and quality, rather than document creation itself | Core / Climate for learning Capability |

Do not force all names into one taxonomy; state what is observed through which lens.

### Observe actual Capability rather than configuration

Tools, configuration, or documents alone do not establish Capability achievement.

| Example Capability | Evidence to inspect |
| --- | --- |
| Continuous integration | Branch lifetimes, actual main integration frequency, feedback time, broken-build repair examples |
| Continuous delivery | Safe on-demand deployability, actual delivery/recovery/approval waiting records |
| Monitoring and observability | Records of signals used in detection, investigation, or debugging, and practitioner experience |
| Loosely coupled teams | Actual change/test/deploy without fine-grained coordination with other teams |
| Documentation quality | Evidence that intended readers found, understood, and used documents in actual work |
| Working in small batches | Actual work item/change size, time to feedback, WIP, and waiting |

Do not equate GitHub Actions, Datadog, Argo CD, or other tool presence with Capability achievement. Leave matters unverified when evidence is unavailable.

### Select only necessary lenses from the problem

| Observed problem | First DORA lens | Possible companion |
| --- | --- | --- |
| Release approval waiting after PRs dominates | Fast flow / Continuous delivery / Streamlining change approval | Lean, DevOps |
| Slow CI feedback or stalled main integration | Fast feedback / Continuous integration / Test automation | XP, Small batches |
| Cross-team coordination blocks change/delivery | Fast flow / Loosely coupled teams | Architecture / Organization, Team Topologies |
| Knowledge concentrated in particular people | Climate for learning / Documentation quality / Generative culture | XP Communication |
| Investigating AI adoption effects/friction | Problem-relevant AI items in the Catalog | Underlying sociotechnical Core Capability |

Do not mechanically add unrelated capabilities to unknowns lists.

### Metrics provide improvement feedback, not the goal itself

Observe changes at application/service level with aligned periods and definitions. Do not combine inconsistent numbers across services into rankings or use them for individual performance evaluation.

Direct manipulation of metrics, such as merely increasing deployment frequency, is not improvement. Check user outcomes, reliability, well-being, and target Capability changes together. Do not use fixed Elite thresholds as universal pass/fail criteria.

For the first improvement, select one Capability or a small group most relevant to current constraints. Organize expected changes, evidence, and reassessment conditions. Follow [shared plan deliverables](assessment.md#plan-deliverables) for answers, Issue records, documents, and implementation; this focused lens alone does not determine Issue saving or the stopping point.
