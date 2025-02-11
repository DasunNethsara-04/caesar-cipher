from fastapi import FastAPI

app: FastAPI = FastAPI()


@app.get("/")
async def home() -> dict[str, str]:
    return {"message": "Hello, World!"}
