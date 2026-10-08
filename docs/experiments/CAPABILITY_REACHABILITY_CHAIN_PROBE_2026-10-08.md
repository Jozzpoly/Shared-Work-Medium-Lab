# Capability Reachability Chain Probe — 2026-10-08

**Status:** LIVE SYNTHESIS + EXPERIMENTAL RULE · DRAFT-BRANCH ONLY · NOT PROJECT AUTHORITY

## Problem

Recent Browser/Medium research repeatedly produced the same failure mode:

> a capability appeared to exist, but the current agent body still could not produce the required real-world effect.

The mistake is treating a capability advertised or exposed at one layer as an end-to-end ability.

For Shared Work Medium and agent orchestration, the relevant unit is therefore not:

`tool / feature exists`

but:

`the required effect is reachable by this body, in this account, through this permission/session/transport chain, and the effect has been independently observed`.

## Proposed evidence ladder

Use the narrowest status supported by evidence.

1. **DOCUMENTED**
   - vendor/source says the substrate supports a capability.

2. **DISCOVERED / EXPOSED**
   - the current environment can see the app/tool/method/schema.

3. **PERMITTED**
   - the current account/session grants the relevant action class.
   - permission does not create missing tools.

4. **PATH COMPLETE**
   - authentication, session identity, transport hops and required intermediary bodies are all reachable by the current agent.

5. **EXECUTION PASS**
   - the requested action was actually invoked successfully.

6. **EFFECT PASS**
   - an independent sensor observed the intended external effect.

7. **OWNER / PRODUCT PASS**
   - where experiential value matters, the Owner confirms the effect actually satisfies the product-level need.

Never promote a lower rung into a higher one by implication.

## Live counterexamples

### Opera One Browser Connector

Live Plugin permissions report:
- app installed/enabled;
- app-specific permission: **Allow all actions**.

Yet the exposed Browser Connector tool surface contains:
- tabs/history/page content/screenshot;
- go-to-page;
- close-tab;

and does **not** expose click/type/fill/keyboard.

Finding:

> PERMITTED != EXPOSED. "Allow all actions" cannot grant an action that the connector never exports.

### Retracted Opera Neon route

Opera-side documentation was interpreted as evidence that Browser ChatGPT could gain real click/form actuation through Neon Free + custom MCP.

The complete ChatGPT-account/client/auth/tool path was never demonstrated. Owner qualification did not yield the claimed Browser-GPT actuator.

Finding:

> DOCUMENTED substrate capability + plausible integration story != PATH COMPLETE.

The route is retracted until an actual end-to-end pass exists.

### FIELDCRAFT / host bridge

A generated interactive surface observed host methods including:
- `setWidgetState`;
- `sendFollowUpMessage`;
- `callTool`;
- `openExternal`;
- `requestDisplayMode`.

The concurrent project analysis explicitly states that write calls / useful tool calls were not yet executed and widget persistence was not behaviorally qualified.

Finding:

> EXPOSED host method != EXECUTION PASS.

### Slack signed file upload

Slack successfully returned a signed upload URL and file ID.

The current Browser body could not perform the required raw-byte POST to the Slack upload host.

Finding:

> service-side operation exists and its first hop succeeds, but one missing transport hop means PATH COMPLETE = FAIL.

### Slack app vs Slack-native Agent

The normal ChatGPT Slack app is installed and can be used through the Browser connector.

The live Slack `Agents & tools` surface reported zero installed Slack-native agents.

Finding:

> APP PRESENCE != AGENT BODY PRESENCE.

### Claude + Opera MCP

Claude UI showed the Opera MCP connector configured with browser tool classes.

The permission UI still required approval for relevant tools, and no Claude-side invocation of the shared browser tools was observed in the campaign.

Finding:

> CONNECTED CONFIG != SHARED-WORLD PERCEPTION PASS.

### GitHub permission versus sensor semantics

Current plugin permissions report:
- GitHub app-specific setting: **Allow all actions**.

This successfully supports real repository writes.

However GitHub observation surfaces remain lossy in different ways:
- recent issues/PR top-N overrepresents high-churn repositories;
- commits can miss live work on other branches depending on query;
- normalized repository listing omits useful raw `pushed_at` metadata.

Finding:

> ACTION REACHABILITY does not imply OBSERVATION COMPLETENESS.

### ChatGPT Slack app DM does not qualify an agent-to-agent cognition path

A bounded DM probe tested whether the installed normal ChatGPT Slack app could serve as an independent consumer for connector-authored messages.

Observed:
- Slack user profile for `U0C7N0DGB8U` identifies a bot named ChatGPT;
- a direct-message conversation with that bot is reachable;
- two separate connector-authored handshake messages existed in that DM (one earlier probe and one 2026-10-08 probe);
- neither produced any bot reply;
- both synthetic probe messages were deleted after qualification.

The current connector renders these outbound messages as Owner-authored messages marked `Sent using ChatGPT`.

Scoped finding:

> **connector-authored Slack message -> installed ChatGPT Slack app is NOT a qualified agent-to-agent cognition path.**

Do not infer from this that the ChatGPT Slack app cannot respond to a human typing directly in Slack UI. That path was not tested here.

What is falsified for current SWM purposes is the tempting shortcut:
- "ChatGPT app is installed"
- therefore "we already have a second independent ChatGPT consumer in Slack."

Current status:
- BOT PRESENCE: PASS;
- DM TRANSPORT REACHABILITY: PASS;
- CONNECTOR-AUTHORED MESSAGE DELIVERY: PASS;
- INDEPENDENT BOT COGNITION/REPLY: **FAIL / NOT OBSERVED across two probes**;
- ECOLOGICAL SUBJECT: NOT QUALIFIED.

This further separates:
`app presence`
from
`agent runtime presence`
from
`usable agent-to-agent transport`.

Current OpenAI product documentation also explains the product-class split:
- **Slack connected to ChatGPT** is available to eligible Plus/Pro/Business/Enterprise/Edu users and lets Browser ChatGPT search/use Slack through the connected app;
- the newer organizational **@ChatGPT inside Slack/Teams** assistant experience is documented separately and is currently available globally for Business and Enterprise users.

Sources:
- https://help.openai.com/en/articles/12525822-using-slack-in-chatgpt
- https://help.openai.com/en/articles/20001536-chatgpt-with-slack-and-microsoft-teams

This means the visible Slack bot/app label must not collapse these two product surfaces into one assumed runtime.


### AgentMail plugin installation / runtime exposure split

A live 2026-10-08 qualification produced a new seam after the Owner installed AgentMail specifically for this campaign.

Observed through Plugin Management:
- AgentMail status: `installed=true`;
- app-specific permission: `Use my default`;
- inherited global permission: `Allow low-risk actions`.

Vendor/current MCP documentation exposes inbox/message/thread primitives including:
- `create_inbox`;
- `list_inboxes`;
- `send_message`;
- `list_threads`;
- `get_thread`;
- `reply_to_message`.

Sources:
- https://docs.agentmail.to/integrations/mcp
- https://www.agentmail.to/docs/integrations/langchain

However, the current Browser execution body's callable tool inventory did **not** expose any AgentMail namespace or the known MCP tool names after installation. Exact runtime introspection returned them as unavailable.

Current evidence state:

- DOCUMENTED: PASS;
- INSTALLED: PASS;
- PERMITTED: PASS (bounded low-risk policy);
- EXPOSED TO CURRENT EXECUTION BODY: **FAIL / NOT PRESENT**;
- PATH COMPLETE: FAIL;
- EXECUTION PASS: NOT RUN;
- EFFECT PASS: NOT RUN.

Do not work around this by asking the Owner for API keys or by substituting metered browser automation. The missing edge is product/runtime tool exposure, not AgentMail service capability.

Important new distinction:

> **installed/connected plugin state may become visible before its tools become callable by the already-running execution body.**

This may be a transient tool-refresh boundary rather than a durable product limitation. Requalify cheaply on a fresh run/turn before making a broader absence claim.

AgentMail remains a strong identity-transport donor candidate because its primitive directly addresses a current SWM gap: agent-owned transport identity instead of connector actions inheriting Owner identity. It is **not yet a Browser capability PASS**.

### Superpowers subagent methodology without a Browser dispatch actuator

A bounded search for an independent fresh subject found that the installed Superpowers plugin exposes skills named:
- `dispatching-parallel-agents`;
- `subagent-driven-development`;
- `executing-plans`.

The skill text explicitly distinguishes harnesses that have a subagent dispatch tool from harnesses that do not; in the latter case it routes execution inline.

Exact runtime inspection of the current Browser tool namespace found no callable subagent/dispatch/run-agent tool, including no Superpowers-specific dispatch namespace.

Current qualification:
- methodology / dispatch pattern: EXPOSED;
- installed skill corpus: PASS;
- independent worker actuator in this Browser body: **ABSENT**;
- fresh independent cognition: NOT QUALIFIED.

Do not infer a worker body merely because a skill describes how to use one.

This closes another tempting shortcut for PR #9/#10 fresh-agent tests: the existing Superpowers skill set cannot itself supply the uncontaminated subject required by the experiment in this harness.

## Permission-state snapshot

Live Plugin Management inspection on 2026-10-08:

- global default: **Allow low-risk actions**;
- Slack: **Use my default**;
- GitHub: **Allow all actions**;
- Opera Browser Connector: **Allow all actions**.

These settings are account/runtime state, not architectural assumptions.

Important consequence:

> "permission denied" and "capability missing" must be diagnosed separately.

### Agent-only Library promotion blocked at container-session alignment

A real follow-up attempted to promote the generalized capability-chain failure into the persistent `Unified Browser GPT` agent-only Friction Ledger.

Observed:
- current v0.6 ledger and CURRENT were materialized successfully;
- a valid v0.7 JSON candidate was produced in `/mnt/data` and passed JSON validation;
- the candidate file remained present in the active container;
- three bounded Library upload attempts returned `container_session_expired`;
- canonical `CURRENT.json` was deliberately **not** modified because the referenced v0.7 artifact never published.

Current classification:

> **artifact prepared locally + Library mutation action exists != publication path complete.**

Blocking seam: container/file-service session alignment between the generated artifact path and Library mutation body.

Do not bypass this by exposing the agent-only ledger as a user-facing attachment merely to obtain a new file reference.

The reusable capability lesson remains preserved in this source-native PR branch; global runtime promotion is deferred until the mutation seam is reachable through a legitimate agent-only path.

## Effect-verification rule

Whenever practical, qualify execution through a second sensor.

Examples already used successfully:
- GitHub write -> fetch exact committed file -> open exact commit through Opera -> read rendered content;
- Opera navigation -> close created tab -> history recovers exact visit;
- Slack scheduled message -> later direct channel read observes the emitted message;
- Slack edit -> direct read sees fresh state while search temporarily exposes stale projection.

This avoids declaring success from the actuator's acknowledgement alone.

## Candidate representation

For any important capability, record only enough to answer:

```
desired_effect:
substrate:
current_body:
documented:
exposed:
permitted:
session_aligned:
transport_complete:
executed:
effect_observed:
owner_observed_if_needed:
blocking_seam:
```

This is an **audit lens**, not a mandatory global schema or registry.

Do not inventory every tool continuously.

Use it when:
- a new capability could materially change project strategy;
- an integration requires multiple bodies/services;
- a previous assumption failed;
- the Owner would otherwise spend manual time qualifying the path;
- another agent is about to build around an unverified capability.

### AgentMail fresh-body E2E qualification

A fresh Browser turn after plugin installation exposed the AgentMail MCP tools that were absent from the already-running execution body.

This confirms the prior seam rather than contradicting it:

> plugin installation/permission may update before an existing execution body receives the provider's callable tools.

#### Minimal reversible probe

Initial state:
- AgentMail inbox count: **0**.

Created two temporary inboxes:
- `swm-probe-a-20261008@agentmail.to`;
- `swm-probe-b-20261008@agentmail.to`.

A -> B:
- A sent subject `SWM reachability probe A→B`;
- payload token: `SWM-AGENTMAIL-E2E-20261008-A2B`;
- send action returned a message ID and sender-local thread ID;
- B independently listed one received thread;
- B's full thread read preserved:
  - `from = SWM Probe A <...a...>`;
  - `to = ...b...`;
  - exact token and body.

B -> A:
- B replied to the received message;
- reply token: `SWM-AGENTMAIL-E2E-20261008-B2A`;
- A then listed the conversation with:
  - both A and B in the sender set;
  - two messages;
  - exact reverse-path token visible in preview.

Cleanup:
- both temporary inboxes deleted successfully;
- final inbox count returned to **0**.

#### Important provider-local identity detail

The same logical email conversation had different AgentMail `threadId` values in the two inbox views:

- A-local thread ID: `984f4535-5809-47b8-b52f-c5d1fd91de44`;
- B-local thread ID: `833f9e7a-32f9-4227-a453-af66d178e775`.

The RFC-style message IDs were shared across sender/receiver observations.

Therefore:

> **provider-local thread identity is not automatically a global exchange identity.**

A future Medium must not use one inbox's `threadId` as universal conversation identity without an explicit correspondence layer.

#### Current reachability state

- DOCUMENTED: PASS;
- INSTALLED: PASS;
- PERMITTED: PASS bounded;
- EXPOSED TO FRESH EXECUTION BODY: **PASS**;
- PATH COMPLETE: **PASS**;
- EXECUTION PASS: **PASS**;
- EFFECT PASS: **PASS** for bounded two-inbox send/read/reply/read transport;
- OWNER/PRODUCT PASS: **NOT CLAIMED**.

#### What this actually qualifies

AgentMail now qualifies, in this bounded Browser context, as:

> **an agent-controllable transport/address identity substrate with real bidirectional message/thread provenance.**

It does **not** qualify:
- an independent second cognition;
- autonomous agent presence;
- cross-model ecological adoption;
- participant/mind continuity;
- a replacement for repository truth;
- a reason to add mailbox/session fields to Quiet Presence.

Both temporary inboxes were controlled by the same Browser agent.

This closes the transport-identity edge while leaving the independent-mind edge open.

## Live dogfood case — independent participant identity without transport collapse

This campaign now has one end-to-end dogfood case where the combined candidate-generation + reachability lens changed actual behavior.

### Pressure

Slack connector actions are attributed to the Owner account and marked as sent using ChatGPT.

The normal ChatGPT Slack bot exists as a distinct Slack bot user, but two connector-authored DM handshakes produced no independent bot response.

Current need:

> find a path toward independent participant/agent transport identity without pretending that app presence or connector authorship already supplies it.

### Candidate generation

Plugin discovery surfaced **AgentMail**, whose documented primitive is directly relevant:
- agent-owned inbox/address;
- send/receive/reply/thread;
- MCP/OAuth;
- low-cost/free bounded use.

This candidate did not require a global SWM capability registry.

### Reachability qualification

After Owner installation:
- plugin state: installed PASS;
- permission: inherited `Allow low-risk actions`;
- current execution body: no AgentMail tools exposed;
- known MCP tool names are not callable in this body.

Decision:

> STOP at EXPOSED-TO-CURRENT-BODY = FAIL.

No API-key request, no TinyFish workaround, no manual REST substitution and no claim that AgentMail "works for us" yet.

### Cold donor

A bounded repository-inventory scout surfaced dormant `cloudflare-multiplayer-lab`, absent from the recent Browser working set.

Its current qualified state defends:
- ActorSession lifetime != one browser transport;
- same ActorSession / NetEntity / WorldEpoch can survive bounded transport/page disruption;
- authority-checked resume;
- foreign profiles must not acquire session authority;
- world epoch may be retired independently;
- capacity errors != transport/handshake failures.

This changed the interpretation of the identity problem:

> a mailbox, Slack user, browser session or connector identity is a transport/address candidate, not automatically participant/mind identity.

### Receiving-project gate

Quiet Presence was then inspected on its own active campaign branch.

It currently:
- keeps participant perspective separate from shared artifact truth;
- keeps place-local interpretation separate again;
- uses a minimal `participant.json`;
- explicitly does **not** claim to solve live multi-agent presence.

Decision:

> **NO SCHEMA CHANGE.**

Do not add session/transport/mailbox fields merely because a donor exposes those distinctions.

Reopen only when SWM makes a real continuity claim across multiple bodies/transports/accounts.

### Why this matters

Without the combined lens, two plausible but bad moves were available:
1. continue setup/research until AgentMail is forced to work, repeating the Neon failure class;
2. import Multi_World identity/session concepts into Quiet Presence prematurely because the analogy is attractive.

The actual outcome was:
- useful candidate discovered;
- unreachable edge isolated cheaply;
- independent donor evidence recovered;
- architectural overreach rejected;
- future requalification point preserved.

This is a **POSITIVE BOUNDED operational result** for the method.

It does not prove the method generalizes or reduces Owner cost across projects.

## Main falsifier

This lens is unnecessary overhead if ordinary agents consistently distinguish documentation, exposure, permission, execution and external effect without it.

Current evidence strongly contradicts that optimistic assumption: the same category error has occurred across browser control, host bridges, Slack transport and agent integration.

## Current research consequence

Shared Work Medium's capability problem is at least two-dimensional:

1. **candidate generation** — does the right capability/project occur to the agent?
2. **reachability qualification** — once it occurs, is the claimed effect actually executable by the current body?

Solving only (1) can make the system worse by surfacing many attractive but unreachable capabilities.

A useful Medium should prefer:
- fewer, source-bound capability candidates;
- explicit body/permission seams;
- cheap end-to-end qualification;
- independent effect verification;

over a large global capability catalog.

