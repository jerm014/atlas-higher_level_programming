#!/usr/bin/python3
"""
SQLAlchemy (task 8)
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
    first_state = session.query(State).order_by(State.id).first()

    # Print the results
    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")

    # Close the session
    session.close()

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    list_states(username, password, db_name)
