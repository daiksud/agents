---
type: Guide
title: Developer documentation practices
description: Plan, draft, review, and maintain technical prose around the reader's task.
---

Apply the relevant practices to the current change. Preserve existing formats, source handling, language rules, and publication permissions from [document-authoring](../SKILL.md).

## Contents

- [Understand the reader and task](#understand-the-reader-and-task)
- [Choose content by purpose](#choose-content-by-purpose)
- [Draft for finding and using information](#draft-for-finding-and-using-information)
- [Make examples and visuals useful](#make-examples-and-visuals-useful)
- [Review task completion before presentation](#review-task-completion-before-presentation)
- [Maintain documentation with the product](#maintain-documentation-with-the-product)

## Understand the reader and task

Before substantive writing, identify the reader, relevant prior knowledge, intended task or decision, and what successful use of the document would look like. Distinguish users, operators, and contributors where their tasks differ. Check existing Issues, maintained documentation, and available feedback; do not assume the reader knows what the implementer knows.

Keep this reasoning in the current plan or working notes. Do not require a separate persona, survey, interview, or planning file for every edit. Treat inferred needs as assumptions, and resolve gaps that materially change the document's purpose through existing clarification procedures. Research needs do not authorize contacting people or disclosing private material.

## Choose content by purpose

Plan needed content and content types before drafting. Use the following local completion criteria where applicable; they are not a mandatory file taxonomy or required sections for every page.

| Reader's need | Content and completion criteria |
| --- | --- |
| Decide whether to use the project | README or overview: purpose, relevant capabilities, prerequisites, a first-use path, and links to deeper guidance |
| Learn through a first successful use | Getting-started guide or tutorial: bounded outcome, prerequisites, a complete path, expected result, and next step |
| Complete a specific task | Procedure: starting state, ordered actions, verification, and relevant recovery or cleanup |
| Understand a model or make a decision | Concept explanation: terminology, relationships, rationale, constraints, and relevant tradeoffs |
| Look up an exact contract | Reference: consistent entries checked against authoritative code or specifications, including relevant defaults, constraints, and failures |
| Recover from a problem | Troubleshooting: recognizable symptom, diagnostic evidence, corrective action, and success check |
| Adopt a changed version | Release or migration guidance: affected behavior and versions, user impact, and necessary action |

Keep entry points short enough to navigate. Link to the authoritative explanation instead of copying detailed contracts into multiple guides. Preserve established paths; separate audiences or purposes only when it improves use, without forcing one new file per row.

## Draft for finding and using information

1. State the outcome and relevant scope early. Build headings from the reader's questions or actions.
2. Complete the necessary explanation or one working path before polishing individual sentences. Resolve gaps before publication, or disclose them without presenting an incomplete path as usable.
3. Put prerequisites before dependent actions and consequential cautions before the affected step. Use numbered steps when order matters.
4. Give alternative methods, platforms, or interfaces separate paths. Explain how to choose without interleaving incompatible instructions.
5. Use focused paragraphs, descriptive headings and links, lists, and tables for their actual relationships. Preserve terminology and define unfamiliar terms when needed.

For example, an original outline for a contributor setup guide could be: supported environment, install dependencies, run the smallest relevant check, recognize success, and resolve common setup failures. Include only steps supported by the repository; this example does not prescribe commands or tooling.

## Make examples and visuals useful

Apply these checks to keep examples useful and consistent with the product:

- State whether a sample is runnable or an illustrative fragment. Include necessary setup, inputs, and expected results, and explain substitutions. Keep copyable commands separate from prompts and output.
- Match actual identifiers, options, and defaults to the supported version. Reuse maintained examples or generated references when suitable; do not establish another manually maintained contract by accident.
- Verify changed runnable examples when feasible and authorized, using an isolated or read-only setting. Do not run destructive or external operations merely to validate prose. Distinguish execution results from static inspection and illustrative output in the existing validation report.
- Use a diagram, table, or screenshot when it explains a relationship, decision, or state more clearly. Include the explanation needed to interpret it, and keep essential instructions available as text. Respect the existing asset policy.

## Review task completion before presentation

Review whether the document enables the reader to complete the task before polishing its expression and structure:

1. Can the intended reader find the information and complete the task or decision? Check missing prerequisites, accuracy, necessary context, and observable results against actual evidence.
2. Is the explanation clear, concise, and consistent? Remove detours and ambiguous wording while preserving conditions and meaning. Apply `yomiyasu` to Japanese prose through the existing language-routing instruction.
3. Apply [Markdown and content checks](validation.md). A clean lint result does not establish usability or technical correctness.

For new or materially changed onboarding and procedures, walk the documented path when feasible and authorized. Capture useful friction briefly as `step / expected / observed / obstacle / next action` in existing notes or an Issue. This is a local recording aid, not a mandatory new artifact. Do not invent observations or claim that an agent walkthrough establishes real-user success. If execution is unavailable, inspect the sequence and state the limitation.

Distinguish an explanation gap from a product defect. Fix the document within scope; route product changes through the responsible workflow. These checks do not authorize extra independent validation or replace ordinary PR review.

## Maintain documentation with the product

- When behavior changes, find affected guides, references, examples, and navigation, and update them in the same approved change where appropriate. Use existing ownership and release workflows.
- When moving or retiring content, check incoming links and supported-version needs. Choose an updated destination, a clearly scoped historical/deprecated page, or removal according to the actual need; do not silently erase still-supported instructions.
- Triage feedback for validity, actionability, and importance. Use existing reporting channels and distinguish documentation, support, and product issues.
- For an actual improvement question, use available evidence tied to the reader's task, such as observed completion, repeated setup questions, or failed searches. State observation limits; page views or time on a page alone do not establish success. Do not add tracking infrastructure, recurring reviews, or a new approval gate by default.
