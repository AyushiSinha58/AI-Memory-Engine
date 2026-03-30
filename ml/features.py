import pandas as pd

# Centralized constants
KEYWORDS = ["like", "love", "hate", "prefer", "my name", "i am"]
FIRST_PERSON = ["i", "my", "me"]

TYPE_MAP = {
    "preference": 2,
    "personal": 2,
    "context": 1,
    "question": 0,
    "casual": 0
}


def extract_features(row):
    message = str(row["message"]).lower()

    features = {
        "length": len(message),
        "has_keyword": int(any(k in message for k in KEYWORDS)),
        "has_first_person": int(any(k in message for k in FIRST_PERSON)),
        "type_score": TYPE_MAP.get(row.get("type", ""), 0)
    }

    return pd.Series(features)


def transform_dataframe(df):
    """Apply feature extraction to entire dataframe"""
    return df.apply(extract_features, axis=1)