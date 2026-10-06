---
type: Instruction
title: Development and feedback
description: Define XP values, incremental design, acceptance conditions, and test-first iteration.
sources:
  - id: ron-jeffries-xp
    resource: https://ronjeffries.com/xprog/what-is-extreme-programming/
  - id: fowler-yagni
    resource: https://martinfowler.com/bliki/Yagni.html
  - id: fowler-evolutionary-design
    resource: https://martinfowler.com/articles/designDead.html
---

## Development and feedback

Use Extreme Programming (XP) to guide daily development decisions, connecting its five values to the following actions.[^ron-jeffries-xp]

| Value | Decisions and actions |
| --- | --- |
| Communication | Share purposes, rules, concrete examples, and unanswered questions, and check differing understandings before implementation |
| Simplicity | Choose the smallest understandable design that meets currently confirmed requirements and contracts |
| Feedback | Use Small Steps to check tests, collaboration, integration, and user reactions early, and reflect them in the next small change |
| Courage | Do not conceal defects or uncertainty; make necessary design improvements based on tests and the existing approval scope |
| Respect | Respect users' decision authority, stakeholders' knowledge and time, and sustainable work |

Follow Simple Design and YAGNI; do not add features or abstractions for hypothetical future changes. Advance Incremental Design and Refactoring from actual feedback. Do not use them as reasons to omit required tests, contracts, design improvements, review, CI, approvals, or publication permission.[^fowler-yagni]

When one human starts XP, begin with the existing small TDD cycles, incremental design, and automated validation. See “Starting XP alone” in `software-development` for concrete adoption methods. The number of humans and AI Driver/Navigator roles are separate; individual practice does not justify omitting existing agent collaboration, ordinary review, CI, or integration conditions.

### Incremental design

Adopt XP's Incremental Design. Instead of completing the design up front, begin with the smallest design meeting current requirements and continuously evolve it through small refactorings based on tests and actual feedback. This does not mean omitting design or postponing necessary design improvements.[^fowler-evolutionary-design]

The following is this environment's application policy. A simple happy-path MVP is the initial approach; subsequent changes also add only the design needed for current requirements, in small steps. Do not arbitrarily reduce the user's explicit scope or agreed acceptance conditions.

- Limit initial implementation to a simple happy-path MVP that achieves the purpose with representative normal input and ordinary operations. Briefly state assumptions and first make the shortest path work.
- Do not cover low-probability edge cases or hypothetical failures up front. Do not preemptively add exception handling, retries, fallbacks, compatibility handling, configuration, or generalization solely “just in case” or because “it may be needed later.”
- Apply the same scope to plans, acceptance conditions, ToDos, tests, and review. Do not add unrequested edge cases as mandatory items or merge conditions; briefly show only unaddressed limitations that need explanation.
- Do not omit explicit requirements, existing contracts, regression protection, or protection needed against concrete security or data-destruction risks. When adding handling outside normal paths, give reasons linked to current requirements, contracts, and confirmed facts, and keep it minimal.
- Once the current change meets acceptance conditions, finish required validation, review, and integration without automatically starting additional hardening. Handle exceptions or extensions as separate small changes after actual use, defects, or additional requests establish their necessity.
- For changes with multiple independent integration units, after integrating each unit into main and confirming required validation, briefly reassess whether new facts from implementation, tests, and review change the remaining plan's assumptions, scope, order, decomposition, dependencies, ownership boundaries, or validation method before starting the next unit. Do not rewrite the plan formally when nothing changes; otherwise share reasons and the updated plan. Do not redo completed integration units without new evidence.

### Shared understanding and validation

Organize rules, concrete examples, and unanswered questions from stakeholders' differing perspectives, and define acceptance conditions before the corresponding implementation. Save the feature document first for domain-rule changes.

Make code changes test-first, expressing expected behavior after implementation in tests before the corresponding implementation code. Write tests assert-first, beginning with the assertion that must ultimately pass.

In TDD, iterate failure, minimal success, and cleanup one item at a time from a ToDo list that includes test items. Follow `software-development` for technical processing, existing specifications, and behavior-preserving cleanup with sufficient existing tests. The existence of documents or tests alone is not evidence of collaboration or test-first work.

[^ron-jeffries-xp]: [Ron Jeffries: What is Extreme Programming?](https://ronjeffries.com/xprog/what-is-extreme-programming/). Adopt the five values, design meeting current requirements, and short validation and design-improvement cycles. Do not make fixed meetings, periods, organizational structures, or effect figures common requirements. Checked on 2026-09-25.
[^fowler-yagni]: [Martin Fowler: Yagni](https://martinfowler.com/bliki/Yagni.html). Avoid anticipating future features while retaining tests, refactoring, and CI supporting current changes. Assert-first work and staged agent checks are this environment's operating policy. Checked on 2026-09-25.
[^fowler-evolutionary-design]: [Martin Fowler: Is Design Dead?](https://martinfowler.com/articles/designDead.html). Adopt continuously evolving design in XP, supported by tests, CI, and refactoring. The specific scope of starting with a happy-path MVP is this environment's application policy, not the definition of XP itself. Checked on 2026-09-28.
