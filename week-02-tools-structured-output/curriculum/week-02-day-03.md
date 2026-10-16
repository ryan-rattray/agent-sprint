# Week 2, Day 3 — Structured Output (Wednesday, Oct 14)

## The idea

Week 1's parser read the model's freeform text with a regex and hoped for the
best. Today you replace hope with a contract: every tool call must arrive as
JSON matching a schema, and anything else gets rejected *before your code acts
on it*. This is the single biggest reliability jump in the whole 8 weeks —
regex parsing catches syntax accidents; schema validation catches *semantic*
ones (right shape, wrong tool name; a string where a number belongs). You'll
feel the difference in the traces by the end of the night.

## What you'll build

`week-02-real-tools/structured.py`:

- **A JSON schema for a tool call:** `{"tool": <name>, "arguments": {...}}`,
  where each registered tool declares its own argument schema. One schema to
  rule them all, plus per-tool argument schemas.
- **`validate_tool_call(raw_text) -> dict`** — parse the model's output as JSON,
  validate against the schema (pydantic or jsonschema — install one today: `pip
  install pydantic`), and return either the validated call or a structured
  validation error that names exactly what failed.
- **The retry path:** on validation failure, feed the error back into the loop as
  an observation — same mechanism as Week 1's malformed-reply correction, now
  with a much more specific error message ("`arguments.timeout` must be a number,
  got a string").

## Steps

1. **Install.** `pip install pydantic` (or jsonschema — one only, pick today).
2. **Define the schemas** for your three tools from Day 2: tool name, required
   arguments, types. Write them as data, not code — you'll thank yourself in
   Week 6.
3. **Rewrite the parse step** of your loop to use `validate_tool_call` instead of
   the regex. Keep the regex file — it's the before/after exhibit for Sunday's
   explain test.
4. **Break it on purpose:** hand the validator malformed JSON, then valid JSON
   with a wrong tool name, then right tool with a wrong-typed argument. All three
   must come back as specific, named errors — and the loop must feed each one
   back for a retry.
5. **Commit.** `week-02 day-03: schema-validated tool calls, retry on invalid`.

## Done criteria (binary)

- [ ] An invalid tool call is rejected by the schema — with the specific field
      named — and the model corrects itself on the next round, visible in the trace.

## What this unlocks

- **Thu:** the research assistant — 3+ tool calls, one answer, cited sources.
- **Week 6:** these schemas become your eval harness's ground truth for "did
      the agent even attempt the right thing."

## Likely snag

**The model wraps the JSON in prose** ("Here is the tool call: {...}").
Your prompt must say the reply contains *only* the JSON object — and keep the
validation-error feedback loop, because even good prompts leak prose
sometimes. The validator is the contract; the prompt is the suggestion.

## When you're done

Reply "Day 3 done". Tomorrow's sheet: the research assistant, wired end to end.
