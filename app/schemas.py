from bson import ObjectId
from .models import UserResponse

# Helper function to convert MongoDB documents to Pydantic models
def document_to_user(doc):
    return UserResponse(
        id=str(doc["_id"]),
        username=doc["username"],
        firstname=doc["firstname"],
        surname=doc["surname"],
        birthday=doc["birthday"],
        region=doc["region"],
        studentsId=[str(student_id) for student_id in doc.get("studentsId", [])],
    )
