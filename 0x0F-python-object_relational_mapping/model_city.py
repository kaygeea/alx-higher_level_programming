#!/usr/bin/python3
"""This module adopts SQLAlchemy to represent an SQL table as Python class"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """Represent and link to a MySQL table - "cities",
    with the table columns represented as class attributes:
        a. id (PK) - A column of an auto-gen'd int, unique int and not null.
        b. name - A column of a str of max 128 chars and not null.
        c. state_id (FK) - A column of an int and can't be null.
    """
    __tablename__ = 'cities'

    id = Column(Integer, autoincrement=True, unique=True, nullable=False,
                primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
