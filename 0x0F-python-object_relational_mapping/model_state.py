#!/usr/bin/python3
"""This module adopts SQLAlchemy to create an SQL table"""
from sqlalchemy import Column, Integer, String, PrimaryKeyConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Represent and link to a MySQL table - "state",
    with the table columns represented as class attributes:
        a. id (PK) - A column of an auto-gen'd, unique int and not null.
        b. name - A column of a str of max 128 chars and not null.
    """
    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True, unique=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
