from typing import List
from pydantic import BaseModel
from tictactoe.models.players import Player


class Movement(BaseModel):
    player: Player
    position: List[int]
    symbol: str

    class Config:
        orm_mode = True
