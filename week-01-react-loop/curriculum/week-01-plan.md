# Week 1 — The Agent Loop, From Scratch (Oct 5–11)

**The one idea:** An agent is a loop, and the model never *does* anything — it emits text, your code acts, and the result goes back in as more text. By Friday you'll have seen the whole trick.

*Prereqs (weekend before):* Gemini API key live, repo + virtualenv ready — see the API setup checklist.

## Mon — First contact
Get a prompt → response round-trip working against the Gemini API in a single script. Wrap it in an `ask(prompt)` function. Done when you can print a reply.

## Tue — Teach it the ReAct shape
Your prompt instructs the model to reason in a strict format:

```
Thought: I need to compute 12*34 first.
Action: calculator
Action Input: 12*34
```

Your code parses the `Action:` / `Action Input:` lines (regex is fine), runs the tool, and appends `Observation: 408` to the prompt. The core mechanism: the model never touches the calculator — it writes the word "calculator" and *you* do the rest.

## Wed — Tools
Build two:

- **Calculator** — parse with `ast`, never `eval` (real engineering habit from day one).
- **Stub search** — a dict of canned answers.

A registry maps names to functions: `{"calculator": calc_fn, "search": search_fn}`. Unknown tool name → feed back `Observation: unknown tool` and let the model recover on its own.

## Thu — The loop
Wire it: prompt → parse → execute → append observation → repeat, until the model writes `Final Answer:` or you hit max iterations (8 is a good number). Malformed output — no Action line, garbage format — gets fed back as an error observation so the model can retry. This is where you meet the loop's failure modes firsthand.

## Fri — Prove it
Three multi-step questions, each needing both tools, run end-to-end. Then deliberately break it: a tool that raises, garbage model output, max iterations hit. Write down what happens in each case — that's your Week 6 seed.

## Weekend — Buffer + the explain test
Done means 3 questions solved **and** you can explain out loud exactly what happens on a malformed tool call. If you can't explain it, you're not done.

## What you'll own by Sunday
- The model emits text; your code acts. There is no magic step.
- Observations are just prompt text — the context grows every iteration (which is exactly why Week 3 exists).
- Error handling *is* the agent. The loop that recovers is the whole game.
