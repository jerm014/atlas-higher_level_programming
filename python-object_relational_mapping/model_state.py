#!/usr/bin/python3
"""
SQLAlchemy (task 6)
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class State(Base):
    __tablename__ = 'states'  # Link to the MySQL table 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
