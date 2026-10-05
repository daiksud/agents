---
type: Reference
title: Principles and relationships of development practices
description: Briefly organize practice roles and overlap, and guide readers to necessary focused references.
---

## Principles and relationships of development practices

These concepts are not separate mandatory checklists. Start from user outcomes and connect feedback across understanding, design, implementation, integration, delivery, and operations.

Do not duplicate details here every time. Read only focused references needed for the problem.

### Roles of the lenses

| Lens | Main question | Details |
| --- | --- | --- |
| XP | Can we build in small increments, learn from feedback, and evolve design toward current requirements? | [XP taxonomy](xp.md) |
| Lean | Improve end-to-end user-value flow, reduce WIP, waiting, rework, and handoffs, and respect people. Do not equate improvement with staff reductions or maximizing each worker's local utilization | This document and [assessment procedures](assessment.md) |
| DDD | What is modeled, and how far do the same meanings and language apply? | Semantic/architecture relationships: [Architecture and Organization](architecture-and-organization.md) |
| CI | Are small changes integrated frequently into main, with fast feedback and continued repair? | Implementation: `change-delivery`; assessment: [assessment procedures](assessment.md) |
| Continuous Delivery | Can verified changes remain safely deliverable when needed? Continuous Deployment is a separate practice of automatically deploying verified changes to production; manual approval can coexist with CD | DORA Capability relationships: [DORA lens](dora.md) |
| DevOps | Can the feedback loop for user outcomes, quality, and operations close from development through operations? CALMS uses Culture / Automation / Lean / Measurement / Sharing to assess organization, automation, flow, measurement, and knowledge sharing together | Evidence: [assessment procedures](assessment.md); CALMS and other sources/adoption decisions: [primary materials](sources.md) |
| Team Topologies / Conway | How should ownership, interaction, cognitive load, and software boundaries align? | [Architecture and Organization](architecture-and-organization.md) |
| DORA | How can Capability, Performance, and Outcome be assessed from evidence? | [DORA lens](dora.md) |

### Do not duplicate overlapping concepts into separate rules

The same concept changes classification and use across frameworks.

| Concept | One lens | Another lens |
| --- | --- | --- |
| Continuous Integration | XP Primary Practice | DORA Fast feedback Capability |
| Continuous Delivery | Delivery system / capability | DORA Fast flow Capability |
| Small Batches | Practice supporting Lean / XP flow and feedback | DORA Capability |
| Loosely Coupled Teams | Architecture / Organization independence | DORA Fast flow Capability |
| Documentation Quality | Usable knowledge state rather than document creation itself | DORA Climate for learning Capability |

Do not treat classification differences as contradictions. State what to observe for the current problem.

### Preserve the relationships among BDD, ATDD, and TDD

These differ not only in test artifacts, but in which feedback is created when.

| Practice | Minimum assessment contract |
| --- | --- |
| BDD | Stakeholders use concrete examples to connect Discovery → Formulation → Automation and deepen understanding of expected behavior |
| ATDD | Make acceptance conditions and tests concrete from customer, development, and testing perspectives before corresponding implementation |
| TDD | From a test list, iterate one at a time through failing test → minimal implementation → necessary cleanup, feeding back into design |

BDD and ATDD overlap in concrete examples and shared understanding; do not require separate meetings or duplicate specifications. TDD can provide a short design/validation loop inside agreed behavior. Completed Gherkin or tests alone do not establish Discovery, agreement before implementation, or Red-first processes.

Use [primary materials](sources.md) for detailed sources/version differences and [assessment procedures](assessment.md) for evidence to gather.

### Do not infer practices from artifacts alone

| Concept | What artifacts alone cannot establish |
| --- | --- |
| BDD | Gherkin alone does not show collaborative Discovery / Formulation |
| ATDD | Acceptance tests alone do not prove conditions were shared before implementation |
| TDD | Completed tests alone do not show Red was checked first |
| DDD | Glossaries or class names alone do not show shared meaning or model boundaries |
| CI | Workflow YAML alone does not show frequent main integration or broken-build repair |
| CD | Deploy jobs alone do not show safe on-demand delivery |
| Team Topologies | CODEOWNERS or team names alone do not show responsibilities, interactions, or cognitive load |
| DORA Capability | Tools/configuration alone do not show observable capabilities |

Check actual changes, history, waiting, failures, delivery, and stakeholder experience through [assessment procedures](assessment.md).

### Combine only necessary lenses

Examples:

- Only a Ubiquitous Language mismatch → focus on DDD. Do not expand into unrelated DORA or Architecture.
- Release approval waiting → Lean / CD + related DORA Fast flow Capability.
- Cross-team dependencies → Architecture / Organization + Team Topologies; add DORA Loosely Coupled Teams if needed.
- Whether to adopt Microservices → Architecture / Organization + DDD + XP Simplicity. Do not assess the entire DORA Catalog.
- XP design/feedback assessment → focused XP lens. Do not score how many practices are adopted.

Expand assessment scope only when its effect on the user's purpose can be explained.

Check sources and version differences in [primary materials and application decisions](sources.md).
