from __future__ import annotations

import importlib.util
import json
import shutil
import tempfile
import unittest
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parent


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            self.hrefs.extend(value for key, value in attrs if key == "href")


class WindowBody(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        shutil.copy2(ROOT / "campaign.json", self.root / "campaign.json")
        for directory in ("places", "episodes", "artifacts", "sources", "participants"):
            shutil.copytree(ROOT / directory, self.root / directory)
        spec = importlib.util.spec_from_file_location("render_under_test", ROOT / "render.py")
        self.renderer = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.renderer)
        self.renderer.ROOT = self.root
        self.renderer.OUT = self.root / "site"
        artifact_file = self.root / "artifacts/codex-exchange-window.json"
        artifact = json.loads(artifact_file.read_text(encoding="utf-8"))
        artifact["body_href"] = "bodies/codex-exchange-window/index.html"
        artifact["body_availability"] = {"status": "recovered", "note": "Preserved episode"}
        artifact_file.write_text(json.dumps(artifact), encoding="utf-8")

    def test_guest_can_open_body_with_its_exact_source_data(self):
        # Catches a card that claims recovery but omits the actual body/link or its sources.
        body_dir = self.root / "bodies/codex-exchange-window"
        body_dir.mkdir(parents=True)
        body = b'<a href="../../artifact-codex-exchange-window.html">Return</a>'
        source = b'{"text":"An exact preserved message"}\n'
        (body_dir / "index.html").write_bytes(body)
        (body_dir / "data.json").write_bytes(source)
        self.renderer.main()
        parser = Links()
        parser.feed((self.renderer.OUT / "artifact-codex-exchange-window.html").read_text(encoding="utf-8"))
        self.assertIn("bodies/codex-exchange-window/index.html", parser.hrefs)
        self.assertEqual((self.renderer.OUT / "bodies/codex-exchange-window/index.html").read_bytes(), body)
        self.assertEqual((self.renderer.OUT / "bodies/codex-exchange-window/data.json").read_bytes(), source)

    def test_missing_body_cannot_be_published_as_recovered(self):
        # Catches an available-status claim that silently produces a broken door.
        with self.assertRaisesRegex(SystemExit, "body"):
            self.renderer.main()

    def test_public_return_door_resolves_in_the_generated_site(self):
        # Catches navigation back to a public snapshot name absent from the local site.
        body_dir = self.root / "bodies/codex-exchange-window"
        body_dir.mkdir(parents=True)
        (body_dir / "index.html").write_text(
            '<a data-medium-return href="../../field-artifact-codex-exchange-window.html">Return</a>',
            encoding="utf-8",
        )
        self.renderer.main()
        parser = Links()
        parser.feed((self.renderer.OUT / "bodies/codex-exchange-window/index.html").read_text(encoding="utf-8"))
        self.assertIn("../../artifact-codex-exchange-window.html", parser.hrefs)

    def test_body_must_stay_inside_the_campaign_body_directory(self):
        # Catches accidental copying of unrelated repository files as artifact bodies.
        artifact_file = self.root / "artifacts/codex-exchange-window.json"
        artifact = json.loads(artifact_file.read_text(encoding="utf-8"))
        artifact["body_href"] = "../../README.md"
        artifact_file.write_text(json.dumps(artifact), encoding="utf-8")
        with self.assertRaisesRegex(SystemExit, "body"):
            self.renderer.main()


if __name__ == "__main__":
    unittest.main()
