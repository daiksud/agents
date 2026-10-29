---
type: Guide
title: Author current Engineering Policies
description: Maintain topical current policy while preserving change-specific historical judgment in PRs and commits.
---

## When to write a policy

For repositories adopting the [change-record model](../../../.apm/instructions/change-records.instructions.md), use `docs/engineering-policies/` for effective decisions that guide other parts of the repository or future changes. Local feature choices and bug fixes normally need only a concise PR description. Respect existing ADR conventions in repositories that have not adopted this model; package installation alone does not migrate their records.

## Content and revision

- Choose a stable topic filename such as `runtime.md`, rather than a selected product or numbered historical event.
- Describe the current choice and applicability, rationale, relevant alternatives, and trade-offs. Include assumptions and reconsideration conditions where they affect the decision; do not invent alternatives or analysis to fill sections.
- Revise the same topical document when policy changes. Keep historical adoption/replacement judgments in the respective PR descriptions and squash commits, self-contained enough to survive changes to living policy links.
- End the document with a link to the PR introducing or revising this version. Fill in the real PR number after creation and before merge; do not ship a placeholder.
- Follow ordinary document metadata and Markdown rules. Link operational rules from policy explanations and link explanations from maintainer navigation. Keep execution instructions reachable without requiring all maintainer notes.

For example, `runtime.md` can describe the current Bun choice and comparison with Node.js. Earlier Node.js adoption remains in its original PR/commit; switch reasons remain in the migration PR/commit. Update the current policy and its final PR reference together rather than appending a chronology.
