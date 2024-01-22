from typing import List

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Tic-Tac-Toe API"
    PROJECT_DESCRIPTION: str = "Fligoo TicTacToe Challenge"
    API_VERSION: str = "v1"
    DOCS: bool = True

    DATABASE_URL: str = "sqlite:///./tictactoe.db"
    API_V1_STR: str = "/api/v1"


settings = Settings()
