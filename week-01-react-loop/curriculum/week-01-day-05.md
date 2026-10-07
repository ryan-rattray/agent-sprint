# Week 1, Day 5 — Prove It (Friday, Oct 9)

## The idea

Today's artifact isn't code — it's proof. Three multi-step questions, each requiring
both tools, run end-to-end through `run()`. Then you attack your own agent: a tool
that raises, garbage model output, the iteration cap — and you write down exactly
what happens in each case. That breakage log is the seed of your Week 6 eval
harness. Engineers don't trust what they haven't broken.

## What you'll build

- **Three test questions** (write them fresh today), each needing the calculator
  *and* the search. Example shape: "What is the boiling point of water in Fahrenheit,
  multiplied by the number of planets?" — search for the facts, calculator for the math.
- **A breakage log** in `notes/daily-log.md` (or `week-01-react-loop/breakage-log.md`):
  three entries, each with what you did and what the loop actually did.

## Steps

1. **Write your three questions.** Make sure every needed fact is in the stub search
   dict — add entries if not. (The point is the loop mechanics, not the search's
   coverage.)
2. **Run all three through `run()`.** Record: solved? how many iterations? any
   recovery turns?
3. **Breakage 1 — the tool raises.** Call the loop on an expression that errors
   (`calculator("1/0")`), or add a tool that raises unconditionally. What does the
   loop do with the exception? If it crashes, that's a finding — wrap dispatch in
   try/except so tool errors become observations.
4. **Breakage 2 — garbage output.** Feed the parser a nonsense reply directly
   (Thursday's one-liner) and record the recovery.
5. **Breakage 3 — max iterations.** The unanswerable question again; record where it
   stopped and what `run()` returned.
6. **Write the breakage log.** Three entries, honest and specific — "the loop retried
   twice then hit the cap" beats "it worked."
7. **Commit.** `week-01 day-05: three questions solved + breakage log`.

## Done criteria (binary)

- [ ] Three multi-step questions solved end-to-end, traces saved or printed.
- [ ] Breakage log documents all three failure cases with what the loop actually did.

## What this unlocks

- **Weekend:** the explain test — the real done criteria.
- **Week 6:** this log is the first draft of your eval suite's failure taxonomy.

## Likely snag

**One of the three questions fails for a silly reason** — a missing search entry, a
format hiccup. Fix it, note it in the log. The log is allowed to contain "first
attempt failed because X; fixed by Y." That's what it's for.

## When you're done

Reply "Day 5 done" plus the one-line summary of what broke most interestingly.
Weekend sheet: buffer and the explain test.
