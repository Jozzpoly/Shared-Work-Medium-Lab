from __future__ import annotations

import argparse
import json
import os
import sys
from dataclasses import dataclass


PROTOCOL = "mp1a-subject-jsonl-v0.1"


@dataclass(frozen=True)
class Config:
    api_key: str
    model: str


def emit(obj):
    sys.stdout.write(json.dumps(obj, ensure_ascii=False) + "\n")
    sys.stdout.flush()


def read_packet():
    line = sys.stdin.readline()
    if not line:
        raise EOFError("subject input closed")
    return json.loads(line)


def load_config(env=None) -> Config:
    env = os.environ if env is None else env
    api_key = str(env.get("OPENAI_API_KEY", "")).strip()
    model = str(env.get("OPENAI_MODEL", "")).strip()

    missing = []
    if not api_key:
        missing.append("OPENAI_API_KEY")
    if not model:
        missing.append("OPENAI_MODEL")

    if missing:
        raise RuntimeError(
            "credentialed OpenAI subject is disabled: missing "
            + ", ".join(missing)
        )

    return Config(api_key=api_key, model=model)


OUTPUT_SCHEMA = {
    "type": "object",
    "properties": {
        "kind": {
            "type": "string",
            "enum": ["action", "final"],
        },
        "action": {
            "type": "string",
            "description": (
                "Exactly one action from the supplied action contract when kind=action; "
                "empty string when kind=final."
            ),
        },
        "answer_json": {
            "type": "string",
            "description": (
                "Empty string when kind=action. When kind=final, a JSON-encoded object "
                "matching the task's final answer contract."
            ),
        },
    },
    "required": ["kind", "action", "answer_json"],
    "additionalProperties": False,
}


def build_request(model: str, prompt: str) -> dict:
    return {
        "model": model,
        "input": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": prompt,
                    }
                ],
            }
        ],
        "text": {
            "format": {
                "type": "json_schema",
                "name": "mp1a_subject_decision",
                "description": (
                    "One constrained browser action or the task's final JSON answer."
                ),
                "schema": OUTPUT_SCHEMA,
                "strict": True,
            }
        },
        "store": False,
        "max_output_tokens": 500,
    }


def parse_model_output(text: str) -> dict:
    try:
        obj = json.loads(text)
    except json.JSONDecodeError as exc:
        raise RuntimeError("OpenAI subject returned non-JSON structured output") from exc

    if not isinstance(obj, dict):
        raise RuntimeError("OpenAI subject output must be an object")

    if set(obj.keys()) != {"kind", "action", "answer_json"}:
        raise RuntimeError(
            f"OpenAI subject output keys violate contract: {sorted(obj.keys())}"
        )

    kind = obj["kind"]
    action = obj["action"]
    answer_json = obj["answer_json"]

    if kind == "action":
        if not isinstance(action, str) or not action.strip():
            raise RuntimeError("action decision requires a non-empty action string")
        if answer_json != "":
            raise RuntimeError("action decision must use empty answer_json")
        return {
            "kind": "action",
            "action": action.strip(),
            "label": "OpenAI structured subject action",
        }

    if kind == "final":
        if action != "":
            raise RuntimeError("final decision must use empty action")
        try:
            answer = json.loads(answer_json)
        except json.JSONDecodeError as exc:
            raise RuntimeError("final answer_json is not valid JSON") from exc
        if not isinstance(answer, dict):
            raise RuntimeError("final answer_json must encode an object")
        return {
            "kind": "final",
            "answer": answer,
        }

    raise RuntimeError(f"unsupported subject decision kind: {kind!r}")


def build_prompt(start_packet: dict, history: list[dict], observation_packet: dict) -> str:
    task = start_packet["task"]
    contract = start_packet["action_contract"]

    transcript = []
    for item in history:
        transcript.append(json.dumps(item, ensure_ascii=False, separators=(",", ":")))

    observation = observation_packet["observation"]

    return (
        "You are the isolated subject in a controlled browser experiment.\n"
        "Use only information actually present in the supplied observations. "
        "Do not invent unseen resources or results.\n"
        "Choose exactly one allowed browser action per turn, or finish with the "
        "required final answer. Do not output explanation outside the structured "
        "decision.\n\n"
        f"TASK:\n{task}\n\n"
        "ACTION / FINAL CONTRACT:\n"
        f"{json.dumps(contract, ensure_ascii=False, indent=2)}\n\n"
        "PRIOR INTERACTION HISTORY (oldest first):\n"
        + ("\n".join(transcript) if transcript else "(none)")
        + "\n\nCURRENT OBSERVATION:\n"
        f"URL: {observation['url']}\n"
        "AXTREE:\n"
        f"{observation['axtree']}\n"
    )


def call_openai(config: Config, prompt: str) -> dict:
    # Import only after the explicit credential/model gate has passed. This keeps
    # default CI/self-tests credential-free and proves that no accidental request
    # can happen before configuration is present.
    try:
        from openai import OpenAI
    except ImportError as exc:
        raise RuntimeError(
            "OpenAI SDK is not installed. Install the official 'openai' package "
            "only in the explicit real-subject runtime."
        ) from exc

    client = OpenAI(api_key=config.api_key)
    response = client.responses.create(**build_request(config.model, prompt))

    output_text = getattr(response, "output_text", None)
    if not isinstance(output_text, str) or not output_text.strip():
        raise RuntimeError("OpenAI Responses API returned no output_text")

    return parse_model_output(output_text)


def run_subject():
    config = load_config()

    start = read_packet()
    if start.get("type") != "start" or start.get("protocol") != PROTOCOL:
        raise RuntimeError("invalid start packet")

    if "task" not in start or "action_contract" not in start:
        raise RuntimeError("start packet missing task/action_contract")

    emit(
        {
            "type": "ready",
            "protocol": PROTOCOL,
            "subject_kind": "openai-responses-structured-output",
            "model": config.model,
        }
    )

    history = []

    while True:
        packet = read_packet()
        if packet.get("type") != "observation" or packet.get("protocol") != PROTOCOL:
            raise RuntimeError("invalid observation packet")

        prompt = build_prompt(start, history, packet)
        reply = call_openai(config, prompt)
        emit(reply)

        history.append(
            {
                "observation": {
                    "url": packet["observation"]["url"],
                    "axtree": packet["observation"]["axtree"],
                },
                "decision": reply,
            }
        )

        if reply["kind"] == "final":
            return


def self_test():
    try:
        load_config({})
    except RuntimeError as exc:
        message = str(exc)
        assert "OPENAI_API_KEY" in message
        assert "OPENAI_MODEL" in message
    else:
        raise AssertionError("empty configuration must fail closed")

    cfg = load_config(
        {
            "OPENAI_API_KEY": "test-only-not-a-real-key",
            "OPENAI_MODEL": "test-model",
        }
    )
    assert cfg.model == "test-model"

    request = build_request("test-model", "hello")
    assert request["model"] == "test-model"
    assert request["store"] is False
    assert request["text"]["format"]["type"] == "json_schema"
    assert request["text"]["format"]["strict"] is True
    assert "tools" not in request

    action = parse_model_output(
        json.dumps(
            {
                "kind": "action",
                "action": "click('12')",
                "answer_json": "",
            }
        )
    )
    assert action["kind"] == "action"
    assert action["action"] == "click('12')"

    final = parse_model_output(
        json.dumps(
            {
                "kind": "final",
                "action": "",
                "answer_json": json.dumps(
                    {
                        "target_resource": "summary-cache-guidance",
                        "supporting_sources": ["source-cache-config"],
                        "judgement": "requires_re_evaluation",
                        "selected_distractor": False,
                    }
                ),
            }
        )
    )
    assert final["kind"] == "final"
    assert final["answer"]["target_resource"] == "summary-cache-guidance"

    bad_cases = [
        {"kind": "action", "action": "", "answer_json": ""},
        {"kind": "action", "action": "click('12')", "answer_json": "{}"},
        {"kind": "final", "action": "go_back()", "answer_json": "{}"},
        {"kind": "final", "action": "", "answer_json": "[]"},
    ]
    for case in bad_cases:
        try:
            parse_model_output(json.dumps(case))
        except RuntimeError:
            continue
        raise AssertionError(f"bad model output unexpectedly accepted: {case!r}")

    print(
        "OPENAI ADAPTER SELF-TEST PASS: configuration fails closed without "
        "credential/model, request uses strict Structured Outputs with store=false, "
        "and action/final translation is validated without making an API request."
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        self_test()
        return

    run_subject()


if __name__ == "__main__":
    main()
