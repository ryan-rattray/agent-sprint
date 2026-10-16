# Week 6, Day 4 — Red Team: Loops and Cost (Thursday, Nov 12)

## The idea

Two failure modes that don't need an attacker. An infinite loop: the agent
calls tools forever without converging (your Week 1 iteration cap was the
first mitigation; today you test it under fire). A cost blowup: a run that
burns 10x the tokens of a normal one. Both get the same treatment:
reproduce on purpose, measure, mitigate, add to the harness.

## What you'll build

Token and dollar tracking per run (wrap the model call, count tokens,
multiply by the gateway rate card), a loop-trap test case, and a
cost-ceiling test case.

## Steps

1. **Type the cost tracker.** Tokens in and out per model call, accumulated
   per run, dollars via your gateway's rate card. Small chunk.
2. **Design the loop trap.** A question with no good answer that invites
   endless tool calls. Run it. Verify the iteration cap fires.
3. **Design the cost test.** A run that would blow past 5x your normal cost.
   Set the ceiling and watch it trip.
4. **Add both as permanent eval cases.** Commit:
   `week-06 day-04: cost tracking and loop/cost red team`. Breakage log.

## Done criteria (binary)

- [ ] Every run logs its token count and dollar cost.
- [ ] The loop trap is caught by the iteration cap and the cost ceiling
      trips on the blowup case, both as permanent eval cases.

## What this unlocks

- **Fri:** five failure modes, documented with mitigations, plus the
  deliberately introduced regression.

## Likely snag

**Costs that are "fine" because the gateway is cheap.** Price it anyway. The
discipline is the point: production bills arrive whether you measured or
not, and Week 7's endpoint will need per-run costs on every log line.

## When you're done

Reply "Day 4 done". Tomorrow's sheet: the five failure modes.
