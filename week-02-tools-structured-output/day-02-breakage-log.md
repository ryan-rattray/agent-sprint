# Day 2 breakage log — draft capture (2026-10-15)

Raw findings from tonight's run_command build session, captured for your red-pen before they go into the log. Everything below happened in the actual session.

## 1. The raw-string path bug

First version: `SAFE_DIR = 'D:\agent-sprint\week-02-tools-structured-output\sandbox'`.

Python reads `\a` inside a plain string as the bell escape character, so the path corrupts the moment the file loads. No error at import time, no traceback. It fails weirdly three steps later when a file operation lands somewhere wrong.

Fix: raw string, `r'D:\...'`. Rule: Windows paths in Python are raw strings, always. Silent corruption is worse than a crash.

## 2. The two typo bugs on the unhappy paths

Both typos were in code that only runs when something goes wrong:

- `"error:"` with a colon inside the key string, in the guard clause. The error contract expects `result["error"]`; the colon variant would KeyError on the one path meant to prevent crashes.
- `MAX_OUTPUTBYTES` (missing underscores) in the stdout truncation line. NameError the first time output actually exceeds the cap.

The happy-path test (`["python", "--version"]`) passed clean and would never have found either one. Unhappy paths are where bugs hide, because that is the code nobody runs until it matters. Testing each failure mode on purpose is the fix.

## 3. PowerShell is not Python

Typed `from shell_tools import run_command` at the PowerShell prompt and got a ParserError. The fix is reading the prompt before typing: `PS>` means PowerShell is listening, `>>>` means Python is. Type `python` first, then the import. `exit()` gets back.

## 4. `dir` is not a real program

On Windows, `dir` is a cmd.exe builtin, not an executable. `["dir", "/w"]` raises FileNotFoundError and looks exactly like a broken tool. Test with real programs: `["python", "--version"]`, `["where", "python"]`. Anything a list-arg subprocess can't find is either a builtin or a typo, and the tool is not the suspect.

## 5. The method switch, and the evidence for it

Tonight was the first session typed out instead of copy/pasted, in bite-size chunks instead of hundreds of lines at once. The two typo bugs above are exactly what copy/paste hides: you would have pasted them in working and never seen them until an unhappy path fired in production. Typing caught them at the keyboard. Smaller stairs, actually climbed, beat big ones skipped.
