# Week 4, Day 2 — The Workers (Tuesday, Oct 27)

## The idea

Workers don't plan; they execute. Take your Week 1 loop, narrow its brief
to a single subtask, give it its own iteration budget, and point it at the
tools. A worker knows nothing about the bigger picture, and that's a
feature: narrow scope means fewer ways to wander. The planner thinks; the
worker does.

## What you'll build

`week-04-orchestration/worker.py`: takes one subtask (objective plus
done_when), runs the ReAct loop with a small iteration cap, returns a
result dict. No planning inside.

## Steps

1. **Type the worker.** Your Week 1 loop, repurposed, with the subtask as
   its entire world. Bite-size: the loop first, the budget cap second.
2. **Hand it a subtask** from yesterday's planner output. Watch it complete
   with no knowledge of the plan.
3. **Judge the result** against the subtask's done condition. Pass or fail;
   no partial credit.
4. **Commit.** `week-04 day-02: narrow executor worker`. Breakage log.

## Done criteria (binary)

- [ ] A worker independently completes a subtask handed to it by the
      planner, judged against the subtask's done condition.

## What this unlocks

- **Wed:** the supervisor gives every worker a budget and a killer.
- **Thu:** planner, workers, and synthesizer run as one system.

## Likely snag

**The worker tries to replan.** If it starts decomposing instead of
executing, the brief is leaking. Narrow the prompt: "Your entire job is
this subtask. Do not plan beyond it."

## When you're done

Reply "Day 2 done". Tomorrow's sheet: the supervisor.
