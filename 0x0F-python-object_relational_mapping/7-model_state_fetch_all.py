#!/usr/bin/python3
"""
This module lists all State objs from the database 'hbtn_0e_6_usa',
using SQLAlchemy.
"""
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import Session
from model_state import Base, State
from sys import argv


url = URL.create('mysql+mysqldb', username=argv[1], password=argv[2],
                 host='localhost', port=3306, database=argv[3])
v6_engine = create_engine(url)

with Session(v6_engine) as session:
    for state_obj in session.query(State).order_by(State.id):
        print("{}: {}".format(state_obj.id, state_obj.name))
