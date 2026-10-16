# Week 2, Day 4 — The Research Assistant (Thursday, Oct 15)

## The idea

Everything this week becomes one build: a question comes in, the agent plans
which tools to use, makes at least three tool calls across your real tools, and
synthesizes an answer that **cites its sources** — which URL, which file, which
command output. Citations aren't decoration here. They're the only way you can
verify an agent that touched the real world: if you can't check where an answer
came from, you can't trust it. This is the pattern your Week 8 capstone lives
on, and it's the pattern the parked VeriHarness and ReviewBench entries are
about verifying.

## What you'll build

`week-02-real-tools/research_agent.py`:

- **The wired loop:** your Week 1 `run()` + three real tools + Wednesday's schema
  validation, all working together. No new tools today — the build is the
  wiring.
- **A citation rule in the prompt:** the final answer must name its sources —
  e.g. "per the fetched page (URL), the README in the safe dir says X, and
  `dir` listed Y." Teach the prompt this; the schema enforces the tool calls,
  the prompt enforces the citations.
- **One real question** you genuinely don't know the answer to — pick something
  small and verifiable (a version number, a date, a stat from a docs page). If
  you already know the answer, you can't tell whether the agent actually used
  its tools. The point is to *watch it work*, not to learn the fact.

## Steps

1. **Pick your question.** Genuinely unknown to you, answerable with your three
   tools, verifiable by you afterward.
2. **Add the citation requirement** to the system prompt: final answers cite
   sources or they're incomplete.
3. **Run it.** Require at least three tool calls before the final answer. Print
   the full trace — this trace is your best Week 6 eval seed yet, because the
   tools are real.
4. **Verify the citations yourself.** Open the URL, read the file, re-run the
   command. If a citation doesn't check out, that's a finding — write it down,
   don't wave it away.
5. **Commit.** `week-02 day-04: research assistant with citations`.

## Done criteria (binary)

- [ ] A real, previously-unknown question is answered end to end with at least
      three tool calls, and every factual claim cites a source you verified.

## What this unlocks

- **Fri:** you break it on purpose — the proof that the error contracts hold.
- **Week 8:** this is the agent the eval harness will be measuring.

## Likely snag

**The agent answers from its own weights without touching any tools.** LLMs are
confident know-it-alls — your prompt has to *require* tool use before a final
answer ("you must call at least one tool before answering; state what you're
uncertain about first"). If it still skips tools, make the citation rule
non-negotiable: no citations, no final answer accepted.

## When you're done

Reply "Day 4 done". Tomorrow's sheet: prove it — break it on purpose.
