from fastapi import FastAPI, APIRouter
from app.routers import user_routers  # Import from __init__.py

# Create the main router
api_router = APIRouter(
    prefix="/api/v1"  # Global prefix
)

# Include sub-routers
api_router.include_router(user_routers.router)

# Main FastAPI app
app = FastAPI()

# Include the main router in the app
app.include_router(api_router)

# Root route
@app.get("/")
async def root():
    return {"message": "Welcome to the API"}
