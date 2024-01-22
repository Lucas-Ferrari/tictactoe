from pydantic import BaseModel
from typing import List

from tictactoe.models.players import Player
from tictactoe.models.movements import Movement


class Games(BaseModel):
    players: List[Player]
    starting_player: Player
    board_status: List[List[str]] = [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]
    next_player: str
    winner: str = None
    finished: bool

    class Config:
        orm_mode = True


class GameMovement(BaseModel):
    game_id: int
    player: Player
    movement: Movement
    board_status: List[List[str]]

    class Config:
        orm_mode = True
