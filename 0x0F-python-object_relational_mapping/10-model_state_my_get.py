#!/usr/bin/python3

"""
10-model_state_my_get.py - Script that prints the State object with
the name passed as an argument from the database hbtn_0e_6_usa.

Usage: ./10-model_state_my_get.py <username> <password> <database> <state_name>

Arguments:
    <username>: MySQL username
    <password>: MySQL password
    <database>: Database name
    <state_name>: State name to search for (SQL injection free)

Requirements:
    - Your script should use the module SQLAlchemy
    - Import State and Base from model_state
    (from model_state import Base, State)
    - Connect to a MySQL server running on localhost at port 3306
    - You can assume you have one record with the state name to search
    - Results must display the states.id
    - If no state has the name you searched for, display "Not found"
    - Code should not be executed when imported
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
import sys

if __name__ == '__main__':
    username, password, db, search = sys.argv[1:]
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                username, password, db),
            pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        result = session.query(State).filter(State.name == str(search)).first()
        if result:
            print(result.id)
        else:
            print("Not found")
    except NoResultFound:
        print("Not found")
    session.close()
