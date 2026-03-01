from fastapi import FastAPI
from db.session import engine, Base
from api import user, role, department, event

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Space Station Event Manager")

app.include_router(role.router)
app.include_router(user.router)
app.include_router(department.router)
app.include_router(event.router)