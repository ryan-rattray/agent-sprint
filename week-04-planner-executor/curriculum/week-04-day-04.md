# Week 4, Day 4 — The Full System (Thursday, Oct 29)

## The idea

Planner, workers, supervisor, synthesizer: one system. Pick a task you'd
never trust a single loop with ("research three approaches to X, compare
them, write a briefing"), let the planner decompose it, run the workers
(sequentially is fine this week), synthesize the results. The deliverable
isn't just the output; it's the trace. Every subtask mapped back to the
plan, every supervisor verdict logged.

## What you'll build

`week-04-orchestration/orchestrator.py` tying the three components together,
plus a `synthesize()` step that assembles worker outputs into the final
answer.

## Steps

1. **Type the orchestrator.** Plan, dispatch each subtask to a worker under
   supervision, collect results. One chunk per stage.
2. **Type the synthesizer.** Takes the worker outputs and the original goal,
   produces the final briefing.
3. **Run the full task end to end.** Save the trace: plan, subtask results,
   verdicts, synthesis.
4. **Commit.** `week-04 day-04: planner-executor-synthesizer end to end`.
   Breakage log.

## Done criteria (binary)

- [ ] The full task completes end to end, and you can trace every subtask
      result back to the plan.

## What this unlocks

- **Fri:** you break the plan on purpose, then the Gemini specialist
  stretch.

## Likely snag

**The synthesizer ignores worker outputs and answers from its own
knowledge.** Ground it: the synthesis prompt gets the worker results as its
primary source, and anything not in them gets flagged, not stated.

## When you're done

Reply "Day 4 done". Tomorrow's sheet: breaking the plan, then the stretch.
