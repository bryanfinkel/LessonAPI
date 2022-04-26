from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello Bryan"}


@app.get("/api/v1/ping")
async def ping():
    return {"message": "pong"}