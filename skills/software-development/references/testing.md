---
type: Reference
title: Change units and reproducible validation
description: Choose test layers, state, time, external boundaries, UI, and performance from contracts and risks.
sources:
  - id: practice-sources
    resource: sources.md
---

## Change units and reproducible validation

### Change units and validation

| Decision | Selection |
| --- | --- |
| Issue decomposition | Use units whose value, validation, and integration can be checked independently. Do not equate one TDD iteration or one concrete example with one Issue |
| The 500-line guide | A local guide to reconsider review burden, not a rule from original BDD or TDD sources. Do not split indivisible changes merely by line count |
| Test layers | Prefer unit tests that identify causes quickly. When actual contracts, connections, or configuration cause the problem, use the smallest effective integration test |
| Technical contracts | Observable results promised to readers, such as API responses or failure notifications to operators, may be shared specifications. Distinguish them from implementation procedures such as internal connection methods |
| Regression fixes | If the agreed specification is correct, retain it and add validation reproducing the defect. Do not change expectations to pass tests |

A DDD Bounded Context is the scope in which model meaning applies, a Subdomain is a division of the problem domain, and a Git repository is a code management unit. Judge their correspondence from terminology, contracts, ownership, and change dependencies; do not define DDD as a universal one-to-one correspondence. Improve testability and deployability incrementally rather than rewriting everything.

### Black-box tests at the intended boundary

At every selected level—unit, integration, or acceptance—test the contract, not the implementation. Choose the smallest effective level for the required behavior; do not require all three levels for every change. Supply inputs through the unit's or system's intended interface and assert specified return values, agreed errors, externally observable state changes, or required effects. Black-box testing does not require end-to-end tests or only return-value assertions. A behavior-preserving replacement should not change the test's expectations.

Choose expectations from the agreed specification, not current output or copied implementation calculations. Do not assert source text, algorithms, private helpers, internal data structures, incidental call counts/order, exact internal command invocations, or coding style. Exporting a helper so tests can import it does not establish a public contract. Test doubles may control external inputs and isolate boundaries; do not make internal collaboration sequences the expected behavior.

### Mapping contracts to observable tests

Use the [applicable contracts and their owners](design.md#expressing-agreed-behavior-as-contracts) to derive representative black-box examples for the next small change.[^practice-sources]

- Preconditions guide valid setup and relevant input boundaries. Test caller-facing rejection only when its observable behavior is agreed or required by the current scope.
- Postconditions guide assertions of promised results, resulting state, and necessary effects. Select observations that can detect a violation without depending on incidental internals.
- Invariants guide checks that construction and valid state transitions preserve valid model state, where applicable. Do not invent invariants or exhaustive cases to fill a checklist.

Keep examples in the existing ToDo list. Select one item, write its assertion first, assemble and confirm Red, implement the minimum for Green, then Refactor before selecting the next item. Do not write every test up front, duplicate implementation calculations in expected values, or use coverage quotas as contract evidence. Preserve the [resilient assertion rules](#resilient-assertions-based-on-contracts).

#### Example: an agreed inventory reservation rule

Suppose the current agreement is that reserving quantity `q` from stock `s` returns the remaining stock. These illustrative rules are not universal inventory requirements.

| Contract | Agreement |
| --- | --- |
| Preconditions | The caller supplies integer stock `s >= 0` and integer quantity `1 <= q <= s` |
| Postcondition | The calculation returns exactly `s - q`, leaving its inputs unchanged |
| Invariant | Every valid inventory state has nonnegative stock; valid reservations preserve it |

For the normal case, first write `self.assertEqual(3, remaining)`, then add `remaining = reserve(stock, quantity)` and setup `stock, quantity = 5, 2`. The completed test in an existing unittest test class is:

```python
def test_reservation_returns_remaining_stock(self):
    stock, quantity = 5, 2
    remaining = reserve(stock, quantity)
    self.assertEqual(3, remaining)
```

Complete that case through Red → Green → Refactor. Next take the agreed upper boundary `reserve(5, 5) = 0` through its own assert-first cycle; it checks the boundary and preservation of nonnegative stock. Use literal expected results drawn from the agreement.

Here `reserve` is a pure calculation; persistence belongs at an explicit boundary. If saving stock is part of the current agreement, verify the promised saved state there with the smallest effective integration test. For mutable inputs, verify that a calculation promising no mutation leaves them unchanged. Add invalid-quantity tests only if the caller-facing rejection behavior is in scope; do not invent exceptions merely to complete the example.

### Reproducible tests suited to their purpose

First decide which contract violation to detect, and choose expectations from the specification. Use minimal data covering normal, boundary, and failure cases; do not copy implementation formulas to construct expectations. Use boolean assertions when booleans themselves are the contract. Do not impose a uniform limit on physical assertion counts.

This environment uses assert-first: write the assertion judging the expected result, state, or exception first. Add the operation required for that observation, then its inputs and setup, to make an executable test. Start by writing the assertion itself, not merely thinking about expectations.

#### Resilient assertions based on contracts

Tests fix contracts observable to users and callers. Do not fix incidental representations generated by frameworks or serializers when those are not contracts. Choose minimal observation points tied to reasons for change, avoiding unnecessary breakage when replacing internals or refactoring without changing behavior.

- For application UI, verify what users can read and do: navigation destinations, meaningful content, keyboard operation, accessible semantics, focus, and required layout usability. Prefer roles and accessible names for interaction. Do not assert raw/generated HTML or CSS strings, CSS declarations, class names, DOM nesting, generated IDs, attribute order, or broad markup/style snapshots. Calling generated markup an output does not establish a representation contract.
- DOM access may observe user-visible outcomes such as focus, clipping, overlap, and scrolling. Do not replace CSS assertions with pixel-perfect screenshots or computed-style assertions that merely restate declarations.
- For independently specified APIs and file formats, including HTML/CSS formats or hooks promised to external consumers, exercise the consumer-facing boundary and preserve its compatibility contract. This differs from asserting incidental application UI representation; do not invent such a contract to retain coupled assertions.
- For JSON and other structured outputs, verify necessary fields, values, and relationships. Do not fix key order, formatting, or extra fields outside the contract. Preserve independently specified API and file-format contracts, including exact strings or order when required; do not invent contracts to retain coupled assertions.
- Use snapshots or complete large-string comparisons only when the complete representation is independently specified as a public artifact or compatibility contract. An intentional broad diff alone is insufficient; the UI rules above still apply.
- If behavior-preserving cleanup fails existing tests, distinguish contractual expectations from incidental assertions. Move implementation assertions to stable observations retaining required behavior, and remove test self-validation under [No tests of tests](#no-tests-of-tests). Do not weaken expectations or copy current output to obtain success.

| Protect | Do not freeze |
| --- | --- |
| Given posts, expected tags, counts, and ordering are returned | Use of `Map`, `sort`, or a particular helper |
| Clicking an article title opens the intended article | An exact anchor string, class, or nesting structure |
| Long content remains readable within the required viewport | A particular Grid/Flex declaration or `overflow-wrap` value |
| Keyboard activation reaches the intended section and transfers focus | Internal event-handler names or listener wiring |

For an agreed specification “shipping is 0 yen when the tax-inclusive subtotal is 5,000 yen,” first write the following. Do not execute intermediate fragments; assemble the test before checking Red.

```python
self.assertEqual(0, fee)
```

Then add `fee = shipping_fee(subtotal)` to obtain the observed value, and its input `subtotal = 5000`. The completed form inside an existing unittest test class is:

```python
def test_free_shipping_at_threshold(self):
    subtotal = 5000
    fee = shipping_fee(subtotal)
    self.assertEqual(0, fee)
```

The writing order is assertion → target operation → setup; the completed test executes setup → action → assertion. This is not a rule to move assertions to the beginning at runtime. For exception checks and similar cases, incorporate operations using the selected framework's syntax. Follow the [implementation entry point](../SKILL.md#test-driven-development-tdd) for test execution, minimal implementation, and cleanup iterations.

| Target or condition | How to construct validation |
| --- | --- |
| Tests depending on state or execution order | Isolate data and shared state per case, and clean up on completion and failure. Do not share identifiers or files during parallel execution |
| Decisions affected by time or randomness | Pass controllable clocks or random sources through boundaries to reproduce boundary values. Record reproducible seeds or inputs for random exploration |
| External connections | Isolate external boundaries in unit tests. Verify issues caused by actual connections, settings, or contracts through effective integration validation; do not achieve success by replacing target logic with mocks |
| Asynchronous UI | Use stable user-identifiable elements such as roles and labels and observable states. Use condition waits and failure-detecting timeouts, not longer fixed sleeps. Do not substitute communication completion for screen completion |
| Changes with performance acceptance conditions | First align agreed targets, loads, data volumes, measurement periods, and environments. Do not treat a single empty-DB measurement as representative-load achievement. Separate actual measurements from unverified scope |

When elapsed time itself is contractual, choose a clock and environment that verify that contract. Do not ban all waits or claim a controlled clock proves real-environment timing properties. Retain UI failure screens and traces as evidence for investigation; restrict recorded scope when confidential information is included.

For tests whose results vary under the same conditions, investigate order, state, time, environment, and other causes. Distinguish a successful retry from resolution of its cause. Follow dependency skill `change-delivery` for CI retries and recovery; do not uniformly defer required integration validation until after merge.

Do not make test-layer ratios, coverage, mutation scores, or response-time measurements for every API shared pass/fail conditions. Choose from target contracts, risks, and existing conventions. Do not add E2E or load tests to simple functions without UI or performance contracts.

Keep validation sources and adoption decisions in the [primary materials](sources.md).[^practice-sources]

[^practice-sources]: References and application decisions for Canon TDD, Continuous Testing, Architecture, and QA Engineering Best Practices; [Design by Contract adoption and limits](sources.md#adoption-decisions-for-design-by-contract).

### No tests of tests

Do not add or retain self-tests of an application's test cases, assertion helpers, acceptance runners, browser-test scripts, smoke checks, or diagnostic artifacts. Remove them rather than reducing them to representative cases or recreating them under another name. Keep actual application-facing checks and useful failure diagnostics. Ordinary TDD verification of the intended Red remains part of its feedback cycle; do not create a persistent suite of deliberately broken pages or runners to prove application tests fail. This application-testing rule does not prohibit testing a separately requested testing-tool product against its public contract.

Preserve required operational coverage wherever it lives, including CI directories: selecting a deployment matching a requested commit, propagating a required-check failure, and protecting security boundaries have meaningful inputs and results. Assert those outcomes, not the helper or exact `gh` command used to produce them. Distinguish these capabilities from self-validation of the application's test runner.

Remove unused callers, fixtures, fault-injection machinery, wrappers, and duplicate server/browser setup left by deleted self-tests. Prefer existing runner capabilities over custom orchestration; do not replace removed machinery with a new framework, policy-enforcement suite, or long shell/YAML replacement just to reduce JavaScript file counts.

Retain the smallest effective unit, integration, or browser coverage for each distinct required behavior. Do not translate every removed assertion into a browser test or prescribe counts, coverage quotas, or layer ratios. In the change record, state the chosen boundary, retained behavior, and obsolete assertions/support code removed; a lower test count alone proves neither improvement nor lost coverage.

### Reproducing and reporting defects

- Reflect defects found through exploratory or acceptance validation in the smallest reproduction test that detects the same problem quickly. Do not complete regression protection with manual rechecking alone.
- For defects involving domain decisions or contracts, check terminology, invariants, and existing features. Update missing or incorrect specifications before implementation. If already correct, retain them and add reproduction tests.
- Put concrete reproduction values in the selected test layer. Add them to features only when examples needed for shared understanding are missing. Record why unit tests cannot reproduce the issue and which integration validation is required.
- Verify failure caused by the target defect before the fix, success after the fix, and related acceptance validation. Do not claim automated tests alone prove user value; also use exploration, demos, and user feedback.
- If skill judgments also change, combine this with independent simulated evaluation. Do not require TDD for changes only to skill text.
- In the final report, show executed tests, Red and Green results, other validation, and unverified scope. Do not report unexecuted checks or inadequate environments as success.
