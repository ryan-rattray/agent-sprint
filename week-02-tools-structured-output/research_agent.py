"""Day 4 - the research assistant: Week 1's loop, Week 2's contract."""

# allows for reading and writing to json files
import json


from ask_gateway import ask_gateway # Function that calls the selected model via the Gateway
from structured import validate_tool_call, error_observation
from tools import TOOLS             # Registry of tool: name -> function

MAX_ITERATIONS = 10 # Caps the loops to 10 iterations so a runaway model can't run on forever

TRACE = True # Set to False to run quietly. True prints the full trace every turn.

def show(label, text):
    """Print one labeled trace section, but only when TRACE is on."""
    if not TRACE:
        return
    print(label)
    print(text)
    print()

# The prompt is the contract, now shorter than week 1 as JSON needs less explaining.
# Also, the example is removed because JSON IS the example.
PROMPT = """You are a research agent. You answer questions by using tools, then cite your sources.
Reply with ONLY a JSON object, no other text. To use a tool:
{"tool": "<tool name>", "arguments": { ... }}
Available tools: run_command (arguments: command, a list), read_file (arguments: rel_path),
fetch_url (arguments: url, timeout).
Do not wrap your reply in markdown or code fences. Send the raw JSON object only.
Reply with exactly one JSON object and nothing else. Never write an Observation line. Observations come only from the tools, after your reply ends.
This computer runs Windows. There is no ls program. To list files, use run_command with ["cmd", "/c", "dir"].
When you have enough to answer, reply with ONLY:
{"answer": "<your answer>", "citations": ["<file or URL>", ...]}

Question: {question}
"""


def observation_from(result):
    """Wrap a tool's return dictionary as the Observation text. 
    Takes the tool's return and decide ok or error.
    """
    if result["ok"]:
        return f"Observation: {result.get('text') or result.get('stdout') or ''}"
    return f"Observation: tool error ({result['error']}): {result.get('detail', '')}"


def run(question, model=ask_gateway):
    """Runs through the whole loop.  
    - Ask the question.
    - Validate the response.
    - Dispatch a tool.
    - Append the observation.
    - Repeat until final answer.
    - Final answer dictionary:  {"answer": str, "citations": [str, ...]}."""

    prompt = PROMPT.replace("{question}", question)

    for turn in range(1, MAX_ITERATIONS +1):
        # Prints the prompt the model sees at the begining of each turn if Trace = True
        show(f"=== Turn {turn} ===\nPrompt:", prompt)

        reply = model(prompt)

        # Prints the models reply every turn if Trace = True
        show("Model reply:", reply)

        # If model attempts a final answer, this checks it against the answer key.
        # The shape of the answer is validated before accepting it.
        try:
            parsed = json.loads(reply)
        except json.JSONDecodeError:
            parsed = None
        if isinstance(parsed, dict) and "answer" in parsed:
            if isinstance(parsed["answer"], str) and isinstance(parsed.get("citations"), list):
                return parsed
            obs = ("Observation: invalid final answer: it must be a JSON object "
                    "with an 'answer' string and a 'citations' list.")
            # Otherwise it must be a tool call. VALIDATE BEFORE ANYTHING RUNS.
        else:
            verdict = validate_tool_call(reply)
            if not verdict["ok"]:
                # Rejected: the error becomes the Observation, the turn
                # repeats, and no tool ever saw the bad request.
                obs = error_observation(verdict)
            else:
                # Dispatch: the validated name picks the function, the
                # validated arguments unpack into its parameters.
                fn = TOOLS[verdict["tool"]]
                obs = observation_from(fn(**verdict["arguments"]))

        # Prints the observation if Trace = True
        show("Observation:", obs)

        # Append reply + Observation: the growing prompt is still the
        # agent's only memory, exactly as in Week 1.
        prompt += "\n" + reply + "\n" + obs + "\n"

    return {"answer": "max iterations reached", "citations": []}


if __name__ == "__main__":
    result = run("List the files in my sandbox. Then read notes.txt and tell me what it says I do for a living and what I am learning. Then fetch the Python 3.13.0 release page on python.org and tell me what date Python 3.13.0 was released.")
    print("ANSWER:", result["answer"])
    print("CITATIONS:", result["citations"])
