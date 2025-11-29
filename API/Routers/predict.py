from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import pickle
import os
from typing import Literal
from Schemas.input import Input
from Utils.preprocess import preprocess_data

predict_router = APIRouter()


models_cache = {}

MODEL_DIR = "./Models"

ALLOWED_MODELS = [
    "LogisticRegression", 
    "NaiveBayes", 
    "SVC", 
    "XGBoostTree"
]

class PredictionResponse(BaseModel):
    """Schema for the prediction result returned to the user."""
    model_used: str
    prediction_label: Literal["Not Fraud (0)", "Fraud (1)"]
    prediction_class: Literal[0, 1]
    probability_fraud: float

def load_model(model_name: str):
    if model_name not in ALLOWED_MODELS:
        raise FileNotFoundError(
            f"Model '{model_name}' is not an allowed model. Choose from: {', '.join(ALLOWED_MODELS)}"
        )
        
    # Return from cache if already loaded
    if model_name in models_cache:
        return models_cache[model_name]
        
    model_path = os.path.join(MODEL_DIR, f"{model_name}.pkl")
    
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found at: {model_path}. Please place it in the {MODEL_DIR} folder.")

    try:
        with open(model_path, 'rb') as file:
            model = pickle.load(file)

        models_cache[model_name] = model
        return model
    except Exception as e:
        print(f"Error loading model {model_name}: {e}")
        raise RuntimeError(f"Error loading model {model_name}. Check the .pkl file integrity.")

@predict_router.post("/predict/{model_name}", response_model=PredictionResponse, status_code=200)
def get_prediction(model_name: str, request_data: Input):
    try:
        model = load_model(model_name)
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    try:
        processed_features = preprocess_data(request_data)
    except Exception as e:
         raise HTTPException(status_code=400, detail=f"Preprocessing failed: {e}")
    
    try:
        prediction_class = int(model.predict(processed_features)[0])
        if hasattr(model, 'predict_proba'):
            probability_fraud = model.predict_proba(processed_features)[0][1]
        else:
            probability_fraud = -1.0 
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed for model '{model_name}': {e}")

    prediction_label = "Fraud (1)" if prediction_class == 1 else "Not Fraud (0)"
    
    return PredictionResponse(
        model_used=model_name,
        prediction_label=prediction_label,
        prediction_class=prediction_class,
        probability_fraud=round(float(probability_fraud), 4)
    )