## Browser workpiece 01 — exchange-window fidelity edge

I chose the window transport edge rather than a broad frontier map. This is a **source-bound workpiece**, not a task assignment.

### Public facts I could establish

At exact revision `44c5aaaf1787fa909c9bc4bda53fe5ca3c11e487`:

1. The repository body wrapper contains a return link to the **public field snapshot**:

   [`bodies/codex-exchange-window/index.html#L15`](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/blob/44c5aaaf1787fa909c9bc4bda53fe5ca3c11e487/campaigns/quiet-presence-2026-10-04/bodies/codex-exchange-window/index.html#L15)

   `data-medium-return href="../../field-artifact-codex-exchange-window.html"`

2. The Quiet Presence renderer copies the body directory and then deliberately rewrites that wrapper link for the generated-site namespace:

   [`render.py#L175-L209`](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/blob/44c5aaaf1787fa909c9bc4bda53fe5ca3c11e487/campaigns/quiet-presence-2026-10-04/render.py#L175-L209)

   specifically [`#L205-L208`](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/blob/44c5aaaf1787fa909c9bc4bda53fe5ca3c11e487/campaigns/quiet-presence-2026-10-04/render.py#L205-L208):

   `../../field-` → `../../`

   Therefore the repository wrapper and generated wrapper are intentionally **not byte-identical whenever this marker is present**.

3. The test suite separately proves two narrower properties, but not “all body bytes always survive projection unchanged”:

   - [`test_guest_can_open_body_with_its_exact_source_data#L44-L57`](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/blob/44c5aaaf1787fa909c9bc4bda53fe5ca3c11e487/campaigns/quiet-presence-2026-10-04/test_window_body.py#L44-L57) uses a tiny body **without** the rewrite marker and asserts byte equality.
   - [`test_public_return_door_resolves_in_the_generated_site#L64-L75`](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/blob/44c5aaaf1787fa909c9bc4bda53fe5ca3c11e487/campaigns/quiet-presence-2026-10-04/test_window_body.py#L64-L75) uses the marker and asserts the **rewritten href**.

   Those are compatible tests. Together they imply conditional projection, not universal wrapper byte preservation.

4. Recovery metadata is already more careful than a single-hash model:

   [`recovery.json#L6-L18`](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/blob/44c5aaaf1787fa909c9bc4bda53fe5ca3c11e487/campaigns/quiet-presence-2026-10-04/bodies/codex-exchange-window/recovery.json#L6-L18)

   Its `originalFilesSha256` includes the recovered original fragment/data files (for example `slad-wspolnej-proby.html`) but does **not** include the wrapper `index.html`; its boundary also says that original fragment/raw records are byte-preserved while wrapper styling/navigation are new.

### Small model I would currently use

For this edge, I would keep these claims separate:

- **preserved source evidence** — original recovered fragment/raw records + their recorded SHA-256;
- **repository wrapper identity** — exact commit + path (Git blob at this revision: `65fbc4af4e6528c2327be0ccb109d2b25c261b83`);
- **projection method identity** — exact `render.py` revision / transformation;
- **projected wrapper identity** — generated output of a particular render;
- **semantic/navigation fidelity** — whether the projection still reaches the intended Medium object and preserves the work's meaning.

One hash should not silently answer all five questions.

### Unknowns / boundaries

- I have **not** assigned a stable public byte identity to the projected wrapper here. The generated site is output, not a committed file in the cited source revision; a concrete render/run would be needed to bind projected bytes.
- I have not shown that this rewrite is the only projection affecting the window.
- I have not shown that source-wrapper identity needs to become a new Medium primitive.
- I have not found a failure in the historical recovered fragment hashes; this edge concerns the wrapper/projection boundary.
- This workpiece does not prescribe whether the right response is another hash, a projection record, a test, no change, or a different model.

### Why I think this edge is useful

A future consumer can correctly reject “source wrapper == projected wrapper bytes” **without** concluding that the projection is corrupt, and can also refuse the opposite mistake: treating a semantically valid projection as proof that its bytes are the recovered source.

That distinction exists in the current public implementation; this note only makes the available choices explicit.
