from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DEFAULT_OUT = ROOT / "site"

SAFE_PASSIVE_MEDIA = {
    "text/markdown",
    "text/plain",
    "application/json",
}
SAFE_PASSIVE_SUFFIXES = {".md", ".txt", ".json"}


def esc(value):
    return html.escape(str(value))


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def page(lang: str, title: str, body: str):
    return f"""<!doctype html>
<html lang="{esc(lang)}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="icon" href="data:,">
<title>{esc(title)}</title>
<style>
:root {{ color-scheme: dark; }}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: #111214; color: #e8e8e8; font: 16px/1.55 system-ui, sans-serif; }}
a {{ color: #b7d7ff; }}
.wrap {{ max-width: 920px; margin: 0 auto; padding: 34px 22px 72px; }}
header {{ margin-bottom: 28px; }}
h1 {{ margin: 0 0 8px; font-size: 34px; }}
h2 {{ margin: 28px 0 10px; }}
.card, .note {{ border: 1px solid #30343a; border-radius: 12px; background: #181a1e; padding: 16px; margin: 12px 0; }}
.muted {{ color: #a6abb3; }}
code, pre {{ color: #c7cbd1; }}
pre {{ white-space: pre-wrap; overflow-wrap: anywhere; background: #15171a; border: 1px solid #343a43; border-radius: 9px; padding: 12px; }}
nav {{ margin-bottom: 24px; }}
footer {{ margin-top: 42px; color: #8f949c; font-size: 13px; }}
</style>
</head>
<body><main class="wrap">{body}</main></body>
</html>"""


def safe_slug(value: str):
    base = re.sub(r"[^A-Za-z0-9._-]+", "-", value).strip("-") or "object"
    digest = hashlib.sha256(value.encode("utf-8")).hexdigest()[:10]
    return f"{base[:60]}-{digest}"


def inside(root: Path, relative: str):
    rel = Path(relative)
    candidate = (root / rel).resolve()
    root_resolved = root.resolve()
    if rel.is_absolute() or ".." in rel.parts or not candidate.is_relative_to(root_resolved):
        raise ValueError(f"path escapes package boundary: {relative}")
    if not candidate.is_file():
        raise ValueError(f"declared package file does not exist: {relative}")
    return candidate


def copy_exact(src: Path, dst: Path):
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_bytes(src.read_bytes())


def record_summary(record: dict, relative_path: str):
    participant = record.get("participant_id")

    owner_scope = (
        record.get("owner_scope")
        if isinstance(record.get("owner_scope"), dict)
        else {}
    )
    from_scope = record.get("from") if isinstance(record.get("from"), dict) else {}
    scope_id = owner_scope.get("scope_id") or from_scope.get("scope_id")

    views = record.get("views") if isinstance(record.get("views"), dict) else {}
    owner_view = views.get("owner") if isinstance(views.get("owner"), dict) else {}

    if owner_view.get("title"):
        label = owner_view["title"]
    elif participant:
        label = f"Perspektywa uczestnika: {participant}"
    elif scope_id:
        label = f"Lokalny zapis: {scope_id}"
    else:
        label = f"Powiązany zapis: {relative_path}"

    texts = []
    if owner_view.get("summary"):
        texts.append(str(owner_view["summary"]))

    local_view = record.get("local_view")
    if isinstance(local_view, dict) and local_view.get("note"):
        texts.append(str(local_view["note"]))

    local_note = record.get("local_note")
    if isinstance(local_note, dict) and local_note.get("text"):
        texts.append(str(local_note["text"]))
    elif isinstance(local_note, str):
        texts.append(local_note)

    if record.get("text"):
        texts.append(str(record["text"]))

    # Preserve order while avoiding duplicate human-facing sentences.
    text = " — ".join(dict.fromkeys(x for x in texts if x)) or None

    relation = record.get("relation") if isinstance(record.get("relation"), dict) else {}
    semantic_hint = (
        record.get("relation_kind")
        or relation.get("kind")
        or record.get("perspective_kind")
        or record.get("record_kind")
        or record.get("kind")
    )

    return label, text, semantic_hint


def find_object_references(value, path="$"):
    refs = []
    if isinstance(value, dict):
        object_id = value.get("object_id")
        if isinstance(object_id, str) and object_id.strip():
            refs.append((f"{path}.object_id", object_id))
        for key, child in value.items():
            refs.extend(find_object_references(child, f"{path}.{key}"))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            refs.extend(find_object_references(child, f"{path}[{index}]"))
    return refs


def load_package(package_root: Path):
    package_root = package_root.resolve()
    object_path = package_root / "object.json"

    attached = []
    for item_path in sorted(package_root.rglob("*.json")):
        if item_path == object_path:
            continue
        relative = item_path.relative_to(package_root).as_posix()
        attached.append(
            {
                "path": item_path,
                "relative": relative,
                "data": read_json(item_path),
            }
        )

    if object_path.is_file():
        obj = read_json(object_path)
        object_id = obj.get("id")
        if not isinstance(object_id, str) or not object_id.strip():
            raise ValueError(f"package object has no stable string id: {package_root}")
        return {
            "role": "object",
            "root": package_root,
            "object_path": object_path,
            "object": obj,
            "id": object_id,
            "kind": obj.get("kind"),
            "attached": attached,
        }

    if not attached:
        raise ValueError(
            f"package has neither object.json nor JSON records: {package_root}"
        )

    return {
        "role": "records",
        "root": package_root,
        "object_path": None,
        "object": None,
        "id": None,
        "kind": None,
        "attached": attached,
    }


def record_package_slug(package):
    digest = hashlib.sha256()
    for item in package["attached"]:
        relative = item["relative"].encode("utf-8")
        digest.update(len(relative).to_bytes(8, "big"))
        digest.update(relative)
        data = item["path"].read_bytes()
        digest.update(len(data).to_bytes(8, "big"))
        digest.update(data)
    return f"records-{digest.hexdigest()[:16]}"


def prepare_records(packages, out_root: Path, object_ids):
    records_by_target = {object_id: [] for object_id in object_ids}
    manifest_records = []

    for package in packages:
        if package["role"] == "object":
            package_slug = safe_slug(package["id"])
            raw_base = out_root / "raw" / package_slug / "records"
        else:
            package_slug = record_package_slug(package)
            raw_base = out_root / "raw" / package_slug

        package_reference_count = 0

        for item in package["attached"]:
            references = []
            for field, target in find_object_references(item["data"]):
                references.append({"field": field, "object_id": target})

            unique_targets = []
            for ref in references:
                target = ref["object_id"]
                if target not in unique_targets:
                    unique_targets.append(target)

            for target in unique_targets:
                if target not in object_ids:
                    raise ValueError(
                        f"{item['relative']}: unresolved object identity {target!r}"
                    )

            package_reference_count += len(unique_targets)

            destination = raw_base / item["relative"]
            copy_exact(item["path"], destination)

            site_href = destination.relative_to(out_root).as_posix()
            record_info = {
                "relative": item["relative"],
                "site_href": site_href,
                "data": item["data"],
                "references": references,
                "source_package_role": package["role"],
                "source_package_slug": package_slug,
            }

            for target in unique_targets:
                records_by_target[target].append(record_info)

            manifest_records.append(
                {
                    "raw_href": site_href,
                    "relative": item["relative"],
                    "source_package_role": package["role"],
                    "source_package_slug": package_slug,
                    "references": references,
                }
            )

        if package["role"] == "records" and package_reference_count == 0:
            raise ValueError(
                f"record-only package has no object identity references: {package['root']}"
            )

    return records_by_target, manifest_records


def expose_passive_file(package, href: str, media_type: str | None, out_root: Path, slug: str, bucket: str):
    source = inside(package["root"], href)

    if media_type and media_type not in SAFE_PASSIVE_MEDIA:
        return {
            "status": "withheld",
            "reason": f"media type {media_type!r} is outside Phase 1 passive allowlist",
            "source": source,
        }

    if source.suffix.lower() not in SAFE_PASSIVE_SUFFIXES:
        return {
            "status": "withheld",
            "reason": f"suffix {source.suffix!r} is outside Phase 1 passive allowlist",
            "source": source,
        }

    relative = Path("raw") / slug / bucket / Path(href)
    destination = out_root / relative
    copy_exact(source, destination)

    return {
        "status": "copied",
        "source": source,
        "relative": relative.as_posix(),
    }


def build_package(package, out_root: Path, related_records):
    obj = package["object"]
    object_id = package["id"]
    kind = package["kind"]
    slug = safe_slug(object_id)

    raw_base = out_root / "raw" / slug
    copy_exact(package["object_path"], raw_base / "object.json")

    # Records keep the bytes/path of the package that owns them. The object view
    # only derives a local association through stable object_id references.
    raw_records = list(related_records)

    body_result = None
    body = obj.get("body")
    if isinstance(body, dict) and body.get("href"):
        execution = body.get("execution")
        if execution not in (None, "none", "passive"):
            body_result = {
                "status": "withheld",
                "reason": (
                    f"execution capability {execution!r} is not granted by "
                    "the Phase 1 passive adapter"
                ),
            }
        else:
            body_result = expose_passive_file(
                package,
                body["href"],
                body.get("media_type"),
                out_root,
                slug,
                "body",
            )

    provenance_results = []
    provenance = obj.get("provenance")
    if isinstance(provenance, list):
        for index, ref in enumerate(provenance):
            if not isinstance(ref, dict) or not ref.get("href"):
                continue
            href = ref["href"]
            if href.startswith("https://") or href.startswith("http://"):
                provenance_results.append(
                    {
                        "label": ref.get("label") or href,
                        "status": "external",
                        "href": href,
                        "declared_hash": ref.get("sha256"),
                    }
                )
                continue

            exposed = expose_passive_file(
                package,
                href,
                None,
                out_root,
                slug,
                f"source-{index}",
            )

            verified = None
            declared_hash = ref.get("sha256")
            if declared_hash:
                verified = (
                    hashlib.sha256(exposed["source"].read_bytes()).hexdigest()
                    == declared_hash
                )
                if not verified:
                    raise ValueError(
                        f"{object_id}: provenance hash mismatch for {href}"
                    )

            provenance_results.append(
                {
                    "label": ref.get("label") or href,
                    "status": exposed["status"],
                    "href": exposed.get("relative"),
                    "reason": exposed.get("reason"),
                    "declared_hash": declared_hash,
                    "verified": verified,
                    "language": ref.get("language"),
                }
            )

    views = obj.get("views") if isinstance(obj.get("views"), dict) else {}
    owner = views.get("owner") if isinstance(views.get("owner"), dict) else {}
    agent = views.get("agent") if isinstance(views.get("agent"), dict) else {}

    owner_title = owner.get("title") or object_id
    owner_summary = owner.get("summary") or (
        "Nieznana wcześniej forma zachowana przez ogólny widok Open Substrate."
    )
    agent_title = agent.get("title") or object_id

    record_cards = []
    for item in raw_records:
        label, text, semantic_hint = record_summary(
            item["data"], item["relative"]
        )
        semantic_html = (
            f'<p class="muted">Deklarowana semantyka: <code>{esc(semantic_hint)}</code></p>'
            if semantic_hint
            else ""
        )
        text_html = f"<p>{esc(text)}</p>" if text else ""
        record_cards.append(
            f"""<article class="note">
<strong>{esc(label)}</strong>
{text_html}
{semantic_html}
<p><a href="{esc(item['site_href'])}">Surowy zapis JSON</a></p>
</article>"""
        )

    body_html = '<p class="muted">Brak zadeklarowanej treści body.</p>'
    if body_result:
        if body_result["status"] == "copied":
            body_text = body_result["source"].read_text(encoding="utf-8")
            body_html = f"""<p><a href="{esc(body_result['relative'])}">Otwórz zachowaną treść</a></p>
<details><summary>Podgląd pasywnej treści</summary><pre>{esc(body_text)}</pre></details>"""
        else:
            body_html = (
                '<p class="muted">Treść istnieje, ale nie została wystawiona '
                f"w Phase 1: {esc(body_result['reason'])}</p>"
            )

    provenance_html = []
    for ref in provenance_results:
        if ref["status"] == "external":
            link = f'<a href="{esc(ref["href"])}">{esc(ref["label"])}</a>'
        elif ref["status"] == "copied":
            link = f'<a href="{esc(ref["href"])}">{esc(ref["label"])}</a>'
        else:
            link = esc(ref["label"])

        details = []
        if ref.get("language"):
            details.append(f"język źródła: {ref['language']}")
        if ref.get("verified") is True:
            details.append("SHA-256 zgodny")
        if ref.get("reason"):
            details.append(ref["reason"])

        suffix = (
            f' <span class="muted">({esc("; ".join(details))})</span>'
            if details
            else ""
        )
        provenance_html.append(f"<li>{link}{suffix}</li>")

    owner_filename = f"object-{slug}.html"
    technical_filename = f"object-{slug}-technical.html"

    owner_body = f"""
<nav><a href="index.html">← Open Substrate</a></nav>
<header>
<h1>{esc(owner_title)}</h1>
<p>{esc(owner_summary)}</p>
<p class="muted">To widok pochodny. Oryginalne dane i źródła pozostają osobno.</p>
</header>
<section class="card">
<strong>Tożsamość</strong>
<p><code>{esc(object_id)}</code></p>
<p class="muted">Deklarowany rodzaj: <code>{esc(kind if kind is not None else "brak")}</code></p>
</section>
<h2>Treść</h2>
{body_html}
<h2>Źródła</h2>
<ul>{''.join(provenance_html) if provenance_html else '<li>Brak zadeklarowanych źródeł.</li>'}</ul>
<h2>Powiązane lokalne i uczestnikowe zapisy</h2>
{''.join(record_cards) if record_cards else '<p class="muted">Brak dodatkowych zapisów.</p>'}
<h2>Głębiej</h2>
<p><a href="{technical_filename}">Dane techniczne / surowe</a></p>
<footer>Nieznany typ nie jest tutaj traktowany jako globalne znaczenie ani jako błąd sam w sobie.</footer>
"""
    (out_root / owner_filename).write_text(
        page("pl", owner_title, owner_body),
        encoding="utf-8",
    )

    object_raw = package["object_path"].read_text(encoding="utf-8")
    technical_records = "".join(
        f'<li><a href="{esc(item["site_href"])}">{esc(item["relative"])}</a></li>'
        for item in raw_records
    )
    technical_body = f"""
<nav><a href="{owner_filename}">← Owner view</a></nav>
<header>
<h1>{esc(agent_title)} — technical view</h1>
<p class="muted">Generic raw inspection. No behavior is dispatched from the declared kind.</p>
</header>
<p><strong>identity:</strong> <code>{esc(object_id)}</code></p>
<p><strong>declared kind:</strong> <code>{esc(kind if kind is not None else "null")}</code></p>
<p><a href="raw/{slug}/object.json">Exact object.json</a></p>
<h2>Exact object metadata</h2>
<pre>{esc(object_raw)}</pre>
<h2>Attached raw records</h2>
<ul>{technical_records if technical_records else '<li>None</li>'}</ul>
<footer>This page is derived. Raw package files remain the evidence surface.</footer>
"""
    (out_root / technical_filename).write_text(
        page("en", f"{agent_title} — technical view", technical_body),
        encoding="utf-8",
    )

    return {
        "id": object_id,
        "kind": kind,
        "owner_page": owner_filename,
        "technical_page": technical_filename,
        "raw_object": f"raw/{slug}/object.json",
        "slug": slug,
        "body": {
            key: value
            for key, value in (body_result or {}).items()
            if key not in {"source"}
        },
        "provenance": provenance_results,
        "record_count": len(raw_records),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--package",
        action="append",
        required=True,
        help="Explicit foreign package root. Repeat for multiple packages.",
    )
    parser.add_argument(
        "--out",
        default=str(DEFAULT_OUT),
        help="Generated Open Substrate output directory.",
    )
    args = parser.parse_args()

    out_root = Path(args.out).resolve()
    if out_root.exists():
        shutil.rmtree(out_root)
    out_root.mkdir(parents=True)

    packages = [load_package(Path(value)) for value in args.package]

    object_packages = [package for package in packages if package["role"] == "object"]
    ids = [package["id"] for package in object_packages]
    if not ids:
        raise SystemExit("at least one explicit package must contribute a shared object identity")
    if len(ids) != len(set(ids)):
        raise SystemExit("duplicate object identity across explicit package roots")

    object_ids = set(ids)
    records_by_target, manifest_records = prepare_records(
        packages, out_root, object_ids
    )

    manifest_objects = [
        build_package(
            package,
            out_root,
            records_by_target.get(package["id"], []),
        )
        for package in object_packages
    ]

    cards = []
    for item in manifest_objects:
        package = next(
            package
            for package in object_packages
            if package["id"] == item["id"]
        )
        views = package["object"].get("views")
        views = views if isinstance(views, dict) else {}
        owner = views.get("owner")
        owner = owner if isinstance(owner, dict) else {}
        title = owner.get("title") or item["id"]
        summary = owner.get("summary") or "Nieznana forma dostępna przez ogólny widok."
        cards.append(
            f"""<article class="card">
<h2>{esc(title)}</h2>
<p>{esc(summary)}</p>
<p class="muted">Rodzaj deklarowany: <code>{esc(item['kind'] if item['kind'] is not None else "brak")}</code></p>
<p><a href="{esc(item['owner_page'])}">Wejdź</a></p>
</article>"""
        )

    index_body = f"""
<header>
<h1>Open Substrate — laboratorium</h1>
<p>Kontrolowany widok do sprawdzania, czy Medium potrafi przyjmować nieprzewidziane formy bez udawania ekologicznej adopcji.</p>
<p class="muted">To nie jest nowa główna powierzchnia Medium ani następca Quiet Presence.</p>
</header>
{''.join(cards)}
<footer>Pakiety są w tej fazie podawane jawnie. Mechanizm globalnego odkrywania nie został jeszcze zaprojektowany.</footer>
"""
    (out_root / "index.html").write_text(
        page("pl", "Open Substrate — laboratorium", index_body),
        encoding="utf-8",
    )

    manifest = {
        "campaign": "open-substrate-2026-10-04",
        "derived": True,
        "discovery": "explicit package roots",
        "objects": manifest_objects,
        "records": manifest_records,
    }
    (out_root / "manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    print(json.dumps(manifest, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
