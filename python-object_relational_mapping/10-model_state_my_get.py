#!/usr/bin/python3
"""
SQLPython - Object-relational mapping (Project 2193, Task 10)

Write a script that prints the State object with the name passed as argument
from the database hbtn_0e_6_usa

 * Your script should take 4 arguments: mysql username, mysql password,
   database name and state name to search (SQL injection free)
 * You must use the module SQLAlchemy
 * You must import State and Base from model_state
   from model_state import Base, State
 * Your script should connect to a MySQL server running on localhost at
   port 3306
 * You can assume you have one record with the state name to search
 * Results must display the states.id
 * If no state has the name you searched for, display Not found
 * Your code should not be executed when imported
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def print_states(username, password, db_name, search):
    # Create a database connection
    connection = "mysql://{}:{}@localhost:3306/{}"
    engine = create_engine(connection.format(username, password, db_name))
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all State objects and sort by id
    states = session.query(State).order_by(State.id).\
        filter(State.name == search).all()

    # Print the results
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()


if __name__ == "__main__":
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    search = sys.argv[4]
    print_states(username, password, db_name, search)
