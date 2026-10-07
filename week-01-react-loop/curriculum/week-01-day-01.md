# Week 1, Day 1 — First Contact (Monday, Oct 5)

## The idea

Before an agent can loop, it needs a voice. Today you build the single function everything
else this week stacks on: `ask(prompt)` — text in, text out, through the Gemini API.
No loop, no tools, no parsing. Just prove the wire is live and wrap it cleanly, because
every day from Tuesday onward calls this function.

This is deliberately boring. Boring and reliable is the whole point — if `ask()` is
flaky, everything downstream wobbles.

## What you'll build

One script, `week-01-react-loop/ask.py`, containing:

- **`ask(prompt) -> str`** — sends `prompt` to the Gemini API, returns the reply text.
  Reads the API key from the `GEMINI_API_KEY` environment variable. Never hardcodes it.
- **A `__main__` block** — calls `ask("This sentence has five words.")` and prints the
  reply. (Your Day 0 smoke test, repackaged as a permanent self-test.)

## Steps

1. **Scaffold the project** (do this with Muse when you're at the laptop):
   `cd` to `C:\Users\ryant\OneDrive\Documents`, create the `agent-sprint/` tree,
   `git init`, add the `.gitignore`, first commit.
2. **Create `week-01-react-loop/ask.py`.**
3. **Write `ask()`.** Reuse the API-call pattern from your `smoke_test.py`. Key comes
   from `os.environ["GEMINI_API_KEY"]` — fail loudly with a clear message if it's missing.
   Model: `gemini-3.8-flash` (or `gemini-3.5-flash` if you prefer the faster one —
   note your choice in the README; either is fine).
4. **Add the `__main__` test block** described above.
5. **Run it:** `python ask.py`. Done when a Gemini reply prints with no manual steps.
6. **Verify the import:** from the same folder, `python -c "from ask import ask; print(ask('Say hi'))"`
   should work. Tuesday's code will import this.
7. **Commit.** Message something like `week-01 day-01: ask() wrapper live`.
```python
cd /d D:\agent-sprint
git add -A
git commit -m "week-01 day-01: ask() wrapper live"
git push
```

## Done criteria (binary)

- [ ] `python ask.py` prints a Gemini reply, no manual steps.
- [ ] `ask()` is importable from another script in the same folder.
- [ ] API key comes from the environment, not from code.

## What this unlocks

- **Tue:** a ReAct-shaped prompt goes through this exact function.
- **Wed:** tools get called based on what comes back through it.
- **Thu:** the loop — prompt → parse → act → repeat — is built around it.

## Likely snag

**HTTP 503s** from the API (you saw these on Day 0). For today, a clear error is fine —
don't build retry machinery yet. Thursday's loop will need it; just note the 503s in
your daily log so the pattern is visible when you get there.

## When you're done

Reply to the check-in with "Day 1 done" (or what's stuck). Tomorrow's sheet covers
teaching the model the ReAct shape.
