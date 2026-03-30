from pathlib import Path
import pandas as pd
import joblib

from ml.features import transform_dataframe

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "ml" / "importance_model.pkl"


def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            "Model not found. Run training.py first."
        )
    return joblib.load(MODEL_PATH)

model = None

def get_model():
    global model
    if model is None:
        model = load_model()
    return model

def predict_message(message, msg_type):
    model = get_model()

    df = pd.DataFrame([{
        "message": message,
        "type": msg_type
    }])

    features = transform_dataframe(df)

    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]

    return int(prediction), float(probability)

def run_tests():
    print("\nTesting model...\n")
    print(predict_message("I like Python", "preference"))
    print(predict_message("ok", "casual"))