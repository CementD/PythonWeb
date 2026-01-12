from fastapi import FastAPI
from routers import user, product
app = FastAPI(
    title="HW7",
    description="HW7",
    version="1.0.0"
)

app.include_router(user.router)
app.include_router(product.router)