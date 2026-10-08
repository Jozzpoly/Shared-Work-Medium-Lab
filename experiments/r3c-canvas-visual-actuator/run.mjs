import { chromium } from 'playwright';
import { PNG } from 'pngjs';
import { createHash } from 'node:crypto';
import { mkdir, writeFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import path from 'node:path';

const URL = 'https://jozzpoly.github.io/ReflexBrain-Lab/probes/medium-d-r3c-shadow-fork.html';
const dir = path.join(path.dirname(fileURLToPath(import.meta.url)), 'evidence');
await mkdir(dir, { recursive: true });

const result = {
  kind: 'single-remote-visual-canvas-actuator-probe',
  target: URL,
  startedAt: new Date().toISOString(),
  claimLimit: 'This tests a scripted remote browser controller against one public R3C session, not autonomous discovery, an Owner UX pass, organism cognition, or stable deployment parity.',
  observations: {},
  errors: [],
  verdict: 'UNRESOLVED'
};
const save = async () => writeFile(path.join(dir, 'result.json'), JSON.stringify(result, null, 2));

let browser;
let page;
try {
  browser = await chromium.launch({ headless: true });
  page = await browser.newPage({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1 });
  page.on('pageerror', e => result.errors.push('pageerror: ' + String(e).slice(0, 300)));

  const response = await page.goto(URL, { waitUntil: 'domcontentloaded', timeout: 45000 });
  result.observations.httpStatus = response?.status() ?? null;
  result.observations.documentTitle = await page.title();
  result.observations.renderedHtmlSha256 = createHash('sha256').update(await page.content()).digest('hex');
  await page.locator('#tick').waitFor({ timeout: 20000 });
  await page.waitForTimeout(1000);

  if (!(await page.locator('#mark').isVisible())) throw new Error('MARK control invisible');
  await page.locator('#mark').click();
  result.observations.markStatus = await page.locator('#status').innerText();
  result.observations.markTick = await page.locator('#markTick').innerText();

  // Force a >240-tick gap as a human-scale fork-pressure condition.
  await page.waitForTimeout(3700);
  if (!(await page.locator('#fork').isVisible())) throw new Error('FORK control invisible');
  await page.locator('#fork').click();
  result.observations.forkStatus = await page.locator('#status').innerText();
  result.observations.forkAge = await page.locator('#markAge').innerText();
  result.observations.preGestureSync = await page.locator('#sync').innerText();
  result.observations.preGestureTicks = {
    a: await page.locator('#tickA').innerText(),
    b: await page.locator('#tickB').innerText()
  };

  const canvas = page.locator('#world');
  const img = PNG.sync.read(await canvas.screenshot({ path: path.join(dir, 'before-canvas.png') }));
  let n = 0, sx = 0, sy = 0;
  // The loose-body outline is #72e4de. Inspect rendered pixels only;
  // do NOT read actor/world internals or call simulation methods.
  for (let y = 0; y < img.height; y++) {
    for (let x = 0; x < img.width; x++) {
      const p = (y * img.width + x) * 4;
      const r = img.data[p], g = img.data[p + 1], b = img.data[p + 2], alpha = img.data[p + 3];
      if (alpha > 220 && Math.abs(r - 114) < 27 && Math.abs(g - 228) < 27 && Math.abs(b - 222) < 27) {
        n++; sx += x; sy += y;
      }
    }
  }
  result.observations.cyanPixelCount = n;
  result.observations.canvasPixels = { width: img.width, height: img.height };
  if (n < 35) throw new Error('No reliable cyan loose-body stroke in canvas screenshot');

  const xLocal = sx / n, yLocal = sy / n;
  const rect = await canvas.boundingBox();
  if (!rect) throw new Error('Visible canvas lacks bounding rectangle');
  // Device-scale factor is 1; screenshot and CSS coordinates correspond.
  const x = rect.x + xLocal, y = rect.y + yLocal;
  result.observations.dragFrom = { xLocal, yLocal, xAbsolute: x, yAbsolute: y };
  result.observations.dragTo = { xAbsolute: x + 82, yAbsolute: y - 24 };

  // Playwright's native mouse produces real pointerdown/move/up
  // on the live canvas. No direct mutation of app state.
  await page.mouse.move(x, y);
  await page.mouse.down();
  await page.mouse.move(x + 82, y - 24, { steps: 9 });
  await page.mouse.up();
  await page.waitForTimeout(500);

  result.observations.releaseStatus = await page.locator('#status').innerText();
  result.observations.ribbonVisible = await page.locator('#ribbon').isVisible();
  result.observations.interventionTick = await page.locator('#impulseTick').innerText();
  result.observations.divergenceTick = await page.locator('#divTick').innerText();
  result.observations.postGestureSync = await page.locator('#sync').innerText();
  await page.screenshot({ path: path.join(dir, 'after-gesture.png'), fullPage: true });

  const didRelease = /RELEASE \/ IMPULSE/.test(result.observations.releaseStatus);
  const didDiverge = result.observations.divergenceTick !== '—' && Number(result.observations.divergenceTick) > 0;
  if (!didRelease || !didDiverge) throw new Error('No source-visible confirmed release + material divergence');

  if (!(await page.locator('#compare').isVisible())) throw new Error('COMPARE remains invisible despite confirmed divergence');
  await page.locator('#compare').click();
  result.observations.compareStatus = await page.locator('#status').innerText();
  result.observations.compareViewVisible = await page.locator('#compareView').isVisible();
  await page.screenshot({ path: path.join(dir, 'compare-ab.png'), fullPage: true });
  if (!result.observations.compareViewVisible || !/COMPARE/.test(result.observations.compareStatus)) {
    throw new Error('No visible A/B comparison');
  }

  await page.locator('#compare').click();
  result.observations.returnStatus = await page.locator('#status').innerText();
  result.observations.returnedToSingleWorld = await page.locator('#singleView').isVisible();
  if (!result.observations.returnedToSingleWorld || !/HABITAT/.test(result.observations.returnStatus)) {
    throw new Error('No confirmed return to the live single-world view');
  }
  result.verdict = 'PASS_SCOPED_REAL_VISUAL_GESTURE';
} catch (error) {
  result.verdict = 'FAIL_OR_INCONCLUSIVE';
  result.errors.push(String(error.stack || error).slice(0, 1400));
  if (page) {
    try { await page.screenshot({ path: path.join(dir, 'failure.png'), fullPage: true }); } catch {}
  }
  process.exitCode = 1;
} finally {
  result.finishedAt = new Date().toISOString();
  await save();
  try { await browser?.close(); } catch {}
  console.log('R3C_VISUAL_ACTUATOR_RESULT ' + JSON.stringify(result));
}
