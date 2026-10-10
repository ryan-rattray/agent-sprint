from ask import ask
from react import build_prompt, parse_action
from tools import run_tool


def run(question, max_iterations=8) -> dict:
    # returns {"answer": ..., "trace": [...]}
    # trace entries: {"thought": ..., "action": ..., "observation": ...}

    # Build the initial prompt for the model, including the question.
    prompt = build_prompt(question)

    # trace is a list of dicts, each representing a step in the reasoning process.  This is the log of what the model thought, what action
        #  it took, and what observation it received.
    trace = []

    # Loop for a maximum number of iterations to allow the model to reason and take actions.
    # Each iteration represents a step in the ReAct loop where the model can think, act, and observe.
    # The entire conversation is accumulated in the prompt to provide context for the model's next response.
    for _ in range(max_iterations):
        response = ask(prompt)  # with your 503 retry wrapped around this

        # If the model provides a final answer, return it along with the trace of reasoning steps.
        if "Final Answer:" in response:
            answer = response.split("Final Answer:")[1].strip()
            return {"answer": answer, "trace": trace}
        parsed = parse_action(response)

        # If nothing could be parsed, add an observation indicating the parsing failure and continue the loop.
        # This observation is sent to the model in the next iteration to help it correct its response format.
        if parsed is None:
            observation = ("I couldn't parse an action from your last response. "
                        "Reply using exactly the format: Thought: ... Action: ... Action Input: ...")
            trace.append({"thought": None, "action": None, "observation": observation})

        # If the parsed action is recieved, unpack thought/action/action_input, run the tool with the run_tool function
            # and log all three in the trace. The observation from the tool is then added to the prompt for the next iteration.
        else:
            action, action_input = parsed
            observation = run_tool(action, action_input)
            trace.append({"thought": None, "action": action, "observation": observation})

        # This is the agent's memory of the conversation so far, including the original question, the model's reasoning, the actions
            # it took, and the observations it received. This context is crucial for the model to make informed decisions
            # in subsequent iterations.
        prompt += f"\n{response}\nObservation: {observation}\n"

    # If the loop completes without the model providing a final answer, return a message indicating that the maximum number of iterations
        # was reached, along with the trace of reasoning steps.
    return {"answer": "Max iterations reached.", "trace": trace}

# Test the run function with a sample question. This is useful for debugging and verifying that the ReAct loop behaves as expected.
if __name__ == "__main__":
    result = run("What is 15% of 240, and what is that number squared?")
    print("ANSWER:", result["answer"])
    for step in result["trace"]:
        print(step)

