# Core
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# Project
from . import models
from .database import engine
from .routers import auth, user, sacred_board


models.Base.metadata.create_all(bind=engine)
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(auth.router)
app.include_router(user.router)
app.include_router(sacred_board.router)