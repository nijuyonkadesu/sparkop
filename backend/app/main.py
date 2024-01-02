from fastapi import FastAPI

from app.api.apiv1.endpoints import shoes

app = FastAPI()

app.include_router(shoes.router)

@app.get("/health")
def health():
    # TODO: get redis status from core module
    return True

@app.get("/ping")
def ping():
    return "pong"
