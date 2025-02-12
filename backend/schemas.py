from pydantic import  BaseModel


class EncText(BaseModel):
    key: int
    plainText: str


class DecText(BaseModel):
    key: int
    cipherText: str
