from typing import Optional
from pydantic import BaseModel

class Profile(BaseModel):
    bio: str
    age: int

class User(BaseModel):
    username: str
    profile: Optional[Profile]