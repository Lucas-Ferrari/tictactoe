from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from tictactoe.conf.database import get_db

games_router = APIRouter()


# FastAPI routes
@games_router.get("/health-check")
def healthcheck():
    return {"Hello": "World"}


@games_router.post("/games/create")
def create_game(request: dict, db: Session = Depends(get_db)):
    return {"Hello": "World"}


@games_router.get("/games/{item_id}")
def read_item(item_id: int, db: Session = Depends(get_db)):
    return {"item_id": item_id}
