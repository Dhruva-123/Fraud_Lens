import pandas as pd
import numpy as np

def preprocess_data(inputs):
    data = pd.DataFrame(inputs)
    v_cols = [f"v{i}" for i in range(1,29)]
    data[v_cols] = (data[v_cols] - data[v_cols].mean())/data[v_cols].std()

