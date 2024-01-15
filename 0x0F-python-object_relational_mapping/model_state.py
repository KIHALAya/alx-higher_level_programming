#!/usr/bin/python3

"""
Module: my_module

Description:
    This module defines a SQLAlchemy model for the 'State' table.
    It includes the 'State' class, which represents
    the structure of the table.

Classes:
    State(Base)
        Represents the 'State' table in the database.

Attributes:
    __tablename__ (str): The name of the table in the database.
    id (Column): Integer column representing the primary key
    with an associated sequence.
    name (Column): String column representing the 'name' field
    with a length of 128 characters.
"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Class: State

    Description:
        Represents the 'State' table in the database.
        It inherits from SQLAlchemy's declarative_base
        and defines the structure of the 'State' table.

    Attributes:
        id (Column): Integer column representing the primary key
        with an associated sequence.
        name (Column): String column representing the 'name' field
        with a length of 128 characters.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
