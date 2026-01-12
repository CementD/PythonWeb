from typing import Optional
from pydantic import BaseModel, Field, EmailStr

class FeedbackCreate(BaseModel):
    name: str = Field(min_length=2)
    email: EmailStr
    rating: int = Field(ge=1, le=5)
    comment: Optional[str] = Field(None, max_length=200)

class FeedbackResponse(BaseModel):
    name: str
    email: EmailStr
    rating: int
    comment: Optional[str] = None
    message: str = "Thank you for your feedback!"

    class Config:
        from_attributes = True
