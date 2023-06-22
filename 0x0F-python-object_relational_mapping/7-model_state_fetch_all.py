#!/usr/bin/python3
"""
Lists all State objs from the database "hbtn_0e_6_usa" using SQLAlchemy.
"""
from sqlalchemy import create_engine, select
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import Session
from model_state import Base, State
import sys
import MySQLdb


url = URL('MySQLdb, username={}, password={}, host=localhost, port=3306,\
        database={}'.format(sys.argv[1], sys.argv[2], sys.argv[3]))
v6_engine = create_engine(url)

with Session(v6_engine) as session:
    for state_obj in session.query(State).order_by(State.id):
        print("{}: {}".format(state_obj.id, state_obj.name))
