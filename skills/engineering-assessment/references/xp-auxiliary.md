---
type: Reference
title: Lightweight lookup of individual XP items
description: Read only diagnostic meanings of individual XP Values / Principles / Practices for XP-primary assessment or support for other lenses.
sources:
  - id: xp-second-edition
    resource: https://www.informit.com/store/extreme-programming-explained-embrace-change-9780134051987
  - id: ron-jeffries-xp
    resource: https://ronjeffries.com/xprog/what-is-extreme-programming/
  - id: xp-second-edition-principles
    resource: https://www.oreilly.com/library/view/extreme-programming-explained/0321278658/ch05.xhtml
  - id: xp-second-edition-primary-practices
    resource: https://www.oreilly.com/library/view/extreme-programming-explained/0321278658/ch07.xhtml
  - id: xp-second-edition-corollary-practices
    resource: https://www.oreilly.com/library/view/extreme-programming-explained/0321278658/ch09.xhtml
---

## Lightweight lookup of individual XP items

Read when checking named-item meanings in XP-primary assessment, or using one or a few XP items to support Architecture, DORA, Lean, or other lenses. Enter through [XP taxonomy](xp.md) for classification and overall relationships; use this shared lookup for item semantics.[^xp-second-edition]

Do not make this reference a mandatory checklist of every XP item. Even in XP-primary assessment, select only items relevant to the current problem; do not expand every item into unknowns lists.

### Values

Cross-check meanings of the five Values against public XP explanations.[^ron-jeffries-xp]

| Value | Compact diagnostic cue |
| --- | --- |
| Communication | Share purposes, constraints, concrete examples, and unanswered questions; align understanding early |
| Simplicity | Smallest understandable design meeting current requirements; avoid complexity based solely on future predictions |
| Feedback | Obtain results from tests, integration, users, and operations at short intervals and apply them to next steps |
| Courage | Do not hide defects, uncertainty, or unnecessary design; proceed to necessary changes from evidence |
| Respect | Respect user decision authority, stakeholder knowledge/time, and sustainable work |

### Principles

Refer to the second edition's Principles chapter for their role.[^xp-second-edition-principles]

| Principle | Compact diagnostic cue |
| --- | --- |
| Humanity | Needs, relationships, and safety enabling people to sustain good work |
| Economics | Economic decisions including time, cost, value, and opportunity cost |
| Mutual Benefit | Choices increasing benefits for today and the future and multiple stakeholders simultaneously |
| Self-Similarity | Reuse feedback, solution structures, and design/delivery patterns that worked at other contexts/scales as hypotheses; verify fit to current constraints |
| Improvement | Improve incrementally from the current state without waiting for perfection |
| Diversity | Bring different experiences, expertise, and perspectives into decisions early |
| Reflection | Reflect on results and methods and feed back into next actions |
| Flow | Reduce queues, handoffs, WIP, and batch delays to let value flow |
| Opportunity | Treat problems, changes, and constraints as learning opportunities for system improvement |
| Redundancy | Avoid relying on one defense against major failures; use complementary safeguards as needed |
| Failure | Try small experiments safely, do not hide failures, and connect them to learning |
| Quality | Do not persistently reduce quality for speed; adjust scope, methods, and order |
| Baby Steps | Split into minimal reversible, verifiable steps |
| Accepted Responsibility | Match necessary authority and information to people/teams accepting responsibility |

### Primary Practices

Refer to the second edition's Primary Practices chapter for their role.[^xp-second-edition-primary-practices]

| Primary Practice | Compact diagnostic cue |
| --- | --- |
| Sit Together | Necessary people can collaborate continuously at low communication cost |
| Whole Team | Access perspectives needed to deliver value; do not fragment responsibility into handoffs alone |
| Informative Workspace | Necessary people can readily understand progress, quality, risks, and similar information |
| Energized Work | Sustainable work preserving quality and judgment |
| Pair Programming | Continuous design, review, and knowledge sharing from multiple perspectives during implementation |
| Stories | Discuss scope, cost, and expectations in user-value units; adjust priorities in small increments |
| Weekly Cycle | Reconsider near-term planning, delivery, and feedback at a short cadence |
| Quarterly Cycle | Periodically reconsider broad themes, investment, and direction |
| Slack | Allow room for uncertainty, improvement, and unexpected work |
| Ten-Minute Build | Keep build/test feedback fast enough for frequent use |
| Continuous Integration | Frequently integrate small changes into shared main and repair failures quickly |
| Test-First Programming | Express expected behavior in tests before implementation; iterate failure → minimal implementation → cleanup |
| Incremental Design | Continuously improve design needed for current requirements |

### Corollary Practices

Refer to the second edition's Corollary Practices chapter for application cautions. Introducing names without Primary Practices or necessary delivery/feedback foundations can be difficult or dangerous; check related foundations and current constraints first.[^xp-second-edition-corollary-practices]

| Corollary Practice | Compact diagnostic cue |
| --- | --- |
| Real Customer Involvement | Obtain continuous feedback from actually affected customers/users |
| Incremental Deployment | Avoid large migrations; adopt, learn, and roll back in small slices |
| Team Continuity | Avoid losing effective team relationships/domain knowledge through unnecessary restructuring |
| Shrinking Teams | Move spare capacity gained from improved capability to new value; do not make staff reduction the goal |
| Root-Cause Analysis | Improve system/process conditions rather than ending defect/incident analysis at individual blame |
| Shared Code | Improve the whole codebase under collective ownership and safeguards |
| Code and Tests | Maintain code and automated tests together as principal executable change contracts |
| Single Code Base | Do not unnecessarily fork or duplicate the same product's source of truth |
| Daily Deployment | Shorten production feedback on safety foundations; do not turn deployment counts into quotas |
| Negotiated Scope Contract | Reflect cost, value, and learning through short contracts and scope renegotiation |
| Pay-Per-Use | Check whether a business model connecting actual use with economic feedback is effective |

If classification or relationships to other XP items become necessary, also read [XP taxonomy](xp.md). Continue using this lookup for item-semantics assessment itself.

[^xp-second-edition]: [Extreme Programming Explained: Embrace Change, 2nd Edition — Kent Beck / Cynthia Andres](https://www.informit.com/store/extreme-programming-explained-embrace-change-9780134051987). Second-edition XP taxonomy. Checked 2026-09-27.
[^ron-jeffries-xp]: [What is Extreme Programming? — Ron Jeffries](https://ronjeffries.com/xprog/what-is-extreme-programming/). Five Values and applying small feedback. Checked 2026-09-27.
[^xp-second-edition-principles]: [Chapter 5. Principles — Extreme Programming Explained, 2nd Edition](https://www.oreilly.com/library/view/extreme-programming-explained/0321278658/ch05.xhtml). Role of Principles. Checked 2026-09-27.
[^xp-second-edition-primary-practices]: [Chapter 7. Primary Practices — Extreme Programming Explained, 2nd Edition](https://www.oreilly.com/library/view/extreme-programming-explained/0321278658/ch07.xhtml). Role of Primary Practices. Checked 2026-09-27.
[^xp-second-edition-corollary-practices]: [Chapter 9. Corollary Practices — Extreme Programming Explained, 2nd Edition](https://www.oreilly.com/library/view/extreme-programming-explained/0321278658/ch09.xhtml). Corollary Practices application cautions. Checked 2026-09-27.
