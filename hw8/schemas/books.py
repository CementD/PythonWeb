from pydantic import BaseModel, Field
from typing import Optional
from datetime import date


class BookBase(BaseModel):
    title: str = Field(None, min_length=3, max_length=100)
    author: str = Field(None, min_length=3, max_length=50)
    description: Optional[str] = Field(default=None, max_length=500)
    year: Optional[int] = Field(None, ge=1450, le=date.today().year)
    rating: Optional[float] = Field(None, ge=0.0, le=5.0)
    tags: Optional[list[str]] = Field(None, min_length=1, max_length=100)

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=3, max_length=100)
    author: Optional[str] = Field(None, min_length=3, max_length=50)
    description: Optional[str] = Field(None, max_length=500)
    year: Optional[int] = Field(None, ge=1450, le=date.today().year)
    rating: Optional[float] = Field(None, ge=1.0, le=5.0)
    tags: Optional[list[str]] = Field(default=None, min_length=1, max_length=100)

class Book(BookBase):
    id: int
    class Config:
        from_attributes = True


