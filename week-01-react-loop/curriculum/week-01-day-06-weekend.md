# Week 1, Weekend — Buffer + the Explain Test (Sat–Sun, Oct 10–11)

## The idea

The week's binary done criteria aren't all in the code. They're in your mouth: **you
can explain out loud exactly what happens on a malformed tool call.** If you can
narrate the path — model emits garbage → parser returns None → loop appends a
correction observation → model retries — you're done. If you stumble, the weekend is
your buffer: finish the code first, then rehearse the explanation.

## What to do

1. **Catch up** on any unfinished day. The week is done when Friday's criteria are
   met, not when Sunday arrives.
2. **The explain test.** Out loud, no notes, walk through: (a) a normal two-step
   turn, (b) a malformed tool call, (c) a tool that raises, (d) the iteration cap.
   If any step is fuzzy, re-read that day's trace until it's crisp.
3. **Week 1 README line.** Add one line to `agent-sprint/README.md`: what you built,
   where it lives. (This file becomes the Week 8 portfolio README skeleton.)
4. **Park the spillover.** Anything you wanted to add but didn't belongs inside this
   week's fence — file it in the sprint parking lot, not in the code.

## Done criteria (binary)

- [ ] Friday's criteria met (3 questions solved, breakage log written).
- [ ] You can explain the malformed-tool-call path out loud without notes.

## What this unlocks

- **Week 2** (Oct 12–18): tools get serious — fetching real data, touching the
  filesystem. The loop you just built is the engine everything else bolts onto.

## When you're done

Reply "Week 1 done" — and Monday's check-in starts Week 2.
