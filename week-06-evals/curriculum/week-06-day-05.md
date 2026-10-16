# Week 6, Day 5 — Five Failure Modes (Friday, Nov 13)

## The idea

The week's deliverable is a document, not just code: five failure modes,
each with a reproduction, a mitigation, and a permanent eval case. Four
come from this week and the weeks before (injection, loops, cost, plus one
of your choice). The fifth comes from a deliberate regression: introduce a
real bug on purpose today, run the harness, and confirm it catches it. A
harness that has never caught anything is a hypothesis.

## What you'll build

`FAILURE_MODES.md`: five entries (failure, reproduction, mitigation, eval
case), plus the deliberate-regression experiment written up.

## Steps

1. **Write up four failure modes** from the week's work, one entry each,
   with the eval case linked.
2. **Introduce a real regression on purpose** (break a tool's error
   contract, loosen a schema). Run the harness. Confirm the catch, then
   revert.
3. **Write up the fifth entry**: the regression, the catch, the revert.
4. **Commit.** `week-06 day-05: five failure modes documented, regression
   caught`. Breakage log.
5. **Stretch/spare.** The parked model-obedience comparison across gateway
   models: same harness, different question. Do the models obey
   tool-calling instructions equally? If it doesn't fit today, it carries
   to the weekend, not into Week 7.

## Done criteria (binary)

- [ ] Five failure modes documented with reproductions, mitigations, and
      eval cases.
- [ ] The harness catches a deliberately introduced regression, written up.

## What this unlocks

- **Week 7** (Nov 16-20): production. The eval harness becomes the
  pre-deploy gate, and per-run cost tracking becomes the billing line.

## Likely snag

**Failure modes written as war stories.** Each entry needs the same shape:
what fails, how to reproduce it, what stops it, which eval case guards it.
Stories are for the retrospective; the document is a reference.

## When you're done

Reply "Day 5 done". Weekend sheet: buffer and the explain test.
