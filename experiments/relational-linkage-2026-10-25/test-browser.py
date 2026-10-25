"""Real Chromium DOM/canvas/export/import smoke for the exact standalone ŁĄCZNIK HTML.
Uses set_content to avoid requiring navigation or network access.
This DOES NOT prove Jaskinia embedding, Chrome URL hosting, a real phone, or Owner acceptance.
Run: python test-browser.py  (pip install playwright + a Chromium binary)
CHROMIUM_PATH may override /usr/bin/chromium.
"""
from pathlib import Path
from tempfile import TemporaryDirectory
from playwright.sync_api import sync_playwright
import json, os

HTML = Path(__file__).with_name("workbench.html").read_text(encoding="utf-8")
checks = []
def check(label, value):
    if not value:
        raise AssertionError(label)
    checks.append(label)

def at_world(page, x, y):
    b = page.locator("#stage").bounding_box()
    scale = min(b["width"] / 1000, b["height"] / 650)
    return (b["x"] + (b["width"] - 1000 * scale) / 2 + x * scale,
            b["y"] + (b["height"] - 650 * scale) / 2 + y * scale)

with TemporaryDirectory(prefix="lacznik-browser-") as temp:
    with sync_playwright() as playwright:
        binpath = os.environ.get("CHROMIUM_PATH", "/usr/bin/chromium")
        opts = {"headless": True, "args": ["--no-sandbox"]}
        if Path(binpath).exists():
            opts["executable_path"] = binpath
        browser = playwright.chromium.launch(**opts)
        context = browser.new_context(viewport={"width": 1280, "height": 720}, accept_downloads=True)
        page = context.new_page()
        errors = []
        page.on("pageerror", lambda error: errors.append(str(error)))
        page.set_content(HTML, wait_until="domcontentloaded")
        m = "window.LINKAGE_TEST_ACCESS.model"
        check("Chrome boot paused authored mechanism", page.evaluate(f"{m}.nodes.length===4 && !{m}.running"))
        check("distinct export controls", page.get_by_role("button", name="Zapisz projekt").count() == 1 and
              page.get_by_role("button", name="Zapisz pozę").count() == 1)
        initial = page.evaluate(f"{m}.authored()")
        page.get_by_role("button", name="Uruchom").click()
        page.wait_for_timeout(850)
        check("genuine RAF simulation", page.evaluate(f"{m}.t>0.2"))
        check("passive physics leaves authored source frozen", page.evaluate(f"{m}.authored()") == initial)
        page.get_by_role("button", name="+ Punkt").click()
        x, y = at_world(page, 850, 530)
        page.mouse.click(x, y)
        authored = page.evaluate(f"{m}.authored()")
        check("actual pointer adds node", len(authored["points"]) == 5)
        check("source ignores incidental motion of other nodes", authored["points"][:4] == initial["points"])
        paths = []
        for label, kind, filename in [("Zapisz projekt", "design", "lacznik-projekt.json"),
                                      ("Zapisz pozę", "pose", "lacznik-poza.json")]:
            with page.expect_download() as pending:
                page.get_by_role("button", name=label).click()
            item = pending.value
            output = Path(temp) / filename
            item.save_as(output)
            data = json.loads(output.read_text(encoding="utf-8"))
            check(f"real download type {kind}", item.suggested_filename == filename and data["kind"] == kind)
            paths.append((output, data))
        designfile, project = paths[0]
        posefile, pose = paths[1]
        check("design differs from runtime pose", abs(project["document"]["points"][1]["x"] -
                                                      pose["document"]["points"][1]["x"]) > 5)
        page.locator("#import").set_input_files(str(designfile))
        page.wait_for_timeout(60)
        check("real import recovers design source", page.evaluate(f"{m}.authored().points.length===5 && {m}.node(2).x===290 && !{m}.running"))
        page.locator("#import").set_input_files(str(posefile))
        page.wait_for_timeout(60)
        check("real import recovers pose as paused new start", page.evaluate(f"{m}.t===0 && !{m}.running") and
              abs(page.evaluate(f"{m}.node(2).x") - pose["document"]["points"][1]["x"]) < 0.0001)
        forged = json.loads(json.dumps(project))
        forged["document"]["rods"][0]["a"] = 9999
        forgedfile = Path(temp) / "forged.json"
        forgedfile.write_text(json.dumps(forged), encoding="utf-8")
        previous = page.evaluate(f"JSON.stringify({m}.authored())")
        page.locator("#import").set_input_files(str(forgedfile))
        page.wait_for_timeout(60)
        check("forged import does not overwrite current work", page.evaluate(f"JSON.stringify({m}.authored())") == previous and
              "Nie udało się" in page.locator("#status").inner_text())
        check("no desktop JavaScript errors", not errors)
        other = context.new_page()
        other.set_content(HTML, wait_until="domcontentloaded")
        other.locator("#import").set_input_files(str(designfile))
        other.wait_for_timeout(60)
        check("independent fresh browser reads same authored data",
              other.evaluate(f"{m}.authored().points.length===5 && {m}.rods.length===3"))
        other.get_by_role("button", name="Połącz").click()
        for index in (3, 5):
            coord = other.evaluate("(id)=>{const n=window.LINKAGE_TEST_ACCESS.model.node(id);return [n.x,n.y]}", index)
            x, y = at_world(other, *coord)
            other.mouse.click(x, y)
        check("independent browser extends graph with preserved IDs", other.evaluate(
            f"{m}.authored().rods.length===4 && {m}.authored().points.map(p=>p.id).join(',')==='1,2,3,4,5'"))
        mobile_ctx = browser.new_context(viewport={"width": 390, "height": 844},
                                         is_mobile=True, has_touch=True, device_scale_factor=2)
        mobile = mobile_ctx.new_page()
        mobile_errors = []
        mobile.on("pageerror", lambda error: mobile_errors.append(str(error)))
        mobile.set_content(HTML, wait_until="domcontentloaded")
        bounds = mobile.locator("#stage").bounding_box()
        check("mobile canvas exists", bounds["width"] > 300 and bounds["height"] > 250)
        mobile.get_by_role("button", name="+ Punkt").tap()
        x, y = at_world(mobile, 780, 400)
        mobile.touchscreen.tap(x, y)
        check("Chromium touch creates node", mobile.evaluate(f"{m}.nodes.length===5"))
        mobile.get_by_role("button", name="Połącz").tap()
        for index in (3, 5):
            coord = mobile.evaluate("(id)=>{const n=window.LINKAGE_TEST_ACCESS.model.node(id);return [n.x,n.y]}", index)
            x, y = at_world(mobile, *coord)
            mobile.touchscreen.tap(x, y)
        check("Chromium touch creates relation", mobile.evaluate(f"{m}.rods.length===4"))
        check("no mobile JavaScript errors", not mobile_errors)
        print(json.dumps({"pass": len(checks), "checks": checks, "qualifier":
            "Exact source in headless Chromium set_content; no actual Jaskinia host and no physical mobile or Owner test."},
            ensure_ascii=False, indent=2))
        browser.close()
