from fastapi import FastAPI
from routers import task1, task2, task3, task4

app = FastAPI()

app.include_router(task1.router)
app.include_router(task2.router)
app.include_router(task3.router)
app.include_router(task4.router)


