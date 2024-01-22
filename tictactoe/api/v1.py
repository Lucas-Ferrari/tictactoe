from fastapi import APIRouter

from tictactoe.api.games.api import games_router

api_v1_router = APIRouter()

api_v1_router.include_router(games_router, prefix="/games", tags=["Games"])
