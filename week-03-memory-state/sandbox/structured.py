"""Day 3 - structured output: schemas as data, and the validator.

The model stops writing freeform Action: lines and must hand over JSON
that matches TOOL_SCHEMAS. Bad requests die here, named, before any
tool runs. Verdicts use the same {"ok": ...} shape as the tools.
"""

import json
from typing import Any

# ----------------------------------------------------------------------------
# The schemas, as data, not code. One entry per registered tool, written
# from the real Day 1/2 signatures. Each argument maps to (type, required?).
# JSON has one number type; Python splits int/float, so a "number" field
# accepts either -- and never True/False (bool is an int subclass in Python).
# ----------------------------------------------------------------------------

# road map for checking a respose.  Maps each tool to its rulebook,
# then maps argument names to a pair of facts about that argument.
TOOL_SCHEMAS: dict[str, dict[str, tuple[type, bool]]] = {
    "fetch_url": {"url": (str, True), "timeout": (float, False)},
    "run_command": {"command": (list, True), "timeout": (float, False)},
    "read_file": {"rel_path": (str, True)},
}

# define the allowable types
TYPE_NAMES = {str: "string", float: "number", list: "list"}

# checks if a value matches the type that the schema demands
# If schema wants a number, ints and floats are good, but never booleans.
# For everythiing else, do the plain type test.
def _type_matches(value: Any, expected: type) -> bool:
    if expected is float: # a JSON number: int or float, never a boolean
        return isinstance(value, (int,float)) and not isinstance(value, bool)
    return isinstance(value, expected)

# translates between python value type and the JSON name for that type.
def _type_name(value: Any) -> str:
    """The JSON-flavored name of a value's type, for error details."""
    if isinstance(value, bool):
        return "boolean"
    if isinstance(value, str):
        return "string"
    if isinstance(value, (int, float)):
        return "number"
    if isinstance(value, list):
        return "list"
    if isinstance(value, dict):
        return "object"
    return (type(value).__name__)

def validate_tool_call(raw_text: str) -> dict[str, Any]:
    """Check a raw model reply against TOOL_SCHEMAS.

    Returns {"ok": True, "tool": ..., "arguments": {...}} when the call
    may run, or {"ok": False, "error": ..., "detail": ...} when it may
    not. The detail names the exact field that failed: it is written to
    be pasted into the prompt for the retry, not just logged.
    """
    # Gate 1: is it JSON at all? Prose-wrapped JSON fails here on purpose.
    try:
        call = json.loads(raw_text)
    except(json.JSONDecodeError, TypeError):
        return {"ok": False,
                "error": "invalid_json",
                "detail": "reply was not valid JSON"}

    # Gate 2: is it an object carrying the two keys a call must have?
    if not isinstance(call, dict) or "tool" not in call or "arguments" not in call:
        return {"ok": False, "error": "invalid_json",
                "detail": "reply must be a JSON object with 'tool' and 'arguments'"}

    name, args = call["tool"], call["arguments"]

    # Gate 3: is the tool real? If not, say what is.
    if name not in TOOL_SCHEMAS:
        return {"ok": False, "error": "unknown_tool",
                "detail": f"unknown tool '{name}'. Available: {', '.join(TOOL_SCHEMAS)}"}
    if not isinstance(args, dict):
        return {"ok": False, "error": "bad_arguments",
                "detail": "'arguments' must be an object"}

    # Gate 4: field by field: required arguments present, types matching.
    for arg, (expected, required) in TOOL_SCHEMAS[name].items():
        if arg not in args:
            if required:
                return {"ok": False, "error": "bad_arguments",
                        "detail": f"arguments.{arg} is required"}
            continue
        if not _type_matches(args[arg], expected):
            return {"ok": False, "error": "bad_arguments",
                    "detail": f"arguments.{arg} must be a {TYPE_NAMES[expected]}, "
                              f"got a {_type_name(args[arg])}"}

    return {"ok": True, "tool": name, "arguments": args}


def error_observation(verdict: dict[str, Any]) -> str:
    """Turn a failed verdict into the Observation the model will read.
    Same mechanism as Week 1's format correction; the message is sharper
    because the validator knows exactly what failed."""
    return (f"Observation: invalid tool call ({verdict['error']}): {verdict['detail']}. "
            f"Reply with ONLY a JSON object: {{\"tool\": ..., \"arguments\": {{...}}}}.")


if __name__ == "__main__":
    cases = [
        "{tool: fetch_url}",  # 1. malformed JSON
        '{"tool": "google_it", "arguments": {}}',  # 2. unknown tool
        '{"tool": "fetch_url", "arguments": {"url": "https://example.com", "timeout": "soon"}}',  # 3. wrong type
        '{"tool": "fetch_url", "arguments": {"url": "https://example.com", "timeout": 15}}',  # 4. a valid call (control)
    ]
    for raw in cases:
        print(raw)
        print(" ->", validate_tool_call(raw))
        print()
