---
type: Guide
title: Author current policy
description: Write the effective guidance a new contributor needs, keeping decision history in commits.
---

## When to write a policy

Use [decision-recording](../../decision-recording/SKILL.md) to decide whether a change affects current working guidance. Write or update a document when a new contributor needs that information to work now. Use the repository's existing topical placement; neither `docs/engineering-policies/` nor the name Engineering Policies is required. An ordinary local fix may need only a concise PR record.

## Content and revision

- Describe the effective technology, specification, rule, responsibility, editable boundary, or procedure. Include current constraints that affect the reader's work.
- Revise the same topic when the policy changes. Put adoption/change reasons, comparisons, rejected alternatives, and chronology in the final self-contained PR body and commit message.
- Do not add superseded-policy sections, revision logs, adoption dates, or introducing/revising PR footers. Readers can inspect the file's Git history when they need the judgment behind a change.
- Follow the document's existing format and make current instructions discoverable. Update only affected guidance; do not require a policy file for every PR.

For example, `runtime.md` can state that the project uses Bun and show its effective commands. The reason for choosing Bun and any comparison with Node.js belong in the PR/commit that makes that choice.
