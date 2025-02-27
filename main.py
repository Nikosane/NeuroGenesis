import argparse
from src.train import train_model
from src.inference import run_inference


def main():
    parser = argparse.ArgumentParser(description="NeuroGenesis: AI Memory Chamber with CoT Reasoning")
    parser.add_argument("--train", action="store_true", help="Train the Neural Network")
    parser.add_argument("--infer", type=str, help="Run inference on a given situation")
    
    args = parser.parse_args()
    
    if args.train:
        print("Starting training process...")
        train_model()
    elif args.infer:
        print("Running inference...")
        result = run_inference(args.infer)
        print("Decision Output:", result)
    else:
        print("Please specify either --train to train the model or --infer '<situation>' to run inference.")


if __name__ == "__main__":
    main()
