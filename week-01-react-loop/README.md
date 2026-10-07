# Week 01 — The ReAct Loop

## What we're building

An agent is a loop. The model never does anything itself — it emits text, my code acts, and the result goes back in as more text. This week we build that loop from scratch in plain Python. No frameworks, no magic.

## Day-by-day

- **Mon (DONE)** — Reusable `ask(prompt)` Gemini wrapper. One job: prompt in, text out. Key from `GEMINI_API_KEY`. Already built as `ask.py`.
- **Tue** — Teach the ReAct shape. Prompt the model to reason in Thought/Action/Action Input format. Parse Action lines with regex, run the tool, append "Observation:" to the prompt.
- **Wed** — Two tools: a calculator (parse with `ast`, never `eval`) and a stub search (dict of canned answers). A registry maps tool names to functions; unknown names get fed back as "Observation: unknown tool".
- **Thu** — Wire the full loop: prompt → parse → execute → append observation → repeat, until "Final Answer:" or max 8 iterations. Malformed output gets fed back as an error observation so the model can retry.
- **Fri** — Prove it: 3 multi-step questions needing both tools, run end to end. Then deliberately break it (tool raises, garbage output, max iterations) and write down what happens.
- **Weekend** — Buffer + explain test.

## Done criteria

- 3 multi-step questions solved end to end (both tools used)
- I can explain out loud exactly what happens on a malformed tool call