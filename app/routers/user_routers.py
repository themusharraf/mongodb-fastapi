from fastapi import APIRouter

from app.crud import (
    create_user_in_db,
    get_user_by_id,
    update_user_in_db,
    delete_user_in_db,
)
from app.models import User, UserResponse
from app.schemas import document_to_user

router = APIRouter(
    prefix="/user",
    tags=["User"],
)


# Create User
@router.post("/users", response_model=UserResponse)
async def create_user(user: User):
    user_data = user.dict()
    new_user = create_user_in_db(user_data)
    return document_to_user(new_user)


# Get User by ID
@router.get("/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: str):
    user = get_user_by_id(user_id)
    return document_to_user(user)


# Update User
@router.put("/users/{user_id}", response_model=UserResponse)
async def update_user(user_id: str, user: User):
    updated_user = update_user_in_db(user_id, user.dict())
    return document_to_user(updated_user)


# Delete User
@router.delete("/users/{user_id}")
async def delete_user(user_id: str):
    delete_user_in_db(user_id)
    return {"detail": "User deleted successfully"}
