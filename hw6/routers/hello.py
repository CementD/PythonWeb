from fastapi import APIRouter

router = APIRouter(
    prefix="/hello",
    tags=["hello"]
)

@router.get("/")
async def root():
    return {"message": "Hello, FastAPI!"}