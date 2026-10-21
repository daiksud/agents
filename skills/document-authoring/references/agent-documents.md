---
type: Instruction
title: Separate execution guidance from maintainer notes
description: Keep Instructions and Skills focused on execution while preserving their provenance and maintenance context outside ordinary task loading.
---

## Place content by its use

When authoring or reorganizing agent Instructions and Skills, ask whether the content changes the agent's next decision, action, or completion judgment.

| Content | Placement and reading condition |
| --- | --- |
| Purpose, applicability, required behavior, constraints, permissions, stopping and completion conditions | Instruction or skill entry point; retain the rules needed to select and start the work |
| Detailed procedures, task-relevant definitions, examples, schemas, commands, and recovery steps | The skill's operational references; link from the entry point with a specific task or stage that requires reading them |
| Source catalogs, citation-only metadata and footnotes, adoption rationale, research/checking history, and maintenance-only evaluation notes | Human-facing `docs/` material; consult when maintaining the guidance or investigating its origin |

Length and a directory name alone do not decide placement. An example that teaches a required response, an equation needed for a judgment, or a limitation affecting safe execution belongs with the operational guidance. Keep the minimum context needed to use it correctly. Move explanatory history and supplementary comparisons when they do not affect execution.

## Preserve meaning while separating

- Read complete source sections before moving them. Extract any actual rule embedded in a footnote or adoption note into the appropriate operational document before moving the rest.
- Preserve triggers, permission boundaries, requirements, exceptions, and success conditions. Moving a rule must not turn it into optional background or create another approval gate.
- Keep source IDs, URLs, relevant versions, source-to-guidance mappings, and prior checking records in the maintainer note. Preserve unknown metadata with its owning content. Do not present relocation as new research or verification.
- Keep direct official lookup URLs where the task needs them, and preserve required license or attribution notices. Source-handling examples may remain when they teach a format the agent must produce.
- Keep evidence and citations required in user-facing outputs. This separation concerns the guidance's own provenance; it does not exempt the resulting document, analysis, Issue, or PR from its evidence requirements.

## Connect and maintain the documents

Make human notes discoverable from the repository README or documentation navigation, and link each note back to the operational files or sections it explains. Do not add a blanket instruction to read the human notes, import their contents, or duplicate their bibliography in every entry point.

Keep operational references within the supported skill/package layout and use file-relative links. Do not make normal execution depend on maintainer documents being installed. Follow the target platform's required metadata format.

When changing guidance, update affected source mappings and maintainer explanations in the same change. Check incoming links, conditional read routes, missing rules, and the final diff. Measure file-text changes separately from actual loaded context or token usage; do not claim runtime savings without measurement.
