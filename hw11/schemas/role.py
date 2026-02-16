from pydantic import BaseModel, Field

class RoleCreate(BaseModel):
    name: str = Field(min_length=1, max_length=50)

class RoleRead(RoleCreate):
    id: int

    class Config:
        from_attributes = True