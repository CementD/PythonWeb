from typing import List

from pydantic import BaseModel, Field

from schemas.event import EventRead


class DepartmentCreate(BaseModel):
    name: str = Field(min_length=1, max_length=50)
    description: str = Field(min_length=1, max_length=200)

class DepartmentRead(DepartmentCreate):
    id: int
    events: List[EventRead]
    class Config:
        from_attributes = True