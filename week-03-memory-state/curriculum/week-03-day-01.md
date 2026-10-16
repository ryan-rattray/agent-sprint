# Week 3, Day 1 — The Sliding Window (Monday, Oct 19)

## The idea

The model's context window is finite. Every turn of the loop appends to the
prompt, so a long session eventually pushes the earliest turns out. Before
building anything fancy, you need to see this failure with your own eyes: cap
what the agent sees to the last N exchanges and watch what breaks. The
mechanism is trivial. The lesson is not.

## What you'll build

A `SlidingWindow` in `week-03-memory/memory.py`: keeps the last N exchanges
(start with 10), drops the oldest as new ones arrive. Wire it into your loop
so the model only ever sees the window, never the full history.

## Steps

1. **Type the window.** An append method and a `get()` returning the last N.
   Keep it under 30 lines, comments in your own words.
2. **Wire it into the loop.** The prompt is built from the window, not the
   full history. One small chunk: find where the prompt is assembled and
   swap the source.
3. **Watch the cut.** Run a multi-turn conversation. Find the exact turn
   where early context falls off and write down what the agent forgot.
4. **Commit.** `week-03 day-01: sliding window short-term memory`. Breakage
   log: what broke when context fell off, and where exactly the window cut.

## Done criteria (binary)

- [ ] The agent holds a multi-turn conversation using only the window.
- [ ] You can point to the exact place the window cuts and name what was lost.

## What this unlocks

- **Tue:** the fact store, so dropped context has somewhere to go instead of
  vanishing.
- **Wed:** summarization, which decides what survives the slide.

## Likely snag

**Off-by-one confusion about what counts as an "exchange".** Define it
crisply: one user turn plus the agent's full response (thought, action,
observation). Count those, not individual messages.

## When you're done

Reply "Day 1 done". Tomorrow's sheet: the long-term fact store.
