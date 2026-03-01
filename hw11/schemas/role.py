from pydantic import BaseModel

class RoleCreate(BaseModel):
    name: str

class RoleRead(RoleCreate):
    id: int

    class Config:
        from_attributes = True