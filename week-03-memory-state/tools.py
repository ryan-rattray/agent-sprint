"""Week 2 tool registry. Same dispatch shape as Week 1: name -> function."""
from web_fetch import fetch_url
from shell_tools import run_command, read_file

# Registry for the available tools.  
    # fetch_url: goes to a web page
    # run_command: safely runs a command in the SAFE_DIR
    # read_file: reads a file and returns it's context (either full or truncated).
        # Will return an error message if the file is not found, the file has no text, OS rejects, or request is outside of sandbox.
TOOLS = {
    "fetch_url": fetch_url,
    "run_command": run_command,
    "read_file": read_file,
}

def run_tool(name, arg):
    """Route a parsed action to its tool."""
    fn = TOOLS.get(name.strip().lower())
    if fn is None:
        return f"unknown tool: {name}"
    return fn(arg)
