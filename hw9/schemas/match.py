from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class MatchBase(BaseModel):
    tournament_id: int
    player1_id: int
    player2_id: int
    player1_score: float = Field(ge=0)
    player2_score: float = Field(ge=0)

class MatchCreate(MatchBase):
    pass

class Match(MatchBase):
    id: int
    winner_id: Optional[int] = None

    class Config:
        from_attributes = True