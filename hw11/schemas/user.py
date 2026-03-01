from pydantic import BaseModel, Field

class UserCreate(BaseModel):
    name: str = Field(max_length=100)
    role_id: int

class UserRead(UserCreate):
    id: int

    class Config:
        from_attributes = True