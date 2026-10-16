# Week 4, Day 1 — The Planner (Monday, Oct 26)

## The idea

A single loop does one thing at a time. For a task with real structure, you
need decomposition first: a planner that takes a goal and returns an ordered
list of subtasks, each with a clear objective and a done condition. The
planner is not a loop. It's one structured-output call, using the schema
skills from Week 2. The plan is always a guess, which is why the rest of the
week exists.

## What you'll build

`week-04-orchestration/planner.py`: goal in, JSON plan out. Each subtask
carries an `id`, an `objective`, and a `done_when`. Validate against a
schema; reject prose plans.

## Steps

1. **Type the plan schema first** (the contract), then the planner prompt.
   Schema before prompt, always.
2. **Hand it a multi-part task** ("research three approaches to X and
   compare them") and read the decomposition like a manager: is the order
   sane? Are the done conditions checkable?
3. **Fix the prompt** based on what you see. One iteration minimum; the
   first plan is never the keeper.
4. **Commit.** `week-04 day-01: planner with structured-output
   decomposition`. Breakage log.

## Done criteria (binary)

- [ ] A multi-part task returns a sensible, ordered subtask list with
      checkable done conditions, as validated JSON.

## What this unlocks

- **Tue:** workers that execute one subtask each, knowing nothing of the
  bigger picture.
- **Wed:** the supervisor, because the plan is a guess and guesses need
  watching.

## Likely snag

**The planner writes essays instead of subtasks.** If the output reads like
an article outline, your done conditions are vague. "Research X" is not a
done condition; "a 5-bullet summary of X with 2 sources" is.

## When you're done

Reply "Day 1 done". Tomorrow's sheet: the workers.
