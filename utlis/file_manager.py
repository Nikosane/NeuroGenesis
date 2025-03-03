import json
import torch
import os

class FileManager:
    @staticmethod
    def load_json(file_path):
        """Loads JSON data from a file."""
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                return json.load(file)
        return {}

    @staticmethod
    def save_json(file_path, data):
        """Saves JSON data to a file."""
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def save_model(model, file_path):
        """Saves a trained PyTorch model."""
        torch.save(model.state_dict(), file_path)

    @staticmethod
    def load_model(model, file_path):
        """Loads a trained PyTorch model."""
        if os.path.exists(file_path):
            model.load_state_dict(torch.load(file_path))
            model.eval()
        return model

# Example Usage
if __name__ == "__main__":
    data = {"test": "This is a test entry"}
    FileManager.save_json("storage/test.json", data)
    loaded_data = FileManager.load_json("storage/test.json")
    print("Loaded Data:", loaded_data)
