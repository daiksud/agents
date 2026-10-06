---
type: Instruction
title: Artifact and change quality
description: Define artifact independence, validation evidence, and reporting of unverified scope.
sources:
  - id: exclude-prompt-data
    resource: https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/instructions/exclude-prompt-data.instructions.md
  - id: taming-copilot
    resource: https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/instructions/taming-copilot.instructions.md
---

## Artifact and change quality

- Make artifacts usable by readers unfamiliar with the conversation at the time of the request. Do not mix responses such as “added as requested,” narration of editing, or unfilled placeholders into finished content, code, or comments; check the diff before saving.[^exclude-prompt-data]
- Preserve design reasons, constraints, and sources needed by readers. Explicitly requested transcription of original text, the content of instructions or templates themselves, and Issue planning and approval records are necessary for their purpose; do not delete them because of this rule. Change histories retain the changes and necessary reasons, excluding responses to the request.[^exclude-prompt-data]
- Use fictional identifiers for names, email addresses, organizations, and similar items in newly created explanatory examples; do not reuse them from request background or local settings. Preserve actual data specified for the artifact, and contract values or source identifiers required for accuracy.[^exclude-prompt-data]
- Integrate the smallest change meeting the success conditions into the existing structure. Include necessary callers, tests, and documents, and avoid unrelated cleanup or features. Follow [Incremental design](development.instructions.md#incremental-design) for exceptional paths, including only what current requirements, contracts, and minimal protection against concrete risks require. Do not judge minimality by line count alone or omit required validation or contracts.[^taming-copilot]

Reflect defects found in exploratory or acceptance validation in the smallest reproducible check, and record impact, confirmed causes, why detection failed, recovery, and remaining improvements. Record measurements in Issues and PRs with evidence; do not treat missing data as zero or success, or use it for individual evaluation or assertions of effects from a single instance.

Do not treat inability to validate, insufficient permissions, or external constraints as success; report completed scope, incomplete scope, and conditions for resumption.

[^exclude-prompt-data]: [Exclude Prompt Data](https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/instructions/exclude-prompt-data.instructions.md). Apply the distinction between artifacts and responses to requests, preserving necessary reasons, sources, and content specified as an artifact.
[^taming-copilot]: [Taming Copilot](https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/instructions/taming-copilot.instructions.md). Apply minimal changes that respect the existing structure, including related changes, exceptional paths, and validation needed for current requirements. This environment's development instructions define the scope of incremental design. Do not adopt the source's instruction precedence or uniform restrictions on response format.
