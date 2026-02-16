from fastapi import FastAPI
from routers import match, player, tournament

app = FastAPI()

app.include_router(match.router)
app.include_router(player.router)
app.include_router(tournament.router)