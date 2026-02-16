from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import datetime

class PlayerBase(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    email: EmailStr
    score: float = Field(default=0)

class PlayerCreate(PlayerBase):
    pass

class PlayerUpdate(BaseModel):
    name: Optional[str] = Field(default=None, min_length=3, max_length=50)
    email: Optional[EmailStr] = Field(default=None)
    score: Optional[float] = Field(default=None)

class Player(PlayerBase):
    id: int
    class Config:
        from_attributes = True

