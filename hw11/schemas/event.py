from pydantic import BaseModel
from datetime import datetime

class EventCreate(BaseModel):
    title: str
    description: str
    date: datetime
    department_id: int

class EventRead(EventCreate):
    id: int

    class Config:
        from_attributes = True