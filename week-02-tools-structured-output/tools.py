"""Week 2 tool registry. Same dispatch shape as Week 1: name -> function."""
from web_fetch import fetch_url

TOOLS = {
    "fetch_url": fetch_url,
}

def run_tool(name, arg):
    """Route a parsed action to its tool."""
    fn = TOOLS.get(name.strip().lower())
    if fn is None:
        return f"unknown tool: {name}"
    return fn(arg)
