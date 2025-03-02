import json
from config import CoT_CONFIG, THOUGHT_TRACES_PATH

class ChainOfThought:
    def __init__(self):
        self.thought_traces = self.load_data(THOUGHT_TRACES_PATH)

    def load_data(self, path):
        try:
            with open(path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_data(self, path, data):
        with open(path, "w") as file:
            json.dump(data, file, indent=4)

    def generate_reasoning(self, situation):
        """
        Generates a step-by-step reasoning chain based on the situation.
        """
        steps = []
        max_steps = CoT_CONFIG["max_steps"]

        # Step-by-step breakdown of thought process
        steps.append(f"Analyze the situation: {situation}")
        steps.append("Identify key factors and constraints.")
        steps.append("Evaluate possible actions and their consequences.")
        steps.append("Compare past similar situations and their outcomes.")
        steps.append("Choose the most effective decision.")

        # Limit to max_steps defined in config
        steps = steps[:max_steps]

        # Store reasoning trace
        self.thought_traces[situation] = steps
        self.save_data(THOUGHT_TRACES_PATH, self.thought_traces)

        return steps

# Example Usage
if __name__ == "__main__":
    cot = ChainOfThought()
    reasoning_chain = cot.generate_reasoning("A faction is under attack but has limited defenses.")
    print("Generated Thought Process:")
    for step in reasoning_chain:
        print("-", step)
