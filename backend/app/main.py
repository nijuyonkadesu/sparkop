from fastapi import FastAPI

from app.api.apiv1.endpoints import shoes
from app.core.vars import app_health_status

app = FastAPI()

app.include_router(shoes.router)

@app.get("/health")
def health():
    return app_health_status 

@app.get("/ping")
def ping():
    return "pong"
