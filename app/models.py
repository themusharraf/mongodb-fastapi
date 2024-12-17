from pydantic import BaseModel
from typing import List

# Request schema for creating/updating a user
class User(BaseModel):
    username: str
    firstname: str
    surname: str
    birthday: str
    region: str
    studentsId: List[str] = []

# Response schema with ID
class UserResponse(User):
    id: str
