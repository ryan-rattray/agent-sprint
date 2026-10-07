# Week 1, Day 3 — Tools (Wednesday, Oct 7)

## The idea

Tools are just functions with names. The registry is just a dict. That's the whole
abstraction — and the reason it's safe: the model never calls anything directly. It
writes the word "calculator," your code looks it up in a dict and runs your function
with its string. Today you build the two tools Friday's questions will need, plus the
dispatch path that turns a parsed action into an observation string.

## What you'll build

In `week-01-react-loop/tools.py`:

- **`calculator(expr) -> str`** — evaluates arithmetic via `ast`, never `eval`.
  Whitelist: numbers, `+ - * / // % **` and parentheses. Anything else returns an
  error string.
- **`search(query) -> str`** — dict lookup over canned answers. Unknown key →
  `"No results found for '...'"` (that's an observation, not an exception).
- **`TOOLS` registry** — `{"calculator": calculator, "search": search}`.
- **`dispatch(action_name, action_input) -> str`** — registry lookup; unknown tool
  name → `Observation: unknown tool 'x'. Available tools: calculator, search.`

## Steps

1. **Write the calculator.** Parse with `ast.parse(expr, mode="eval")`, walk the
   tree, allow only `Expression`, `BinOp`, `UnaryOp`, `Constant` (numbers) and the
   operator nodes. Any other node → return `"Error: unsupported expression"`.
   Wrap division by zero in try/except → `"Error: division by zero"`.
2. **Quick-test all five:** `calculator("12*34 + 8")` → 416, `calculator("2**10")`,
   `calculator("(5+3)*2")`, `calculator("__import__('os')")`, `calculator("1/0")`.
   Every one must return a sensible result or a clean error string — no tracebacks.
3. **Write the stub search** as a plain dict of 5–6 entries you'll need Friday (pick
   now: e.g. "capital of France", "boiling point of water in Fahrenheit", "number of
   planets"). The values are full answer-text strings.
4. **Write `TOOLS` and `dispatch`.** Test the unknown-tool path:
   `dispatch("web_search", "cats")` must return the unknown-tool observation, not raise.
5. **Run one full manual turn end-to-end** (no loop yet): build prompt → ask() →
   parse_action → dispatch → print the Observation string. Confirm the pieces talk
   to each other.
6. **Commit.** `week-01 day-03: tools + registry + dispatch`.

## Done criteria (binary)

- [ ] `calculator` handles the five test expressions with no `eval` anywhere and no
      tracebacks.
- [ ] `search` returns a canned answer for a known key and "no results" for an unknown one.
- [ ] A manual prompt → parse → dispatch turn prints a correct Observation string.

## What this unlocks

- **Thu:** the loop — this turn wrapped in `while`, with observation appending and two
  exit conditions.
- **Fri:** three real questions through the finished loop.

## Likely snag

**The `ast` whitelist feels fiddly.** That's normal — it's the actual shape of input
validation in production, and it's why engineers get paid. Keep the allowed node list
small and the error strings informative; the loop *uses* those error strings as
observations.

## When you're done

Reply "Day 3 done". Tomorrow's sheet: the loop itself — the week in one function.
