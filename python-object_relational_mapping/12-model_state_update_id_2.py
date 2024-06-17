#!/usr/bin/python3
"""
SQLAlchemy (task 12)
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
