import asyncio
from schemas.task2 import Item

from fastapi import HTTPException, APIRouter

router = APIRouter(
    prefix="/task2",
    tags=["task2"]
)

items_db = [
    {
        "id": 1,
        "name": "ewwvve",
        "price": 5.00
    },
    {
        "id": 2,
        "name": "bvve",
        "price": 14.88
    },
    {
        "id": 3,
        "name": "bvve",
        "price": 5.67
    }
]

@router.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: int):
    await asyncio.sleep(2)
    for item in items_db:
        if item['id'] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")