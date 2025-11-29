from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from Routers.health import health_router
from Schemas.input import input_router
from Routers.predict import predict_router, load_model, ALLOWED_MODELS

@asynccontextmanager
async def lifespan(app: FastAPI):
    for model_name in ALLOWED_MODELS:
        try:
            load_model(model_name)
            print(f"Loaded model: {model_name}")
        except Exception as e:
            print(f"Failed to load model {model_name}: {e}")
    yield
    print("Shutting down...")

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router, tags=["Health"])
app.include_router(input_router, tags=["Input"])
app.include_router(predict_router, tags=["Prediction"])

@app.get("/")
def root():
    return {"Service": "FraudLens", "Status": "Running"}
