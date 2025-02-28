import json
from config import DECISIONS_DB_PATH, THOUGHT_TRACES_PATH

class MemoryManager:
    def __init__(self):
        self.decisions = self.load_data(DECISIONS_DB_PATH)
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

    def process_decision(self, decision_entry):
        """
        Stores a new decision and its reasoning trace.
        """
        situation = decision_entry["situation"]
        thought_process = decision_entry["thought_process"]
        decision = decision_entry["decision"]

        self.decisions[situation] = decision
        self.thought_traces[situation] = thought_process

        self.save_data(DECISIONS_DB_PATH, self.decisions)
        self.save_data(THOUGHT_TRACES_PATH, self.thought_traces)

        return decision

# Example Usage
if __name__ == "__main__":
    memory = MemoryManager()
    decision = memory.process_decision({
        "situation": "A faction is under attack and low on resources.",
        "thought_process": [
            "Assess the enemy strength.",
            "Check for available allies.",
            "Weigh the option of retreating vs. defending.",
            "Decide based on survival chances."
        ],
        "decision": "Send a distress signal and request reinforcements."
    })
    print("Stored Decision:", decision)
