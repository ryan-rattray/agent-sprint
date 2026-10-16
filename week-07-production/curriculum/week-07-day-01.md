# Week 7, Day 1 — The Endpoint (Monday, Nov 16)

## The idea

A demo runs when you're watching. A product runs when you're not. Today
the agent moves behind an HTTP endpoint: FastAPI, one POST route that takes
a question and returns the agent's answer. Nothing else: no auth, no
logging, no polish. The narrowest possible slice that proves the agent can
live behind HTTP.

## What you'll build

`week-07-production/app.py`: a FastAPI app with `POST /ask` accepting
`{"question": "..."}` and returning the agent's final answer as JSON.

## Steps

1. **Install fastapi and uvicorn** in your conda env. Then type the app
   skeleton: one route, wired to your agent's entry point.
2. **Run it locally** with uvicorn. Curl the endpoint with a real question.
3. **Confirm the answer matches** what the agent produces standalone. Same
   brain, new mouth.
4. **Commit.** `week-07 day-01: FastAPI endpoint serving the agent`.
   Breakage log.

## Done criteria (binary)

- [ ] A curl POST to /ask returns the agent's answer for a real question.

## What this unlocks

- **Tue:** auth and logging, so you know who asked and what happened.
- **Wed:** cost tracking and timeouts, so it can't burn money or hang.

## Likely snag

**The agent blocks the event loop.** Your agent is synchronous; FastAPI is
async. Run the agent in a threadpool (or accept the block for now and note
it). Don't rewrite the agent today. The endpoint is the deliverable.

## When you're done

Reply "Day 1 done". Tomorrow's sheet: auth and logging.
