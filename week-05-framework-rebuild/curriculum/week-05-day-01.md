# Week 5, Day 1 — The Graph Skeleton (Monday, Nov 2)

## The idea

Frameworks are opinions about graphs. LangGraph's opinion: your agent is a
set of nodes (each does one thing) connected by edges (each decides what
happens next), with shared state flowing through. Today you learn that
opinion by rebuilding the skeleton of your Week 2 agent: a model node, a
tool node, and the edge between them. No tools ported yet, no fancy routing.
Just the shape.

## What you'll build

`week-05-langgraph/` with a `StateGraph`: state holds the message list; one
node calls the model, one node executes tools. Install `langgraph` in your
conda env first.

## Steps

1. **Install langgraph** in the agent-sprint env. Pin the version and note
   it in the README; the library moves fast.
2. **Type the state schema.** Message list, nothing else. Smallest possible
   chunk.
3. **Type the two nodes**: `call_model` and `run_tools`. Typed by hand,
   comments in your own words.
4. **Connect them with a plain edge** and run one turn. Watch state flow
   through both nodes.
5. **Commit.** `week-05 day-01: LangGraph skeleton with two nodes`.
   Breakage log.

## Done criteria (binary)

- [ ] The graph runs one model-then-tools turn with state flowing through
      both nodes.

## What this unlocks

- **Tue:** conditional edges, so the graph decides when it's done.
- **Wed:** your real tools move in as LangGraph tools.

## Likely snag

**Version churn.** If a tutorial's API doesn't match your installed version,
trust your installed version's docs, not the tutorial. Pinning the version
today saves an hour of confusion later.

## When you're done

Reply "Day 1 done". Tomorrow's sheet: conditional edges.
