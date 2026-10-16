# Week 5, Day 3 — Port the Tools (Wednesday, Nov 4)

## The idea

Your three Week 2 tools (fetch_url, run_command, read_file) already have
the right shape: structured in, structured out, errors as observations.
Porting them into LangGraph is mostly an adapter exercise, which is the
point. Well-designed tools survive framework changes. Keep the sandbox
rules exactly as they are. The framework doesn't get a vote on security.

## What you'll build

The three tools registered as LangGraph tools, called from the tool node,
sandbox rules intact.

## Steps

1. **Type the adapters.** Wrap each Week 2 tool so the graph can call it.
   One chunk per tool: fetch first, then shell, then file.
2. **Run each tool through the graph**, including one deliberate failure per
   tool (the same three as Week 2: 404, timeout, path escape).
3. **Confirm the sandbox rules survived the move.** run_command still pinned
   to SAFE_DIR, read_file still rejects escapes. Test both rejections on
   purpose.
4. **Commit.** `week-05 day-03: Week 2 tools ported with sandbox rules
   intact`. Breakage log.

## Done criteria (binary)

- [ ] All three tools run through the graph, and the deliberate failures
      still return structured observations.

## What this unlocks

- **Thu:** human-in-the-loop interrupts and checkpointing.
- **Fri:** the verdict: whiteboard the execution model and name what the
  framework does worse.

## Likely snag

**The framework wants to "help" with errors.** If LangGraph's default error
handling swallows your structured errors, bypass it. Your error contract
outranks the framework's convenience.

## When you're done

Reply "Day 3 done". Tomorrow's sheet: interrupts and checkpointing.
