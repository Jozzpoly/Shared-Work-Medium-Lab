# AGENTS.md

This repository is an experimental lab for **Shared Work Medium (SWM)**.

Your first responsibility is to recover the real project state from the repository rather than relying on a prompt summary.

## Start here

1. Read `START_HERE.md`.
2. Read `docs/RESEARCH_STATE.md`.
3. Read `docs/NORTH_STAR.md` and `docs/DESIGN_GUARDRAILS.md` when direction or scope is material.
4. Inspect the current live work object(s), beginning with GitHub Issue #1 while it remains the active frontier.

## Working contract

- Treat repository state as authority for repository facts.
- Distinguish established evidence, hypotheses, Owner observations, and decisions.
- A machine/test PASS is only valid for the scope it actually tests.
- Do not overwrite experiential/product-level Owner feedback with narrower mechanical evidence.
- Prefer exact repository paths, commits, issues, PRs, and artifacts over prose context copying.
- Preserve links to rich sources instead of replacing them with one canonical summary.
- Keep changes small, reversible, and justified by observed collaboration friction.
- Do not invent infrastructure because it might be useful later.
- Do not turn GitHub Issues or documents into a project-manager bureaucracy the Owner must maintain.
- Do not hardcode Browser→Codex as the architecture. It is only the first live collaboration specimen.
- If the smallest valid result is "no code is needed yet", say so and explain why.

## Owner burden

A central success criterion is reducing the amount of context transfer, routing, recovery, and technical administration the Owner must do.

Do not ask the Owner to make low-level technical choices when you can investigate and make a reversible engineering judgement yourself.

Escalate to the Owner when the question genuinely depends on:
- product feel,
- experiential judgement,
- vision,
- priorities,
- meaningful trade-offs in project direction.

## Current research posture

The current leading hypothesis is:

> a thin shared epistemic spine — shared referents, recoverable orientation, source/authority lineage — coupled to at least one real agent-native capability bridge.

This is **not** a frozen architecture.

The repository is intentionally being used as the first self-hosting substrate. Learn from its friction before proposing a database, MCP server, Cloudflare deployment, event system, or richer UI.

## Before material implementation

Ask yourself:

- What concrete friction does this remove?
- Does it increase real capability or only add organization?
- Does it reduce Owner burden?
- Could existing GitHub/repository primitives already do the job?
- Is this preserving freedom and composability?
- Can this choice be replaced cheaply later?

If those answers are weak, stop and investigate before building.
