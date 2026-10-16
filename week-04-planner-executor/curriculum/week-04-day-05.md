# Week 4, Day 5 — Break the Plan (Friday, Oct 30)

## The idea

The plan is always a guess, so today's job is to watch a guess fail and see
what catches it. Give the system a task where the initial decomposition is
wrong: a subtask that's impossible, two subtasks in the wrong order, a
missing dependency. Then write down exactly where it went wrong and which
mechanism handled it (supervisor kill? re-plan? silent failure?). A failure
nobody can point to is a failure you'll repeat.

## What you'll build

One adversarial task, one written failure analysis. The analysis is the
deliverable.

## Steps

1. **Design the adversarial task.** At least one impossible subtask and one
   ordering trap. Make it genuinely hostile, not just hard.
2. **Run it. Watch. Don't intervene.**
3. **Write the analysis.** Where the plan went wrong, what caught it (or
   didn't), what you'd change.
4. **Commit.** `week-04 day-05: adversarial plan failure analysis`.
   Breakage log.
5. **Stretch (optional).** Wire Gemini as a specialist via your `ask.py`
   (gemini-3.8-flash): the orchestrator delegates one subtask to Gemini and
   synthesizes its response with the rest. Hub-and-spoke: your orchestrator
   holds state, the specialist is stateless. If it doesn't fit today, it
   carries to the weekend, not into next week.

## Done criteria (binary)

- [ ] You can point to at least one place the plan went wrong and show the
      mechanism that handled it (or document that nothing did).

## What this unlocks

- **Week 5** (Nov 2-6): frameworks. You rebuild the Week 2 agent in
  LangGraph, and you'll recognize every piece: nodes are workers, edges
  carry the supervisor's verdicts.

## Likely snag

**Nothing goes wrong.** Then your adversarial task wasn't adversarial
enough. Make a subtask genuinely impossible, not just hard. The supervisor
needs a real kill to prove itself.

## When you're done

Reply "Day 5 done". Weekend sheet: buffer and the explain test.
