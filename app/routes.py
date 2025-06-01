from fastapi import APIRouter

router = APIRouter()  # This object MUST be called router

@router.get("/")
async def home():
    return {"message": "Welcome to the API!"}

