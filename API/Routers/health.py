from fastapi import APIRouter

health_router = APIRouter()

@health_router.get("/health")
def router():
    return {
        "Service":"FraudLens",
        "Status":"OK"
        }
