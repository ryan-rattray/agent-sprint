from agent import run

# List of multi-step reasoning questions to test the agent's capabilities
questions = [
    "What is the boiling point of water in Celsius divided by the speed of sound in meters per second?",  # 100/343 ≈ 0.292
    "What is the number of letters in the capital of france times the number of letters in the name of the largest planet in our solar system?",  # 5 * 7 = 35
    "What is the speed of light in meters per second divided by the speed of sound in feet per second +100?",  # 299792458/1125 + 100 ≈ 266582.63
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

