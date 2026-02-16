from typing import List

from pydantic import BaseModel, Field

from schemas.user import UserRead


class EventCreate(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    description: str = Field(min_length=3, max_length=200)
    department: str = Field(min_length=3, max_length=50)

class EventRead(EventCreate):
    id: int
    users: List[UserRead]

    class Config:
        from_attributes = True