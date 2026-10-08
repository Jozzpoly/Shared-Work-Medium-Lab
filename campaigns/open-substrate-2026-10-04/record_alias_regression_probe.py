"""Regression: identical raw records with different declared targets must not alias.

Uses the real open_render.load_package + prepare_records path. Zero network,
zero source-repository mutation, output isolated to a temporary directory.
"""
import json
from pathlib import Path
from tempfile import TemporaryDirectory

from open_render import load_package, prepare_records, record_package_slug


def create_record_package(root: Path, target: str):
    root.mkdir(parents=True)
    (root / "observation.json").write_bytes(b'{"observation":"same facts"}\n')
    links = {"version": 1, "links": [
        {"record": "observation.json", "object_id": target}
    ]}
    (root / "medium.refs.json").write_text(
        json.dumps(links, indent=2) + "\n", encoding="utf-8"
    )
    return load_package(root)


def probe_distinct_refs(root: Path):
    first = create_record_package(root / "first", "object.A")
    second = create_record_package(root / "second", "object.B")
    assert first["attached"][0]["path"].read_bytes() == second["attached"][0]["path"].read_bytes()

    first_slug, second_slug = record_package_slug(first), record_package_slug(second)
    assert first_slug != second_slug, "different declared identities aliased one output slug"

    by_target, records = prepare_records(
        [first, second], root / "site", {"object.A", "object.B"}
    )
    assert len(records) == 2
    assert {r["source_package_slug"] for r in records} == {first_slug, second_slug}
    assert records[0]["raw_href"] != records[1]["raw_href"]
    assert records[0]["refs_href"] != records[1]["refs_href"]
    assert len(by_target["object.A"]) == len(by_target["object.B"]) == 1

    for record, target in zip(records, ("object.A", "object.B"), strict=True):
        persisted = json.loads((root / "site" / record["refs_href"]).read_text())
        assert persisted["links"] == [{"record": "observation.json", "object_id": target}]
        assert record["references"][0]["object_id"] == target
        assert (root / "site" / record["raw_href"]).read_bytes() == b'{"observation":"same facts"}\n'


def probe_exact_duplicate_fail_closed(root: Path):
    first = create_record_package(root / "duplicate-first", "object.A")
    second = create_record_package(root / "duplicate-second", "object.A")
    assert record_package_slug(first) == record_package_slug(second)
    out = root / "duplicate-out"
    try:
        prepare_records([first, second], out, {"object.A"})
    except ValueError as error:
        assert "alias the same output slug" in str(error), str(error)
    else:
        raise AssertionError("duplicate independent source packages were silently conflated")
    assert not out.exists(), "collision must be rejected before creating output"


if __name__ == "__main__":
    with TemporaryDirectory(prefix="swm-record-alias-") as temp:
        root = Path(temp)
        probe_distinct_refs(root)
        probe_exact_duplicate_fail_closed(root)
    print(
        "RECORD_ALIAS_REGRESSION_PASS: identical record bytes with different "
        "medium.refs.json remain separate; exact duplicate packages fail "
        "closed before output"
    )
