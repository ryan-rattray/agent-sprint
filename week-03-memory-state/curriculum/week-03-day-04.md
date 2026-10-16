# Week 3, Day 4 — Memory Meets the Agent (Thursday, Oct 22)

## The idea

Three components, one loop. At the start of a run the agent queries the
fact store for relevant context; during the run the sliding window manages
the conversation; at the end (or when the window fills) new facts get
written back. Today is plumbing: no new concepts, just the discipline of
wiring three pieces together without breaking the Week 2 agent.

## What you'll build

The wired research assistant: `recall()` at startup (relevant facts injected
into the opening prompt), the sliding window during the run, `remember()`
for anything new at the end.

## Steps

1. **Type the startup query.** Before the first model call, pull relevant
   facts and prepend them to the prompt. One small chunk.
2. **Type the write-back.** At run end, ask the model "anything worth
   remembering?" and store what it says via `remember()`.
3. **Run it live.** Teach it a fact in one session, start a completely fresh
   session, and ask a question that needs that fact.
4. **Commit.** `week-03 day-04: memory wired into the research assistant`.
   Breakage log.

## Done criteria (binary)

- [ ] The agent answers a question using a fact from a previous session,
      live and end to end.

## What this unlocks

- **Fri:** you attack the seams on purpose: stale facts, contradictions,
  forced summarizations.

## Likely snag

**The write-back stores trivia.** "Anything worth remembering?" will happily
store noise. That's fine today. Friday you learn why indiscriminate writing
is a failure mode with real consequences.

## When you're done

Reply "Day 4 done". Tomorrow's sheet: proving it by breaking it.
