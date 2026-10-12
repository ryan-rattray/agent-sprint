from ask_gateway import ask_gateway
from react import build_prompt, parse_action
from tools import run_tool
import re


def run(question, max_iterations=8) -> dict:
    # returns {"answer": ..., "trace": [...]}
    # trace entries: {"thought": ..., "action": ..., "observation": ...}

    # Build the initial prompt for the model, including the question.
    prompt = build_prompt(question)

    # trace is a list of dicts, each representing a step in the reasoning process.
    trace = []

    # tools_used is a counter to keep track of how many times the model has used external tools.
    tools_used = 0

    # Loop for a maximum number of iterations to allow the model to reason and take actions.
    for _ in range(max_iterations):
        response = ask_gateway(prompt)

        thought_match = re.search(r"Thought:\s*(.+)", response)
        thought = thought_match.group(1).strip() if thought_match else None

        # If the model provides a final answer, return it along with the trace.
        if "Final Answer:" in response:
            if tools_used == 0:
                observation = ("You must call at least one tool before giving your "
                            "Final Answer. Remember: "
                            "Use the calculator for all arithmetic. "
                            "Use the search tool to look up facts. "
                            "What is your first action?")
                trace.append({"thought": thought, "action": None, "observation": observation})
                # Reset the prompt to the original question plus the correction.
                # This prevents the model from getting confused by seeing its own
                # premature Final Answer in the conversation history.
                prompt = build_prompt(question)
                prompt += f"\n{observation}\n"
                continue

            answer = response.split("Final Answer:")[1].strip()
            return {"answer": answer, "trace": trace}

        parsed = parse_action(response)

        # If nothing could be parsed, add an observation indicating the parsing failure.
        if parsed is None:
            observation = ("I couldn't parse an action from your last response. "
                        "Reply using exactly the format: Thought: ... Action: ... Action Input: ...")
            trace.append({"thought": thought, "action": None, "observation": observation})

        # If the parsed action is received, run the tool and log the result.
        else:
            action, action_input = parsed
            observation = run_tool(action, action_input)
            tools_used += 1
            trace.append({"thought": thought, "action": action, "observation": observation})

        # Append the model's response and the observation to the prompt for context.
        prompt += f"\n{response}\nObservation: {observation}\n"

    # If the loop completes without a final answer, return a message indicating that.
    return {"answer": "Max iterations reached.", "trace": trace}

# Test the run function with a sample question. This is useful for debugging and verifying that the ReAct loop behaves as expected.
if __name__ == "__main__":
    result = run("What is 15% of 240, and what is that number squared?")
    print("ANSWER:", result["answer"])
    for step in result["trace"]:
        print(step)

# temp test, bottom of agent.py (delete after or comment out)
# from unittest.mock import patch

# calls = 0
# real_ask = ask_gateway
# def flaky_ask(prompt):
#     global calls
#     calls += 1
#     if calls == 1:
#         return "I think the answer is probably 42 or something"
#     return real_ask(prompt)

# with patch("agent.ask_gateway", flaky_ask):
#     result = run("What is 15% of 240?")
# print("ANSWER:", result["answer"])
# for step in result["trace"]:
#     print(step["observation"])

# if __name__ == "__main__":
#     result = run("What did I have for breakfast?", max_iterations=3)
#     print("ANSWER:", result["answer"])
#     print("iterations used:", len(result["trace"]))

# temp cap test (comment out after)
# from unittest.mock import patch

# def stub_ask(prompt):
#     return "Thought: still looking\nAction: search\nAction Input: breakfast diary"

# with patch("agent.ask_gateway", stub_ask):
#     result = run("What did I have for breakfast?", max_iterations=3)
# print("ANSWER:", result["answer"])
# print("iterations used:", len(result["trace"]))



