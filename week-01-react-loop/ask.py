"""Day 1 - a reusable Gemini wrapper.

No tools, no loops, no parsing yet. One job: send a prompt, get text back.
The API key comes from the GEMINI_API_KEY environment variable, never from code.
"""

import json
import os
import sys
import urllib.request

MODEL ="gemini-3.7-flash"
ENDPOINT = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"


def ask(prompt: str) -> str:
    """Send *prompt* to Gemini and return the model's text reply."""
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY environment variable is not set")

    body = json.dumps({"contents": [{"parts": [{"text": prompt}]}]}).encode("utf-8")
    request = urllib.request.Request(
        f"{ENDPOINT}?key={api_key}",
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(request) as response:
        payload = json.loads(response.read().decode("utf-8"))

    return payload["candidates"][0]["content"]["parts"][0]["text"]


if __name__ == "__main__":
    prompt = " ".join(sys.argv[1:]) or "Explain what a ReAct loop is in one sentence."
    print(ask(prompt))
