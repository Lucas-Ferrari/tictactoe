from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from tictactoe.conf.database import get_db


games_router = APIRouter()


@games_router.post("/games/create")
def create_game(request: dict, db: Session = Depends(get_db)):
    """
    Create a new game.
    request:
        {
        "players": [
        {"name": "me"},
        {"name": "other"}
        ],
        "starting_player": "me"
        }

    response:
        {
        “game_id”: 1234,
        “players”: [{“name”: “me”, “symbol: “X”}, {“name”: “other”, “symbol”: “O”}]
        “movements_played”: 0,
        “next_turn”: “other”,
        “board”: [[null, null, null], [null, null, null], [null, null, null]],
        “winner”: null
        }
    """
    import ipdb

    ipdb.set_trace()
    return {"Hello": "World"}


@games_router.get("/games/{item_id}")
def read_item(item_id: int, db: Session = Depends(get_db)):
    return {"item_id": item_id}
