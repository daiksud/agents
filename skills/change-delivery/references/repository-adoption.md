---
type: Guide
title: Adopt repository change records
description: Connect decision-recording adoption to approved repository delivery.
---

## Adopt within the approved change

Use [decision-recording](../../decision-recording/SKILL.md) for the intended readers, recording boundaries, development practices, and repository-adoption guidance. Its [PR template](../../decision-recording/assets/pull_request_template.md), [local instruction example](../../decision-recording/assets/agents-decision-records.md), and [commitlint workflow](../../decision-recording/assets/commitlint.yml) are the reusable assets.

At the start of repository change work, inspect the target's local instructions, effective templates, current documentation, and existing adoption decisions. Accept equivalent arrangements and address confirmed gaps relevant to the approved work. Keep current rules in local files and adoption reasons in PR descriptions and commits. Do not repeatedly ask about a recorded deferral or block unrelated work on adoption.

Show concrete paths and changes before applying adoption. Deliver approved file changes through ordinary branch, PR, review, CI, and merge procedures. If adoption exceeds the approved scope, present the proposal and continue unaffected work. Installation alone does not copy assets, adopt rules, or apply GitHub settings.

## Preserve target conventions

For repositories adopting verbatim PR records, propose English PR bodies. Preserve explicit local choices, resolve language conflicts before publication, and retain the agreed text at merge without translation. This local language convention is separate from the independent skill's recording rules.

Adapt the instruction fragment and local links to the target. Keep consumer rules understandable without the installed agents package; do not copy this distribution repository's entire `AGENTS.md` or its APM/independent-validation exclusions.

## Apply settings in their authorized scope

Use the [GitHub settings guide](../../decision-recording/references/github-settings.md) for merge methods, message defaults, rule alignment, and the required `commitlint` check. When performing settings diagnosis or application under this environment's workflow, use [github-repo](../../github-repo/SKILL.md).

Record which settings were actually verified or applied. File adoption does not itself authorize live settings changes, and explicit merge messages do not establish that repository defaults changed. Preserve required approvals and CI throughout delivery.
