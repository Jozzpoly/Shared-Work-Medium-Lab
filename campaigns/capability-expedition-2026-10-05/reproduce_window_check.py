"""Source-bound exploratory check for the existing exchange window.

Read exact public Git blobs using one native batch process. Optionally compare
an actually observed local preview. This is research apparatus, not product code.
It does not authenticate the historical ChatGPT export or prove semantic fidelity.
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path, PurePosixPath
import subprocess
from urllib.request import urlopen

SOURCE_REF = "44c5aaaf1787fa909c9bc4bda53fe5ca3c11e487"
PREFIX = "campaigns/quiet-presence-2026-10-04/"
BODY = "bodies/codex-exchange-window/"
OLD = 'data-medium-return href="../../field-'
NEW = 'data-medium-return href="../../'

def sha(data):
    return hashlib.sha256(data).hexdigest()

class GitBlobs:
    def __init__(self, repo):
        self.repo = Path(repo).resolve()
        self.process = subprocess.Popen(
            ["git", "-c", f"safe.directory={self.repo.as_posix()}", "-C",
             str(self.repo), "cat-file", "--batch"],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        )
        self.reads = 0
        self.bytes = 0
        self.paths = []

    def read(self, relative):
        query = f"{SOURCE_REF}:{PREFIX}{relative}"
        if "\n" in query or "\r" in query:
            raise ValueError("Git request must occupy one line")
        self.process.stdin.write((query + "\n").encode())
        self.process.stdin.flush()
        header = self.process.stdout.readline().decode().strip().split()
        if len(header) != 3 or header[1] != "blob":
            raise ValueError(f"Public source is unavailable: {relative}")
        size = int(header[2])
        data = self.process.stdout.read(size)
        if len(data) != size or self.process.stdout.read(1) != b"\n":
            raise ValueError("Incomplete Git blob response")
        self.reads += 1
        self.bytes += size
        self.paths.append(relative)
        return data

    def close(self):
        self.process.stdin.close()
        self.process.wait(timeout=10)

def project_wrapper(source, renderer):
    source_text = source.decode("utf-8").replace("\r\n", "\n").replace("\r", "\n")
    renderer_text = renderer.decode("utf-8")
    # Verify that the method exists in the pinned source before applying it.
    if OLD not in renderer_text or NEW not in renderer_text:
        raise ValueError("Pinned renderer does not contain the declared rewrite")
    if source_text.count(OLD) != 1:
        raise ValueError("This workpiece only covers the single return-door marker")
    return source_text.replace(OLD, NEW).encode("utf-8")

def check(repo, served_base=None):
    blobs = GitBlobs(repo)
    http_reads = 0
    http_bytes = 0
    def observe(relative):
        nonlocal http_reads, http_bytes
        if not served_base:
            return None
        with urlopen(served_base.rstrip("/") + "/" + relative, timeout=20) as response:
            if response.status != 200:
                raise ValueError(f"Preview did not return a file: {relative}")
            data = response.read()
        http_reads += 1
        http_bytes += len(data)
        return data
    try:
        source = blobs.read(BODY + "index.html")
        renderer = blobs.read("render.py")
        recovery_bytes = blobs.read(BODY + "recovery.json")
        recovery = json.loads(recovery_bytes)
        originals = recovery["originalFilesSha256"]
        if not isinstance(originals, dict) or not originals:
            raise ValueError("Recovery has no declared preserved-file set")
        expected = project_wrapper(source, renderer)
        projected = observe(BODY + "index.html")
        files = []
        for filename, declared_hash in originals.items():
            if PurePosixPath(filename).name != filename:
                raise ValueError("Original-file reference must be package-local")
            raw = blobs.read(BODY + filename)
            observed = observe(BODY + filename)
            files.append({
                "path": filename,
                "declared_sha256": declared_hash,
                "source_sha256": sha(raw),
                "source_matches_declaration": sha(raw) == declared_hash,
                "observed_sha256": sha(observed) if observed is not None else None,
                "observed_matches_source": observed == raw if observed is not None else None,
                "bytes": len(raw),
            })
        all_source_hashes = all(x["source_matches_declaration"] for x in files)
        all_observed_sources = (
            all(x["observed_matches_source"] for x in files) if served_base else None
        )
        result = {
            "schema_version": 1,
            "observed_at_utc": datetime.now(timezone.utc).isoformat(),
            "source_ref": SOURCE_REF,
            "source_wrapper": PREFIX + BODY + "index.html",
            "projection_method": PREFIX + "render.py",
            "source_wrapper_sha256": sha(source),
            "projection_method_sha256": sha(renderer),
            "expected_projected_wrapper_sha256": sha(expected),
            "observed_projected_wrapper_sha256": sha(projected) if projected is not None else None,
            "source_wrapper_equals_expected_projection": source == expected,
            "expected_projection_matches_observed": expected == projected if projected is not None else None,
            "declared_original_file_count": len(files),
            "original_sources": files,
            "all_original_source_hashes_match": all_source_hashes,
            "all_observed_originals_match_source": all_observed_sources,
            "observation_scope": "local-rendered-preview" if served_base else "expected-projection-only",
            "acquisition": {
                "git_blob_reads": blobs.reads, "git_blob_bytes": blobs.bytes,
                "git_processes": 1, "http_reads": http_reads, "http_bytes": http_bytes,
            },
            "boundaries": [
                "Not independent verification against the original ChatGPT conversations",
                "No general claim about semantic fidelity from hashes",
                "No live activity, ecological adoption or general capability claim",
                "The observation binds one pinned source and one observed projection",
            ],
        }
        result["scoped_checks_pass"] = (
            all_source_hashes and
            (not served_base or (result["expected_projection_matches_observed"] and all_observed_sources))
        )
        return result
    finally:
        blobs.close()

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True, help="Checkout containing the pinned public source commit")
    parser.add_argument("--served-base", help="Optional actual rendered-site base URL; omission is not runtime proof")
    parser.add_argument("--out", help="Optional evidence JSON; otherwise print without writing")
    args = parser.parse_args()
    result = check(args.repo, args.served_base)
    output = json.dumps(result, ensure_ascii=False, indent=2)
    if args.out:
        Path(args.out).write_bytes((output + "\n").encode("utf-8"))
    print(output)
    return 0 if result["scoped_checks_pass"] else 1

if __name__ == "__main__":
    raise SystemExit(main())
