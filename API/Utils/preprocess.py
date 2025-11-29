import pandas as pd
import numpy as np
import pickle
import os

# Load scaler once and cache it
SCALER_PATH = "./Models/scaler.pkl"
scaler = None
if os.path.exists(SCALER_PATH):
    with open(SCALER_PATH, "rb") as f:
        scaler = pickle.load(f)

FEATURE_ORDER = ["Time"] + [f"v{i}" for i in range(1,29)] + ["Amount"]

def preprocess_data(input_obj):
    global scaler

    # Convert input to DataFrame
    data = pd.DataFrame([input_obj.model_dump()])

    # Drop model column
    if "Model" in data.columns:
        data = data.drop(columns=["Model"])

    # Reorder columns exactly like training
    data = data[FEATURE_ORDER]

    # Apply saved scaler if available
    if scaler is not None:
        data_scaled = scaler.transform(data)
    else:
        # fallback: just return raw values
        data_scaled = data.values

    return data_scaled
