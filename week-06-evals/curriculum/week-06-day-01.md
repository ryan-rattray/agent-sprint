# Week 6, Day 1 — The Eval Harness (Monday, Nov 9)

## The idea

If you can't measure it, you can't ship it. An eval harness is a fixed set
of test cases with pass/fail rubrics that you run on every change: the
agent's regression suite. Today you build the harness, not the tests: the
runner, the rubric format, and the report. Ten to twenty cases come
tomorrow. Today is the machine that runs them.

## What you'll build

`week-06-evals/harness.py`: loads test cases (question, expected behavior,
rubric), runs the agent on each, scores pass/fail, prints a report with
per-case results.

## Steps

1. **Type the test-case format first.** What a case contains, how a rubric
   judges it. Keep it simple: JSON lines, one case per line.
2. **Type the runner.** For each case: run the agent, apply the rubric,
   record pass/fail. One chunk.
3. **Type the report.** Totals plus the failing cases with their outputs
   attached. A report you won't read is decoration.
4. **Commit.** `week-06 day-01: eval harness with runner and rubrics`.
   Breakage log.

## Done criteria (binary)

- [ ] The harness runs end to end on a dummy set of 3 cases and produces a
      readable report.

## What this unlocks

- **Tue:** the real test cases go in, and the harness earns its keep.
- **Wed-Thu:** red-teaming, scored by the harness as just another set of
  cases.

## Likely snag

**Rubrics that are vibes.** "Good answer" is not a rubric. Each rubric needs
a checkable claim: "cites at least 2 sources", "tool calls between 2 and
5", "no hallucinated URLs". Write rubrics you'd trust a stranger to apply.

## When you're done

Reply "Day 1 done". Tomorrow's sheet: the test cases.
