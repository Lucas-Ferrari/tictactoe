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
        from_attributes = True


class GameMovement(BaseModel):
    id: int
    game_id: int
    player: str
    position: str
    symbol: str
    new_board_status: list

    class Config:
        from_attributes = True


def make_new_board():
    return flatten_board([[None, None, None], [None, None, None], [None, None, None]])


def create_players(players):
    """
    This function receives a list of players with two possible formats.
    If the symbol is not provided, it will be assigned automatically.
    [ {"name": "me"}, {"name": "other"} ]
    or
    [ {"name": "me", "symbol" : "x"}, {"name": "other", "symbol": "o"} ]

    and return a list of players with the following format:
    [ {"name": "me", "symbol" : "x"}, {"name": "other", "symbol": "o"} ]

    """
    assert players is not None

    if len(players) != 2:
        raise Exception("Invalid number of players")
    else:
        if "symbol" not in players[0]:
            players[0]["symbol"] = "X"
            players[1]["symbol"] = "O"

    return str(players)


def flatten_board(board):
    # We use this to store the board in the database as a string
    assert board is not None

    return ",".join(str(cell) for row in board for cell in row)


def recover_game_board(flat_board):
    # We use this to recover the board from the database
    assert flat_board is not None

    board = flat_board[2:-2].split("], [")
    board = [row.split(", ") for row in board]
    board = [[eval(cell) if cell != "None" else None for cell in row] for row in board]
    return board


def get_starting_player(request):
    assert request is not None

    if "starting_player" in request:
        return request["starting_player"]
    else:
        return request["players"][0]["name"]


def regenerate_players(players):
    assert players is not None

    return str(players)
