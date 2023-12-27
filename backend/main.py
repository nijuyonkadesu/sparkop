from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    # TODO: get redis status from core module
    return True

@app.get("/ping")
def ping():
    return "pong"
