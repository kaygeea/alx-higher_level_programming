#!/usr/bin/python3
"""
This module changes the name of a State object from the database,
'hbtn_0e_6_usa', based on a given condition.
"""
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


if __name__ == "__main__":
    url = URL.create('mysql+mysqldb', username=argv[1], password=argv[2],
                     host='localhost', port=3306, database=argv[3])
    v12_engine = create_engine(url)
    Session = sessionmaker(v12_engine)

    with Session.begin() as session:
        new_name = session.query(State).filter_by(id=2).first()
        new_name.name = 'New Mexico'
