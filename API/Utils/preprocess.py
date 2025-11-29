import pandas as pd
import numpy as np
import pickle
import os
SCALER_PATH = "./Models/scaler.pkl"
scaler = None
if os.path.exists(SCALER_PATH):
    with open(SCALER_PATH, "rb") as f:
        scaler = pickle.load(f)

FEATURE_ORDER = ["Time"] + [f"v{i}" for i in range(1,29)] + ["Amount"]

def preprocess_data(input_obj):
    global scaler

    data = pd.DataFrame([input_obj.model_dump()])

    if "Model" in data.columns:
        data = data.drop(columns=["Model"])

    data = data[FEATURE_ORDER]

    if scaler is not None:
        data_scaled = scaler.transform(data)
    else:
        data_scaled = data.values

    return data_scaled
