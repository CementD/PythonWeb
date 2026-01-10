from fastapi import FastAPI
from routers import hello, square, items, greet, calc

app = FastAPI(
    title="HW1",
    description="HW1",
    version="1.0.0"
)

app.include_router(hello.router)
app.include_router(square.router)
app.include_router(items.router)
app.include_router(greet.router)
app.include_router(calc.router)

