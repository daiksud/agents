---
type: Guide
title: Attested Computation contracts and verification
description: Distinguish computation definitions, permitted parameters, definition verification, and execution attestation.
---

## When to write a contract

Use a separate concept with `type: Attested Computation` when it is necessary to verify that a value was obtained through an approved computation method. Reference it from metric explanations through ordinary Markdown links; do not pack multiple computations into one frontmatter. OKF records definitions and verification methods; it is not an execution platform.

| Field | What the contract clarifies |
| --- | --- |
| `runtime` | Required for this type. Examples: `bigquery`, `dbt`, `python`. Determines parameter binding |
| `parameters` | List of declared holes, each with `name`, `type`, and `required`. The value provider does not alter the definition |
| `computation` | Reference when stored in a separate file. If omitted, one code fence under `# Computation` in the body |
| `executor.resource` | Reference to execution procedures or code |
| `executor.receipt` | Evidence fields returned by execution and what verification uses |
| `attester.resource` | Reference to deterministic code that inspects receipts and decides. Do not use LLM judgment as an attester |

Field roles follow specification §§10.2–10.3. Do not uniformly treat omission of fields other than `runtime` as Bundle nonconformance; separately check whether the contract is usable.

The following is a contract format example, not evidence that computation, execution procedures, or an attester are implemented. Document it after establishing the target authoritative source and real references.

```yaml
type: Attested Computation
title: Approved aggregation by fiscal year
description: Execute an approved computation with a fiscal-year parameter.
runtime: bigquery
parameters:
  - { name: year, type: integer, required: true }
computation: ../references/computations/annual.sql
executor:
  resource: ../references/run-annual.md
  receipt: [job_id, executed_sql, result]
attester:
  resource: ../references/attesters/annual.py
```

Resolve paths from the contract file's location. Do not make both a `computation` file and a body computation fence authoritative. If required capabilities or real references are missing, explicitly mark it unimplemented. Do not introduce cloud connections or runtimes solely on this skill's authority.

## Validate Markdown together with the contract

When placing computation definitions in the body, include both `title` and the body's `# Computation`. Default rumdl MD025 counts frontmatter title as an H1, so add the following setting only for computation documents. `front-matter-title = ""` treats frontmatter separately while retaining checks for duplicate body H1s. This is a local choice based on rumdl 0.2.69 configuration definitions; do not apply it to ordinary concepts or GitHub posts.

```sh
rumdl check --config /path/to/rumdl.toml --config 'MD025.front-matter-title = ""' --deny-config-warnings /path/to/computation.md
```

Add `--fix` with the same configuration when formatting. For multiple files, run computation documents separately from others. When fixing duplicate body H1s, retain the specification's `# Computation` and check its code fence. Cross-check computation definitions and reference contents; rumdl success alone is not contract validation.

## Specifying values and changing definitions

Agents using a computation may specify only declared parameter values, not create or rewrite arbitrary SQL. The consumer constructs the bound execution artifact; the attester independently reconstructs the same binding and compares it with the actual artifact.

A request to change the computation definition is separate from a request to obtain values. Follow existing authoritative sources, approval, and review. Do not mix definition changes into runtime “adjustments” or recreate definitions merely upon receiving an execution request.

## Definition verification and attestation of one execution

`verified` is document-level confirmation that a definition conforms to policy; attestation proves that the specified computation occurred in one execution. Execution attestation can succeed even for an expired definition, and fresh definition verification does not remove the need to attest each execution.

When documenting verification procedures, clarify the following.

1. Read the computation definition version, runtime, declared parameters, and values.
2. Define evidence returned by the executor and a trusted execution destination from which to obtain it.
3. Check how the attester compares the bound computation with actual execution.
4. Verify displayed values against authoritative execution results without relying solely on text returned by an agent.
5. Define how to show failure decisions to users without hiding them, together with expiration and trust states.

This execution procedure model is based on informative §10.5. Receipt and verdict wire formats, attester ABI, sandbox, and cache are unspecified in v0.2; this environment does not fill them in as a shared runtime. Receipts and decisions are runtime artifacts; do not embed them in Bundle frontmatter.

## Check attester evidence and limits

Do not claim that a sample's successful SQL or displayed-value comparison proves parameter correctness, actual job execution, or result authenticity. Inspect parameter validation, binding reconstruction, and retrieval of authoritative execution results for the chosen attester. Do not assume comment or whitespace normalization preserves SQL semantics, including string literals, or unconditionally reuse reference code as a production attester. Check evidence acquisition, comparison targets, and failure conditions for each contract.
