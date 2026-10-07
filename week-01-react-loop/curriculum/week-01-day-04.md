# Week 1, Day 4 — The Loop (Thursday, Oct 8)

## The idea

Everything you've built becomes one function. The loop is five lines of logic wearing
a trench coat: ask, parse, dispatch, append the observation to the prompt, repeat —
until the model writes "Final Answer:" or you hit the iteration cap. Two insights
today: (1) errors are observations, not crashes — a malformed reply gets fed back to
the model as a correction it can recover from; (2) the context grows every turn,
which is exactly the problem Week 3 will fix. Notice it, don't fix it.

## What you'll build

`week-01-react-loop/agent.py` with:

- **`run(question, max_iterations=8) -> dict`** — returns
  `{"answer": ..., "trace": [...]}` where each trace entry is
  `{"thought": ..., "action": ..., "observation": ...}`.
- **Malformed-output handling:** if `parse_action` returns `None` and there's no
  "Final Answer:", append `Observation: I couldn't parse an action from your last
  response. Reply using exactly the format: Thought: ... Action: ... Action Input: ...`
  and continue.
- **The Day 1 snag, paid off:** wrap the `ask()` call with simple retry on HTTP 503
  (up to 3 tries, short sleep). Your 503 notes tell you exactly where this goes.

## Steps

1. **Write `run()`.** The prompt is the full conversation so far: start with
   `build_prompt(question)`, and after each turn append the model's reply plus your
   `Observation:` line.
2. **First run:** a two-step question both tools can answer. Print the trace. Read it
   like a log — this trace is your Week 6 eval seed.
3. **Force the malformed path:** temporarily bypass the model with a canned garbage
   reply ("Hmm, let me think... 42!") and confirm the loop feeds back the correction
   observation instead of crashing. Remove the bypass after.
4. **Force the iteration cap:** ask a question the stub search can't answer and watch
   it stop at 8 with a clear "max iterations reached" result. Verify the cap fires —
   don't trust it, test it.
5. **Commit.** `week-01 day-04: the loop, with error recovery`.

## Done criteria (binary)

- [ ] A two-step question solves end-to-end with a printed trace of
      Thought / Action / Observation turns.
- [ ] A malformed model reply produces a recovery attempt visible in the trace, not a crash.
- [ ] The max-iterations cutoff fires on an unanswerable question.

## What this unlocks

- **Fri:** the proof — three real questions, then you break it on purpose.
- **Week 6:** this trace format is the raw material your eval harness will consume.

## Likely snag

**The model loops — same action, same input, forever.** The iteration cap is the
safety net, but the real fix (dedupe detection, stop conditions) is a Week 7
production conversation. For now, the cap plus a trace you can read is enough.

## When you're done

Reply "Day 4 done". Tomorrow's sheet: prove it — three questions, three deliberate
breakages.
