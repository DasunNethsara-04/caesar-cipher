from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schemas import  EncText, DecText
# from controllers import TextController

app: FastAPI = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=['http://localhost:5173'],
                    allow_credentials=True,
                    allow_methods=["POST", "GET"],
                    allow_headers=["*"],
                )
# text_controller: TextController = TextController()


@app.get("/api/")
async def home() -> dict[str, str]:
    return {"message": "Hello, World!"}


@app.post("/api/enc")
async def encrypt_text(text: EncText) -> dict[str, EncText]:
    # print(text)
    return {"returned: ": text}
