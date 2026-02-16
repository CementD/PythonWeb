from fastapi import APIRouter

from schemas.task1 import UserCreate

router = APIRouter(
    prefix="/task1",
    tags=["task1"]
)

@router.post("/users")
async def create_user(user: UserCreate):
    return user