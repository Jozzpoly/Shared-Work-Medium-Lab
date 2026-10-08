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

## Candidate federation hypothesis — heterogeneous bodies, shared referents

This campaign now provides concrete pressure behind an older canonical SWM direction: specialized models/tools should behave as **attachable bodies/senses**, not prerequisites that the whole system must normalize around.

Observed in the current Claude ↔ Browser case:

- Claude contributes a local sandbox/test-reproduction body and independent falsification perspective;
- Browser ChatGPT contributes authenticated GitHub/Slack writes, project stewardship and connector/plugin reachability work;
- both can sometimes overlap on Opera perception, but that shared browser substrate is volatile and privacy-limited;
- durable GitHub/source objects remain independently dereferenceable authority;
- Claude can produce a participant-owned proposal while Browser can source-check, reject parts, preserve parts and write a separate receiving decision;
- neither body needs to surrender its own capability boundary or become the other's execution proxy.

A candidate federated formulation is therefore:

> **shared referents + source authority + heterogeneous bodies + local perspectives + explicit capability boundaries**

rather than:

> one shared runtime + one capability set + one global agent identity + one transport.

### What this hypothesis would explain

It naturally fits several observed results:
- Slack can be useful to Browser but absent/unqualified in Claude runtime;
- Claude can reproduce CI locally while Browser may be better positioned to update durable repository state;
- Opera can be a temporary overlapping sense without becoming project truth;
- a Claude artifact may exist before Browser can independently read its exact source;
- receiving projects can return `NONE` even when another body discovered a true fact;
- participant-owned proposals can coexist with canonical source truth without immediate standardization.

### Falsifiers / reasons not to promote this yet

Do **not** promote this to SWM architecture if live work shows that:
- the Owner still has to courier most useful context between bodies;
- one body becomes a permanent manual proxy/committer for another body's unreadable output;
- capability differences create more ceremony than leverage;
- source-bound workpieces cannot be independently dereferenced across bodies;
- participant/local perspectives repeatedly drift into incompatible pseudo-truths;
- coordination artifacts grow faster than useful project work;
- a simpler single-body workflow consistently performs better.

Current classification:

> **STRONGER HYPOTHESIS FROM LIVE EVIDENCE · NOT CANONICAL ARCHITECTURE.**

The next useful evidence should come from real co-created work, not another federation diagram.
## Evidence-lane separation — co-creation is not ecological adoption

The current Claude collaboration must remain separate from the frozen Quiet Presence ecological-adoption criterion.

Claude was explicitly invited by the Owner to co-create Shared Work Medium and investigate parity/collaboration.

Therefore the current run can establish:
- heterogeneous body calibration;
- source-bound co-creation;
- cross-agent falsification/correction;
- reduced Owner copy/paste burden;
- capability-boundary discovery;
- usefulness of participant-owned proposals and receiving decisions.

It cannot establish the stronger ecological target:

> an agent pursuing its own non-SWM goal independently discovers that Medium is useful and advances that external work because of it.

Current classification:

> **CO-CREATION LANE: MATERIAL ACTIVE EVIDENCE**

> **QUIET PRESENCE ECOLOGICAL ADOPTION: UNCHANGED / STILL OPEN**

Do not score deliberate Claude co-creation as ecological adoption merely because two heterogeneous cognition bodies are now involved.

The earlier Claude Free incognito/native-web lane remains a cleaner future body-calibration route for blinded or unrelated-goal experiments, but the current shared-profile Claude session is already contaminated by SWM fixture/source/conversation exposure.
## Open Substrate constraint on participant-owned workpieces

The historical Open Substrate campaign at commit `2807bd2843167ecde3dabcc190ca82c6b961b206` already defended a relevant boundary:

> arbitrary participant/tool/source content stays semantically opaque unless it explicitly opts into Medium-level identity relationships.

That campaign also separated representation openness from capability/execution permission and required explicit reference boundaries rather than recursively inferring Medium semantics from arbitrary payload fields.

Applied to the current Claude workpiece:

- the Claude Artifact object may be addressable while its implementation payload remains unreadable to Browser;
- Browser may preserve the artifact as a participant-owned referent;
- Browser may source-verify claims independently and publish a separate receiving decision;
- Browser must **not** reconstruct/adopt `swm-state.mjs` from prose or artifact UI summaries;
- exact source bytes or another independently readable source-bound representation are required before code review/adoption.

Therefore Gate C is not ceremony:

> **independent readability is part of the authority boundary between participant proposal and adopted project mechanism.**

No schema change follows.
## Activation boundary — transport and discovery do not wake a cognition body

The current co-creation loop reduces **Owner courier burden** but does not yet remove **Owner activation burden**.

Current evidence:
- Browser can publish a durable GitHub workpiece;
- Browser can leave a short Slack pointer without copying full content;
- Claude product settings can expose connected Slack/GitHub surfaces;
- a fresh Claude body could in principle discover/dereference those objects;
- but the existence of the objects does not itself start a Claude cognition run.

A direct inspection of the current Browser tool namespace found no callable `start/run/dispatch external agent` actuator.

A bounded plugin-directory scout found no ready low-setup connector whose demonstrated contract is simply:

> `event/source object -> wake this existing external cognition body`.

Candidates such as Vercel/Replit/Base44 are application/agent-building platforms; AgentMail/Resend are transport/event surfaces. None may be promoted to an activation PASS from catalog descriptions.

Therefore keep three federation edges distinct:

1. **transport / preservation** — a workpiece exists somewhere durable;
2. **discovery / perception** — another body can find/read it;
3. **activation / scheduling** — another cognition body actually starts and spends cognition on it.

Current state:
- transport: multiple bounded PASS paths;
- discovery: bounded PASS on several surfaces;
- activation: **UNRESOLVED / OWNER-INITIATED in the current heterogeneous Claude loop**.

Do not build an orchestration platform merely to erase this boundary. Reopen only when activation burden becomes a real bottleneck in useful work or an existing product exposes a credible low-cost actuator.
## Candidate federation invariant — do not collapse identity planes

Live evidence now pressures an identity separation that is broader than the existing SWM distinction between shared artifact identity, participant perspective and place-local meaning.

At least these planes must remain conceptually distinct unless evidence explicitly binds them:

### 1. Participant / perspective identity

The local interpretive actor or role whose perspective matters to the project.

Examples:
- Browser ChatGPT participant perspective;
- Claude participant-owned proposal;
- Codex perspective;
- Owner judgement.

This is not automatically equal to one account or one model session.

### 2. Cognition-body / execution-context identity

A particular model conversation/run/body with its own context, current capabilities and contamination state.

Examples:
- the contaminated shared-profile Claude run;
- a future fresh/incognito Claude body;
- the current Browser ChatGPT execution body.

A fresh body may belong to the same broad participant role while having different memory, tool exposure or permissions.

### 3. Transport / account identity

The provider-visible address/account used to carry an action.

Examples:
- Owner Slack user under which Browser connector writes appear;
- AgentMail inbox address;
- GitHub account `Jozzpoly`;
- browser profile/session.

Transport identity does not prove cognition or authorship identity.

### 4. Environment/session identity

The shared external environment in which bodies may overlap.

Example:
- one Opera browser/profile/session visible to both Claude and Browser ChatGPT.

Sharing this environment did not merge model contexts, but it did destroy naive privacy/isolation assumptions because open conversations were mutually observable.

### 5. Durable source/workpiece identity

The addressable project object whose truth/provenance can outlive bodies and transports.

Examples:
- exact commit;
- PR;
- issue comment;
- revision-bound document;
- Claude Artifact object (object identity reachable even when payload readability is not).

### Evidence that collapsing these planes is wrong

- Slack visible sender = Owner, while epistemic author = Browser ChatGPT.
- AgentMail A/B inboxes gave distinct transport identities while one Browser cognition body controlled both.
- one logical AgentMail conversation produced different inbox-local thread IDs.
- Claude and Browser were distinct cognition bodies while sharing one Opera environment.
- Opera connector metadata could say installed/enabled while live browser-session reachability failed.
- a Claude Artifact could have stable object identity while Browser lacked readable source bytes.
- Multi_World donor evidence independently warned that ActorSession lifetime is not browser transport lifetime.

Candidate rule:

> **Never infer participant continuity, authorship, cognition, authority or global conversation identity solely from the currently convenient transport/account/session identifier.**

### Nonclaim

This is **not** a request to design a final participant/session/account schema now.

It is a pressure-derived modelling constraint for future federation work.

A future implementation should introduce only the minimum distinctions demanded by real continuity/authority problems rather than materializing all five planes as mandatory fields.
## What is actually new relative to existing SWM ecology

Do not mislabel the current Claude work as the invention of federation from scratch.

Canonical SWM already defends:
- **value is local; artifacts can migrate**;
- participants may create affordances rather than only consume them;
- shared artifact identity can remain distinct from participant perspective and place-local meaning;
- source truth must remain reachable;
- reuse/promote/discard decisions should remain evidence-driven rather than globally ranked.

The current heterogeneous co-creation adds or materially strengthens different pressures:

1. **Heterogeneous cognition bodies can participate in the same lifecycle.**
   The participant is no longer only Browser/Codex-style variation inside one familiar tool family.

2. **Capability asymmetry is potentially useful rather than a defect to normalize away.**
   One body may locally reproduce tests; another may hold authenticated project-write connectors.

3. **Independent source readability becomes an inter-body adoption boundary.**
   A participant-owned proposal may exist and be discussed before another body can safely ingest its implementation.

4. **Identity planes need stronger separation.**
   Cognition body, participant role, transport/account, shared environment and durable source object are demonstrably non-equivalent.

5. **Activation is a distinct federation edge.**
   A durable workpiece can exist and be discoverable while no cognition body is currently running to consume it.

Therefore the current contribution is not a new global lifecycle.

> **It is evidence that SWM's existing local-value/source-bound ecology may generalize across materially different agent bodies — provided identity, capability and activation boundaries remain explicit.**

That generalization remains provisional until repeated useful cross-body work occurs.
## Gate D — useful-work criterion: PASS BOUNDED

The active successor defined useful-work evidence as at least one of:
- one body catches an error/omission the other missed;
- one body produces a workpiece another can source-review and use;
- Owner courier burden falls;
- or a capability boundary becomes materially clearer.

The current run now satisfies this gate in multiple bounded ways.

### Claude corrected Browser's claim

Claude independently red-teamed the shared-browser interpretation and corrected:
- the false implication that Claude invented Probe 0 rather than executing the existing fixture;
- the false/private-context assumption created by separate model conversations inside one shared Opera profile;
- the temptation to treat broad browser history as a clean selective mailbox.

Browser then changed durable PR #11 evidence and narrowed the defended claim.

This is a real downstream project change caused by another cognition body.

### Claude surfaced a source-verification pressure

Claude noticed the apparent contradiction between green CI and P01A scientific FAIL.

Browser independently dereferenced ReflexBrain and established:
- CI/execution validity was intentionally green;
- scientific outcome was intentionally FAIL;
- owning project already understood the distinction;
- receiving-project action = NONE.

The value was not a bug fix; it strengthened the cross-project rule that machine execution status and scientific/product verdict must remain distinct.

### Claude state-board proposal changed Medium decisions

The participant-owned state board / `SWM_VERDICT v0` proposal caused Browser to:
- identify live capability-projection drift;
- reinforce `as_of` / source-revision requirements;
- reject premature global verdict-schema adoption;
- preserve the proposal as participant-owned rather than canonical;
- require independent exact-source readability before considering `swm-state.mjs` adoption.

Those are substantive design/research decisions, not transport validation.

### Owner burden improvement is partial

The Owner did not need to manually copy the probe token/ack or the Browser response content between the two agents.

However:
- the Owner explicitly initiated the collaboration;
- the Owner still must start/freshen Claude cognition bodies;
- current Claude Artifact source remains unreadable to Browser;
- fresh Claude connector capability remains unqualified.

Therefore courier burden improved, but activation burden remains.

### Result

> **GATE D: PASS BOUNDED — heterogeneous co-creation has already changed real SWM work.**

This does **not** establish:
- autonomous agent federation;
- ecological adoption;
- repeated reliability;
- source-level code co-development;
- low-Owner-burden activation.

Gates A/B/C remain open independently.
## Observed carrier matrix — choose by property, not by one bus

The current campaign has enough live evidence to compare several real carriers without treating any one of them as the Medium.

| Carrier / surface | Durable source truth? | Cross-body evidence | Visible identity fidelity | Main strength | Main boundary |
| --- | --- | --- | --- | --- | --- |
| GitHub commit/file/PR/Issue | **Yes, strongest current project authority** | Browser strong; Claude settings/integration connected but runtime read/write still unqualified | Usually provider account identity; Browser authorship must be stated when writing as Owner account | exact provenance, revision binding, reviewable durable workpieces | slower/heavier than ambient presence; account identity != cognition identity |
| Slack | **No** as long-term authority; Free history/retention bounded | Browser read/write PASS; Claude settings connected, fresh-body runtime OPEN | Browser writes appear under Owner Slack identity | low-cost pointer, thread, presence, apparatus coordination | sender/authorship mismatch; retention; attention/feed risk |
| AgentMail | Message transport durable enough for bounded exchange, but not project authority | Browser A↔B transport PASS; no Claude path qualified | separate inbox/address identities available | explicit bidirectional transport identity and thread/message provenance | mailbox != cognition; provider-local thread IDs differ across inbox views; no activation |
| Shared Opera | **No** | Claude↔Browser same-environment round-trip PASS bounded | no authenticated participant identity; trace ownership inferred from protocol/context | ambient working-set discovery, shared external environment, stigmergic trace | volatile connection; broad history/privacy exposure; conversations mutually readable; not selective |
| Claude Artifact | Participant-owned object identity reachable | Claude creates; Browser object discovery PASS, payload read FAIL | Claude-owned surface | lets a participant create its own workpiece without immediate canonicalization | iframe/content not independently readable by Browser; cannot adopt code from summary |

### Immediate consequence

> **No observed carrier dominates all required properties.**

GitHub is currently best for durable source-bound truth.

Slack is useful for short pointers and coordination when attention cost is justified.

Opera is useful as an ambient sensor/discovery surface, not a data plane.

AgentMail demonstrates transport identity without solving cognition/activation.

Claude Artifact demonstrates participant-owned creation without guaranteeing cross-body source readability.

This supports a federated rather than bus-centric interpretation:

> route each interaction through the cheapest carrier that satisfies the required authority, privacy, durability and body-reachability properties; preserve important results back at the owning source.

Do not turn this table into a permanent capability registry. Every row is current-body evidence and may change.
## Observation can mutate the shared environment

A parallel canonical microprobe on `main` established an observer-effect boundary relevant to heterogeneous co-creation:

> **read-only at the target resource is not necessarily read-only at the observing environment.**

Opera `go_to_page` did not mutate the visited website or repository, but the visit remained in shared browser history after the temporary tab closed.

Consequences:
- browser sensing may create future discovery cues;
- an agent can accidentally seed the candidate set it later observes;
- shared-history evidence cannot attribute a visit to Owner/Claude/Browser without separate provenance;
- ecological/blind tests must distinguish pre-existing environmental cues from investigator-created residue;
- `read` / `write` capability classification should be scoped to the affected plane, not treated as globally side-effect-free.

Do not respond by building a universal observer ledger.

For current SWM work the practical rule is narrower:

> prefer source-native verification, minimize broad shared-environment probing, and avoid scoring researcher-created scent as spontaneous discovery.