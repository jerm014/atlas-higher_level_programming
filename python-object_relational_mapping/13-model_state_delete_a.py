#!/usr/bin/python3
"""
SQLPython - Object-relational mapping (Project 2193, Task 13)

Write a script that deletes all State objects with a name containing the letter
'a' from the database hbtn_0e_6_usa

 * Your script should take 3 arguments: mysql username, mysql password and
   database name
 * You must use the module SQLAlchemy
 * You must import State and Base from model_state
   from model_state import Base, State
 * Your script should connect to a MySQL server running on localhost at
   port 3306
 * Your code should not be executed when imported
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def list_states(username, password, db_name, search):
    # Create a database connection
    connection = "mysql://{}:{}@localhost:3306/{}"
    engine = create_engine(conection.format(username, password, db_name))
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the State with name like a
    states = session.query(State).filter(State.name.like('%a%')).all()

    # Delete the states with name like a
    for state in states:
        session.delete(state)

    # Close the session
    session.close()


if __name__ == "__main__":
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    list_states(username, password, db_name, search)
