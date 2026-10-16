# This is the only directory the agent is allowed to work from (read or write)
SAFE_DIR = r'D:\agent-sprint\week-02-tools-structured-output\sandbox'

# How many secods an action gets (tool call) before it is killed.
MAX_TIMEOUT = 30

# Limits the data coming back from a tool call - prevents flooding the context window.
MAX_OUTPUT_BYTES = 20000

# Run a shell command in a safe way, returning the output or an error message.
import subprocess

def run_command(command, timeout=MAX_TIMEOUT):

    # 1. This ensures that only a list is is passed.  This is the no-shell rule.
    if not isinstance(command, list) or len(command) == 0:
        return {"ok": False, "error": "bad_command", "detail": "command must be a non empty list, e.g. ['python', '--version']"}

    # 2.  Runs the command in SAFE_DIR.  Killed if MAX_TIMEOUT is exceeded.  Output is captured and returned.
    try:
        result = subprocess.run(command, capture_output=True, text=True, timeout=timeout, cwd=SAFE_DIR)

    except subprocess.TimeoutExpired:
        return {"ok": False, "error": "timeout", "detail": f"command timed out after {timeout} seconds"}
    
    except FileNotFoundError:
        return {"ok": False, "error": "not_found", "detail": f"program not found: {command[0]}"}

    # 3. This truncates the output to prevent flooding the context window.
    stdout = result.stdout
    stderr = result.stderr
    truncated = False
    if len(stdout) > MAX_OUTPUT_BYTES:
        stdout = stdout[:MAX_OUTPUT_BYTES]
        truncated = True
    if len(stderr) > MAX_OUTPUT_BYTES:
        stderr = stderr[:MAX_OUTPUT_BYTES]
        truncated = True

    # 4. Returns a structured output.
    return {"ok": True, "command": command, "stdout": stdout, "stderr": stderr, "exit_code": result.returncode, "truncated": truncated}

# read_file reads a file in the SAFE_DIR.  The return will be the file contents or an error message.

# pathlib is used to ensure that the file path is within SAFE_DIR, preventing directory traversal attacks. (DEEPSEEK WRITTEN)
from pathlib import Path

# Path(SAFE_DIR) turns the raw SAFE_DIR string into a Path object.  Then .resolve() turns it into a canonical absolute path.
    # This allows the script to later answer the question "is this file inside the safe sandbox, the SAFE_DIR directory?"
_SAFE_DIR = Path(SAFE_DIR).resolve()

def read_file(rel_path):
    # Resolve the requested path against the sandbox...
    target = (_SAFE_DIR / rel_path).resolve()
    # ...and reject anything that escapes it.
    if not target.is_relative_to(_SAFE_DIR):
        return {"ok": False, "error": "path_escape", "requested": rel_path, "resolved": str(target)}

    # Attempt to read the file, and return the one of the following error messages if it fails.
    try:
        # Read the whole file. This can fail 3 ways:
            # 1. FileNotFoundError: The file does not exist.
            # 2. UnicodeDecodeError:The bytes are not text, like a binary file.
            # 3. OSError: The OS refuses, due to permissions failure or it's a directory, not a file.
        text = target.read_text(encoding="utf-8")

    # 1. FileNotFoundError:
    except FileNotFoundError:
        return {"ok": False, "error": "not_found", "requested": rel_path}

    # 2. UnicodeDecodeError and
    # 3. OSError
    except (UnicodeDecodeError, OSError):
        return {"ok": False, "error": "decode_error", "requested": rel_path}

    # Truncate giant files so that a huge file can't flood the context window.
    # Start with a truncated flag as False.
    truncated = False

    # If the file is too big, set it to True and truncate the text to the length specified in MAX_OUTPUT_BYTES.
    if len(text) > MAX_OUTPUT_BYTES:
        text = text[:MAX_OUTPUT_BYTES]
        truncated = True

    # Return response for the happy path
    return {"ok": True, "path": str(target), "text": text, "truncated": truncated}


    

    