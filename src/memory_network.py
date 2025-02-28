import torch
import torch.nn as nn
import torch.optim as optim
import json
from config import MODEL_WEIGHTS_PATH, HYPERPARAMS

class MemoryNetwork(nn.Module):
    def __init__(self, input_size, output_size):
        super(MemoryNetwork, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(input_size, HYPERPARAMS["hidden_layers"][0]),
            nn.ReLU(),
            nn.Dropout(HYPERPARAMS["dropout"]),
            nn.Linear(HYPERPARAMS["hidden_layers"][0], HYPERPARAMS["hidden_layers"][1]),
            nn.ReLU(),
            nn.Linear(HYPERPARAMS["hidden_layers"][1], output_size)
        )

    def forward(self, x):
        return self.model(x)

def load_model(input_size, output_size):
    model = MemoryNetwork(input_size, output_size)
    if torch.cuda.is_available():
        model = model.cuda()
    
    try:
        model.load_state_dict(torch.load(MODEL_WEIGHTS_PATH))
        print("Model loaded successfully.")
    except FileNotFoundError:
        print("No pre-trained model found. Training required.")

    return model
