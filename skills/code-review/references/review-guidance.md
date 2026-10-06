---
type: Guide
title: Concrete review criteria and reporting examples
description: Connect 11 areas to concrete investigation and distinguish formal findings, optional suggestions, and design decisions to retain from evidence.
sources:
  - id: github-instructions-code-review-generic-instructions-md
    resource: https://github.com/github/awesome-copilot/blob/main/instructions/code-review-generic.instructions.md
  - id: fowler-beck-design-rules
    resource: https://martinfowler.com/bliki/BeckDesignRules.html
  - id: fowler-yagni
    resource: https://martinfowler.com/bliki/Yagni.html
---

## Investigation

1. Understand actors' purposes, contracts, and overall design, check impact through responsibilities, model boundaries, and dependency directions, then proceed to implementation and tests. Compare specifications and diffs, checking changed judgments, boundaries, inputs/outputs, and where their reasons are recorded. Treat PR descriptions of intentions or causes as claims, substantiated by implementation/specifications and, for migrations or past behavior, history.
2. Compare the perspectives below with the diff and deepen relevant areas. Read applicable [Concrete checking criteria](#concrete-checking-criteria), adapting investigation to project specifications, conventions, and versions. Split large diffs by responsibilities or paths, then compare cross-boundary effects. Check necessity for current requirements through contracts and callers, investigating understanding/validation burdens from unnecessary complexity. Find locations needing future updates through preserved contracts/intent and consistency among implementations of the same rule. This is not a priority order that postpones serious defects.
3. Use `rg` or similar tools to find and open paired implementations outside the diff (lists/details, totals/items), definitions with the same value/meaning as new constants, actual references, and callers of shared components. Do not judge by reference counts alone; trace production paths, configuration, and test replacement targets. Respect intentional differences belonging to different models.
4. Trace how failures reach users or operators, comparing client settings, exception-catching conditions, logs, notifications, and display. For external API behavior, check used versions through lock files or similar evidence, and confirm with corresponding official material or implementation. Also read types, schemas, and settings guaranteeing application assumptions.
5. Connect each candidate's current usage conditions or expected changes, evidence-based dependencies, and impact. Seek counterevidence in caller guarantees, recorded intent, existing types, constraints, and tests. Distinguish pre-existing problems from those introduced or worsened by this change.
6. If validation is needed, reproduce read-only or in isolation. Do not run tests involving external transmission or actual-data modification. Separate executed commands/results from unexecuted checks and reasons. Ground performance/cost in frequency, measurement conditions, and measurements; distinguish unmeasurable claims from confirmed facts.

## Investigation perspectives

Not every area needs findings. Line counts, nesting depth, and design principles guide deeper investigation, but exceeding numbers or principle names alone is not a reason to fix. Use them as questions about relationships with the diff; do not duplicate the same cause across areas.

| Area | Questions and checking targets |
| --- | --- |
| Consistency | Do paired displays/processes or constants disagree on the same rule in the same model? Are there duplicate definitions allowing only one side to be updated, or compatibility aliases never actually referenced? |
| Contracts and intent | Can the next maintainer trace reasons for specifications, numbers, and dependencies? Are pre-migration contracts, reasons for changes, and conditions needing updates preserved in specifications, code, and tests? |
| Value correctness | Do unit prices/totals, units, boundaries, dates/time zones, and exceptional values match specifications? Do tests duplicate the same mistaken assumption? |
| Failure detection | Are failures displayed as success? Can users/operators detect and act on failures without exceptions, logs, or notifications disappearing through catching/conversion? |
| Users and operations | What happens through navigation, filtering, actions during processing, and operational procedures? Do they cause mistaken actions or difficult recovery? |
| External boundaries | Do SDK, communication, OS, and framework contracts, permission boundaries, actual versions, and settings satisfy calling assumptions? |
| Data preservation | Does consistency survive failures, concurrency, or deletion? Do DB constraints guarantee assumptions such as membership counts? Can retries or partial failures be recovered? |
| Understandable design | Are domain rules separate from technical processing, with responsibilities, types, and names expressing contracts? Do abstractions/configuration unnecessary for current requirements impede understanding or validation? Does the next change require understanding or modifying unrelated locations? |
| Performance and cost | How many seconds/how much cost for data volume and call frequency? Can indexes and outer timeouts also be checked? |
| Change impact | How do defaults, shared state, or breaking argument changes reach existing callers? Can effects of additions/changes remain within boundaries? |
| Testability | Can tests detect contract violations or missed changes? Do mocks replace actual call targets? Can target paths be tested before merging while preventing external transmission? |

## Concrete checking criteria

Use these for diff-relevant items in the 11 areas. Check target repository specifications, conventions, and design decisions; do not make these uniform prohibitions or finding-count goals. When abnormalities are suspected, trace callers, configuration, constraints, and tests for existing guarantees and counterevidence.

### Security and boundaries

Corresponding areas: external boundaries, data preservation, failure detection, change impact.

- Separate authentication from authority to operate on target resources; check owner, tenant, and role restrictions on every path. Read upstream guards and DB constraints as well; do not demand duplicate checks.
- Trace external input to queries, commands, and displays, checking validation and appropriate escaping or parameterization at boundaries. Names saying “validated” alone do not establish safety.
- Trace credentials or unnecessary personal information into code, configuration, logs, exceptions, and notifications. Do not copy confidential values into findings or reproduction output; identify types, locations, and paths.
- Check established cryptographic libraries' contracts and settings. Verify known dependency vulnerabilities against actual lock-file versions and official advisories, showing applicability conditions. Being behind the latest version alone is not a defect.

### Responsibilities, dependencies, and readability

Corresponding areas: consistency, contracts and intent, understandable design, change impact.

- Check that names, types, and responsibilities express domain rules/contracts, without UI, communication, or persistence concerns intruding on rule changes or validation. Identify concrete locations where dependency direction or large interfaces require modifying or starting unrelated implementations.
- Compare current contracts and callers to concrete understanding/validation burdens from premature abstraction, unnecessary interfaces, unused extension points, configuration for hypothetical future requirements, or unrequested generalization. Do not uniformly criticize necessary boundaries or extensions.
- Check related processing is grouped and processing with different reasons to change can be separated. Investigate reasons for departures from existing patterns; do not mechanically perpetuate existing problems.
- Compare duplication by meaning and model boundaries, not just values or syntax. Investigate missed updates in duplicate definitions of the same rule while preserving intentional independence of different models.
- Use long functions or deep nesting as entry points to investigate missed conditions, mixed responsibilities, or scattered changes. Do not make the reference guide's approximate 20–30 lines or 3–4 nesting levels common pass/fail thresholds. Check applicability of explicit project conventions.
- Check traceable reasons and dependencies for fixed values, complex expressions, or compatibility handling. Do not require redundant comments when constants, types, expressions, tests, or specifications convey intent. Judge unused code/TODOs from references and current operations.

### Tests and failure detection

Corresponding areas: value correctness, failure detection, data preservation, testability.

- Check which tests detect broken main contracts, added behavior, boundaries, or exceptional paths. Show concrete misses rather than relying on file presence or coverage.
- Check expectations express specifications rather than copying implementation calculations. Investigate weak assertions such as testing only truthiness for amounts; when booleans themselves are the contract, boolean checks are appropriate.
- Check conditions, operations, and results are readable from names and Given/When/Then or Arrange/Act/Assert. Do not demand rewriting merely to unify notation.
- Investigate dependencies on execution order, time, shared state, networks, environment variables, and cleanup. Check mocks isolate external boundaries rather than replacing target domain logic and claiming correctness.
- Compare exception types, catching/conversion, HTTP return values, logs, and displays, tracing detectability and recovery. Put input validation/error handling at responsibility-appropriate boundaries; do not treat failure as success.

### Performance, cost, and resource management

Corresponding areas: performance and cost, users and operations, data preservation.

- Investigate N+1, indexes, complexity, and memory from call frequency and data volume. Distinguish first-time processing from paths used every time.
- Check connections, files, and streams are released on exceptions and cancellation as well as success. Compare timeouts with outer limits and total retries.
- Include freshness, invalidation, missed retrieval, and management cost when considering caches, pagination, or lazy loading. Do not require optimization without evidence of concrete effects.
- Separate measurement conditions and actual measurements, counts statically derived from inputs, and unmeasured predictions. Do not invent unmeasured seconds, prices, or improvement rates.

### Public contracts, documents, and operations

Corresponding areas: contracts and intent, users and operations, external boundaries, change impact, testability.

- Check public API purpose, arguments, returns, failures, and side effects are understandable through types or user specifications. Prioritize preserving invisible contracts over duplicating information apparent in code.
- Compare API/default changes with existing callers and compatibility policy. Check migration methods and impact for breaking changes; version bumps alone do not validate compatibility.
- Compare feature, configuration, or startup-procedure changes with README and operational procedures. For complex functionality, investigate whether examples show necessary decisions or failure responses.
- For deployment/data migration, check partial failures, mixed old/new versions, and recovery procedures. Do not uniformly demand destructive reverse migrations when safe forward repair is designed.

## Findings and results

- Report formal findings, optional improvements, then design decisions to retain, including only useful categories. See [Category decisions and reporting examples](#category-decisions-and-reporting-examples). Do not require counts or praise or duplicate content across categories.
- Formal findings include unnecessary complexity for current requirements, evidence-based obstacles to modification/validation, and defects/regressions. Do not downgrade to optional solely because impact is local, arises during future changes, or concerns documents/readability.
- Optional improvements apply when the current state meets confirmed contracts and safe-change needs and alternatives have concrete benefits. Explain benefits, costs, and tradeoffs without requiring adoption. Do not revive stylistic preferences, unsupported hypotheses, or unnecessary abstractions as suggestions.
- For design decisions to retain, show locations, protected contracts/invariants, and reasons to retain them for future changes. Do not use formulaic author praise or guarantee all quality, or offset formal problems with good points.
- Connect “triggering conditions or expected change → evidence-based paths/dependencies → concrete user/maintainer impact,” with severity, minimal file/line locations, and fix direction. Choose the smallest diff location, also showing specifications, callers, or tests if needed. Constructively discuss code and decisions rather than author evaluation; add existing implementation, official material, or short fix examples when useful.
- Choose severity from scope and conditions, using P0 (widespread breakage, immediate action), P1 (serious loss or major functionality stopped), P2 (limited-condition malfunction, or concrete modification/validation obstacles from missed updates or unclear contracts), and P3 (minor defects or local understanding/change burden) as guidance. Separate evaluation priorities from urgency; future concerns alone do not justify P0/P1.
- Show target SHA, specifications, diffs, callers, and test evidence needed for fix decisions, validation results, and uncertainties. Do not require formulaic reports proving the skill was read.
- “No formal findings” means no design/change problems or defects/regressions requiring fixes were found within checked scope. “Insufficient evidence” means necessary material or results are missing; show unverified scope and next information needed. No findings does not guarantee all quality; unexecuted tests are not successful.
- Follow execution-environment output formats and severity scope, stating scope/restrictions in permitted fields. In findings-only formats, do not mix optional suggestions or good decisions into findings, or add unpermitted sections/fields. This skill does not decide GitHub completion or approval.

## Category decisions and reporting examples

Use formal findings when evidence explains current defects or concrete obstacles to modification/validation. Use optional suggestions when the current state meets contracts and can be changed safely and alternatives' benefits and burdens can be compared. Investigate further if the distinction is unclear; do not fill evidence gaps with optional suggestions.

Locations and numbers below are explanatory examples; replace them with checked targets in actual reviews. Match expression to format/content without empty fields or unnecessary code examples.

### Formal finding example

#### [P2] Contracts and intent: Express dependencies that follow column-width changes

`3.5rem` at `timeline.css:12` is half the current column width of 6rem plus a 1rem gap, so the current display is correct. However, theme width/gap changes do not update it, and the locations needing adjustment are unclear. Calculate from theme variables or record the formula's reasons and update conditions. Related definitions are at `theme.css:4-5`.

Choose severity from confirmed scope/conditions rather than copying the example's P2. Keep fixes proportional to the problem.

### Optional improvement example

#### Optional suggestion: Also provide a copyable operation example

The public specification contains required headers, arguments, and failure handling, making the current contract understandable. A curl example in `docs/api.md` could help shorten user experimentation. It adds example-maintenance work, so it is unnecessary if an existing API-client collection is sufficient.

If documentation gaps prevent correct usage, treat them as formal findings. Compare additional benefits and maintenance burdens only when the current state is sufficient, as in this example.

### Design decision to retain example

#### Design decision to retain: Prevent duplicate registration during retries through the DB

The unique constraint at `orders.sql:18` and conflict retrieval at `create_order.py:24` use the same request key, protecting the contract that concurrent retries do not duplicate orders. Preserve the design of routing added registration paths through this key and constraint.

Show confirmed mechanisms and protected contracts rather than merely “thorough tests” or “good design.” Report problems in other paths as formal findings first.

## Sources and application policy

Referenced the quality perspectives, overall-to-detail investigation, and concrete constructive reporting in GitHub awesome-copilot's Generic Code Review Instructions.[^github-instructions-code-review-generic-instructions-md]

Using Martin Fowler's Beck Design Rules[^fowler-beck-design-rules] and Yagni[^fowler-yagni], established five perspectives for investigating complexity unnecessary for current requirements. These are this skill's application examples; the originals do not uniformly prohibit each structure.

This skill evaluates the simplest design meeting current requirements and safety for actual changes, assigning P0–P3 severity by impact. Do not directly apply the sources' area-specific severities, line-count guidance, or Copilot frontmatter. Report review results as judgments within checked scope; do not decide GitHub approval or merge.

[^github-instructions-code-review-generic-instructions-md]: [GitHub awesome-copilot Generic Code Review Instructions](https://github.com/github/awesome-copilot/blob/main/instructions/code-review-generic.instructions.md). Evidence for the reference scope and adoption decisions stated in the text.
[^fowler-beck-design-rules]: [Beck Design Rules](https://martinfowler.com/bliki/BeckDesignRules.html). Apply to design meeting current requirements, clear intent, and judging unnecessary elements.
[^fowler-yagni]: [Yagni](https://martinfowler.com/bliki/Yagni.html). Distinguish anticipation of hypothetical future features from currently necessary health.
