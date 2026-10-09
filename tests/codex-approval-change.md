## Change

Replace the approval policy introduced in #197 with the simpler policy explicitly approved by the requester.

- Trigger only on created or edited Codex Review Summary comments from `chatgpt-codex-connector[bot]` on PRs.
- Require both Code Review and Security Review to be `Completed`, plus Codex's thumbs-up on the PR body.
- When only the thumbs-up is missing, check immediately and retry up to six times with 30-second waits. Reread the Summary on every retry; stop if either review becomes incomplete.
- Remove approval withdrawal, approval HEAD checks, eyes checks, history reconciliation, and manual/lifecycle review triggers. Preserve CI's existing Draft/Ready operations and their separate eligibility guards.
- Update the native shell regression tests and README. The workflow shrinks from 121 to 75 lines without moving code to another production file.

## Verification

The delayed-thumbs-up regression failed against the original workflow. All 12 updated shell scenarios pass locally, covering immediate/delayed approval, the final retry, timeout, each incomplete or restarted review, and API/approval failures. YAML parsing and Bash syntax checks pass; the reusable CI job and input definitions are unchanged.

Local checks use fixtures at the `gh` and `sleep` boundaries, not live approval requests. Required GitHub CI and ordinary external review remain delivery requirements. No APM execution or additional independent simulated validation is performed.

## Accepted limits

This policy deliberately does not establish that the latest commit was reviewed. Older completed evidence and an existing thumbs-up can approve newer code before Codex publishes updated status. Existing approvals are never withdrawn by this workflow. The polling budget is six 30-second waits; API request time is additional. A later Summary creation or edit is needed after the polling window ends.
