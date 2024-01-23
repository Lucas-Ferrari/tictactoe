from sqlalchemy import Column, Integer, String, ForeignKey

from tictactoe.conf.database import Base


class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    players = Column(String, nullable=False)
    starting_player = Column(String, nullable=False)
    next_player = Column(String, nullable=True)
    winner = Column(String, nullable=True)
    board_status = Column(String, nullable=True)
    movements = Column(Integer, nullable=False, default=0)

    def __init__(self, data):
        self.players = data["players"]
        self.starting_player = data["starting_player"]
        self.next_player = data["starting_player"]
        self.winner = data["winner"]
        self.board_status = data["board_status"]
        self.movements = data["movements"]


class GameMovement(Base):
    __tablename__ = "game_movements"

    id = Column(Integer, primary_key=True, index=True)
    game_id = Column(Integer, ForeignKey("games.id"))
    player = Column(String, nullable=False)
    position = Column(String, nullable=False)
    symbol = Column(String, nullable=False)
    new_board_status = Column(String, nullable=False)
