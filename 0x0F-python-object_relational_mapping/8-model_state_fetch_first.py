#!/usr/bin/python3
"""
Lists the first State obj from the database "hbtn_0e_6_usa" using SQLAlchemy.
"""
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import Session
from model_state import Base, State
from sys import argv


if __name__ == "__main__":
    url = URL.create('mysql+mysqldb', username=argv[1], password=argv[2],
                     host='localhost', port=3306, database=argv[3])
    v6_engine = create_engine(url)

    with Session(v6_engine) as session:
        first_state_obj = session.query(State).first()

    if first_state_obj is None:
        print("Nothing")
    else:
        print("{}: {}".format(first_state_obj.id, first_state_obj.name))
