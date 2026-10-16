# Week 7, Day 4 — Health Checks and Hostile Input (Thursday, Nov 19)

## The idea

Two more boring pieces. A /health endpoint that answers "am I alive"
without running the agent (load balancers and uptime monitors need this).
And hostile input handling: malformed JSON, missing fields, absurdly long
questions. Each gets a clean 4xx, never a crash, never a traceback leaking
internals.

## What you'll build

`GET /health` returning status plus a version string, and request
validation that rejects malformed input with structured errors.

## Steps

1. **Type the /health endpoint.** It must not call the agent; liveness only.
2. **Type the input validation.** Schema-check the request body before the
   agent ever sees it (Week 2's validation instinct, at the HTTP layer).
3. **Attack it deliberately.** Malformed JSON, a missing question field, a
   100KB question. Confirm clean 4xx responses, no tracebacks.
4. **Commit.** `week-07 day-04: health check and hostile-input handling`.
   Breakage log.

## Done criteria (binary)

- [ ] /health returns 200 without invoking the agent.
- [ ] Three hostile inputs each return clean 4xx responses with no
      traceback leakage.

## What this unlocks

- **Fri:** the production proof: curl everything, read the logs, confirm
  the bills.

## Likely snag

**Validation that duplicates the agent's parsing.** Keep the HTTP layer
dumb: shape checks only (is there a question, is it a string, is it under
the size cap?). Meaning belongs to the agent.

## When you're done

Reply "Day 4 done". Tomorrow's sheet: the production proof.
