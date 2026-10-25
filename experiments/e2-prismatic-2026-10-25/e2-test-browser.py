"""E2 interactive witness in genuine headless Chromium (set_content, no network).
Run: python e2-test-browser.py  (requires playwright and Chromium).
The right-hand scene is an analytic reference, NOT a second physical solver.
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
  page.get_by_role('button',name='Uruchom').click()
  check(label+' run state',page.evaluate('E2_PROBE.state.playing'))
  page.evaluate('E2_PROBE.step(720)')
  state=page.evaluate('E2_PROBE.state')
  check(label+' missing guide causes drift',state['maxDrift']>120)
  check(label+' analytic guide remains exact',state['idealEnd']['y']==260)
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
print(json.dumps({'passed':len(passed),'checks':passed,'limit':'Chrome set_content of exact standalone HTML. No Jaskinia host, no physical phone, no Owner acceptance, no second physics engine.'},ensure_ascii=False,indent=2))
