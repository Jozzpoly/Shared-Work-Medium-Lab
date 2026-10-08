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

## Permission-state snapshot

Live Plugin Management inspection on 2026-10-08:

- global default: **Allow low-risk actions**;
- Slack: **Use my default**;
- GitHub: **Allow all actions**;
- Opera Browser Connector: **Allow all actions**.

These settings are account/runtime state, not architectural assumptions.

Important consequence:

> "permission denied" and "capability missing" must be diagnosed separately.

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

