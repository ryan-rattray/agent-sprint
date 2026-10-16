# Week 7, Day 2 — Auth and Logging (Tuesday, Nov 17)

## The idea

An open endpoint is a public utility. API-key auth draws the line between
yours and everyone else's, and request logging draws the line between "it
worked" and "I can prove it worked." Both are boring. Both are what make it
a product.

## What you'll build

An API-key check on every request (key in a header, compared against an env
var, never in code) plus structured request logging: timestamp, question
hash, run duration, outcome.

## Steps

1. **Type the auth dependency.** Read the key from the header, compare to
   the env var, 401 otherwise. Small chunk.
2. **Type the logging.** One structured line per request; JSON to a file is
   fine.
3. **Curl twice**: once with the right key, once without. Confirm 200 vs.
   401, then check the log.
4. **Commit.** `week-07 day-02: API-key auth and request logging`. Breakage
   log.

## Done criteria (binary)

- [ ] Correct key returns 200 with the answer; wrong or missing key returns
      401; both requests appear in the log.

## What this unlocks

- **Wed:** per-run cost tracking joins the log line.
- **Thu:** health checks and malformed-request survival.

## Likely snag

**The key in code.** If the API key appears anywhere git can see, stop and
rotate it. Env var or a local secrets file that's gitignored. This is the
pre-public secret scrub habit, applied daily.

## When you're done

Reply "Day 2 done". Tomorrow's sheet: costs and timeouts.
