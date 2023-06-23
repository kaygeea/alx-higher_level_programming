#!/usr/bin/python3
"""
This module prints State objs from the database "hbtn_0e_6_usa", whose name
matches the name passed as command-line argument, using SQLAlchemy.
"""
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import Session
from model_state import Base, State
from sys import argv


url = URL.create('mysql+mysqldb', username=argv[1], password=argv[2],
                 host='localhost', port=3306, database=argv[3])
v8_engine = create_engine(url)

with Session(v8_engine) as session:
    cl_name_state_obj = session.query(State).filter(State.name == argv[4]).\
            first()

    if not cl_name_state_obj:
        print("Not found")
    else:
        print("{}".format(cl_name_state_obj.id))
