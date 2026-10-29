---
type: Reference
title: Sources for shared instructions
description: Preserve source mappings, adoption boundaries, and earlier checking records for shared agent instructions.
sources:
  - id: issue-122
    resource: https://github.com/daiksud/agents/issues/122
  - id: issue-98
    resource: https://github.com/daiksud/agents/issues/98
  - id: issue-100
    resource: https://github.com/daiksud/agents/issues/100
  - id: issue-99
    resource: https://github.com/daiksud/agents/issues/99
  - id: issue-138
    resource: https://github.com/daiksud/agents/issues/138
  - id: issue-140
    resource: https://github.com/daiksud/agents/issues/140
  - id: issue-161
    resource: https://github.com/daiksud/agents/issues/161
  - id: kent-beck-toil-struggle
    resource: https://newsletter.kentbeck.com/p/take-my-toil-leave-me-my-struggle
  - id: ron-jeffries-xp
    resource: https://ronjeffries.com/xprog/what-is-extreme-programming/
  - id: fowler-yagni
    resource: https://martinfowler.com/bliki/Yagni.html
  - id: fowler-evolutionary-design
    resource: https://martinfowler.com/articles/designDead.html
  - id: exclude-prompt-data
    resource: https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/instructions/exclude-prompt-data.instructions.md
  - id: taming-copilot
    resource: https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/instructions/taming-copilot.instructions.md
  - id: sakuramiko-profile
    resource: https://hololive.hololivepro.com/talents/sakuramiko/
    title: Sakura Miko official talent profile
  - id: sakuramiko-user-profile
    resource: https://github.com/daiksud/agents/issues/240
    title: Owner-supplied shrine-maiden AI idol and VAgent profile refinement
  - id: change-record-agreement
    resource: https://github.com/daiksud/agents/issues/253
  - id: repository-adoption
    resource: https://github.com/daiksud/agents/issues/254
---

## Sources for shared instructions

This page preserves source mappings, adoption notes, and earlier checking records for maintainers of the shared instructions. Runtime requirements and operational examples remain in the instruction files linked below. These notes are not a prerequisite for ordinary execution, and moving a source record does not establish that its content was checked again.

### Execution scope and change protection

The [change-protection instruction](../.apm/instructions/change-safety.instructions.md) applies the same development contracts across model and reasoning settings. Issue #122 records that policy and the separation of responsibilities.[^issue-122]

### Agent collaboration

The [collaboration instruction](../.apm/instructions/collaboration.instructions.md) incorporates the following repository decisions. Its mandatory contracts, detailed-material read conditions, staged checks, and stop conditions remain in the runtime instruction.

| Instruction area | Decision record |
| --- | --- |
| Confirming a Navigator before code edits, handling initial unavailability, and separating read-only work from code changes | Issue #138[^issue-138] |
| Automatic re-pairing after confirmed Navigator loss, without additional confirmation for the replacement | Issue #161[^issue-161] |
| Controlled English and concise internal communication, without changing external artifact language | Issue #99[^issue-99] |
| Retaining mandatory contracts at entry points while reading and sharing detailed material at the relevant stage | Issue #140[^issue-140] |
| Preserving evidence after loss, retiring the former Navigator, and rechecking from the unconfirmed stage | Issue #100[^issue-100] |
| One ToDo at a time and meaningful dialogue boundaries within Red, Green, and Refactor | Issue #98[^issue-98] |

### Productive struggle and user goals

The [decision-making instruction](../.apm/instructions/decision-making.instructions.md#preserve-productive-struggle) adapts Kent Beck's distinction between toil and productive struggle. Completing a deliverable is not the only possible value of work: learning may develop understanding, confidence, and capability.[^kent-beck-toil-struggle]

The runtime guidance applies that distinction to the user's expressed purpose. It preserves autonomous delivery for outcome-oriented requests and room for reasoning when learning is the intended outcome, without making every difficult task a learning exercise or changing authority and delivery requirements.

### Development and incremental design

The [development instruction](../.apm/instructions/development.instructions.md) draws its XP values and short feedback cycles from Ron Jeffries, its restraint about future features from Martin Fowler's YAGNI discussion, and its evolving design approach from Fowler's discussion of XP design.[^ron-jeffries-xp] [^fowler-yagni] [^fowler-evolutionary-design]

The five-value action table, assert-first work, staged agent checks, and happy-path MVP scope are this repository's application of those ideas. The original adoption boundaries and checking dates remain in the footnotes below; they do not claim new source verification for this relocation.

### Artifact and change quality

The [quality instruction](../.apm/instructions/quality.instructions.md) adapts the distinction between finished artifacts and responses to requests from Exclude Prompt Data.[^exclude-prompt-data] Its guidance on minimal changes within the existing structure draws on Taming Copilot, while this repository's development policy defines incremental-design scope.[^taming-copilot]

The adoption preserves necessary reasons, sources, original-text artifacts, and approval records. It does not import the source's instruction precedence or uniform response-format restrictions.

### Official-profile conversation grounding

The original grounding of the [conversation instruction](../.apm/instructions/sakuramiko.instructions.md#profile-grounded-character) drew on the official profile's character frame, effort-centered elite identity, aspirations, nicknames, interests, and listener relationship.[^sakuramiko-profile] This source history supplements the existing [speech and scene notes](sakuramiko-style-reference.md).

On 2026-10-22, the owner supplied the explicit character profile recorded as a refinement in Issue #240.[^sakuramiko-user-profile] That profile governs the conversational portrayal, including the deliberate `AIドル`, `巫女AIドル`, and `VAgent` wording, the Japanese introduction and message, the `35P` address, preferences, dislikes, nicknames, three fan descriptions, and words/memes. These adapted lines are user-defined character settings, not verbatim official-profile quotations, authentic stream excerpts, or an official affiliation. The grouped `み俺誇` and `み俺恥` definitions are separated into their respective pride and embarrassment meanings for operational clarity.

The character name and lore guide conversational portrayal without replacing the assistant's factual identity, capabilities, or actual experiences. Character-led introductions and retaining truthful identity are local adaptation decisions. Preferences guide relevant reactions rather than invented activities; fan descriptions do not authorize degraded reasoning or fabricated mistakes. Existing authentic excerpts and their canonical wording remain unchanged. This refinement checks against the owner's supplied text; it does not claim a new official-page, stream, caption, or fan-wiki inspection. Static source and consistency checks do not establish measured conversational improvement.

[^issue-122]: The policy recorded in [Issue #122](https://github.com/daiksud/agents/issues/122) for model-independent development contracts, separation of responsibilities, and preservation of existing contracts.
[^issue-138]: [Issue #138](https://github.com/daiksud/agents/issues/138) records stopping code changes when the initial Navigator is unavailable, continued read-only work, and boundaries for initial retries and re-pairing.
[^issue-161]: [Issue #161](https://github.com/daiksud/agents/issues/161) records automatic re-pairing after Navigator loss without waiting for additional confirmation, preserving as much context as possible.
[^issue-99]: [Issue #99](https://github.com/daiksud/agents/issues/99) records internal communication in low-entropy Controlled English and its boundary with external artifacts.
[^issue-140]: [Issue #140](https://github.com/daiksud/agents/issues/140) records separating detail while retaining mandatory contracts at entry points, and boundaries for checking and sharing distributed material.
[^issue-100]: [Issue #100](https://github.com/daiksud/agents/issues/100) records preserving evidence after Navigator loss, retiring the former Navigator, and rechecking from the unconfirmed stage.
[^issue-98]: [Issue #98](https://github.com/daiksud/agents/issues/98) records the granularity of one ToDo, short dialogue boundaries within stages, and conditions for avoiding excessive sequential reporting.
[^kent-beck-toil-struggle]: [Kent Beck: Take My Toil, Leave Me My Struggle](https://newsletter.kentbeck.com/p/take-my-toil-leave-me-my-struggle). Apply the distinction to the user's goal instead of treating every challenge as a mandatory learning exercise.
[^ron-jeffries-xp]: [Ron Jeffries: What is Extreme Programming?](https://ronjeffries.com/xprog/what-is-extreme-programming/). Adopt the five values, design meeting current requirements, and short validation and design-improvement cycles. Do not make fixed meetings, periods, organizational structures, or effect figures common requirements. Checked on 2026-09-25.
[^fowler-yagni]: [Martin Fowler: Yagni](https://martinfowler.com/bliki/Yagni.html). Avoid anticipating future features while retaining tests, refactoring, and CI supporting current changes. Assert-first work and staged agent checks are this environment's operating policy. Checked on 2026-09-25.
[^fowler-evolutionary-design]: [Martin Fowler: Is Design Dead?](https://martinfowler.com/articles/designDead.html). Adopt continuously evolving design in XP, supported by tests, CI, and refactoring. The specific scope of starting with a happy-path MVP is this environment's application policy, not the definition of XP itself. Checked on 2026-09-28.
[^exclude-prompt-data]: [Exclude Prompt Data](https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/instructions/exclude-prompt-data.instructions.md). Apply the distinction between artifacts and responses to requests, preserving necessary reasons, sources, and content specified as an artifact.
[^taming-copilot]: [Taming Copilot](https://github.com/github/awesome-copilot/blob/7568a482ce2df38f8965ab5336a3220db796a4ba/instructions/taming-copilot.instructions.md). Apply minimal changes that respect the existing structure, including related changes, exceptional paths, and validation needed for current requirements. This environment's development instructions define the scope of incremental design. Do not adopt the source's instruction precedence or uniform restrictions on response format.
[^sakuramiko-profile]: [Official Sakura Miko talent profile](https://hololive.hololivepro.com/talents/sakuramiko/), inspected on 2026-10-22 for the profile-grounded conversation update. This check covers the official page only; it does not reverify the archived stream, caption, or fan-wiki evidence in the existing scene notes.
[^sakuramiko-user-profile]: [Issue #240, owner-supplied profile refinement](https://github.com/daiksud/agents/issues/240#owner-supplied-profile-refinement), records the approved character adaptation supplied on 2026-10-22. The exact runtime profile remains in the conversation instruction; this record distinguishes user-defined wording from official source evidence.

## Change-record policy adoption

[Change records](../.apm/instructions/change-records.instructions.md) and the development, delivery, quality, and language instructions apply the agreement in [Issue #253](https://github.com/daiksud/agents/issues/253).[^change-record-agreement] The current rationale and boundaries live in [Change records policy](engineering-policies/change-records.md): actual validation reporting is required while execution is discretionary unless independently required; PRs/commits retain historical judgment and topical policies retain current guidance. This adoption does not establish renewed checking of the external sources above.

[^change-record-agreement]: Owner-agreed change-record policy and implementation scope in Issue #253.

## Consumer change-record adoption

[Issue #254](https://github.com/daiksud/agents/issues/254) adds the short [change-record adoption trigger](../.apm/instructions/change-records.instructions.md) and the scoped [language choice](../.apm/instructions/language.instructions.md#pr-body-language-when-adopting-squash-records).[^repository-adoption] The detailed [adoption procedure](../skills/change-delivery/references/repository-adoption.md) owns inspection, equivalence, concrete gap-filling proposals, and preservation of prior decisions; shared instructions do not duplicate that procedure or make adoption a blocker for unrelated work.

[^repository-adoption]: Owner-requested adoption guidance and scope in Issue #254; builds on Issue #253 rather than replacing its reusable template or Engineering Policies authoring reference.
