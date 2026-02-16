from schemas.task4 import User
from fastapi import APIRouter
import asyncio

router = APIRouter(
    prefix="/task4",
    tags=["task4"]
)

@router.post("/profile-check")
async def profile_check(user: User):
    if user.profile is not None:
        await asyncio.sleep(2)
        return {
            "username": user.username,
            "profile_exists": True,
            "message": "Profile received and checked"
        }
    return {
        "username": user.username,
        "profile_exists": False,
        "message": "No profile provided, skipping check"
    }