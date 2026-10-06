---
type: Reference
title: Designing responsibilities, contracts, and comments
description: Criteria for choosing structure from model boundaries and retaining intent and public contracts in code.
sources:
  - id: practice-sources
    resource: sources.md
---

## Designing responsibilities, contracts, and comments

### Using the five XP values in implementation decisions

- **Communication**: Share purposes, expectations, and unanswered questions with stakeholders, and check differences in understanding through tests and actual diffs.
- **Simplicity**: Choose an understandable structure that meets current contracts, without adding unrequested features or abstractions.
- **Feedback**: Choose the next implementation and design improvements from small tests, collaboration, integration, and user responses.
- **Courage**: Do not hide defects or uncertainty; carry out necessary Refactor based on tests and the agreed scope. This does not mean skipping approval or validation.
- **Respect**: Respect users' decision authority and stakeholders' knowledge and time. Do not make unagreed business decisions on their behalf or gain speed through overload.

This applies XP values to the implementation procedure. Use this mapping even when the distribution destination lacks shared Instructions. Keep the original sources and the scope of application in this environment in the [source materials](sources.md).[^practice-sources]

### Simple Design and YAGNI

Provided that current contracts and tests are met, examine whether structure conveys intent, duplicates the same rule, or contains unnecessary elements. Do not add interfaces that might be used someday, unused extension points, configuration for hypothetical requirements, or unrequested generalization. Add minimal structure when you can explain an actual gap in callers, contracts, or changes.[^practice-sources]

YAGNI is not a reason to omit necessary validation or refactoring. Handle design improvements identified at Green in Refactor within the same cycle, preserving code health that supports small changes. Judge intent and duplication from model meaning; do not make abstract types or line counts quality targets.[^practice-sources]

### Expressing agreed behavior as contracts

For the next small behavior change, start from agreed stories, domain rules, and acceptance conditions. Reuse existing specification and discovery outcomes; use `behavior-specification` for unsettled rules, without making EventStorming or another ceremony a new gate. Make only the applicable contracts explicit before the corresponding test and implementation.[^practice-sources]

| Category | Meaning and owner |
| --- | --- |
| Precondition | A caller obligation that holds before the operation, including relevant input and starting-state constraints |
| Postcondition | A callee guarantee when preconditions hold, including promised results and observable effects |
| Invariant | A condition of valid model state established by construction and preserved by valid operations |

Use existing domain names, types, schemas, API documentation, and tests to express these agreements. Supplement constraints that those forms cannot convey. Do not require three boilerplate sections for every operation or invent state invariants for stateless calculations.

#### Ownership and enforcement

- Identify which caller or boundary establishes each precondition and which operation guarantees each postcondition. Distinguish assuming valid input from promising caller-facing rejection behavior.
- Enforce current requirements at the boundary that owns validation, using existing types, constructors, schemas, or runtime checks as appropriate. Do not repeat defensive guards throughout trusted internal calls whose obligations are already established.
- Keep model state valid through construction and valid operations; avoid exposing mutation that can violate its invariants. Choose immutable values when they simplify the current behavior.
- Define invalid-input observations only when agreed or required in the current scope. A precondition alone does not choose an exception, error response, retry, or fallback policy.

Follow happy-path MVP and incremental design: add conditions for current requirements, existing contracts, confirmed defects, or concrete safety risks. Do not retrofit the whole repository or introduce speculative hardening, a new framework, or formal proof requirements.

#### Visible effects and meaningful abstractions

Prefer pure calculations where they simplify reasoning. Isolate necessary I/O and mutation at explicit boundaries, and state their promised effects rather than hiding them behind a calculation name.[^practice-sources]

- For a calculation, make its inputs and returned value clear, including whether inputs remain unchanged.
- For an operation that persists or mutates state, retain the promised resulting state and any agreed failure behavior in its contract; select tests at the boundary capable of observing them.
- Choose the smallest meaningful function or type that exposes the agreement. Do not mandate classes, interfaces, patterns, or an architectural rewrite.

Map these contracts to [observable tests](testing.md#mapping-contracts-to-observable-tests), implementing one item at a time. Contracts and passing tests provide evidence within their checked scope, not a formal or “100% correct” guarantee; existing review, security, CI, and integration conditions still apply.

### Choosing design from responsibilities and contracts

Check actors' purposes, agreed rules and invariants, and model boundaries before choosing the smallest structure that meets current requirements. OOP groups state and behavior into objects as a design tool; it is not a required form of DDD. Retain functions and data when they express contracts clearly.

Use SOLID to inspect responsibilities, extension, substitutability, interfaces, and dependency direction. Do not use class counts or the presence of abstract types as pass/fail criteria.

| What to check | Decision and response |
| --- | --- |
| Responsibilities and reasons for change | Group the same business rule and separate processing with different reasons for change. Do not share rules from different models merely because values or syntax look similar |
| Parts that vary | Separate a part when there are multiple agreed approaches or actual change points. Do not abstract in anticipation of unrequested extensions |
| Substitutability | Preserve promised input conditions, results, failures, and side effects when implementations are exchanged. Reconsider the contract or structure if a subtype tightens input conditions or weakens guarantees |
| Contracts for each caller | Split an interface when callers depend on unused operations and are forced to make unrelated changes or implementations |
| Dependency direction | Follow the DDD policy in AGENTS.md. Pass dependencies as arguments or similar at boundaries actually exchanged or isolated. Use the smallest contract that fits the language and existing design |

Use GoF patterns as shared vocabulary for recurring design problems. For example, consider Strategy for exchanging agreed calculation methods, Adapter for translating external contracts, and Builder for staged construction with constraints. Adopt a pattern when you can explain the problem, contract to preserve, and burden of added structure. Do not require every pattern or name suffixes.

Consider composition and delegation first for reuse and combining behavior. Use inheritance when sharing substitutable contracts; do not mechanically replace existing simple inheritance. Keep state so external access cannot break invariants, and make values immutable when they need no changes. Verify contractual behavior, not just pattern structure or mock call counts.

### Communicating boundaries through names, placement, and types

Check existing naming, placement, and language conventions. Within the scope added or changed, make meaning and contracts traceable for users. Record decisions on applying Context Engineering and Taming Copilot in the [source materials](sources.md#sources-of-instruction-examples-and-application-decisions).[^practice-sources]

- Use words expressing roles or business meaning in names and paths. If a value's meaning or units are unclear, use a named constant at that model boundary. Do not share different rules merely because they use the same number.
- For new placement, make related code, types, and tests easy to find as one feature. Follow existing colocation; if tests belong in a separate directory, align corresponding names and structure. Do not move large numbers of existing files solely for colocation.
- State input/output types and contracts at public API and module boundaries. Supplement constraints not expressible in static types through existing schemas, API documentation, or docstrings. Retain obvious local type inference; do not force annotations unsuitable for the language or project.
- Distinguish public entry points from internal implementation. Expose only intended contracts through existing export, visibility, and package mechanisms. Do not require uniform index files or re-export every symbol, or expand internal implementation into public APIs.
- First check whether standard features and existing dependencies meet requirements. When adding a dependency, explain the gap it resolves and maintenance and compatibility effects. Do not make unrelated cleanup solely to replace existing dependencies with standard features.

### Retaining intent in code and comments

First express business meaning and dependencies through names, types, function decomposition, and expressions. Before writing comments, check that they do not repeat what code already shows.

- Retain design reasons, external constraints, and grounds for compatibility handling or workarounds that code alone cannot convey. Add known references and removal conditions to workarounds; do not invent unverified incidents or future plans.
- When names, types, and decomposition do not explain complex processing, briefly supplement its purpose and flow. Do not mix responses to change requests or editing narration into comments, or require boilerplate explanations in every module.
- Retain public contract purposes, arguments, return values, failures, and side effects in a form users can understand, including types and existing API documentation. Do not remove invisible contracts such as ownership, units, or destructive input updates on the grounds of “write only reasons.”
- Do not merely explain the name of an adopted pattern. Retain its rationale when code does not reveal it. Refer to existing ADRs rather than duplicating their explanations.
- Cross-check related comments when making changes. Leave unnecessary commented-out code and history lists to version control, but check references and removal conditions when handling operational TODOs and similar notes.
- Follow project conventions for docstring language and format. Do not make comments on all functions or a particular language's documentation format shared requirements.

Keep design sources and adoption decisions in the [primary materials](sources.md).[^practice-sources]

[^practice-sources]: References and application decisions for Simple Design, YAGNI, DDD, OOP Design Patterns, Self-explanatory Code Commenting, Context Engineering, and Taming Copilot; [Design by Contract adoption and limits](sources.md#adoption-decisions-for-design-by-contract).

## Change scope and decomposition

- Check the premises for design decisions in AGENTS.md and the agreed design policy.
- If design policy must change, summarize reasons and effects and separate a task to reconsider it. Do not request the same approval again in a task already authorized to make that change.
- Inspect related callers, tests, configuration, and documentation to determine the affected scope.
- Estimate additions and deletions per file and in total, and record the basis in the plan.
- Split into small units independently verifiable, reviewable, and integrable. Multiple scenarios showing normal, boundary, and error cases of the same rule may belong to one task.
- Use a total of 500 lines or more as a cue to reconsider decomposition. Do not split solely by line or scenario counts; explain splitting or retaining the unit through independent value, validation, and dependencies.
- For a Sub-issue, state the target behavior or technical change purpose, files, estimate, dependencies, and validation method. Decide and record implementation targets and order within the purpose; follow `issue-management` for changes needing confirmation.
- If scope or change volume grows during implementation, reconsider estimates, decomposition, and the approved scope before expanding work.
