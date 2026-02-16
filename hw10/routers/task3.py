from schemas.task3 import Order, Product
from fastapi import HTTPException, APIRouter
import asyncio

router = APIRouter(
    prefix="/task3",
    tags=["task3"]
)

orders_db = [
    {
        "order_id": 1,
        "products": [
            {"title": "Laptop", "price": 1200.50},
            {"title": "Mouse", "price": 25.00}
        ]
    },
    {
        "order_id": 2,
        "products": [
            {"title": "Monitor", "price": 300.00}
        ]
    }
]

async def get_product(product_data: dict):
    await asyncio.sleep(1)
    return Product(**product_data)


@router.get("/orders/{order_id}")
async def get_order(order_id: int):
    for order_data in orders_db:
        if order_data["order_id"] == order_id:

            products = await asyncio.gather(
                *(get_product(p) for p in order_data["products"])
            )

            order = Order(order_id=order_id, products=products)

            total_sum = sum(product.price for product in order.products)

            return {
                "order_id": order.order_id,
                "products": order.products,
                "total_sum": total_sum
            }

    raise HTTPException(status_code=404, detail="Order not found")
