# Day 3 — Give It Hands (Oct 8, 2026)

## What was built

`tools.py`: three pieces. A `calculator(expr)` that safely evaluates math via
`ast` (never `eval`), a `search(query)` stub that answers from a canned dict,
and a `TOOLS` registry mapping action-name strings to functions — plus
`run_tool(name, arg)`, the dispatcher that routes a parsed action to its
function. Unknown tool names return `"unknown tool: X"` as a string, never a
crash.

The core insight: the model only emits *text* — the string `"calculator"`.
The registry is what turns that string into a running function. And because
every tool returns a string (results *and* errors), the loop can always feed
the outcome back to the model as an Observation. That's the contract that
makes tomorrow's loop possible.

**Done criteria (all met):** calculator evaluates math and rejects hostile
input · stub search answers known queries, `"no results"` otherwise ·
registry routes parsed actions to functions · unknown tool names return an
observation string · integration test: `parse_action` output feeds
`run_tool` end to end.

## Line-by-line walkthrough

```python
"""Day 3: real tools for the ReAct agent."""
import ast
import operator
```

`ast` lets us parse an expression into a syntax tree without executing it.
`operator` gives us the actual math functions to call on the safe nodes.

```python
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
```

The allowlist. Every node type the tree-walker will accept, paired with the
real function to run. Anything not in this dict — function calls, names,
attribute access — is rejected. This is the entire security model: default
deny, explicit allow.

```python
def _eval(node):
    if isinstance(node, ast.Expression):
        return _eval(node.body)
```

`ast.parse(expr, mode="eval")` returns an `Expression` wrapper; unwrap it and
recurse into the real tree.

```python
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
```

Leaf case: a plain number. Note the type check — a string constant like
`"pwned"` is a `Constant` too, but it's not int/float, so it falls through to
the `ValueError` at the bottom. No strings pass.

```python
    if isinstance(node, ast.BinOp) and type(node.op) in _ALLOWED:
        return _ALLOWED[type(node.op)](_eval(node.left), _eval(node.right))
    if isinstance(node, ast.UnaryOp) and type(node.op) in _ALLOWED:
        return _ALLOWED[type(node.op)](_eval(node.operand))
    raise ValueError("unsafe expression")
```

Binary ops (`2 + 3`) and unary ops (`-4`): check the operator is allowlisted,
recursively evaluate both sides, apply the real function. Anything else —
`Call`, `Name`, `Attribute`, a disallowed operator — hits the `raise`. The
model can emit whatever it wants; only math survives.

```python
def calculator(expr):
    """Safely evaluate a math expression. Returns the result or an error string."""
    try:
        return str(_eval(ast.parse(expr, mode="eval")))
    except Exception as e:
        return f"error: {e}"
```

The public face. Parse, evaluate, stringify — or catch *everything* and
return it as a string. The `try/except` is deliberate: a tool must never
raise into the loop. Malformed input becomes the observation
`"error: unsafe expression"`, which the model reads and recovers from.
Proved live: `__import__('os').system('echo pwned')` → rejected, not run.

```python
_SEARCH_DB = {
    "capital of france": "Paris",
    "largest planet": "Jupiter",
    "python creator": "Guido van Rossum",
}

def search(query):
    """Stub search: look up a canned answer. Returns 'no results' when unknown."""
    return _SEARCH_DB.get(query.strip().lower(), "no results")
```

A dict standing in for a real search API (Week 2 replaces it). Keys are
lowercased, and the lookup normalizes the query the same way — so
`"capital of France"` matches. Unknown queries return `"no results"`, not
an exception: same contract as the calculator, tools always return strings.

```python
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
```

The registry: action-name strings → functions. `run_tool` is the single
choke point Day 2's `parse_action` feeds into — it takes the `(name, input)`
tuple apart and calls the right function with the `Action Input:` text as
its argument. Unknown name? `"unknown tool: teleport"` goes back to the
model as an observation, and the model can try again. No crash, no special
cases in the loop.

## Verification

```
python tools.py
416
6.0
error: unsafe expression
Paris
no results
42
Jupiter
unknown tool: teleport
```

Plus the integration one-liner proving the Day 2 → Day 3 handoff:

```
python -c "from react import parse_action; from tools import run_tool; p = parse_action('Thought: x\nAction: calculator\nAction Input: 7*6'); print(p); print(run_tool(*p))"
('calculator', '7*6')
42
```

Model text in, executed tool out. Tomorrow: the loop that ties it together.
