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
