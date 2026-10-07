# Day 1 — First Contact (Oct 6, 2026)

## What was built

`ask.py`: one function, `ask(prompt) -> str`. Text in, text out, through the
Gemini API. No loop, no tools, no parsing — just proof the wire is live, wrapped
cleanly enough that every later day can import it. Deliberately boring; boring and
reliable is the point, because if `ask()` wobbles, everything downstream wobbles.

**Done criteria (all met):** `python ask.py` prints a Gemini reply with no manual
steps · `ask()` imports cleanly from another script · key comes from the
environment, never from code.

## Line-by-line walkthrough

```python
"""Day 1 - a reusable Gemini wrapper.

No tools, no loops, no parsing yet. One job: send a prompt, get text back.
The API key comes from the GEMINI_API_KEY environment variable, never from code.
"""
```

The docstring is the contract. Anyone (or any model) opening this file learns the
rules in ten seconds: one job, and the key never lives in code.

```python
import json
import os
import sys
import urllib.request
```

Standard library only — no `pip install` step, nothing to break on a fresh
machine. Each import earns its place: `json` builds the request body and parses
the response, `os` reads the environment variable, `sys` reads command-line
arguments in the self-test block, `urllib.request` does the HTTPS call.

```python
MODEL = "gemini-3.7-flash"
ENDPOINT = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"
```

The model name lives in exactly one place, and the endpoint URL is derived from
it — so switching models means editing one line, not hunting through the file.
(History: this started as `gemini-3.8-flash`. On Oct 7 both `3.8-flash` and the
`gemini-flash-latest` alias returned HTTP 503s; `gemini-2.5-flash` returns 404
because new API keys can't invoke older models. `3.7-flash` works. See Day 2's
summary for the full story.)

```python
def ask(prompt: str) -> str:
    """Send *prompt* to Gemini and return the model's text reply."""
```

The foundation of the whole week: a plain function, text in, text out. Every
day from here on calls this.

```python
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY environment variable is not set")
```

The key comes from the environment, never from source code — so it can never
leak into the git repo. If it's missing, fail loudly with a message that tells
you exactly what to do, instead of sending a broken request and getting a
cryptic API error back.

```python
    body = json.dumps({"contents": [{"parts": [{"text": prompt}]}]}).encode("utf-8")
```

This is Gemini's request shape: `contents` → `parts` → `text`. The nesting looks
odd, but it's the API's envelope format (it supports multi-part prompts: text +
images). `.encode("utf-8")` turns the JSON string into bytes, because HTTP sends
bytes, not strings.

```python
    request = urllib.request.Request(
        f"{ENDPOINT}?key={api_key}",
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
```

Builds the POST request. The key rides as a `?key=` query parameter — that's
Google's convention for API keys. `Content-Type: application/json` tells the
server how to read the body. `method="POST"` because we're *sending* data
(a GET with a body would be ignored or rejected).

```python
    with urllib.request.urlopen(request) as response:
        payload = json.loads(response.read().decode("utf-8"))
```

Sends the request and reads the reply. The `with` block closes the network
connection cleanly when done. `response.read()` gives bytes → `.decode("utf-8")`
gives a string → `json.loads` gives a Python dict.

```python
    return payload["candidates"][0]["content"]["parts"][0]["text"]
```

Walks the response JSON down to the actual text. The `[0]`s are there because
the API returns *lists* — multiple answer candidates, each with multiple parts.
We take the first candidate's first part: the model's reply.

```python
if __name__ == "__main__":
    prompt = " ".join(sys.argv[1:]) or "Explain what a ReAct loop is in one sentence."
    print(ask(prompt))
```

The permanent self-test. Run `python ask.py` and it exercises the whole path
with zero manual steps. `" ".join(sys.argv[1:])` lets you pass your own prompt
from the command line (`python ask.py Say hi`); if you pass nothing, it falls
back to the default question. The `if __name__ == "__main__"` guard means this
block only runs when you execute the file directly — importing `ask` from
another script (which is what Days 2–5 do) skips it.

## Why it matters

Days 2 through 5 all funnel through this function. The ReAct prompt goes
through it, the loop calls it every iteration, the eval harness will call it
hundreds of times. One reliable choke point beats five scattered API calls.

## Later update (Oct 7)

`MODEL` changed from `gemini-3.8-flash` to `gemini-3.7-flash` after the 503
diagnosis described in Day 2's summary. Nothing else in the file changed.
