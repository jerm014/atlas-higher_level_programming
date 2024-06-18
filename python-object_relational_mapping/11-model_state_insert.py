#!/usr/bin/python3
"""
SQLPython - Object-relational mapping (Project 2193, Task 11)

Write a script that adds the State object “Louisiana” to the database hbtn_0e_6_usa

 * Your script should take 3 arguments: mysql username, mysql password and
   database name
 * You must use the module SQLAlchemy
 * You must import State and Base from model_state
   from model_state import Base, State
 * Your script should connect to a MySQL server running on localhost at
   port 3306
 * Print the new states.id after creation
 * Your code should not be executed when imported
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def list_states(username, password, db_name, search):
    # Create a database connection
    engine = create_engine(f"mysql://{username}:{password}@localhost:3306/{db_name}")
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create the Louisiana State object
    louisiana = State(name="Louisiana")
    session.add(louisiana)
    session.commit()

    # Print the new states.id
    print(f"{louisiana.id}")

    # Close the session
    session.close()

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    list_states(username, password, db_name, search)
