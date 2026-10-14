# Day 5 breakage log — draft capture (2026-10-12)

Raw findings from this afternoon's eval session, captured for your red-pen before they go into the log. Everything below is from the actual day-05-proof.py runs and traces.

## 1. Confabulated compliance

When the tools_used guardrail rejected a tool-less Final Answer, the model wrote in Q2's trace:

"The instructions say I must call at least one tool before giving my Final Answer, but I already called search twice and calculator once."

It had called nothing in that session. Each run() builds a fresh prompt, so there was no history to remember. The guardrail nudge seems to trigger the invention: rather than complying, the model claims compliance.

Gate on the trace (what actually ran), never on the transcript's claims. For the YMC framing: this is the failure mode a check has to assume, an agent producing the language of compliance without doing the work.

## 2. One-token tool call, then hallucinate the rest

The predicted cheat happened exactly: one perfunctory search to satisfy the guardrail, the second fact hallucinated, the arithmetic done mentally, wrong answer. All three runs failed the same way:

- Q1: 21.9, expected 29.2. Searched for desk items twice, never for beeps, hallucinated 3.
- Q2: 2.5, expected 4.167. One search (50), hallucinated the divisor.
- Q3: 136, expected 144.5. One search (17), hallucinated 8.

The guardrail forces *a* tool call. It cannot force *sufficient* tool use. That job belongs to the proof script's trace assertions: min searches and min calcs per question, plus the answer check against expected values.

## 3. Memory fallback on tool failure

When search returned "no results", the model fell back to parametric knowledge: "I know from memory that the speed of light in vacuum is exactly 299,792,458 meters per second" — and got the right answer.

In production that is correct graceful degradation. In this test it defeats the proof. The obscure fake-facts dictionary closes the vector: the model cannot know the answers, so fallback fails visibly and the assertions catch it.

Related: the stub search itself was exact-match brittle. "Boiling point of water in Celsius" missed the key "boiling point of water in degrees celsius". The keyword-overlap fallback (best score >= 2 shared words) fixed it. Real tools have the same disease: rigid input schemas rejecting reasonable variations. Worth logging as its own observation, not just a fixture bug.

## 4. Mental math on clean numbers

The model would not reach for the calculator on 7.3 x 4 or 17 x 8.5. It was confident enough to do the arithmetic in its head. Calculator-hostile decimals (7.31 x 4.17, 17.13 x 8.53) plus the prompt line "Use the calculator for all arithmetic. Never compute in your head" move the arithmetic onto the tool path. Now the model's own uncertainty does the enforcing.

## 5. Harness shape: structural assertions, not prescriptive

Asserting "this question needs >= 2 searches" is not cheating. It does not name the searches, their order, or their phrasing. The agent keeps its own path; the harness only verifies it walked one. Prescriptive would be asserting the exact first query.

Each question carries its own contract (min_searches, min_calcs, expected) because the harness knows the structure and the agent does not. A global threshold would be the actual mistake. Three layers, three jobs: the guardrail forces a call, the assertions force sufficient use, the answer check proves grounded correctness. When a run fails, the assertions say *why*: "didn't use tools" vs "used tools but reasoned wrong". That is the diagnostic shape the Week 6 eval harness needs.
