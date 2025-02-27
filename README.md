# NeuroGenesis

## Overview
NeuroGenesis is an **Artificial Neural Network-based memory chamber** designed to learn patterns from AI-driven decisions in the **SaneGenesis** simulation. It uses **Chain of Thought (CoT) reasoning** to analyze, store, and optimize decision-making processes, enabling AI agents to improve their strategies over time.

## Features
- **Neural Network Memory**: Stores and learns from AI decisions in complex scenarios.
- **Chain of Thought Reasoning**: Generates step-by-step thought processes before making decisions.
- **Decision Optimization**: Identifies patterns in past actions to find the most efficient solutions.
- **Seamless Integration**: Can be used independently or connected with SaneGenesis.

## Installation
```bash
git clone https://github.com/Nikosane/NeuroGenesis.git
cd NeuroGenesis
pip install -r requirements.txt
```

## Usage
### Training the Neural Network
```bash
python train.py
```

### Running Inference
```bash
python inference.py
```

### Example Decision Processing
```python
from src.memory_manager import MemoryManager

memory = MemoryManager()
decision = memory.process_decision({
    "situation": "A faction is low on food but has surplus iron.",
    "thought_process": [
        "Food is a necessity; trade is an option.",
        "Identify factions with food surplus.",
        "Iron is valuable for trade.",
        "Negotiate iron-for-food deal."
    ],
    "decision": "Trade iron for food with a nearby faction."
})
```

## Integration with SaneGenesis
NeuroGenesis can be integrated with SaneGenesis by linking decision storage files or using an API to exchange data.

## Future Enhancements
- Improve CoT reasoning using **Transformer-based architectures**.
- Optimize inference time for real-time decision-making.
- Implement reinforcement learning for adaptive decision refinement.

## License
MIT License

## Contact
For queries, reach out to [niteshkotian3@gmail.com].

