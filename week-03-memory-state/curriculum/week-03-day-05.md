# Week 3, Day 5 — Stress the Seams (Friday, Oct 23)

## The idea

Memory fails in specific ways, and you want to meet each one in a lab before
meeting it in production. Three experiments: a fact that becomes wrong
(stale memory), two contradictory facts (which wins, and why?), and a
session long enough to force multiple summarizations (what survives two
rounds of compression?). Write down what happened in each case. This is
Week 6's world in miniature.

## What you'll build

Three scenarios run against your wired agent, plus a written record of the
outcomes. The write-up is the deliverable as much as the runs.

## Steps

1. **Stale fact.** Teach it X, then teach it not-X. Ask about X. Does the
   agent notice the conflict? Which timestamp wins?
2. **Contradiction.** Seed two contradictory facts with different timestamps
   and different sources. Ask. Record which one the agent used and why.
3. **Double compression.** Run a session long enough to summarize twice.
   Compare what survived round one vs. round two.
4. **Write it all up** in the breakage log, then commit:
   `week-03 day-05: memory stress tests and findings`.

## Done criteria (binary)

- [ ] The agent recalls a fact from a previous session.
- [ ] You can explain exactly what got summarized away, what was kept, and
      why, for the compression test.
- [ ] All three experiments are written up with outcomes.

## What this unlocks

- **Week 4** (Oct 26-30): one loop can't do everything. The
  planner-executor, with memory as the shared state the workers read.

## Likely snag

**No clean answer for contradictions.** That's the point. Timestamp-wins and
source-wins are both defensible policies. The deliverable is the documented
decision, not the right answer.

## When you're done

Reply "Day 5 done". Weekend sheet: buffer and the explain test.
