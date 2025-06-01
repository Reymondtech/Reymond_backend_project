import os
from dotenv import load_dotenv

# Load environment variables from a .env file (optional)
load_dotenv()

# App Configuration
class Config:
    APP_NAME = "Spelling & Grammar Learning API"
    VERSION = "1.0.0"
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"

    # Database Configuration (if applicable)
    DB_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")

    # API Key (if needed)
    SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key")

config = Config()
