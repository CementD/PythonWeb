from typing import List
from pydantic import BaseModel

class Product(BaseModel):
    title: str
    price: float

class Order(BaseModel):
    order_id: int
    products: List[Product]
