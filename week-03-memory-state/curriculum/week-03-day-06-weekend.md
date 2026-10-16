# Week 3, Weekend — Buffer + the Explain Test (Sat-Sun, Oct 24-25)

## The idea

Same as always: the week's binary done criteria aren't all in the code.
They're in your mouth. This week's explain test: **what's the difference
between the sliding window and the fact store, what each one is for, what
each one loses, and why you need both instead of just a bigger window?**
Out loud, no notes. If you can also explain what your summarizer kept vs.
dropped on Wednesday and why, you own Week 3.

## What to do

1. **Catch up** on any unfinished day. The week is done when Friday's
   criteria are met, not when Sunday arrives.
2. **The explain test.** Out loud, no notes: (a) sliding window vs. fact
   store, purpose and loss profile of each; (b) why a bigger window doesn't
   solve it; (c) one stale-memory and one contradiction outcome from Friday.
3. **Week 3 README line.** Add one line to `agent-sprint/README.md`:
   two-tier memory, sliding window plus timestamped SQLite fact store with
   summarization.
4. **Park the spillover.** Embeddings-based retrieval, fancier recall,
   memory consolidation schemes: parking lot, not code.

## Done criteria (binary)

- [ ] Friday's criteria met (cross-session recall plus the three experiment
      write-ups, breakage log written).
- [ ] You can explain out loud, without notes, why memory is an
      architecture and not a window size.

## What this unlocks

- **Week 4** (Oct 26-30): planning and orchestration. The planner
  decomposes, workers execute, the supervisor watches, and memory is the
  shared state they all read.

## When you're done

Reply "Week 3 done" — and Monday's check-in starts Week 4.
