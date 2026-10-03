# Design Guardrails

These are active constraints for the campaign, not a final architecture.

## Protect the human-project system

Do not optimize model convenience at the cost of the Owner or the project.

A useful addition should improve the full Owner–agent–project loop.

## Environment over workflow scripting

Prefer a legible, addressable environment and composable capabilities.

Avoid encoding every useful procedure as a special workflow. The "Shinden criterion" is important: the environment should leave room for a capable model to discover something useful that we did not explicitly program.

## Rich sources over lossy replacement

Structure should point back to original conversations, commits, artifacts, captures, tests, and observations.

Do not silently replace them with a single canonical summary.

## Scope-aware truth

A claim, hypothesis, test result, Owner observation, and decision are not the same thing.

A mechanical PASS must not automatically become a product PASS.

Conflicting evidence may need to coexist.

## Persistence without bureaucracy

Material state should survive session loss, but ordinary work must not require ceremony for every minor action.

If the Owner has to maintain the ontology, the design has failed.

## Surface is not world

Browser chat, Codex threads, GitHub, Work, future UI, and future vendors are surfaces or substrates.

Do not make any one of them conceptually identical to the project world.

## Reversibility

Early choices should be cheap to replace.

Do not add a database, queue, hosting layer, event system, or private/public split merely because it may be useful later.

## Failure is ordinary

Interrupted sessions, stale context, retries, uncertain liveness, and partial execution are normal conditions.

The design should expose uncertainty instead of inventing completion.

## Public repository boundary

This repository can stay public and may eventually support open-source release.

Do not over-engineer secrecy, but do not accidentally make "everything must be public" an architectural assumption.

Private/source-specific layers remain allowed when evidence justifies them.
