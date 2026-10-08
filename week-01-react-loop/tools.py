"""Day 3: real tools for the ReAct agent."""
import ast
import operator

_ALLOWED = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}

def _eval(node):
    if isinstance(node, ast.Expression):
        return _eval(node.body)
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    if isinstance(node, ast.BinOp) and type(node.op) in _ALLOWED:
        return _ALLOWED[type(node.op)](_eval(node.left), _eval(node.right))
    if isinstance(node, ast.UnaryOp) and type(node.op) in _ALLOWED:
        return _ALLOWED[type(node.op)](_eval(node.operand))
    raise ValueError("unsafe expression")

def calculator(expr):
    """Safely evaluate a math expression. Returns the result or an error string."""
    try:
        return str(_eval(ast.parse(expr, mode="eval")))
    except Exception as e:
        return f"error: {e}"

_SEARCH_DB = {
"capital of france": "Paris",
"largest planet": "Jupiter",
"python creator": "Guido van Rossum",
}

def search(query):
    """Stub search: look up a canned answer. Returns 'no results' when unknown."""
    return _SEARCH_DB.get(query.strip().lower(), "no results")

TOOLS = {
    "calculator": calculator,
    "search": search,
}

def run_tool(name, arg):
    """Route a parsed action to its tool."""
    fn = TOOLS.get(name.strip().lower())
    if fn is None:
        return f"unknown tool: {name}"
    return fn(arg)


if __name__ == "__main__":
    print(calculator("12*34 + 8"))
    print(calculator("(100 - 4) / 16"))
    print(calculator("__import__('os').system('echo pwned')"))
    print(search("capital of France"))
    print(search("something nobody asked"))
    print(run_tool("calculator", "7*6"))
    print(run_tool("search", "largest planet"))
    print(run_tool("teleport", "mars"))


