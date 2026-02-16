from pydantic import BaseModel


class Adress(BaseModel):
    city: str
    street: str

class UserCreate(BaseModel):
    name: str
    adress: Adress