"""E2 interactive witness in genuine headless Chromium (set_content, no network).
Run: python e2-test-browser.py  (requires playwright and Chromium).
Both scenes use the original ŁĄCZNIK PBD; the right adds one explicit prismatic rail projection.
"""
from pathlib import Path
import os, json
from playwright.sync_api import sync_playwright
source=Path(__file__).with_name('e2-rail-witness.html').read_text(encoding='utf8')
passed=[]
def check(name,condition):
 if not condition: raise AssertionError(name)
 passed.append(name)
def xy(page,selector,x,y):
 box=page.locator(selector).bounding_box()
 return box['x']+x*box['width']/700,box['y']+y*box['height']/440
with sync_playwright() as pw:
 kw={'headless':True,'args':['--no-sandbox']}
 if Path(os.environ.get('CHROMIUM_PATH','/usr/bin/chromium')).exists(): kw['executable_path']=os.environ.get('CHROMIUM_PATH','/usr/bin/chromium')
 browser=pw.chromium.launch(**kw)
 for label,viewport in [('desktop',{'width':1300,'height':800}),('mobile-emulated',{'width':390,'height':844})]:
  page=browser.new_page(viewport=viewport)
  errors=[]
  page.on('pageerror',lambda e:errors.append(str(e)))
  page.set_content(source,wait_until='domcontentloaded')
  state=page.evaluate('E2_PROBE.state')
  check(label+' initial mechanism',state['time']==0 and state['guideY']==260)
  check(label+' two visible canvases',page.locator('canvas').count()==2 and all(page.locator('canvas').nth(i).bounding_box()['width']>300 for i in (0,1)))
  page.evaluate('E2_PROBE.step(120)')
  manual=page.evaluate('E2_PROBE.state')
  check(label+' paused diagnostic steps both runtimes',manual['time']>0.9 and not manual['playing'])
  check(label+' diagnostic retains identical motor',abs(manual['crank']['x']-manual['guideCrank']['x'])<1e-8 and abs(manual['crank']['y']-manual['guideCrank']['y'])<1e-8)
  check(label+' diagnostic guide remains constrained',abs(manual['idealEnd']['y']-260)<1e-8)
  page.get_by_role('button',name='Reset').click()
  page.get_by_role('button',name='Uruchom').click()
  check(label+' run state',page.evaluate('E2_PROBE.state.playing'))
  page.evaluate('E2_PROBE.step(720)')
  state=page.evaluate('E2_PROBE.state')
  check(label+' missing guide causes drift',state['maxDrift']>120)
  check(label+' guided PBD constraint stays on rail',state['idealEnd']['y']==260)
  check(label+' guided PBD length constraint remains satisfied',state['guidedRodStrain']<2)
  check(label+' same crank input in both models',abs(state['crank']['x']-state['guideCrank']['x'])<1e-6 and abs(state['crank']['y']-state['guideCrank']['y'])<1e-6)
  check(label+' native distance constraints remain satisfied',state['maxStrain']<2)
  page.get_by_role('button',name='Pauza').click()
  page.locator('#guide').fill('230')
  page.locator('#guide').dispatch_event('input')
  state=page.evaluate('E2_PROBE.state')
  check(label+' reference guide is adjustable',state['guideY']==230 and state['idealEnd']['y']==230)
  page.get_by_role('button',name='Reset').click()
  check(label+' reset does not inherit time',page.evaluate('E2_PROBE.state.time')==0)
  if label=='desktop':
   x,y=xy(page,'#free',400,260);page.mouse.move(x,y);page.mouse.down()
   a,b=xy(page,'#free',455,298);page.mouse.move(a,b,steps=5);page.mouse.up()
   check('desktop real drag changes free material endpoint',abs(page.evaluate('E2_PROBE.state.freeEnd.x')-400)>30)
   check('free drag did not invent rail',page.evaluate('E2_PROBE.state.guideY')==230)
   x,y=xy(page,'#guided',310,230);page.mouse.move(x,y);page.mouse.down()
   a,b=xy(page,'#guided',310,204);page.mouse.move(a,b,steps=5);page.mouse.up()
   check('desktop real guide drag controls analytical rail',page.evaluate('E2_PROBE.state.guideY')==204)
  check(label+' no uncaught errors',not errors)
  page.close()
 browser.close()
print(json.dumps({'passed':len(passed),'checks':passed,'limit':'Chrome set_content of exact standalone HTML. Same ŁĄCZNIK PBD solver + one rail constraint, not a full rigid-body physics engine. No Jaskinia host, physical phone or Owner acceptance.'},ensure_ascii=False,indent=2))
