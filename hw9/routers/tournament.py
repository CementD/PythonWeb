from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from schemas.player import Player
from schemas.tournament import Tournament, TournamentCreate, TournamentUpdate
from schemas.match import Match
from db import match_db, players_db, tournaments_db


router = APIRouter(
    prefix="/tournaments",
    tags=["tournaments"]
)

current_id = 1

@router.post("/", response_model=Tournament)
async def create_tournament(tournament: TournamentCreate):
    global current_id
    new_tournament = Tournament(id=current_id, **tournament.model_dump())
    tournaments_db.append(new_tournament)
    current_id += 1
    return new_tournament

@router.get("/", response_model=List[Tournament])
async def get_tournaments(
        game: Optional[str] = Query(None)
    ):
    tournaments = tournaments_db
    if game:
        tournaments = [t for t in tournaments if t.game == game]
    return tournaments

@router.get("/{tournament_id}", response_model=Tournament)
async def get_tournament(tournament_id: int):
    for tournament in tournaments_db:
        if tournament.id == tournament_id:
            return tournament
    raise HTTPException(status_code=404, detail="Tournament not found")

@router.put("/{tournament_id}", response_model=Tournament)
async def update_tournament(tournament_id: int, tournament_update: TournamentUpdate):
    for index, tournament in enumerate(tournaments_db):
        if tournament.id == tournament_id:
            tournament_updated = tournament.model_copy(update=tournament_update.model_dump(exclude_unset=True))
            tournaments_db[index] = tournament_updated
            return tournament_updated
    raise HTTPException(status_code=404, detail="Tournament not found")

@router.delete("/{tournament_id}", response_model=Tournament)
async def delete_tournament(tournament_id: int):
    for index, tournament in enumerate(tournaments_db):
        if tournament.id == tournament_id:
            return tournaments_db.pop(index)
    raise HTTPException(status_code=404, detail="Tournament not found")

@router.post("/{tournament_id}/players/{player_id}", response_model=Player)
async def add_player_tournament(tournament_id: int, player_id: int):
    for index, tournament in enumerate(tournaments_db):
        if tournament.id == tournament_id:
            if player_id in tournament.player_ids:
                raise HTTPException(status_code=404, detail="Player already registered")
            tournament.player_ids.append(player_id)
            for player in players_db:
                if player.id == player_id:
                    return player
            raise HTTPException(status_code=404, detail="Player not found")
    raise HTTPException(status_code=404, detail="Tournament not found")

@router.get("/{tournament_id}/matches", response_model=List[Match])
async def get_tournament_matches(tournament_id: int):
    for tournament in tournaments_db:
        if tournament.id == tournament_id:
            return [
                match
                for match in match_db
                if match.id in tournament.match_ids
            ]
    raise HTTPException(status_code=404, detail="Tournament not found")

@router.get("/{tournament_id}/standings", response_model=List[Player])
async def get_tournament_standings(tournament_id: int):
    for tournament in tournaments_db:
        if tournament.id == tournament_id:
            players = [
                player
                for player in players_db
                if player.id in tournament.player_ids
            ]
            players.sort(key=lambda x: x.score, reverse=True)
            return players
    raise HTTPException(status_code=404, detail="Tournament not found")