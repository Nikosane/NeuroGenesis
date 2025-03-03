import logging
import os
from datetime import datetime

LOG_FILE = "neurogenesis.log"

# Ensure logs directory exists
if not os.path.exists("logs"):
    os.makedirs("logs")

logging.basicConfig(
    filename=f"logs/{LOG_FILE}",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def log_info(message):
    logging.info(message)
    print(f"[INFO] {message}")

def log_warning(message):
    logging.warning(message)
    print(f"[WARNING] {message}")

def log_error(message):
    logging.error(message)
    print(f"[ERROR] {message}")

# Example Usage
if __name__ == "__main__":
    log_info("NeuroGenesis logging system initialized.")
