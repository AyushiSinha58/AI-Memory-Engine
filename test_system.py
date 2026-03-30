from pathlib import Path

from ml.training import train
from ml.testing import run_tests
from db.memory_manager import init_db
from db.retrieval import test_retrieval
from app.chatbot import run_chatbot


DATA_PATH = Path("data/memory_dataset.csv")
MODEL_PATH = Path("ml/importance_model.pkl")


def check_dataset():
    print("\nChecking dataset...")

    if not DATA_PATH.exists():
        raise FileNotFoundError("Dataset not found!")

    print("Dataset found")


def main(run_tests_flag=True):
    print("AI MEMORY SYSTEM STARTING...\n")

    # 1. Dataset check
    check_dataset()

    # 2. Train model
    print("\nTraining model...")
    train()

    # 3. Optional testing
    if run_tests_flag:
        run_tests()

    # 4. DB check
    init_db()

    # 5. Retrieval test
    test_retrieval()

    # 6. Start chatbot
    run_chatbot()


if __name__ == "__main__":
    main()