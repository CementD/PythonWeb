from fastapi import APIRouter

router = APIRouter(
    prefix="/square",
    tags=["square"]
)

@router.get("/{number}")
async def square(number: int):
    return { "number": number, "square": number**2 }
