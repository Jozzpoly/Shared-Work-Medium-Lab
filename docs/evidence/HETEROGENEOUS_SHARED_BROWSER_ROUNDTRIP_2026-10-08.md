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

## Asymmetric co-creation loop — first live instance

The Owner explicitly invited Claude to co-create Shared Work Medium using the imperfect capabilities available today, including the deliberate shared-visibility cheat of one Opera session.

Claude then produced a concrete contribution rather than another transport probe:
- a Claude Artifact titled `Tablica stanu SWM v0 (as-of 7367c7a)`;
- a candidate tool `swm-state.mjs`;
- a generated `STATE_AS_OF.json`;
- an analysis of ReflexBrain result/verdict recovery pressure;
- explicit proposals for machine-readable verdict projection and Owner-verdict handling.

### Artifact reachability

Browser ChatGPT independently discovered the artifact URL through Opera history:
`https://claude.ai/artifact/WbG4GNSh7RHbEG6wZS3gWE`

The shared Opera session exposes:
- artifact title;
- Artifact UI;
- access label `Only you`;
- a `User-generated artifact content` iframe.

But Browser ChatGPT's current Opera body does not traverse/read the iframe payload, and an ordinary external web fetch cannot access the artifact URL.

Therefore:

> **Claude Artifact object reachability: PASS. Independent Browser ChatGPT full-content read: NOT YET PASS.**

The shared browser account/session is sufficient to expose the object, but not sufficient to make the artifact payload a qualified cross-agent data plane.

### Conversation as provisional source channel

Because the Owner explicitly accepts mutual visibility of the agent conversations for this experiment, Claude's own conversation remains readable through Opera.

That conversation exposed the candidate tool's claimed behavior and limitations, but not independently readable tool bytes suitable for adoption.

Browser ChatGPT therefore refused to copy/commit the implementation from the summary.

### Source-native reply

Browser ChatGPT independently verified that ReflexBrain branch `research/pre-o0-foundations-campaign` still pointed to:
`7367c7ab7fd27382fc1a01b51387ed21cc258de7`

and wrote a durable response on this PR branch:
`docs/medium/REPLY_7367c7a.md`

The response:
- accepted the recovery problem;
- verified P01A's intentional `scientific FAIL / execution PASS` separation;
- rejected a global SWM-owned verdict ontology;
- preserved project-local authority for Owner/scientific verdicts;
- kept `swm-state.mjs` as a donor pending exact source review;
- requested a future independently readable source path before adoption.

Browser ChatGPT then left only a non-mutating browser-history pointer:
`#swm-reply-7367c7a`

and closed the tab.

### Current observed co-creation shape

This is the first live instance of:

```
Claude native work / local execution
  -> Claude-side workpiece + shared-browser pointer
  -> Browser ChatGPT discovers pointer
  -> Browser ChatGPT verifies owning source
  -> Browser ChatGPT writes durable project-side reply
  -> shared-browser pointer back to Claude
```

The loop is asymmetric by design:
- Claude currently has local execution / publishing capabilities that Browser ChatGPT does not use in the same way;
- Browser ChatGPT currently has authenticated GitHub/Slack/AgentMail write actuators Claude does not have in that body;
- Opera is a shared discovery substrate, not authority.

Do not generalize this into a permanent architecture yet.

The next useful qualification is whether Claude, on a later callable turn, independently finds `#swm-reply-7367c7a`, reads the durable reply, and exposes the exact `swm-state.mjs` source in a form Browser ChatGPT can actually inspect.

## Shared-history hygiene boundary

The shared Opera history surface is useful but broad.

During live work both agents observed that it may include unrelated navigation and URLs carrying OAuth-style query parameters.

Therefore raw history should not be treated as a clean mailbox or copied wholesale into evidence.

Current hygiene rule for this experiment:

- query/read history only through in-tool allowlist filtering when possible;
- emit only project-relevant safe URLs/tokens to the model context;
- prefer short URL **fragments** on a known public/canonical page for ephemeral acknowledgements/pointers;
- do not encode substantive payloads, secrets, credentials or private content in the fragment;
- dereference the pointer to source-native truth rather than treating the history entry as authority;
- do not infer inactivity from absence in history.

A filtered live read successfully recovered only the intended SWM/Claude traces, including:
- `PR #11#swm-reply-7367c7a`;
- the earlier PR #11 red-team task pointer;
- the prior PR #10 ACK pointer;
- the Claude Artifact URL.

This reduces accidental exposure inside the research process, but does not make a shared browser session private.

## Claude GitHub Integration boundary

Browser ChatGPT independently inspected Claude's current `GitHub Integration` settings.

Observed product state:
- GitHub Integration is **Connected**;
- account `Jozzpoly` is shown as **Installed**;
- Chat: attach repo files as context;
- Projects: sync repository files;
- Claude Code: select repositories, browse branches and track pull requests in remote sessions;
- the repository-access status surface is labelled **Cloud sessions only**.

What is **not** established by this settings page:
- repository write tools in Claude Chat;
- create/update/delete file actions;
- issue/PR comment actions;
- commit/merge capability;
- exposure of GitHub actions in the already-running Claude cognition body.

Therefore:

> **Claude GitHub integration connected: PASS. Claude Chat GitHub write actuator: NOT QUALIFIED.**

On a fresh Claude body, inspect actual tool exposure before changing the co-creation model.
If direct durable GitHub write becomes genuinely available, Browser ChatGPT should stop acting as mandatory committer for Claude workpieces.

## Receiving-project gate on Claude's ReflexBrain finding

Claude independently highlighted a real distinction in ReflexBrain: green CI does not necessarily mean scientific PASS.

Source-native verification confirmed the concrete P01a case:
- `docs/runs/OCTRL-P01A_RESULT.md` explicitly says `SCIENTIFIC FAIL · EXECUTION VALID`;
- H2 falsified the frozen contact+1 timing criterion (contact 58, required divergence <=59, observed 60);
- the Vitest intentionally accepts `PASS | FAIL | INCONCLUSIVE` and only asserts detailed pair criteria when the scientific outcome is PASS;
- the current ReflexBrain campaign state already records P01a as `SCIENTIFIC FAIL · EXECUTION VALID · CLOSED` and explicitly states that FAIL is a completed scientific result.

Therefore Claude's observation was factually useful but **not a missing warning for ReflexBrain**.

Receiving-project decision:

> **NO ROUTE / NO PROJECT CHANGE.**

This is another important Medium behavior: an independent cognition body may discover a true fact, while the receiving project's own current truth shows that the fact is already locally understood and requires no intervention.

## Shared-browser reachability is volatile

Later in the same campaign Browser ChatGPT attempted to inspect whether Claude had consumed a new PR #11 history-trace task.

The Opera connector returned:

`Browser not connected. Make sure to enable Allow AI connection ...`

The shared-browser substrate had therefore become unreachable to this Browser execution body between turns.

Scoped conclusion:

> **shared browser state is a volatile peripheral/stigmergic substrate, not durable transport or authority.**

Do not require continuity, handoff or project truth to depend on it remaining connected.

A durable source (GitHub/other project authority) must preserve any result that matters after the environmental interaction disappears.

## Opera capability-state split after disconnect

After the successful heterogeneous round-trip, the Opera substrate became unreachable to Browser ChatGPT.

A four-layer check produced mutually non-equivalent states:

1. Plugin discovery/search reported Opera Browser Connector as:
   - `installed: true`;
   - `status: ENABLED`.
2. Plugin permission inspection for the same app id reported:
   - `status: not_installed`;
   - global permission policy still `Allow low-risk actions`.
3. The current Browser execution body still exposed the Opera tool namespace.
4. Both `list_tabs` and the minimal `greeting` handshake failed with:
   - `Browser not connected`.

Scoped conclusion:

> **catalog installation state, permission metadata, tool exposure, and live provider/session reachability are separate capability layers and may disagree.**

Therefore a future Medium capability model must not collapse any of these into one boolean `available` flag.

The only defensible operational claim is the effect-verified one at the current layer.

## Reconciliation with the 2026-10-07 heterogeneous-browser fixture

The closed PR #10 already contained `HETEROGENEOUS_SHARED_BROWSER_PROBE_2026-10-07.md` with a staged probe design. The 2026-10-08 result should therefore be interpreted against that prior fixture rather than as a newly invented test family.

### Probe 0 — one-body trace persistence

**PASS BOUNDED in Claude's body.**

Claude executed the existing open→close→history pattern and recovered its unique trace after tab closure.

Correction: Claude did not independently invent Probe 0; it executed the pre-existing fixture.

### Probe A — same-world identity

**PASS BOUNDED, bidirectional.**

- Claude created unique shared-browser traces visible to Browser ChatGPT without Owner token copy/paste.
- Browser ChatGPT created a unique acknowledgement trace visible to Claude before Claude read the ChatGPT conversation.

This strongly supports that both connectors were observing the same ordinary Opera environment during the qualified window.

It does not prove stable identity across browser/profile changes or after the connector disconnects.

### Probe B — environmental handoff without context copy

**NOT PASSED.**

The actual exchange used explicit probe-like tokens and both participants knew shared-browser parity was under investigation.

The stronger fixture required ordinary work by-products, no instruction encoded for the receiver, and instrumental reuse under a separately phrased goal.

That has not occurred.

### Probe C — same referent / different private interpretations

**UNRUN.**

The current shared session also invalidates any naive assumption that the participants' conversation surfaces are private: open model conversations are mutually readable through the shared browser.

A clean interpretation-divergence test would need either:
- separate browser profiles/sessions;
- precommitted interpretation hashes before either side can inspect the other's conversation;
- or another isolation mechanism.

### Probe D — stale observer state

**NOT DELIBERATELY RUN.**

The later Opera disconnect demonstrates substrate volatility, but is not itself the stale-source comparison specified by Probe D.

### Ecological success candidate

**OPEN.**

No unrelated project task has yet been materially advanced because one heterogeneous agent spontaneously reused the other's ambient browser trace.

Therefore the strongest surviving result remains:

> **shared-world / heterogeneous-body reachability is boundedly demonstrated; ecological instrumental reuse is not.**

## Historical donor check — Open Substrate

The shared-browser result was checked against the historical Open Substrate campaign at exact commit:

`2807bd2843167ecde3dabcc190ca82c6b961b206`

Open Substrate had already defended a relevant thin-waist boundary:

> **arbitrary participant/tool/source content stays semantically opaque unless it explicitly opts into Medium-level identity relationships.**

Its Phase-3 result specifically rejected recursive inference of Medium semantics from arbitrary raw fields such as foreign `object_id` values. Intentional relationships required an explicit, scoped reference declaration instead.

### Consequence for shared-browser traces

The experiment-local tokens:
- `claude_probe=...`;
- `#swm-reply-...`;

must **not** become evidence that URL query parameters/fragments are a general Medium message or relation protocol.

They were only local conventions inside this bounded test.

If a future environmental trace deserves preservation:
- preserve the raw trace exactly or by an appropriate minimal referent;
- keep provider/browser payload semantically opaque by default;
- attach any Medium-level interpretation through a deliberately scoped local record/reference;
- never infer participant identity, authority or relation semantics merely from arbitrary URL fields.

Current receiving-project decision:

> **NO SCHEMA CHANGE. Open Substrate acts as a constraint on interpretation, not as a request to formalize browser tokens.**
