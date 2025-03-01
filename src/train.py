import torch
import torch.nn as nn
import torch.optim as optim
from src.memory_network import MemoryNetwork
from src.dataset_builder import DatasetBuilder
from config import MODEL_WEIGHTS_PATH, HYPERPARAMS

def train_model():
    builder = DatasetBuilder()
    X, y = builder.build_dataset()
    
    input_size = X.shape[1]
    output_size = y.shape[1]

    model = MemoryNetwork(input_size, output_size)
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=HYPERPARAMS["learning_rate"])

    for epoch in range(HYPERPARAMS["epochs"]):
        optimizer.zero_grad()
        outputs = model(X)
        loss = criterion(outputs, y)
        loss.backward()
        optimizer.step()

        if epoch % 10 == 0:
            print(f"Epoch [{epoch}/{HYPERPARAMS['epochs']}], Loss: {loss.item():.4f}")

    torch.save(model.state_dict(), MODEL_WEIGHTS_PATH)
    print("Training complete. Model saved.")

if __name__ == "__main__":
    train_model()
