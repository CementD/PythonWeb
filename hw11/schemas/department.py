from pydantic import BaseModel

class DepartmentCreate(BaseModel):
    name: str
    description: str

class DepartmentRead(DepartmentCreate):
    id: int

    class Config:
        from_attributes = True