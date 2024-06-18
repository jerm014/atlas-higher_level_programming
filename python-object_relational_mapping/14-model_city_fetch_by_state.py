#!/usr/bin/python3
"""
SQLPython - Object-relational mapping (Project 2193, Task 14)

Write a Python file similar to model_state.py named model_city.py that contains
the class definition of a City.

 * City class:
   * inherits from Base (imported from model_state)
   * links to the MySQL table cities
   * class attribute id that represents a column of an auto-generated, unique
     integer, can’t be null and is a primary key
   * class attribute name that represents a column of a string of 128
     characters and can’t be null
   * class attribute state_id that represents a column of an integer, can’t be
     null and is a foreign key to states.id
 * You must use the module SQLAlchemy

Next, write a script 14-model_city_fetch_by_state.py that prints all City
objects from the database hbtn_0e_14_usa:

 * Your script should take 3 arguments: mysql username, mysql password and
   database name
 * You must use the module SQLAlchemy
 * You must import State and Base from model_state
   from model_state import Base, State
 * Your script should connect to a MySQL server running on localhost at
   port 3306
 * Results must be sorted in ascending order by cities.id
 * Results must be display as they are in the example below
   (<state name>: (<city id>) <city name>)
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

    # Query the State with id = 2
    state_to_update = session.query(State).filter_by(id=2).first()

    if state_to_update:
        # Change the name to "New Mexico"
        state_to_update.name = "New Mexico"
        session.commit()
    else:
        print("State with ID 2 not found.")

    # Close the session
    session.close()

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    list_states(username, password, db_name, search)
