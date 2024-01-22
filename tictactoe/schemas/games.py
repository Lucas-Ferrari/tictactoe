from pydantic import BaseModel


class Game(BaseModel):
    id: int
    players: list
    starting_player: str
    next_player: str
    winner: str
    board_status: list
    movements: int

    class Config:
        orm_mode = True


class GameMovement(BaseModel):
    id: int
    game_id: int
    player: str
    position: str
    symbol: str
    new_board_status: list

    class Config:
        orm_mode = True
