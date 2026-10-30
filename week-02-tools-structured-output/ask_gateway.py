"""Day 1.1 - work gateway wrapper. Same job as ask(): prompt in, text out."""

import json
import urllib.request
import keyring

GATEWAY_URL = "https://ai-gateway.nexteer.app/v1/chat/completions"
MODEL = "claude-sonnet-5"
#MODEL = "deepseek-v4-pro"


def ask_gateway(prompt: str) -> str:
    # Send *prompt* through the work gateway, return the model's text reply.
    # Key comes from Windows Credential Manager, never from code or files.
    api_key = keyring.get_password("nexteer-ai-gateway", "api-key")
    if not api_key:
        raise RuntimeError("Gateway API key not found in Credential Manager")
    body = json.dumps({
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
    }).encode("utf-8")
    req = urllib.request.Request(
        GATEWAY_URL,
        data=body,
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"},
    )
    with urllib.request.urlopen(req) as response:
        payload = json.loads(response.read().decode("utf-8"))
    return payload["choices"][0]["message"]["content"]
