from bson import ObjectId
from bson.errors import InvalidId
from fastapi import HTTPException
from app.database import collection


# Create a new user
def create_user_in_db(user_data: dict):
    user_data["studentsId"] = [ObjectId(student_id) for student_id in user_data["studentsId"]]
    result = collection.insert_one(user_data)
    return collection.find_one({"_id": result.inserted_id})

# Retrieve a single user
def get_user_by_id(user_id: str):
    try:
        user = collection.find_one({"_id": ObjectId(user_id)})
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid user ID format")

# Update user
def update_user_in_db(user_id: str, user_data: dict):
    try:
        user_data["studentsId"] = [ObjectId(student_id) for student_id in user_data["studentsId"]]
        update_result = collection.update_one({"_id": ObjectId(user_id)}, {"$set": user_data})
        if update_result.matched_count == 0:
            raise HTTPException(status_code=404, detail="User not found")
        return collection.find_one({"_id": ObjectId(user_id)})
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid user ID format")

# Delete user
def delete_user_in_db(user_id: str):
    try:
        delete_result = collection.delete_one({"_id": ObjectId(user_id)})
        if delete_result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="User not found")
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid user ID format")
