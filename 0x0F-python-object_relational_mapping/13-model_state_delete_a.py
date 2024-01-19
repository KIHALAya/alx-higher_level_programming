#!/usr/bin/python3

"""
13-model_state_delete_a.py - Script that deletes all State objects
with a name containing the letter 'a' from the database hbtn_0e_6_usa.

Usage: ./13-model_state_delete_a.py <username> <password> <database>

Arguments:
    <username>: MySQL username
    <password>: MySQL password
    <database>: Database name

Requirements:
    - Your script should use the module SQLAlchemy
    - Import State and Base from model_state
    (from model_state import Base, State)
    - Connect to a MySQL server running on localhost at port 3306
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

    states_to_delete = session.query(
            State).filter(State.name.like("%a%")).all()
    try:
        if states_to_delete:
            for each in states_to_delete:
                session.delete(each)
            session.commit()
        else:
            print("No element found")
    except NoResultFound:
        print("Error : state not found")

    session.close()
