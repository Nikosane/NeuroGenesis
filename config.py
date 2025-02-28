# config.py

# Paths
MODEL_WEIGHTS_PATH = "storage/model_weights.pth"
DECISIONS_DB_PATH = "storage/decisions.json"
THOUGHT_TRACES_PATH = "storage/thought_traces.json"

# Neural Network Hyperparameters
HYPERPARAMS = {
    "learning_rate": 0.001,
    "batch_size": 32,
    "epochs": 50,
    "hidden_layers": [128, 256, 128],
    "dropout": 0.3
}

# Chain of Thought Parameters
CoT_CONFIG = {
    "max_steps": 5,  # Max steps in reasoning process
    "temperature": 0.7  # Controls randomness in decision-making
}
