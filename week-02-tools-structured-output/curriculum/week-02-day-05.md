# Week 2, Day 5 — Prove It (Friday, Oct 16)

## The idea

Same ritual as last Friday: you break it on purpose. The difference is that
this week's failures are *real* — a URL that 404s mid-run, a command that hangs
past its timeout, a model output that fails schema validation twice in a row.
Last week you proved the loop could survive its own mistakes. This week you
prove the error contracts hold when the real world is the thing
misbehaving. That's the week in one sentence: toys to tools, hope to contracts.

## What you'll build

No new code — today is evidence. `week-02-real-tools/BREAKAGE_LOG.md`:

- **Breakage 1:** a URL that 404s mid-run. The agent must retry, route around
  (try a different source), or report cleanly — without dying.
- **Breakage 2:** a shell command that times out. Same bar: the timeout becomes
  an observation, the agent adjusts, the run continues or ends honestly.
- **Breakage 3:** a model output that fails schema validation twice in a row.
  The agent must either get it right on the retry or give up with a clear
  statement — "I couldn't produce a valid tool call" beats a silent wrong tool.
- **The proof run:** one question requiring 3+ tool calls, answered with
  verified citations, surviving at least one tool failure along the way. Write
  down what happened in each case — what failed, what the agent did, what you'd
  change.

## Steps

1. **Stage the breakages** — pick your 404 URL, your hanging command (a
   `ping -n 30 127.0.0.1` on Windows is a fine stand-in for a hung process),
   your deliberately tricky prompt.
2. **Run each one.** Watch the traces, not just the final answers — the
   recovery is the product.
3. **Write BREAKAGE_LOG.md.** Three cases, each with: what you broke, what the
   agent did, whether the error contract held. Honest notes, including the ones
   where the recovery was ugly.
4. **The proof run.** One real question, 3+ tool calls, citations, one failure
   survived. This is the run you'll show someone.
5. **Commit.** `week-02 day-05: breakage log and proof run`.

## Done criteria (binary)

- [ ] A question requiring 3+ tool calls is answered with verified citations.
- [ ] BREAKAGE_LOG.md documents three deliberate failures and the agent
      recovered from at least one without dying.

## What this unlocks

- **Week 3:** the context problem you noticed on Day 4 of Week 1 ("the context
      grows every turn — notice it, don't fix it") becomes the whole week.
- **Week 6:** this breakage log is your eval harness's failure test suite.

## Likely snag

**The agent retries the same failing call forever.** Your iteration cap from
Week 1 is the backstop — but "tried the 404 URL four times then gave up" is an
honest finding worth writing down. A smart retry policy is Week 7 territory;
this week, the cap plus the log is enough.

## When you're done

Reply "Day 5 done". The weekend sheet is the buffer plus the explain test.
