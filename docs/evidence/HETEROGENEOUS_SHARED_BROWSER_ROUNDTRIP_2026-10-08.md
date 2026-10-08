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

Claude began probing the shared Opera environment while following the pre-existing heterogeneous-browser fixture and the Owner's parity instruction. The specific open→close→history Probe 0 was **not invented independently by Claude**; it was executed from the existing fixture.

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

The run showed meaningful overlap as well as asymmetry.

Observed overlap:
- both bodies had web-research capability;
- both bodies had sandbox/code-execution-class capability in their current product surfaces;
- both bodies had the same Opera history/tab/read/navigation surface.

Browser ChatGPT additionally had authenticated action surfaces that Claude did not demonstrate in this probe:
- direct GitHub connector writes;
- direct Slack connector writes/edits;
- Plugin Management;
- AgentMail connector actions.

Claude demonstrated its own sandbox workflow with package installation, local test reproduction and source inspection, but this experiment did **not** perform a controlled sandbox/network parity comparison against Browser ChatGPT.

Do not convert this into a fixed capability table. These bodies may change between runs.

The useful point is:

> heterogeneous bodies can substantially overlap while still exposing different authenticated/private actuators and different effective workflows.

## Why this matters to Shared Work Medium

This is stronger than the earlier Slack synthetic probes because:
- there are genuinely two separate cognition bodies;
- both can perceive the same environmental substrate;
- one body executed an existing shared-browser probe and left a trace;
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

## Claude red-team corrections

After the round-trip, Claude independently reviewed the situation and corrected several overclaims/hidden assumptions.

### Probe origin correction

Claude explicitly noted that the open-tab → close → history test was taken from the existing heterogeneous-browser fixture. Therefore the result is **execution by an independent cognition body**, not independent invention of the primitive.

### Conversation isolation is false in this setup

Both agents can read the other's conversation tab through the shared Opera accessibility surface when that tab is open.

Therefore:

> **separate cognition contexts != private contexts in the shared-browser session.**

This materially contaminates any experiment that assumes the agents cannot inspect each other's reasoning/messages.

### Browser history has a privacy/selection boundary

Claude observed that the Opera history tool cannot be narrowed below its supported time-window semantics in this session and that the returned history can include URLs carrying sensitive OAuth-style query parameters.

Browser ChatGPT had independently observed the same broad-history phenomenon while using history as a working-set sensor.

Therefore:
- history remains useful as a candidate generator;
- it is **not** a clean selective mailbox;
- agents should avoid copying unrelated URL parameters into durable evidence;
- experiments that require privacy or strict information isolation need separate profiles/sessions or a different substrate.

### Revised strength of the PASS

The defended claim is now:

> **Two distinct cognition bodies, sharing one browser session and knowingly participating in a parity experiment, successfully completed a non-mutating trace/acknowledgement round-trip without Owner copy/paste.**

Do not upgrade this to:
- blind discovery;
- private independent contexts;
- authenticated messaging;
- ecological adoption;
- spontaneous invention of the trace primitive.

The correction itself is useful evidence: the second body did not merely consume the interaction; it materially narrowed the first body's claim.

## Receiving-project check — Claude's ReflexBrain observation

During the parity run Claude independently noticed that a green ReflexBrain CI run did not imply scientific PASS.

Source-native verification by Browser ChatGPT confirmed:
- the P01a test intentionally allows scientific PASS/FAIL/INCONCLUSIVE while enforcing execution validity;
- the result document explicitly records **SCIENTIFIC FAIL · EXECUTION VALID · RUN CLOSED**;
- one held-out case violates the frozen immediate-timing rule;
- the parent current-state document also preserves P01a as scientific FAIL and forbids retroactive threshold repair.

Receiving-project decision:

> **NONE — correct independent observation, but no missing ReflexBrain truth and no routing need.**

This is useful evidence that a heterogeneous body can independently detect a real epistemic distinction, while the receiving-project gate still prevents duplicate traffic.

## Security / privacy stop-rule for shared-browser traces

The same run exposed a stronger substrate boundary.

Observed:
- both agents can inspect the other's open conversation tab through the shared Opera accessibility surface;
- Opera history in this body returns a broad history window rather than a narrowly scoped project stream;
- returned URLs may contain unrelated session-adjacent or sensitive metadata;
- the tool does not provide a per-agent privacy partition for history reads.

Therefore:

> **shared Opera state is qualified as a powerful co-presence / candidate substrate, but NOT as a safe general-purpose agent message bus in the current shared profile.**

Immediate research posture:
- stop using full browser history for deliberate agent-to-agent messaging in this profile;
- do not copy unrelated history URLs or sensitive URL metadata into durable evidence;
- prefer source-native public objects or narrowly scoped non-sensitive live-tab traces when a bounded experiment genuinely needs them;
- any blind/private heterogeneous-agent experiment requires stronger isolation, such as separate profiles/sessions or another substrate.

The successful round-trip remains evidence of capability. The privacy boundary prevents promoting that capability into architecture.

## Independent re-validation case — ReflexBrain P01A

During the same heterogeneous run, Claude independently noticed that a green GitHub Actions check could coexist with a logged scientific `FAIL` in ReflexBrain.

Browser ChatGPT then verified the claim directly from source-native evidence:

- PR #14 head: `4f8e2d92d2efc5676a34cf6dc069667f3e85083b`;
- workflow run #548 / job `112550470392`: conclusion `success`;
- the same job log contains:
  - `P01A_RESULT {"outcome":"FAIL", ...}`;
  - H2 failing the frozen `contact+1` timing criterion;
  - Vitest reporting all 8 tests passed;
- the exact test intentionally asserts that outcome is one of `PASS | FAIL | INCONCLUSIVE` and only requires all pair-level passes when the scientific outcome itself is `PASS`;
- `docs/runs/OCTRL-P01A_RESULT.md` explicitly states `SCIENTIFIC FAIL · EXECUTION VALID · RUN CLOSED` and says the test intentionally permits scientific PASS/FAIL while requiring execution validity.

Therefore Claude's observation was factually useful but the stronger interpretation `green CI masked an accidental research failure` would have been wrong.

Receiving-project decision:

> **NONE for ReflexBrain — the distinction was already intentional and source-native.**

Medium-level value:

> a second cognition body can serve as an independent anomaly detector / re-validator, while the owning project's source remains the authority that determines whether the anomaly is a bug, a deliberate contract, or a misunderstanding.

This is qualitatively more useful than a transport-only ACK: the second body changed what the first body chose to inspect, and the source-native gate then corrected both agents' possible overclaim.
