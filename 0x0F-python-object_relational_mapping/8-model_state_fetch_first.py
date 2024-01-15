#!/usr/bin/python3

"""
8-model_state_fetch_first.py - Script that prints the first State
object from the database hbtn_0e_6_usa.

Usage: ./8-model_state_fetch_first.py <username> <password> <database>

Arguments:
    <username>: MySQL username
    <password>: MySQL password
    <database>: Database name

Requirements:
    - Your script should use the module SQLAlchemy
    - Import State and Base from model_state
    (from model_state import Base, State)
    - Connect to a MySQL server running on localhost at port 3306
    - The state you display must be the first in states.id
    - You are not allowed to fetch all states from
    the database before displaying the result
    - If the table states is empty, print "Nothing" followed by a new line
    - Code should not be executed when imported
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
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
    first_element = session.query(State).filter_by(id=1)
    try:
        first_element = session.query(State).order_by(State.id).first()
        if first_element:
            print("{}: {}".format(first_element.id, first_element.name))
        else:
            print("Nothing")
    except NoResultFound:
        print("Nothing")
    session.close()
