// Standalone Node regression: node tests/keyboard-shortcuts.test.mjs
// Extract and directly exercise the exact keyboard event handler in portable-variant.html.
// Scoped JS-event contract, NOT an end-to-end browser test.
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';

const html = readFileSync(new URL('../portable-variant.html', import.meta.url), 'utf8');
const prefix = "document.addEventListener('keydown',e=>";
assert.equal(html.split(prefix).length, 2, 'Expected exactly one document-level keydown handler');
const after = html.slice(html.indexOf(prefix) + prefix.length);
const end = after.indexOf('\n});');
assert.ok(end > 0, 'Cannot isolate keyboard callback; review test extraction');
const callback = after.slice(0, end + 2); // { ... }
const keydown = new Function('e', 'choose', 'initial', '$', callback);

const cases = [
  ['typing r in JSON textarea', 'TEXTAREA', 'r', 'KeyR', {}, [0, 0, '', 0]],
  ['typing space in JSON textarea', 'TEXTAREA', ' ', 'Space', {}, [0, 0, '', 0]],
  ['typing 1 in input', 'INPUT', '1', 'Digit1', {}, [0, 0, '', 0]],
  ['button focus blocks reset', 'BUTTON', 'r', 'KeyR', {}, [0, 0, '', 0]],
  ['contenteditable blocks reset', 'SPAN', 'r', 'KeyR', {editing:true}, [0, 0, '', 0]],
  ['browser Ctrl+R is untouched', 'BODY', 'r', 'KeyR', {ctrlKey:true}, [0, 0, '', 0]],
  ['browser Alt+1 is untouched', 'BODY', '1', 'Digit1', {altKey:true}, [0, 0, '', 0]],
  ['IME composition is untouched', 'BODY', 'r', 'KeyR', {isComposing:true}, [0, 0, '', 0]],
  ['world-surface R still resets', 'BODY', 'r', 'KeyR', {}, [1, 0, '', 0]],
  ['world-surface Space still pauses', 'BODY', ' ', 'Space', {}, [0, 1, '', 1]],
  ['world-surface 1 chooses MUR', 'BODY', '1', 'Digit1', {}, [0, 0, 'wall', 0]],
  ['world-surface 2 chooses DŁUTO', 'BODY', '2', 'Digit2', {}, [0, 0, 'erase', 0]],
];

for (const [name, tagName, key, code, opts, expected] of cases) {
  const state = {reset:0,pause:0,tool:'',prevented:0};
  const target = {tagName,closest: () => (
    ['TEXTAREA','INPUT','SELECT','BUTTON'].includes(tagName) || opts.editing ? {} : null
  )};
  const e = {target,key,code,preventDefault(){state.prevented++},...opts};
  keydown(e, value => {state.tool=value}, () => {state.reset++},
    () => ({click(){state.pause++}}));
  assert.deepEqual([state.reset,state.pause,state.tool,state.prevented], expected, name);
  process.stdout.write('PASS  ' + name + '\n');
}
process.stdout.write('\n12/12 scoped keyboard-handler checks PASS. This does not qualify the full browser app.\n');
