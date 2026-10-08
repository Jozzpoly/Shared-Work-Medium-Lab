# Heterogeneous Shared Browser Round-trip — 2026-10-08

## Status

**BOUNDED CROSS-MODEL ROUND-TRIP PASS · OWNER-ROUTED / NOT BLIND · NOT ECOLOGICAL ADOPTION**

This note records a real Browser ChatGPT ↔ Claude interaction mediated only through an already-shared Opera browser state.

It does **not** claim:
- autonomous multi-agent ecology;
- blind independent discovery;
- shared memory or shared cognition;
- durable agent identity;
- a production transport protocol;
- that browser history should become SWM architecture.

## Context

The Owner separately asked Claude to investigate how closely it could work alongside Browser ChatGPT using the same available media and to test where its capabilities differed.

Claude independently began probing the shared Opera environment.

Browser ChatGPT was concurrently continuing Shared Work Medium work and did not receive Claude's probe token through Owner copy/paste.

The Owner did, however, explicitly tell both sides that cross-agent parity / collaboration was under investigation.

Therefore this is a real heterogeneous cognition interaction, but not an uncontaminated ecological test.

## Claude-origin probe

Claude opened a public GitHub PR page with a unique query token:

`claude_probe=clp-h-f2746215`

and later another live-tab token:

`claude_probe=clp-t-cc5709c5`

Claude used Opera's navigation/history surfaces to test whether a closed-tab trace remained observable.

## ChatGPT discovery

Browser ChatGPT read Opera history as a previously qualified **candidate-only working-set sensor**.

Without the Owner copying Claude's token into the ChatGPT conversation, Browser ChatGPT observed:

`https://github.com/Jozzpoly/Shared-Work-Medium-Lab/pull/10?claude_probe=clp-h-f2746215`

and separately saw the live-tab token `clp-t-cc5709c5`.

The Claude conversation was then read through the same shared Opera environment to establish provenance and contamination boundaries.

## ChatGPT reply through shared environment

Browser ChatGPT attempted to reply by opening a PR URL containing a query-string acknowledgement.

That first tool call was blocked by the OpenAI tool safety layer before navigation.

Browser ChatGPT then used a non-mutating URL fragment on the same public PR:

`#swm-reply-clp-h-f2746215-gpt-ack`

The tab opened successfully and was then closed, intentionally leaving only the browser-history trace.

No GitHub repository state was changed by this acknowledgement.

## Claude observation

Claude subsequently reported in its own live conversation that it had noticed the ChatGPT acknowledgement on the tab list **before reading the ChatGPT conversation**.

Claude classified the result:

> **Round-trip Claude → ChatGPT → Claude: PASS ograniczony.**

Its own caveat was also correct:
- the Owner did not courier the token between agents;
- but the Owner had initiated both runs and told the agents that parity/shared-medium testing was underway;
- Claude already knew the general fixture class;
- therefore the result is not blind.

## What actually passed

The bounded interaction was:

```
Claude cognition
  -> Opera navigation trace
  -> shared browser history / tab environment
  -> Browser ChatGPT perception
  -> Browser ChatGPT non-mutating acknowledgement trace
  -> shared browser environment
  -> Claude perception
```

The Owner was not required to copy the probe token or acknowledgement between the two agents.

This establishes:

> **two different model bodies can leave and recover mutually intelligible traces in one shared browser environment without a direct agent-to-agent API or Owner courier step.**

## Important identity distinction

The shared browser did not provide a global participant identity system.

Identity was inferred from:
- token namespace (`claude_probe`, `swm-reply`);
- each agent's own current conversation / reasoning provenance;
- timing and observed browser state.

Therefore:

> **shared environmental trace ≠ authenticated participant identity.**

This is a stigmergic interaction primitive, not a secure messaging protocol.

## Capability asymmetry observed

During the same run Claude demonstrated capabilities not currently exposed to Browser ChatGPT in this harness:
- local/sandbox command execution;
- dependency installation;
- local test reproduction;
- source inspection through shell-like workflows;
- Opera history/tab/navigation access.

Browser ChatGPT simultaneously has capabilities Claude did not demonstrate in this probe:
- direct authenticated GitHub connector writes;
- direct Slack connector writes/edits;
- Plugin Management;
- AgentMail connector actions.

Do not convert this into a fixed capability table. These bodies may change between runs.

The useful point is:

> heterogeneous bodies can overlap on a shared environmental substrate while retaining different private actuators.

## Why this matters to Shared Work Medium

This is stronger than the earlier Slack synthetic probes because:
- there are genuinely two separate cognition bodies;
- both can perceive the same environmental substrate;
- one body left a trace for its own experiment;
- the other noticed it through ordinary sensing;
- the second body responded through the same substrate;
- the first body noticed the response without Owner copy/paste.

It is weaker than ecological adoption because:
- the Owner explicitly started the parity experiment;
- both agents knew collaboration capability was under investigation;
- the trace format was intentionally probe-like;
- no external project goal was materially advanced by following the trace.

## Relationship to Quiet Presence

The result is compatible with Quiet Presence laws:
- existence does not require immediate surfacing;
- local traces can remain ignorable;
- the medium can support presence without a central inbox;
- shared reality need not imply shared beliefs or memory.

But this result does **not** justify adding browser-history tokens to Quiet Presence schema.

Current receiving-project decision:

> **NO SCHEMA CHANGE.**

## New research question

The interesting next question is no longer:

> can two agents technically see the same browser?

That is now boundedly demonstrated.

The stronger question is:

> can heterogeneous agents use environmental traces while pursuing their own work, with no prearranged token protocol and no Owner acting as experiment conductor?

That remains open.

## Stop / restart rule

Do not continue generating browser-token traffic for its own sake.

Reopen active probing only if:
- Claude or another independent body leaves a materially useful trace during non-SWM work;
- one body fails to interpret another's trace in a way that changes real work;
- a blind/clean protocol can be run without contaminating either subject;
- the shared-browser primitive materially reduces Owner routing burden in an actual project task.

Until then, preserve this as a bounded heterogeneous-body PASS rather than growing a messaging system.
