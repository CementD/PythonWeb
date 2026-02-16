from fastapi import APIRouter, HTTPException
from typing import List
from schemas.match import Match, MatchCreate
from db import tournaments_db, players_db, match_db

router = APIRouter(
    prefix="/matches",
    tags=["matches"]
)

current_id = 1

@router.post("/", response_model=Match)
async def create_match(match: MatchCreate):
    global current_id

    tournament = next((t for t in tournaments_db if t.id == match.tournament_id), None)
    if tournament is None:
        raise HTTPException(status_code=404, detail="Tournament not found")

    if match.player1_id not in tournament.player_ids or match.player2_id not in tournament.player_ids:
        raise HTTPException(status_code=404, detail="Player not in tournament")

    if match.player1_id > match.player2_id:
        winner_id = match.player1_id
    elif match.player2_id > match.player1_id:
        winner_id = match.player2_id
    else:
        winner_id = None
    new_match = Match(id=current_id, **match.model_dump(), winner_id=winner_id)
    match_db.append(new_match)

    for tournament in tournaments_db:
        if tournament.id == match.tournament_id:
            tournament.match_ids.append(new_match.id)
            break

    for player in players_db:
        if player.id == match.player1_id:
            player.score += match.player1_score
        if player.id == match.player2_id:
            player.score += match.player2_score

    current_id += 1
    return new_match
