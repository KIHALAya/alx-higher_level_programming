#!/usr/bin/python3

"""
11-model_state_insert.py - Script that adds the State object
"Louisiana" to the database hbtn_0e_6_usa.

Usage: ./11-model_state_insert.py <username> <password> <database>

Arguments:
    <username>: MySQL username
    <password>: MySQL password
    <database>: Database name

Requirements:
    - Your script should use the module SQLAlchemy
    - Import State and Base from model_state
    (from model_state import Base, State)
    - Connect to a MySQL server running on localhost at port 3306
    - Print the new states.id after creation
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

    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()
    print(new_state.id)
    session.close()
