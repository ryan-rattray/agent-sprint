# Week 2 Day 3 — Structured Output: Schema-Validated Tool Calls (Oct 26, 2026)

## What was built

`structured.py`: the contract that now stands between the model's reply and the tools. Week 1's loop parsed freeform text with a regex and hoped; this file replaces hope with a check that runs *before* anything executes.

`TOOL_SCHEMAS` is the contract as data, not code — one entry per registered tool, written from the real Day 1/2 signatures. Each argument maps to a pair: `(type, required?)`. `fetch_url` takes a required string `url` and an optional number `timeout`; `run_command` takes a required `command` that must be a *list* (the Day 2 no-shell rule, now enforced by schema) plus an optional `timeout`; `read_file` takes a required string `rel_path`. Because the schemas are a table, the table can be read by other code later — Week 6's eval harness gets its ground truth from this same file.

`validate_tool_call(raw_text) -> dict` runs four gates, in order, and returns a verdict in the same `{"ok": ...}` shape the Day 1/2 tools return, so the loop can handle a validation failure exactly like a tool failure:

1. **Gate 1 — is it JSON at all?** `json.loads`; failure returns `invalid_json`. Prose-wrapped JSON ("Here is the tool call: {...}") dies here, on purpose.
2. **Gate 2 — is it the right shape?** An object carrying both `tool` and `arguments`, else `invalid_json` with the expected shape in the detail.
3. **Gate 3 — is the tool real?** A name not in `TOOL_SCHEMAS` returns `unknown_tool`, with the available tools listed in the detail; a non-object `arguments` returns `bad_arguments`.
4. **Gate 4 — field by field.** A missing required argument returns `bad_arguments` naming it; a present argument of the wrong type returns `bad_arguments` naming the field, the expected type, and what arrived: `arguments.timeout must be a number, got a string`.

Two helpers carry the type system. `_type_matches` decides pass/fail, with one special case: a schema `float` means "a JSON number," so it accepts `int` or `float` — and never `bool`, because in Python `True` is an `int` subclass and would otherwise pass as a number. `_type_name` writes the failure sentence in JSON's vocabulary (string, number, boolean, object) rather than Python's (`str`, `dict`), because the detail is written to be read by the model on the retry, not just logged for a human. Its `bool` check comes first for the same subclass reason.

`error_observation(verdict)` turns a failed verdict into the Observation text the loop feeds back into the prompt — Week 1's malformed-reply correction mechanism, with a far more specific message.

**Done criteria (met, with one deliberate deferral):** the three break-it cases are rejected with the specific field named, and a valid control call passes — verified in the run below. The retry wiring (feeding `error_observation` back through the loop so the model corrects itself in the trace) was deferred by decision, not omission: the upgraded loop is Day 4's build, and the validator's feedback function is written and waiting for it. Committed as `70569ad` and pushed; verified on the remote.

## What actually happened

**The pydantic detour.** The skeleton's header said `pip install pydantic`, and the day's first confusion was that the file being typed imports nothing from pydantic — just `json` and `typing.Any`. Checking the lesson notebook settled it: the curriculum's reference implementation (`Reference: structured.py (Day 3)` in `week-02-structured-output-lesson.ipynb`) is hand-rolled — schemas as dictionaries, types checked manually. The install line was the road not taken. Rule earned: when guidance and the materials disagree, the
...[truncated 5571 chars]