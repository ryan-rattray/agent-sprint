# Week 5, Day 4 — Interrupts and Checkpointing (Thursday, Nov 5)

## The idea

Two production-flavored features in one day. A human-in-the-loop interrupt
pauses the graph before a consequential action and waits for approval: your
YMC instinct, implemented as a graph primitive. Checkpointing saves the
state after every step, so a crashed or interrupted run resumes instead of
restarting. Both are about the same thing: control surviving contact with
reality.

## What you'll build

An interrupt before the tool node (approve, edit, or abort the pending tool
call) and a checkpointer on the graph. Then kill a run mid-flight and
resume it.

## Steps

1. **Type the interrupt.** Pause before tool execution, print the pending
   call, accept approve/edit/abort from the keyboard.
2. **Type the checkpointer setup.** Run a task, then kill it halfway
   (Ctrl+C is fine).
3. **Resume from the checkpoint** and watch it continue, not restart.
4. **Commit.** `week-05 day-04: human-in-the-loop interrupt and checkpoint
   resume`. Breakage log.

## Done criteria (binary)

- [ ] A tool call is approved, edited, and aborted through the interrupt
      across three runs.
- [ ] A killed run resumes from its checkpoint instead of restarting.

## What this unlocks

- **Fri:** the framework verdict, from evidence, not impressions.

## Likely snag

**The interrupt fires on every trivial call.** Scope it: interrupt only on
the consequential tools (run_command, not read_file). Approval fatigue is
how humans become rubber stamps.

## When you're done

Reply "Day 4 done". Tomorrow's sheet: the verdict.
