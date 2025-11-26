from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import pickle
import os
from typing import Literal

# Local imports
from Schemas.input import Input
from Utils.preprocess import preprocess_data

router = APIRouter()

# Dictionary to hold the loaded models in memory (caching)
models_cache = {}
# Directory where the .pkl models are stored
MODEL_DIR = "./Models"

# List of model filenames (without .pkl extension) you expect to find
# These models must be classification models trained on the fraud dataset
ALLOWED_MODELS = [
    "LogisitcRegression", 
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
    """
    Loads a .pkl model file from the Models directory, using the cache.
    This function is called by the startup event in main.py and by the endpoint itself.
    """
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
            # Load the pickled model object
            model = pickle.load(file)
        
        # Store in cache for future requests
        models_cache[model_name] = model
        return model
    except Exception as e:
        print(f"Error loading model {model_name}: {e}")
        raise RuntimeError(f"Error loading model {model_name}. Check the .pkl file integrity.")

@router.post("/predict/{model_name}", response_model=PredictionResponse, status_code=200)
def get_prediction(model_name: str, request_data: Input):
    """
    Accepts transaction features, preprocesses them, and returns a fraud classification 
    using the specified model.
    """
    
    # 1. Load the model
    try:
        model = load_model(model_name)
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    try:
        # Pass the data to the external preprocessing utility
        processed_features = preprocess_data(request_data)
    except Exception as e:
         raise HTTPException(status_code=400, detail=f"Preprocessing failed: {e}")
    
    # 3. Make Prediction
    try:
        # Get the class prediction (0 or 1)
        prediction_class = int(model.predict(processed_features)[0])
        
        # Get the probability of the positive class (1, which is Fraud)
        # Most classification models use predict_proba
        if hasattr(model, 'predict_proba'):
            # The second column [0][1] is the probability of class 1 (Fraud)
            probability_fraud = model.predict_proba(processed_features)[0][1]
        else:
            # Fallback for models like SVC without probability=True
            probability_fraud = -1.0 
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed for model '{model_name}': {e}")

    # 4. Format and return result
    prediction_label = "Fraud (1)" if prediction_class == 1 else "Not Fraud (0)"
    
    return PredictionResponse(
        model_used=model_name,
        prediction_label=prediction_label,
        prediction_class=prediction_class,
        probability_fraud=round(float(probability_fraud), 4)
    )