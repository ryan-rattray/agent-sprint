from agent import run

# List of multi-step reasoning questions to test the agent's capabilities
questions = [
    "What is the average items on a desk multiplied by the beeps in a microwave cycle?",  # 7.3 * 4 = 29.2
    "What is the standard paperclip length in mm divided by the teeth on a standard zipper per inch?",  # 50 / 12 ≈ 4.167
    "What is the average blinks per minute times the hours to charge a forklift battery?",  # 17 * 8.5 = 144.5
]

# Loop through the questions, run the agent, and print the results
for i, q in enumerate(questions, 1):
    result = run(q)
    print(f"=== Q{i}: {q}")
    print("ANSWER:", result["answer"])
    for step in result["trace"]:
        print(f"  Thought: {step['thought']}")
        print(f"  Action: {step['action']}")
        print(f"  Observation: {step['observation']}")
        print()

