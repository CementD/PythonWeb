from fastapi import APIRouter
from schemas.user import UserCreate, UserResponse

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/register", response_model=UserResponse)
def create_user(user: UserCreate):
    return {
        "id": 1,
        "email": user.email,
        "age": user.age,
        "is_active": user.is_active
    }