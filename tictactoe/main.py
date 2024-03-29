from fastapi import FastAPI

from tictactoe.conf.settings import settings
from tictactoe.conf.database import Session, engine, Base
from tictactoe.api.v1 import api_v1_router

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.API_VERSION,
)

Base.metadata.create_all(bind=engine)
app.include_router(api_v1_router, prefix=settings.API_V1_STR)
