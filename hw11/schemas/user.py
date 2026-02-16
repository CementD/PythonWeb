from pydantic import BaseModel, Field

class UserCreate(BaseModel):
    name: str = Field(max_length=100)
    role: str = Field(min_length=3, max_length=100)

class UserRead(UserCreate):
    id: int
    class Config:
        from_attributes = True
