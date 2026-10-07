"""Day 2 - teach the model the ReAct shape.

The model doesn't know it's an agent. All it sees is text, so we give it
a contract: respond in a strict Thought / Action / Action Input format,
and our code treats that format as a command. No tools run today.
"""

REACT_PROMPT = """You solve problems by reasoning step by step, then taking actions.

Reply using exactly this format, nothing else:

Thought: <your reasoning about what to do next>
Action: <the tool to use: calculator or search>
Action Input: <the input to pass to the tool>

When you have the final answer, reply using exactly this format, nothing else:

Thought: <your reasoning>
Final Answer: <the answer>

Example:

Question: What is 12*34?

Thought: I need to compute 12*34 first.
Action: calculator
Action Input: 12*34
Observation: 408

Thought: I have the result of the computation.
Final Answer: 408

Question: {question}
"""
import re

def build_prompt(question: str) -> str:
    """Slot a question into the ReAct prompt template."""
    return REACT_PROMPT.format(question=question)

def parse_action(reply: str) -> tuple[str, str] | None:
    """Extract (action_name, action_input) from a model reply.

    Returns None when the reply contains no Action line.
    """
    action_match = re.search(r"Action:\s*(\w+)", reply)
    input_match = re.search(r"Action Input:\s*(.+)", reply)
    if not action_match or not input_match:
        return None
    return action_match.group(1), input_match.group(1).strip()
