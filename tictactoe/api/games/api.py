from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from tictactoe.conf.database import get_db

from tictactoe.models.games import Game
from tictactoe.schemas.games import make_new_board, create_players

games_router = APIRouter()


@games_router.post("/create")
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
    # TODO: Abstract this sanitization into a validator/serializer
    try:
        new_game_dict = {}
        new_game_dict["players"] = create_players(request["players"])
        new_game_dict["winner"] = None
        new_game_dict["movements"] = 0
        new_game_dict["board_status"] = make_new_board()
        new_game_dict["starting_player"] = (
            str(request["starting_player"])
            if request["starting_player"]
            else str(request["players"][0]["name"])
        )
    except Exception as e:
        return {"Whoops, something went wrong!"}
    new_game = Game(new_game_dict)
    db.add(new_game)
    db.commit()
    return new_game


@games_router.get("/")
def read_item(db: Session = Depends(get_db)):
    """queries all games and returns them"""
    # TODO: Add pagination
    # TODO: Add filtering by status
    # TODO: Iterate data to restore game board format
    return db.query(Game).all()
