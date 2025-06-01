from pydantic import BaseModel

class Word(BaseModel):
    word: str
    status: str  # "correct" or "incorrect"
    timestamp: str
