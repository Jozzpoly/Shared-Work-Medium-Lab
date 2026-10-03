from __future__ import annotations

import argparse
import json
import re
import sys


PROTOCOL = "mp1a-subject-jsonl-v0.1"


def emit(obj):
    sys.stdout.write(json.dumps(obj, ensure_ascii=False) + "\n")
    sys.stdout.flush()


def read_packet():
    line = sys.stdin.readline()
    if not line:
        raise EOFError("subject input closed")
    return json.loads(line)


def link_bid(axtree: str, label: str) -> str:
    pattern = re.compile(
        r"\[([^\]]+)\]\s+link\s+" + re.escape(repr(label))
    )
    match = pattern.search(axtree)
    if not match:
        raise RuntimeError(f"required link not found: {label!r}")
    return match.group(1)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--judgement",
        choices=["requires_re_evaluation", "proven_false"],
        required=True,
    )
    args = parser.parse_args()

    start = read_packet()
    if start.get("type") != "start" or start.get("protocol") != PROTOCOL:
        raise RuntimeError("invalid start packet")

    emit(
        {
            "type": "ready",
            "protocol": PROTOCOL,
            "subject_kind": "deterministic-t1-trace-score-fixture",
        }
    )

    phase = 0

    while True:
        packet = read_packet()
        if packet.get("type") != "observation":
            raise RuntimeError(f"unexpected packet type: {packet.get('type')!r}")

        tree = packet["observation"]["axtree"]

        if phase == 0:
            label = "Derived summaries"
            phase += 1
            emit(
                {
                    "kind": "action",
                    "action": f"click({link_bid(tree, label)!r})",
                    "label": label,
                }
            )
        elif phase == 1:
            label = "Observation polling guidance"
            phase += 1
            emit(
                {
                    "kind": "action",
                    "action": f"click({link_bid(tree, label)!r})",
                    "label": label,
                }
            )
        elif phase == 2:
            label = "source-cache-config"
            phase += 1
            emit(
                {
                    "kind": "action",
                    "action": f"click({link_bid(tree, label)!r})",
                    "label": label,
                }
            )
        elif phase == 3:
            emit(
                {
                    "kind": "final",
                    "answer": {
                        "target_resource": "summary-cache-guidance",
                        "supporting_sources": ["source-cache-config"],
                        "judgement": args.judgement,
                        "selected_distractor": False,
                    },
                }
            )
            return
        else:
            raise RuntimeError("subject invoked after final")


if __name__ == "__main__":
    main()
