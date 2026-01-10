from contextlib import nullcontext
from typing import Optional
from fastapi import APIRouter

router = APIRouter(
    prefix="/greet",
    tags=["greet"]
)

@router.get("/")
async def greeting(name: str, age: Optional[int] = None):
    return {"message": f"Hello, {name}", "age": age}