from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "mongodb://admin:securepassword@localhost:27017/?authSource=admin"
client = AsyncIOMotorClient(MONGO_URI)
database = client["spelling_project"]
words_collection = database["words"]

