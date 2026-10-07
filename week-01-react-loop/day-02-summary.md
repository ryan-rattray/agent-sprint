# Day 2 — Teach It the ReAct Shape (Oct 7, 2026)

## What was built

`react.py`: three pieces. A `REACT_PROMPT` template that teaches the model a
strict Thought / Action / Action Input contract, `build_prompt(question)` that
slots a question into it, and `parse_action(reply)` that reads the model's
reply back with regex. No tools run today — the point is proving the model can
hold the shape, then proving our code can read it.

The core insight: the model doesn't know it's an agent. It only sees text. So
the entire "agentic" trick, at this stage, is formatting discipline plus a
parser.

**Done criteria (all met):** the model replies to a fresh question in exact
Thought / Action / Action Input format · `parse_action` extracts the action
name and input · `parse_action` returns a clean `None` sentinel on replies with
no Action line.

## Line-by-line walkthrough

```python
"""Day 2 - teach the model the ReAct shape.

The model doesn't know it's an agent. All it sees is text, so we give it
a contract: respond in a strict Thought / Action / Action Input format,
and our code treats that format as a command. No tools run today.
"""
```

Same pattern as Day 1: the docstring states the idea before the code states the
mechanism.

```python
import re
```

Regex, for pulling the Action name and input out of the model's reply.

```python
REACT_PROMPT = """You solve problems by reasoning step by step, then taking actions.

Reply using exactly this format, nothing else:

Thought: <your reasoning about what to do next>
Action: <the tool to use: calculator or search>
Action Input: <the input to pass to the tool>

When you have the final answer, reply using exactly this format, nothing else:

Thought: <your reasoning>
Final Answer: <the answer>

Example:

Question: What is 12*34?

Thought: I need to compute 12*34 first.
Action: calculator
Action Input: 12*34
Observation: 408

Thought: I have the result of the computation.
Final Answer: 408

Question: {question}
"""
```

The template has four jobs:

1. **Role instruction** ("You solve problems by reasoning step by step, then
   taking actions") — tells the model what job it's doing. One sentence is
   enough; the example does the heavy lifting.
2. **Format spec** — the exact `Thought:` / `Action:` / `Action Input:` /
   `Final Answer:` shapes. The phrase "exactly this format, nothing else" is
   doing real work: it's the cheapest fix for format drift (the model adding
   chatter or wrapping everything in fences).
3. **Worked example** — a complete 12×34 exchange. Models learn formats faster
   from an example than from rules (few-shot teaching). Note the `Observation:
   408` line: the model will never write that — *our code* produces
   Observations, starting Thursday. It's in the example so the model sees what
   a complete multi-turn exchange looks like.
4. **`{question}` slot** — the blank where the real question goes. Everything
   above it is fixed; only this changes per call.

```python
def build_prompt(question: str) -> str:
    """Slot a question into the ReAct prompt template."""
    return REACT_PROMPT.format(question=question)
```

Mail merge. `.format()` swaps `{question}` for the actual question string and
returns the finished prompt. Keeping the template fixed and the question
variable means the contract can't accidentally drift between calls.

```python
def parse_action(reply: str) -> tuple[str, str] | None:
    """Extract (action_name, action_input) from a model reply.

    Returns None when the reply contains no Action line.
    """
    action_match = re.search(r"Action:\s*(\w+)", reply)
    input_match = re.search(r"Action Input:\s*(.+)", reply)
    if not action_match or not input_match:
        return None
    return action_match.group(1), input_match.group(1).strip()
```

The mirror image of the prompt: the prompt teaches the model to *write* the
shape, the parser teaches our code to *read* it.

- `Action:\s*(\w+)` — finds the Action line; `(\w+)` captures the action name
  as a single word token (`calculator`, `search`). Action names are always one
  token, so `\w+` is the right strictness.
- `Action Input:\s*(.+)` — captures the rest of the line. `(.+)` is deliberately
  loose: inputs contain spaces, symbols, whole expressions (`12*34 + 8`).
- `re.search` (not `re.match`) scans the whole reply, so leading chatter or
  fences don't break it.
- If either line is missing → return `None`. That's the sentinel: "the model
  didn't emit an action." Returning `None` instead of raising matters because
  Thursday's loop treats a missing action as a *normal case* to handle, not a
  crash.
- `.strip()` trims stray whitespace off the input.

## How it was verified

**Live run** (through Day 1's `ask()`):

```
Thought: I need to calculate 12*34 + 8.
Action: calculator
Action Input: 12*34 + 8
```

The format held on the first try.

**Break-it tests** (all passed):

| Input | Result | Meaning |
|---|---|---|
| Real reply shape | `('calculator', '12*34 + 8')` | Extracts name + input |
| `"I think the answer is 42"` | `None` | Clean sentinel, no crash |
| Reply wrapped in ` ``` ` fences | `('calculator', '12*34')` | Fences don't crash it; regex sees through them |

## The 503 saga (why `MODEL` changed)

The morning started with `gemini-3.8-flash` returning HTTP 503 on every call,
then the `gemini-flash-latest` alias too. Diagnosis, step by step:

1. Listed available models via the API's model-list endpoint — the key, the
   network, and the code were all fine; only text generation was refusing.
2. `gemini-2.5-flash` returned 404: new API keys can't invoke older models,
   even though they're listed.
3. `gemini-3.7-flash` worked immediately.

`MODEL` in `ask.py` was updated to `gemini-3.7-flash`. Lesson worth keeping: a
503 is "the server can't right now" (wait or switch deployments); a 404 is
"that doesn't exist for you" (don't retry, pick something else). And when the
model name is in doubt, ask the API what it actually has instead of debating
memories.

## Environment notes

- PowerShell vs Anaconda Prompt kept colliding: `cd /d` is cmd-only
  (PowerShell's `cd` switches drives on its own), and multi-line `python -c`
  works in PowerShell but not in cmd — use semicolons for one-liners there.
- Split that stuck: PowerShell for git, Anaconda Prompt for Python.

## What this unlocks

- **Wed:** the Action name routes to a real function through a registry; the
  Action Input becomes its argument.
- **Thu:** the loop wraps this — prompt → parse → act → append observation →
  repeat.
