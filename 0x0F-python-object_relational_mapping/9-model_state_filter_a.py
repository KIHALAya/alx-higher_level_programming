#!/usr/bin/python3

"""
9-model_state_filter_a.py - Script that lists all State objects
that contain the letter 'a' from the database hbtn_0e_6_usa.

Usage: ./9-model_state_filter_a.py <username> <password> <database>

Arguments:
    <username>: MySQL username
    <password>: MySQL password
    <database>: Database name

Requirements:
    - Your script should use the module SQLAlchemy
    - Import State and Base from model_state
    (from model_state import Base, State)
    - Connect to a MySQL server running on localhost at port 3306
    - Results must be sorted in ascending order by states.id
    - The results must be displayed as they are in the example below
    - Code should not be executed when imported
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
import sys

if __name__ == '__main__':
    username, password, db = sys.argv[1:]
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                username, password, db),
            pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).filter(State.name.like('%a%')).all():
        print("{}: {}".format(state.id, state.name))

session.close()
