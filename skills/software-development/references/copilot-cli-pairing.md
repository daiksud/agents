---
type: Reference
title: Continuing Navigator use in Copilot CLI
description: Show launch and follow-up methods implementing common collaboration contracts in Copilot CLI.
---

## Continuing Navigator use in Copilot CLI

Follow common collaboration instructions for Driver/Navigator roles, edit permissions, shared ToDos, staged checks, stopping when initial launch is unavailable, and automatic re-pairing after losing continuity with launched Navigators. This material handles Copilot CLI-specific implementation.

Before the first Navigator request, read [Internal Driver/Navigator communication](agent-communication.md), using it under common collaboration contracts. In Copilot CLI, put initial sharing in `task` and later messages to the same Navigator in `write_agent` with the same `agent_id`. This material does not redefine communication formats or stop conditions.

For Navigators needing follow-up communication in GitHub Copilot CLI, launch the initial `task` with `mode: "background"`. Reserve `mode: "sync"` for requests completed in one response; even if `idle` appears afterward, do not assume they can receive `write_agent` messages.

Retain the returned `agent_id`, sending subsequent checks/feedback with `write_agent` to the same ID. Confirm processing by and responses from the same Navigator. Launch or state displays alone do not prove continuity; follow common stop conditions for failed resumption, lost history, and similar cases.

If the original `agent_id` becomes unreachable, pause subsequent code changes requiring checking under common instructions, and read [Handoff and rechecking after Navigator loss](navigator-recovery.md) before recovery/re-pairing. Investigate continuity through responses, available agent lists, and history. Once inability to continue is confirmed, without waiting for additional user confirmation stop new `write_agent` messages to the old ID and record its retirement. Launch a new `task` with `mode: "background"`, passing as much retrievable/retained work context and evidence as possible to the different `agent_id`. Confirm follow-up `write_agent` responses from that same new ID and complete recovery-material rechecks before resuming. Launch success or `idle` alone is not evidence. Follow common instructions prohibiting switching back to the old ID and automatically re-pairing after new-ID loss.

### CLI checking example

- 前提: Code changes need repeated checks from the same Navigator after its initial response.
- もし: The Driver launches the Navigator through GitHub Copilot CLI `task`
- ならば: The Driver launches with `mode: "background"`
- かつ: Subsequent `write_agent` is processed under the same `agent_id`, and that Navigator responds
- かつ: `mode: "sync"` responses or `list_agents` showing `idle` alone do not establish continuing communication
