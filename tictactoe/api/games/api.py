from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from tictactoe.conf.database import get_db

from tictactoe.models.games import Game
from tictactoe.schemas.games import make_new_board, create_players, get_starting_player

games_router = APIRouter()


@games_router.post("/create", status_code=status.HTTP_201_CREATED)
def create_game(request: dict, response: Response, db: Session = Depends(get_db)):
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
        new_game_dict["starting_player"] = get_starting_player(request)
        new_game = Game(new_game_dict)
        db.add(new_game)
        db.commit()
        return db.query(Game).filter(Game.id == new_game.id).first()

    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"Whoops, something went wrong!"}


@games_router.get("/", status_code=status.HTTP_200_OK)
def get_all_games(db: Session = Depends(get_db)):
    """queries all games and returns them"""
    # TODO: Add pagination
    # TODO: Add filtering by status
    # TODO: Iterate data to restore game board format
    return db.query(Game).all()


@games_router.get("/{game_id}", status_code=status.HTTP_200_OK)
def get_game_by_id(game_id: int, response: Response, db: Session = Depends(get_db)):
    """queries a game by id and returns it"""
    # TODO: Format data to restore game board format and players
    assert game_id, "game_id is required"
    try:
        game = db.query(Game).filter(Game.id == game_id).first()
        if game is not None:
            return game
        else:
            response.status_code = status.HTTP_204_NO_CONTENT
            return {"message": "Game not found, insert a valid ID."}
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"message": "Whoops, something went wrong!"}


@games_router.delete("/{game_id}", status_code=status.HTTP_200_OK)
def delete_game_by_id(game_id: int, response: Response, db: Session = Depends(get_db)):
    """deletes a game by id and returns a confirmation"""
    assert game_id, "game_id is required"
    try:
        game = db.query(Game).filter(Game.id == game_id).first()
        if game is not None:
            db.delete(game)
            db.commit()
            return {"message": f"Game {game_id} deleted successfully."}
        else:
            response.status_code = status.HTTP_204_NO_CONTENT
            return {"message": f"Game {game_id} not found, insert a valid ID."}
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"message": "Whoops, something went wrong!"}


@games_router.post("/movement", status_code=status.HTTP_201_CREATED)
def create_movement(request: dict, response: Response, db: Session = Depends(get_db)):
    """
    Create a new movement for a player for a game
    request:
        {
        "game_id": 1234,
        "player": "me",
        "position": [0, 0],
        "symbol": "X"
        }
    """
    game_id = request["game_id"]
    assert game_id, "game_id is required"
    try:
        game = db.query(Game).filter(Game.id == game_id).first()
        if game is None:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"message": f"Game {game_id} not found. Can't create movement."}
        else:
            # Serialize request data
            # Create movement
            # Check if it's winning movement
            # Update game
            return {"message": f"Movement created successfully.", "game": game}
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"message": "Whoops, something went wrong!"}
