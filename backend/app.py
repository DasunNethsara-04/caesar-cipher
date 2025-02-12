# imports
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schemas import  EncText, DecText
from controllers import TextController

# app initialization
app: FastAPI = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=['http://localhost:5173'],
                    allow_credentials=True,
                    allow_methods=["POST", "GET"],
                    allow_headers=["*"],
                )

# controller initialization
text_controller: TextController = TextController()


# routes
@app.get("/api/")
async def home() -> dict[str, str]:
    return {"message": "Hello, World!"}


@app.post("/api/enc")
async def encrypt_text(text: EncText) -> dict[str, str]:
    cipher_text: str = text_controller.encrypt(text.key, text.plainText)
    return {"cipherText": cipher_text}


@app.post("/api/dec")
async def decrypt_text(text: DecText) -> dict[str, DecText]:
    return {"returned": text}
