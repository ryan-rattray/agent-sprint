# Week 02 — Tools & Structured Output

## What we're building

Replacing the Week 1 ReAct loop's stub tools and free-text responses with real tool implementations and structured output.

## Key pieces

- **Real tools** — actual file I/O, shell execution, and web fetch instead of hardcoded stubs
- **Structured output** — JSON schema / typed responses so the agent's output is machine-readable and deterministic
- **Tool registry** — a proper tool-definition system (name, description, parameter schema) that the LLM can reason over
- **Parse + validate** — take the LLM's tool-call response, parse it, validate against the schema, and route to the right tool

## Why

The Week 1 loop works but everything is fake — tools return canned strings and the agent just dumps free text. This week makes it real: the agent can actually read files, run commands, and fetch URLs, and its responses are structured enough that downstream code can act on them reliably.