# Week 2, Day 2 — Shell and Filesystem (Tuesday, Oct 13)

## The idea

The agent now has hands for the machine it's running on: it can run commands and
read files. This is the most powerful day of the week and the most dangerous —
which is why the sandbox rules come *first*, not after something goes sideways.
A tool that runs shell commands with no guardrails isn't an agent, it's a
liability. The error contract from Day 1 extends here too: every failure is an
observation the loop can reason about.

## What you'll build

`week-02-real-tools/shell_tools.py` with two tools, both registered in the
Week 1 registry with descriptions, parameter schemas, and error contracts:

- **`run_command(command, timeout=30) -> dict`** — runs a command, returns
  `{"ok": true, "stdout": ..., "stderr": ..., "exit_code": ...}` or a structured
  error on timeout/failure. Sandbox rules: fixed working directory (your
  `week-02-real-tools/` sandbox dir), a timeout that kills, and **no `shell=True`**
  — pass the command as a list. Document *why* in the code; it's a real
  security decision, not style.
- **`read_file(path) -> dict`** — reads a text file, returns content or a
  structured error. Sandbox rule: the path must resolve inside a designated safe
  directory — reject anything that escapes it (`..` traversal included). Test the
  rejection on purpose.

## Steps

1. **Write the sandbox rules as constants** at the top of the file — `SAFE_DIR`,
   `MAX_TIMEOUT`, `MAX_OUTPUT_BYTES`. Rules you can read are rules you'll keep.
2. **Build `run_command`.** Start with `subprocess.run(cmd_list, capture_output=True,
   timeout=..., cwd=SAFE_DIR)`. Timeouts and nonzero exits become observations,
   not crashes.
3. **Build `read_file`.** Resolve the path, check it's inside `SAFE_DIR`,
   read up to a size cap. Binary or oversized files return a structured error.
4. **Register all three tools** (web, shell, file) and run each one through the
   loop once — including one deliberate failure per tool, so every error contract
   has a tested failure mode.
5. **Commit.** `week-02 day-02: shell and filesystem tools with sandbox rules`.

## Done criteria (binary)

- [ ] Three real tools (web, shell, file) all run through the registry.
- [ ] Each tool has a documented, tested failure mode — 404, timeout, and path
      escape are all confirmed to return structured observations.

## What this unlocks

- **Wed:** the model stops writing freeform `Action:` lines — schemas take over.
- **Thu:** the research assistant wires all three tools together.

## Likely snag

**Windows path and quoting quirks.** You're on Windows in Anaconda Prompt — list
args to `subprocess.run` dodge the quoting mess that `shell=True` invites. If a
command behaves differently than you expect, print the exact arg list before
debugging the agent.

## When you're done

Reply "Day 2 done". Tomorrow's sheet: structured output — the model's contract.
