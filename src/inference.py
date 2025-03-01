import torch
from src.memory_network import load_model
from src.dataset_builder import DatasetBuilder
from config import MODEL_WEIGHTS_PATH

def run_inference(situation):
    builder = DatasetBuilder()
    model = load_model(input_size=200, output_size=100)  # Adjusted based on dataset size
    
    situation_vector = builder.encode_text(situation)
    input_vector = torch.tensor(situation_vector, dtype=torch.float32).unsqueeze(0)

    with torch.no_grad():
        output_vector = model(input_vector)

    decision = "".join([chr(int(i)) for i in output_vector[0].numpy()])
    return decision.strip()

# Example Usage
if __name__ == "__main__":
    situation = "A faction is struggling with resource allocation."
    decision = run_inference(situation)
    print("Suggested Decision:", decision)
