# Repository Instructions

## Validation policy

For changes to `daiksud/agents` itself, do not require the following validation as acceptance or completion conditions.

### APM validation

- Do not perform execution validation using APM CLI `install` or `compile`, actual deployment for Codex/Copilot, or reference resolution.
- Do not leave an Issue or PR incomplete solely because APM validation has not been performed.
- Static checks of `apm.yml`, skill placement, reference targets, and similar items may be performed as ordinary file review where needed. Do not treat these as completed APM execution validation.

### Independent validation

- Do not perform additional validation through another agent, another execution context, or independent simulated execution.
- Do not leave an Issue or PR incomplete solely because independent validation has not been performed.
- Ordinary PR review, required CI, and static Markdown, link, and reference validation are separate from independent validation and follow existing procedures.

APM validation or independent validation is in scope only when the user explicitly requests it for an individual task. Do not report validation that was not performed as completed.

## Change records

Apply [Change records](.apm/instructions/change-records.instructions.md) and the [PR template](.github/pull_request_template.md). Keep descriptions proportional: Summary, optional Decisions, and substantive Validation status (`Not run` is valid). Remove every HTML comment when creating/updating the actual description and check again during review and before merge. Preserve the final title/body as the squash message under `change-delivery`.

Keep current durable policy in topical `docs/engineering-policies/` documents and change-specific historical judgments in PRs/commits. See the [current change-record policy](docs/engineering-policies/change-records.md) for rationale. The validation exclusions above remain in force, alongside ordinary PR review and required CI.
