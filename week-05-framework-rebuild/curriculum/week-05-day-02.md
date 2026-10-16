# Week 5, Day 2 — Conditional Edges (Tuesday, Nov 3)

## The idea

A plain edge always goes to the same place. A conditional edge reads the
state and decides: tool call requested, go to the tool node; final answer
ready, end; error, go to recovery. This is your Week 1 loop's
parse-and-dispatch step wearing graph clothes. The routing function is
small and pure, which makes it testable in a way the old loop wasn't.

## What you'll build

A `route(state)` function plus conditional edges from the model node: to
tools, to end, to a recovery node.

## Steps

1. **Type the routing function.** Inspect the last message, return the next
   node name. Keep it pure: state in, string out.
2. **Wire the conditional edges.** Then test each route on purpose: a tool
   call, a final answer, a malformed model output.
3. **Run the loop to completion** on a simple question.
4. **Commit.** `week-05 day-02: conditional routing with tested routes`.
   Breakage log, especially the malformed-output route.

## Done criteria (binary)

- [ ] All three routes (tools, end, recovery) are tested deliberately and
      behave as designed.

## What this unlocks

- **Wed:** real tools plug into the tool node.
- **Thu:** interrupts and checkpointing, the production-flavored pieces.

## Likely snag

**Routing on vibes instead of structure.** Route on the parsed action (Week
2's schema discipline), not on keywords in the model's prose. If the router
reads English, it's guessing.

## When you're done

Reply "Day 2 done". Tomorrow's sheet: porting your tools.
