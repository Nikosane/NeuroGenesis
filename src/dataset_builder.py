import json
import torch
import numpy as np
from config import DECISIONS_DB_PATH, THOUGHT_TRACES_PATH

class DatasetBuilder:
    def __init__(self):
        self.decisions = self.load_data(DECISIONS_DB_PATH)
        self.thought_traces = self.load_data(THOUGHT_TRACES_PATH)

    def load_data(self, path):
        try:
            with open(path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def encode_text(self, text):
        """
        Encodes text into numerical representation (basic word embedding).
        """
        return np.array([ord(c) for c in text[:100]])  # Limit to 100 chars

    def build_dataset(self):
        X, y = [], []
        for situation, decision in self.decisions.items():
            if situation in self.thought_traces:
                situation_vector = self.encode_text(situation)
                thought_vector = self.encode_text(" ".join(self.thought_traces[situation]))
                decision_vector = self.encode_text(decision)

                input_vector = np.concatenate((situation_vector, thought_vector))
                X.append(input_vector)
                y.append(decision_vector)

        X, y = np.array(X, dtype=np.float32), np.array(y, dtype=np.float32)
        return torch.tensor(X), torch.tensor(y)

# Example Usage
if __name__ == "__main__":
    builder = DatasetBuilder()
    X, y = builder.build_dataset()
    print("Dataset Size:", X.shape, y.shape)
