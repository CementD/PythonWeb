from typing import Optional
from pydantic import BaseModel, Field, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)
    age: int = Field(ge=14)
    is_active: Optional[bool] = True

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    age: int
    is_active: Optional[bool] = True
    class Config:
        from_attributes = True