#!/usr/bin/python3
"""
This module prints all City objs from the database 'hbtn_0e_14_usa',
using SQLAlchemy.
"""
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import City
from sys import argv


if __name__ == "__main__":
    url = URL.create('mysql+mysqldb', username=argv[1], password=argv[2],
                     host='localhost', port=3306, database=argv[3])
    v6_engine = create_engine(url)

    with Session(v6_engine) as session:
        for state, city in session.query(State, City).\
                filter(City.state_id == State.id).order_by(City.id).all():
            print("{}: ({}) {}".format(state.name, city.id, city.name))
