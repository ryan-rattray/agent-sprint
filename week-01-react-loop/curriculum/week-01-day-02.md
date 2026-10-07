# Week 1, Day 2 — Teach It the ReAct Shape (Tuesday, Oct 6)

## The idea

The model doesn't know it's an agent. All it sees is text — so today you give it a
contract written in plain English: respond in a strict Thought / Action / Action Input
format, and your code will treat that format as a command. The whole "agentic" trick is
formatting discipline plus a parser. No tools run today. You prove the model can hold
the shape, then you prove your code can read it.

## What you'll build

`week-01-react-loop/react.py`, containing:

- **`REACT_PROMPT` template** — instructions, one worked few-shot example, and a slot
  for the question.
- **`build_prompt(question) -> str`** — slots the question into the template.
- **`parse_action(reply) -> tuple[str, str] | None`** — regex extraction of the Action
  name and Action Input; returns `None` when no Action line is found.

## Steps

1. **Write the prompt template.** Include: a one-sentence role instruction ("You solve
   problems by reasoning step by step, then taking actions"), the exact format block
   (`Thought:` / `Action:` / `Action Input:` / `Final Answer:`), and one complete
   worked example (a `12*34` calculator turn ending in `Final Answer: 408`).
2. **Write `build_prompt(question)`** that slots the question into the template.
3. **Run it through yesterday's function:**
   `python -c "from react import build_prompt; from ask import ask; print(ask(build_prompt('What is 12*34 plus 8?')))"`.
   Read the raw reply. Did it hold the format? On the first try, usually yes — if it
   rambles, add "Reply using exactly the format above, nothing else" and rerun.
4. **Write `parse_action`** with regex: `Action:\s*(\w+)` and `Action Input:\s*(.+)`.
   Test it on the real reply from step 3.
5. **Break it on purpose.** Feed it a reply with no Action line (e.g. "I think the
   answer is 42") and a reply with Markdown fences around everything. Confirm it
   returns `None` cleanly instead of crashing.
6. **Commit.** `week-01 day-02: ReAct prompt + parser`.

## Done criteria (binary)

- [ ] The model replies to a fresh question in exact Thought / Action / Action Input
      format.
- [ ] `parse_action` extracts the action name and input from that reply.
- [ ] `parse_action` returns a clear no-action sentinel on replies with no Action line.

## What this unlocks

- **Wed:** the Action name routes to a real function through a registry; the Action
  Input becomes its argument.
- **Thu:** the loop wraps this — prompt → parse → act → append observation → repeat.

## Likely snag

**Format drift.** The model adds chatter around the format or wraps it in ``` fences.
Fix the prompt first ("exactly this format, nothing else"), and strip fences in the
parser as a safety net. Record which one worked — this is the first entry in your
"prompt vs. code" ledger.

## When you're done

Reply "Day 2 done" (or what's stuck). Tomorrow's sheet: real tools — the calculator
and the stub search — wired into the Action line.
