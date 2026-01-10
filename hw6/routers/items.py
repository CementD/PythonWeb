from fastapi import APIRouter
from typing import Optional

router = APIRouter(
    prefix="/items",
    tags=["items"]
)

@router.get("/{item_id}")
async def get_item(item_id: int, q: Optional[str] = None):
    return { "item_id": item_id, "q": q }
