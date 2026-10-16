# Week 7, Day 3 — Costs and Timeouts (Wednesday, Nov 18)

## The idea

Two production guarantees: no run burns unbounded money, no run hangs
forever. Per-run cost tracking (your Week 6 tracker, now per request) goes
into the log line, and a timeout kills runs that exceed it. These are the
same guardrails from Weeks 1 and 2 wearing production clothes: iteration
caps and timeouts were always about this.

## What you'll build

Cost accumulation per request added to the log, plus a request timeout that
aborts long runs with a clean structured response instead of a hang.

## Steps

1. **Type the per-request cost accumulator**, reusing the Week 6 tracker.
   Each log line gets tokens and dollars.
2. **Type the timeout.** Kill the agent run past N seconds; return a
   structured timeout response.
3. **Test both deliberately.** A normal run (check the cost line), then a
   run that exceeds the timeout (confirm the clean abort, no hang).
4. **Commit.** `week-07 day-03: per-run cost tracking and request timeouts`.
   Breakage log.

## Done criteria (binary)

- [ ] Every log line carries the run's token count and dollar cost.
- [ ] A run exceeding the timeout aborts cleanly with a structured
      response.

## What this unlocks

- **Thu:** /health and malformed requests, the last two production pieces.
- **Fri:** the full production proof via curl.

## Likely snag

**Timeouts that kill the server instead of the request.** The timeout must
scope to the request, not the process. Test by sending a second request
right after aborting the first. The server should still be standing.

## When you're done

Reply "Day 3 done". Tomorrow's sheet: health checks and hostile input.
