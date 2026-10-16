# Week 7, Day 5 — The Production Proof (Friday, Nov 20)

## The idea

The week's done criteria, proven in one session: curl the endpoint,
confirm every run is logged with its token cost, and confirm it survives
malformed requests without crashing. Then read the logs like an operator,
not a developer: what would you alert on? What would you bill on? Write
both answers down.

## What you'll build

A proof session (a short script or a curl batch) plus operator notes: what
to alert on, what to bill on.

## Steps

1. **Curl the full matrix.** Good request, bad key, malformed body,
   oversized question, /health.
2. **Read the logs.** Verify every run has its cost line.
3. **Write the operator notes.** Two alerts you'd set, one billing rule
   you'd enforce.
4. **Commit.** `week-07 day-05: production proof with operator notes`.
   Breakage log.

## Done criteria (binary)

- [ ] You can curl it, every run is logged with its token cost, and
      malformed requests don't crash it.

## What this unlocks

- **Week 8** (Nov 23-27): capstone. The production wrapper is now a solved
  problem; the capstone inherits it instead of building it.

## Likely snag

**Proving it once and calling it robust.** Run the matrix twice. The second
run catches the state you didn't know the first run left behind.

## When you're done

Reply "Day 5 done". Weekend sheet: buffer and the explain test.
