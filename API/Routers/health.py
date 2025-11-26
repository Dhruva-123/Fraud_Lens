from fastapi import FastAPI

router = FastAPI()

@router.get("/health")
def router():
    return {
        "Service":"FraudLens",
        "Status":"OK"
        }
