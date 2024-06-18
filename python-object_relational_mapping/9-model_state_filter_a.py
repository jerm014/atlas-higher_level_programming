#!/usr/bin/python3
"""
SQLPython - Object-relational mapping (Project 2193, Task 9)

Write a script that lists all State objects that contain the letter a from the
database hbtn_0e_6_usa

 * Your script should take 3 arguments: mysql username, mysql password and
   database name
 * You must use the module SQLAlchemy
 * You must import State and Base from model_state
   from model_state import Base, State
 * Your script should connect to a MySQL server running on localhost at
   port 3306
 * Results must be sorted in ascending order by states.id
 * The results must be displayed as they are in the example below
 * Your code should not be executed when imported
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def list_states(username, password, db_name):
    # Create a database connection
    engine = create_engine(f"mysql://{username}:{password}@localhost:3306/{db_name}")
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all State objects and sort by id
    states = session.query(
                           State
                          ).order_by(
                                     State.id
                                    ).filter(
                                             State.name.like('%a%')
                                            ).all()

    # Print the results
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    list_states(username, password, db_name)
