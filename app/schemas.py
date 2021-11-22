from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr


# Authentication
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str]


# Users
class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True
    

# Sacred Boards
class SacredBoardCreate(BaseModel):
    name: str


class SacredBoardResponse(BaseModel):
    id: int
    name: str
    created_at: datetime
    owner: UserResponse

    class Config:
        orm_mode = True
