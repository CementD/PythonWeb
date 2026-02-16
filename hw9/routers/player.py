from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from schemas.player import Player, PlayerCreate, PlayerUpdate
from db import players_db


router = APIRouter(
    prefix="/players",
    tags=["players"]
)

current_id = 1

@router.post("/", response_model=Player)
async def create_player(player: PlayerCreate):
    global current_id
    new_player = Player(id=current_id, **player.model_dump())
    players_db.append(new_player)
    current_id += 1
    return new_player

@router.get("/", response_model=List[Player])
async def get_players(
        min_score: Optional[int] = Query(None, gt=0),
        name: Optional[str] = Query(None, min_length=3, max_length=100)
):
    players = players_db
    if min_score:
        players = [p for p in players if p.score >= min_score]
    if name:
        players = [p for p in players if name.lower() in p.name.lower()]

    return players

@router.get("/{player_id}", response_model=Player)
async def get_player(player_id: int):
    for player in players_db:
        if player.id == player_id:
            return player
    raise HTTPException(status_code=404, detail="Player not found")

@router.put("/{player_id}", response_model=Player)
async def update_player(player_id: int, update: PlayerUpdate):
    for index, player in enumerate(players_db):
        if player.id == player_id:
            update_player = player.model_copy(update=update.model_dump(exclude_unset=True))
            players_db[index] = update_player
            return update_player
    raise HTTPException(status_code=404, detail="Player not found")

@router.delete("/{player_id}", response_model=Player)
async def delete_player(player_id: int):
    for index, player in enumerate(players_db):
        if player.id == player_id:
            return players_db.pop(index)
    raise HTTPException(status_code=404, detail="Player not found")