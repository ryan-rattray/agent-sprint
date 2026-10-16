# Week 3, Day 2 — The Fact Store (Tuesday, Oct 20)

## The idea

The sliding window is amnesia with a delay. For anything that must survive a
restart, you need durable memory: a store of facts with timestamps, written
deliberately and queried on demand. SQLite is the right tool: stdlib,
file-based, zero setup, and it forces you to think about schema. What is a
fact, exactly? Today's answer: text, a timestamp, and a source.

## What you'll build

`week-03-memory/fact_store.py`: a SQLite table `facts(id, fact_text,
learned_at, source)` with two operations, `remember(fact, source)` and
`recall(query)`. Retrieval starts as keyword match. No embeddings this week;
the lesson is the write/query discipline, not retrieval quality.

## Steps

1. **Type the schema and the two functions.** Create the DB file next to
   your agent. Small chunks: schema first, then `remember`, then `recall`.
2. **Seed it by hand** with 5-10 real facts from your sprint ("SAFE_DIR is
   the sandbox", "the timeout bug hid on the unhappy path").
3. **Kill the process and start fresh.** Read the facts back. The restart is
   the test: memory that dies with the process isn't memory.
4. **Commit.** `week-03 day-02: SQLite fact store with timestamps`. Breakage
   log.

## Done criteria (binary)

- [ ] A fact written Tuesday is recalled on demand across a full process
      restart.
- [ ] You can explain the schema: what each column is for and why the
      timestamp matters.

## What this unlocks

- **Wed:** the summarization step writes into this store.
- **Thu:** the agent queries it at the start of every run.

## Likely snag

**Treating recall as search-engine magic.** Keyword match is dumb on purpose
this week. If you're tempted to reach for embeddings, that's parking-lot
material. The discipline (deliberate writes, timestamped reads) is the
lesson.

## When you're done

Reply "Day 2 done". Tomorrow's sheet: summarization, the interesting day.
