from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class TournamentBase(BaseModel):
    name: str = Field(min_length=3, max_length=100)
    game: str
    date: datetime
    max_players: int = Field(ge=2, le=100)
    player_ids: Optional[list] = Field(default_factory=list)
    match_ids: Optional[list] = Field(default_factory=list)

class TournamentCreate(TournamentBase):
    pass

class TournamentUpdate(BaseModel):
    name: Optional[str] = Field(default=None, min_length=3, max_length=100)
    game: Optional[str] = Field(default=None)
    date: Optional[datetime] = Field(default=None)
    max_players: Optional[int] = Field(default=None)
    player_ids: Optional[list] = Field(default_factory=list)
    match_ids: Optional[list] = Field(default_factory=list)

class Tournament(TournamentBase):
    id: int
    class Config:
        from_attributes = True