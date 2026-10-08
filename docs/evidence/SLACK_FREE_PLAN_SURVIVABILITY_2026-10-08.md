# Slack Free-Plan Survivability — 2026-10-08

**Status:** CURRENT PRODUCT-BOUNDARY CHECK · SOURCE-BOUND EVIDENCE · NOT ARCHITECTURE

## Question

The current workspace is on a paid-feature trial that will end unless upgraded.

The relevant research question is not:

> which Slack features are interesting during the trial?

It is:

> **which observed Slack affordances remain available on Free strongly enough that Shared Work Medium could depend on them without creating a paid-plan dependency?**

## Current official Free boundaries

Current Slack documentation states:

### Messages / files / retention

Free workspaces:
- expose/search only the most recent **90 days** of message/file history;
- may retain data for 90 days or one year;
- content older than one year is permanently deleted on Free;
- Slack may also apply high-volume message/file limits.

Sources:
- https://slack.com/help/articles/115002422943-Usage-limits-for-free-workspaces
- https://slack.com/help/articles/203457187-Customize-data-retention-in-Slack
- https://slack.com/pricing/free

Implication:

> Slack Free is not a durable evidence archive.

Durable project/research truth must remain in source repositories or another durable authority plane.

### Apps

Slack Free currently supports **up to 10 apps**.

Source:
- https://slack.com/pricing/free

This is enough for a bounded connector/app surface but not justification for building a many-app architecture.

### Lists

Lists are paid-plan functionality.

When downgrading to Free, existing Lists become read-only and no new Lists can be created.

Source:
- https://slack.com/help/articles/27204752526611-Feature-limitations-on-the-free-version-of-Slack

Implication:

> trial Lists are donor/prototype evidence only.

Do not make SWM depend on List mutability.

### Workflow Builder

Workflow Builder is available on paid plans.

When downgrading to Free, existing workflows stop working and new ones cannot be created.

Sources:
- https://slack.com/help/articles/360035692513-Guide-to-Slack-Workflow-Builder
- https://slack.com/help/articles/27204752526611-Feature-limitations-on-the-free-version-of-Slack

Implication:

> Slack-native workflow automation is not a Free foundation.

Any future event/trigger path must qualify independently from Slack Workflow Builder.

### Canvases

Current Slack product docs distinguish:
- standalone canvases: paid;
- Free: one canvas can exist for a channel or DM / conversation surface.

Sources:
- https://slack.com/help/articles/33536064287891-Manage-canvas-settings-in-Slack
- https://slack.com/help/articles/21290478840979-Feature-change-notice--Channel-canvases
- https://slack.com/help/articles/27204752526611-Feature-limitations-on-the-free-version-of-Slack

Important connector boundary:

The current ChatGPT Slack tool `slack_create_canvas` explicitly reports:

> Not available on free teams.

Therefore the specific Canvas creation path qualified during the trial is **not Free-safe** even though Slack itself retains a limited conversation-canvas concept.

Implication:

> current connector Canvas write capability is optional/paid donor evidence, not a required SWM surface.

## Free-safe core observed in this campaign

The campaign should assume only the smallest primitives that remain useful without the paid surfaces:

- public/private channels and DMs;
- ordinary messages;
- threads;
- reactions;
- message links;
- channel membership;
- lexical Slack search inside the available Free history window;
- normal app integrations within the Free app-count limit.

Each still needs its own connector/reachability qualification where material.

## What this changes

Earlier exploration tested:
- Lists;
- Canvases;
- Workflow Builder;
- rich Slack-native structure.

That work remains useful as donor evidence about:
- structured human/agent envelopes;
- task-like fields;
- private/public lifecycle;
- projection behavior;
- event-trigger ideas.

But the strongest current Medium direction no longer needs those features.

The current candidate-generation model increasingly relies on:
- project-local current-truth/front doors;
- ChatGPT sidebar/project topology;
- Opera current tabs + recent history;
- source-native GitHub PR/branch activity;
- cold repository inventory only under pressure;
- sparse Slack scents only when ordinary source-native surfaces leave a material gap.

This means Slack can degrade to a **thin peripheral transport/presence layer** without collapsing the research direction.

## Durability boundary

Because Free Slack cannot be relied on as long-horizon storage:

> **Slack message identity is a live/peripheral referent, not durable project truth.**

If a Slack observation becomes research-significant:
1. preserve the claim/evidence in the owning repository or another durable source;
2. keep the Slack message as ephemeral live context;
3. never require future recovery to depend on a >90-day Slack search result.

The one-year deletion boundary makes this architectural, not merely operational.

## Current decision

**PASS BOUNDED — the useful current SWM direction survives Slack Free, provided paid/trial features remain optional.**

Do not depend on:
- Lists;
- standalone Canvas creation through the current connector;
- Workflow Builder;
- unlimited Slack history;
- Slack as a durable archive.

Allowed Free-safe posture:

> Slack may supply temporary shared presence, threads, lightweight scents and human-readable peripheral interaction. Source repositories remain authority and long-term memory.

## Falsifier

This result should be reopened if:
- the ChatGPT Slack connector itself becomes unavailable on the actual Free workspace after trial end;
- connector permissions/tool exposure materially change after downgrade;
- a currently essential live use turns out to require a paid-only Slack object;
- Free message/search limits make even bounded peripheral use too unreliable.

The strongest requalification date is immediately after the real trial ends, using the same reachability chain rather than assuming documentation equals execution.
