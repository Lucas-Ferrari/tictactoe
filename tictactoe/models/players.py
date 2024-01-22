from pydantic import BaseModel


class Player(BaseModel):
    id: int
    name: str
    symbol: str

    class Config:
        orm_mode = True
