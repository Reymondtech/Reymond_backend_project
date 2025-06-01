from fastapi import FastAPI
from app.routes import router  # Import the APIRouter instance from routes.py

app = FastAPI()  # Initialize the FastAPI instance

app.include_router(router)  # Attach the defined routes

print(f"App instance created: {app}")  # Optional debugging
