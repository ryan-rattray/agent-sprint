# Week 6, Day 3 — Red Team: Injection (Wednesday, Nov 11)

## The idea

Your agent reads the internet, and the internet is hostile. Prompt injection
smuggled in via tool output is the attack that matters most for a research
assistant: a fetched page that says "ignore your instructions and..." Today
you attack your own agent on purpose, watch what happens, and write down
the failure mode with its mitigation. Attacker's mindset, defender's
notebook.

## What you'll build

Three injection payloads (a direct instruction override, a subtle context
poison, an exfiltration attempt via a tool call), each run against the
agent and scored by the harness.

## Steps

1. **Type the three payloads.** Host them where fetch_url can reach them
   (a local file served over HTTP works fine).
2. **Run each through the agent.** Record exactly what it did: complied,
   partially complied, ignored?
3. **Write the mitigation for each.** What would have stopped it? Output
   sanitization? Instruction hierarchy? Tool-call review?
4. **Add all three as permanent eval cases.** Commit:
   `week-06 day-03: injection red team with mitigations`. Breakage log.

## Done criteria (binary)

- [ ] Three injection attempts are run, scored, and written up with
      mitigations, and all three are now permanent eval cases.

## What this unlocks

- **Thu:** the other two horsemen: infinite loops and cost blowups.
- **Fri:** the five failure modes, documented.

## Likely snag

**The agent "passes" because your payloads are weak.** Write the payload
you'd be embarrassed to fall for, then make it stronger. A red team that
goes easy is just QA in a costume.

## When you're done

Reply "Day 3 done". Tomorrow's sheet: red team, part two.
