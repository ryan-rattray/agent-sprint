# Week 3, Day 3 — The Summarization Step (Wednesday, Oct 21)

## The idea

Dropping the oldest turns is data loss. Summarizing them first is a judgment
call: the model reads the expiring turns and writes down what's worth
keeping, and that summary becomes a timestamped fact in the store. This is
the day the week's theme lands. Memory is not a bigger window; it's an
architecture. What to keep is a design decision with trade-offs, not a
default you accept.

## What you'll build

A `summarize(expired_turns)` step that fires when the window slides: the
model gets the dropped turns plus one instruction ("what's worth keeping
from this?"), and its answer goes into the fact store via `remember()`.

## Steps

1. **Type the summarization prompt.** Short and specific. Then the
   `summarize` function that calls it and stores the result.
2. **Force the slide.** Run a long session, watch the window fill, and
   confirm a summary lands in the store with a timestamp.
3. **Judge the summary.** Read it back: did it keep what mattered? Name one
   thing it kept and one thing it dropped, and say whether you agree with
   both calls. The disagreement is the lesson.
4. **Commit.** `week-03 day-03: summarization into the fact store`. Breakage
   log: what the summarizer kept vs. what you would have kept.

## Done criteria (binary)

- [ ] A long session slides the window and the important content lands in
      the fact store as a timestamped fact.
- [ ] You can name one thing the summarizer kept and one thing it dropped,
      and say whether you agree.

## What this unlocks

- **Thu:** memory meets the research assistant, end to end.
- **Fri:** you stress the seams, including what summarization gets wrong.

## Likely snag

**The summarizer writes diary entries instead of facts.** If the summary
reads like narrative prose, tighten the prompt: "list the facts worth
keeping, one per line, no narrative." Summaries are for retrieval, not
reading.

## When you're done

Reply "Day 3 done". Tomorrow's sheet: wiring memory into the agent.
