# Week 6, Day 2 — The Test Cases (Tuesday, Nov 10)

## The idea

The harness is a machine; today you feed it. Write 10-20 test cases
covering what your agent actually does: research questions needing multiple
tool calls, questions with known tricky answers (your Week 1
obscure-fake-facts trick belongs here), and at least two cases designed to
fail. Then run the harness and read the report like a scientist, not a
proud parent.

## What you'll build

10-20 JSON-lines test cases with rubrics, plus the first full harness run
and its report.

## Steps

1. **Type the cases in small batches**, 5 at a time. Mix: straightforward,
   multi-tool, tricky-known-answer, designed-to-fail.
2. **Run the harness.** Read every failure before touching any code.
3. **Classify each failure**: bad test or bad agent? Fix the right one and
   write down which it was.
4. **Commit.** `week-06 day-02: 10-plus test cases with first full run`.
   Breakage log.

## Done criteria (binary)

- [ ] 10+ cases with checkable rubrics exist and the harness runs them all.
- [ ] Every failure from the first run is classified as bad test or bad
      agent, in writing.

## What this unlocks

- **Wed:** prompt injection, scored as just another failing case.
- **Thu:** loops and cost blowups, same treatment.

## Likely snag

**Designing cases your agent already passes.** That's vanity testing. At
least a third of the cases should make you nervous. If the first run is all
green, the cases are too easy.

## When you're done

Reply "Day 2 done". Tomorrow's sheet: red team, part one.
