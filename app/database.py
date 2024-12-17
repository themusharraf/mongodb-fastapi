from pymongo import MongoClient
from pymongo.errors import OperationFailure

MONGO_URI = "mongodb://admin:1@localhost:27017/mydatabase?authSource=admin"

try:
    client = MongoClient(MONGO_URI)
    db = client["mydatabase"]
    collection = db["users"]
    print("MongoDB connection successful!")
except OperationFailure as e:
    print(f"Authentication failed: {e}")
