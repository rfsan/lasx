from sqlalchemy import Column, ForeignKey, Integer, String, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
# Project
from .database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=text('now()')
    )
    

class SacredBoard(Base):
    __tablename__ = 'sacred_board'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    owner_id = Column(
        Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True), 
        nullable=False, 
        server_default=text('now()'))
    
    owner = relationship('User')


class Marks(Base):
    __tablename__ = 'marks'

    user_id = Column(
        Integer, ForeignKey('users.id', ondelete='CASCADE'), primary_key=True)
    post_id = Column(
        Integer, 
        ForeignKey('sacred_board.id', ondelete='CASCADE'), 
        primary_key=True)
    commnent = Column(String, nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True), 
        nullable=False, 
        server_default=text('now()'))