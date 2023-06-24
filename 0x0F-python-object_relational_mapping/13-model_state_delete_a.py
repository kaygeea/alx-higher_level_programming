#!/usr/bin/python3
"""
This module deletes all State objects with 'a' in their names,
from the 'hbtn_0e_6_usa' databasae.
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
        for states_to_del in session.query(State).filter(State.name.
                    like('%a%')):
            session.delete(states_to_del)
