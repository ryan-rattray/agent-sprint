# Week 4, Day 3 — The Supervisor (Wednesday, Oct 28)

## The idea

"The planner is smart enough" is not a safety policy. Every subtask gets a
budget (max iterations, wall-clock timeout), and the supervisor watches:
kill runaways, flag outputs that fail validation, and decide retry vs.
abort vs. escalate back to the planner for re-planning. The supervisor is a
policy, not a model call. Mostly if-statements with teeth.

## What you'll build

`week-04-orchestration/supervisor.py`: wraps worker execution with budgets;
on violation, kills and classifies (runaway, invalid output, timeout);
returns a verdict the planner can act on.

## Steps

1. **Type the budget checks.** Iteration cap and timeout around the worker
   call. Small chunk, comments in your own words.
2. **Type the verdict logic.** What counts as retryable vs. abort vs.
   escalate. Write the policy before you need it.
3. **Launch a runaway on purpose.** A goal with no achievable done
   condition. Watch the supervisor catch and kill it. This is the test;
   don't skip it.
4. **Commit.** `week-04 day-03: supervisor with budgets and kill policy`.
   Breakage log.

## Done criteria (binary)

- [ ] A deliberately runaway subtask is caught and killed by the
      supervisor, and the verdict is recorded.

## What this unlocks

- **Thu:** the full system runs, and the supervisor is what makes it safe
  to watch.
- **Fri:** you break the plan on purpose and see what catches it.

## Likely snag

**Killing feels wrong, so you set budgets too generous.** A 50-iteration
budget on a 5-iteration task isn't supervision, it's decoration. Set budgets
from the subtask's done condition, then halve them once to see what breaks.

## When you're done

Reply "Day 3 done". Tomorrow's sheet: wiring it all together.
