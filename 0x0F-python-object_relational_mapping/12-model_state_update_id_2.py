#!/usr/bin/python3

"""
12-model_state_update_id_2.py - Script that changes the name of a
State object from the database hbtn_0e_6_usa.

Usage: ./12-model_state_update_id_2.py <username> <password> <database>

Arguments:
    <username>: MySQL username
    <password>: MySQL password
    <database>: Database name

Requirements:
    - Your script should use the module SQLAlchemy
    - Import State and Base from model_state
    (from model_state import Base, State)
    - Connect to a MySQL server running on localhost at port 3306
    - Change the name of the State where id = 2 to "New Mexico"
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

    state_update = session.query(State).filter_by(id=2).one()
    try:
        state_update.name = "New Mexico"
        session.commit()
    except NoResultFound:
        print("Error : state not found")

    session.close()
