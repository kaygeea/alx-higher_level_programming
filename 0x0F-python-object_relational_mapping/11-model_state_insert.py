#!/usr/bin/python3
"""This module adds a new State obj, 'Louisiana', to the hbtn_0e_6_usa DB"""
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


if __name__ == "__main__":
    url = URL.create('mysql+mysqldb', username=argv[1], password=argv[2],
                     host='localhost', port=3306, database=argv[3])
    v10_engine = create_engine(url)
    Session = sessionmaker(v10_engine)

    with Session.begin() as session:
        # .begin() runs a context manager which auto-commits & closes session.
        new_state = State(name="Louisiana")
        session.add(new_state)

        new_state_obj = session.query(State).filter(State.name == 'Louisiana')\
            .first()
        print('{}'.format(new_state_obj.id))
