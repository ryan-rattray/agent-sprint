# Day 1 breakage log (2026-10-14)

Findings from the fetch_url build session. The tool took twenty minutes; the environment took the rest of the morning. Every detour taught something real.

## 1. The environment is part of the system

First fetch failed with `SSL: CERTIFICATE_VERIFY_FAILED`. The diagnosis, in order: certifi's bundle existed; `SSL_CERT_FILE` pointed at the conda bundle, which existed too; Python's cert read came back empty; openssl showed the real story — the certificate was issued by Zscaler Intermediate Root CA, verify return code 20. The corporate proxy re-signs every HTTPS connection. Browsers trust it because the root is in the Windows store; Python uses its own bundle, which had no Zscaler root.

Fix: exported the Zscaler root CA from the Windows store and appended it to the env's `cacert.pem`. Verification stays fully on. No new trust was added — Python now trusts exactly what Windows already trusts. `verify=False` was explicitly rejected, and that rejection is the finding: the lazy fix would have worked and been wrong.

Rule: when the code is right and the call still fails, the trust store is the suspect.

## 2. The drive that didn't switch

`cd D:\agent-sprint` silently did nothing. In cmd, `cd` doesn't switch drives — it changes the directory on the *current* drive and stays put. No error, no warning.

Fix: `D:` then `cd agent-sprint`. Rule: silent no-ops are worse than errors. If a command seems to do nothing, check what it actually did before assuming it worked.

## 3. The terminal that couldn't find Python

Fresh conda env didn't show in VS Code's interpreter picker — fixed by pasting the full interpreter path. Then the integrated terminal couldn't find `python` or `conda` at all: PowerShell didn't have conda on PATH. Fix: `conda init powershell` (one-time, new terminals only).

Rule: a new environment is a new machine. Nothing is on PATH until you put it there.

## 4. The key survived, the package didn't

The gateway key lives in Windows Credential Manager — outside any conda env — so it survived the move to the new env untouched. But the `keyring` package itself needed reinstalling. State and the code that reads it live in different places, and they move independently.

Rule: when migrating environments, audit what lives outside the env, not just what's in it.

## 5. The test that failed for the wrong reason

The W3C dummy PDF link 404'd — so instead of exercising the `non_html` path, the tool correctly reported a dead link. Switched to the IRS W-9 PDF, which returned `non_html` as expected.

The finding isn't the switch, it's what the wrong failure proved: the 404 path worked exactly as designed, on a URL nobody planned. A test that fails for the wrong reason is still information — it just answers a different question than the one you asked.
