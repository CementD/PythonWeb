from fastapi import Query
from re import search
from typing import Optional

from fastapi import APIRouter

router = APIRouter(
    prefix="/products",
    tags=["Product"]
)

@router.get("/")
def get_products(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    search: Optional[str] = Query(None, min_length=3),
):
    return {
        "page": page,
        "limit": limit,
        "search": search
    }
