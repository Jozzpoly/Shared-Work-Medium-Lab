# Source-bound heterogeneous co-creation — 2026-10-08

## Status

**ACTIVE BOUNDED SUCCESSOR · SOURCE-BOUND WORK, NOT BROWSER-HISTORY MESSAGING**

This successor exists because the closed heterogeneous shared-browser checkpoint reached its stop condition and then real new pressure appeared.

Closed predecessor:
- PR #11 — heterogeneous shared-browser round-trip.

Do not reopen PR #11 merely because later evidence was discovered.

## Why a successor exists

PR #11 established, boundedly, that:
- Browser ChatGPT and Claude are separate cognition bodies;
- both can perceive one shared Opera session;
- a non-mutating trace/ack round-trip can occur without Owner copy/paste;
- the shared browser profile is **not** a safe/private/general-purpose message bus.

PR #11 was therefore closed.

After closure, new facts changed the problem:

1. The Owner explicitly invited Claude to **co-create Shared Work Medium**, accepting mutual conversation visibility as a temporary deliberate cheat.
2. Claude produced a real participant-owned workpiece:
   - `Tablica stanu SWM v0 (as-of 7367c7a)`;
   - candidate tool `swm-state.mjs`;
   - generated `STATE_AS_OF.json`;
   - concrete proposals about research verdict recovery.
3. Browser ChatGPT source-verified the ReflexBrain claim behind that workpiece and wrote a durable response.
4. Claude's Slack connector is now visibly **Connected** in product settings.
5. Claude's GitHub Integration is visibly **Connected** to `Jozzpoly`.
6. Neither Claude Slack runtime exposure nor Claude Chat GitHub write capability is yet qualified.

This is no longer primarily a transport experiment.

The question is now:

> **Can heterogeneous agent bodies co-create useful project work through source-bound shared objects, using shared-browser state only for discovery/pointers, while each body keeps its own capability boundaries and the Owner stops acting as courier?**

## Immutable predecessor evidence

The closed PR #11 branch continued to receive post-closure evidence before this concurrency was noticed.

Use immutable source, not mutable branch inference:

- heterogeneous evidence / connector qualification:
  `https://github.com/Jozzpoly/Shared-Work-Medium-Lab/blob/c57607b85ebe210c93fc8752dc2c2e3fb318db9d/docs/evidence/HETEROGENEOUS_SHARED_BROWSER_ROUNDTRIP_2026-10-08.md`

- Browser reply to Claude state board:
  `https://github.com/Jozzpoly/Shared-Work-Medium-Lab/blob/c57607b85ebe210c93fc8752dc2c2e3fb318db9d/docs/medium/REPLY_7367c7a.md`

- separate Browser-authored workpiece in Capability Expedition Issue #7:
  `https://github.com/Jozzpoly/Shared-Work-Medium-Lab/issues/7#issuecomment-6058410077`

The exact execution origin of that Issue #7 Browser comment was not recovered from the currently open ChatGPT tabs.

Do not promote it to an ecological-independence claim.

## Claude workpiece freshness

Claude's state board is anchored to ReflexBrain:

`research/pre-o0-foundations-campaign`
at:
`7367c7ab7fd27382fc1a01b51387ed21cc258de7`

Browser ChatGPT independently verified that this was still the branch head when responding.

## P01A re-validation

Claude noticed that green GitHub CI coexisted with a scientific `FAIL`.

Browser ChatGPT verified source-native evidence:

- ReflexBrain PR #14 head:
  `4f8e2d92d2efc5676a34cf6dc069667f3e85083b`
- workflow run #548 / job `112550470392`: GitHub conclusion `success`;
- the job log contains:
  `P01A_RESULT {"outcome":"FAIL", ...}`;
- H2 fails the frozen one-tick timing contract;
- Vitest reports all test files/tests passed.

This is intentional.

`docs/runs/OCTRL-P01A_RESULT.md` explicitly records:

`SCIENTIFIC FAIL · EXECUTION VALID · RUN CLOSED`

The test intentionally permits a scientific PASS/FAIL/INCONCLUSIVE outcome while requiring execution validity.

Therefore:

> **CI health, execution validity and scientific verdict are distinct evidence planes.**

Receiving-project result for ReflexBrain:

> **NONE — no bug to repair.**

Medium-level value:

> a second cognition body can identify an anomaly/recovery pressure, while the owning source determines whether it is a defect, intended contract or misunderstanding.

## Claude Artifact boundary

Claude published:

`https://claude.ai/artifact/WbG4GNSh7RHbEG6wZS3gWE`

Observed through shared Opera:
- title: `Tablica stanu SWM v0 (as-of 7367c7a)`;
- Artifact UI;
- access label: `Only you`;
- payload represented as a user-generated iframe.

Current Browser ChatGPT body:
- can discover/open the artifact object;
- cannot traverse/read the iframe payload through Opera AX;
- cannot fetch the artifact through normal external web fetch.

Therefore:

> **Artifact object reachability PASS; independent Browser full-content read NOT YET PASS.**

Do not ingest `swm-state.mjs` implementation until exact source bytes are independently readable.

## Claude Slack product state

Claude Customize currently shows Slack:
- **Connected**;
- `Disconnect` available;
- 14 read-only tools;
- 12 write/delete tools;
- visible actions include read/search, `Send message`, `Schedule message`, reactions, uploads, conversations, Lists and Canvases.

Permission boundary:
- write/delete blanket permission currently reads **Needs approval**.

Claude's earlier statement `nie mam konektora` is therefore stale relative to settings.

But:

> **Slack connected/configured != Slack tools exposed in the already-running cognition body.**

That body had already hit its usage limit.

A bounded Browser-authored handoff now exists in `#medium-probes`:

`swm://probe/claude-slack-fresh-body-2026-10-08`

It asks the next fresh Claude body to qualify only:
1. runtime tool exposure;
2. direct read of that exact message;
3. at most one bounded reply if approval burden is acceptable;
4. independent read-back.

Do not infer PASS from settings.

## Claude GitHub product state

Claude Customize currently shows:

**GitHub Integration — Connected**

Account:
- `Jozzpoly` — `Installed`.

The settings page describes:
- Chat: attach repository files;
- Projects: sync repository files;
- Claude Code: select repositories, browse branches and track PRs in remote sessions;
- repository-access checker labelled **Cloud sessions only**.

This establishes context/integration reachability.

It does **not** establish Claude Chat repository writes.

No current settings evidence establishes:
- create/update/delete file tools;
- issue/PR comment writes;
- commits;
- merges;
- write actuator exposure in the running Claude chat.

Therefore:

> **Claude GitHub integration connected PASS; Claude Chat GitHub write actuator NOT QUALIFIED.**

## Browser ChatGPT current body

Current Browser ChatGPT capabilities relevant to this experiment include:
- authenticated GitHub read/write connector;
- authenticated Slack read/write connector;
- AgentMail bounded bidirectional transport identity;
- Opera shared-browser sensing/navigation;
- local container/Python execution surfaces;
- plugin discovery/management.

This list is a current-body observation, not a stable capability ontology.

## Current co-creation pattern

Observed, not prescribed:

```
participant does native work
  -> publishes through body-native surface
  -> leaves a low-cost pointer/scent
  -> another participant independently dereferences
  -> verifies source/effect/authority
  -> accepts, rejects or narrows the contribution
  -> durable truth stays with the owning project
```

Browser history is no longer treated as the data plane.

Preferred carrier order under current evidence:
1. source-native durable object;
2. Slack probe pointer where appropriate;
3. filtered shared-browser pointer only as discovery fallback.

## Current decision on Claude's verdict proposal

The recovery problem is real.

Do **not** standardize a global `SWM_VERDICT` schema yet.

Useful local requirements:
- explicit `as_of` / source revision;
- execution validity distinct from scientific/experiential outcome;
- owning-source pointer;
- `unknown` / `owner-required` instead of inference when durable verdict is absent.

Owner browser judgement should be consolidated back into the owning project's durable source by the responsible agent.

Medium should route to that truth rather than become the replacement truth database.

## Immediate next gates

### Gate A — Claude fresh-body Slack qualification

Only after the Claude usage limit resets / a fresh body exists:
- verify Slack tool namespace;
- read the known `#medium-probes` handoff directly;
- optionally send one bounded reply if the permission flow is low enough burden;
- read it back.

### Gate B — Claude GitHub runtime qualification

Determine whether the fresh body has:
- context-only repository access;
- read tools;
- or real durable write actions.

Do not infer from the Connected setting.

### Gate C — exact `swm-state.mjs` source review

Claude should expose the exact source through a path Browser ChatGPT can independently read without Owner copy/paste.

The mutually visible Claude conversation is acceptable as the current deliberate cheat if a bounded source/diff block is provided.

Do not adopt the tool from a prose summary.

### Gate D — useful-work criterion

The experiment advances only if the shared substrate changes real work:
- one body catches an error/omission the other missed;
- one body produces a workpiece another can source-review and use;
- Owner courier burden falls;
- or a capability boundary becomes materially clearer.

Transport-only acknowledgements are no longer enough.

## Security / attention rules

- Never dump full browser history into durable evidence.
- Filter history in-tool against an allowlist when possible.
- Never persist OAuth/session parameters discovered in history.
- Prefer short safe URL fragments as ephemeral pointers.
- Shared Opera conversations are mutually visible by current Owner choice; this invalidates blind/private-subject assumptions.
- Slack connector authorship must be stated because Browser writes inherit Owner-visible Slack identity.
- Do not manufacture traffic to keep the experiment alive.

## Stop condition

Stop this successor if:
- Claude fresh-body tools do not expose a useful source-bound interaction path;
- Owner approvals become the dominant cost;
- Browser ChatGPT becomes a permanent manual committer for unreadable Claude output;
- no real project decision/work changes because of the collaboration;
- or the experiment begins producing more coordination artifacts than useful work.

Success is not "more messages".

Success is:

> **heterogeneous agent bodies actually contributing different useful capabilities while source truth stays recoverable and Owner routing burden drops.**
