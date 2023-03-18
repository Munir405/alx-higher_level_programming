#!/usr/bin/python3
"""
create state "California" with city attribute "San Francisco"
parameters given to script: username, password, database
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City

if __name__ == "__main__":
    '''
    user_name = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    '''
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = State(name='State')
    state.cities = [City(name='San Francisco')]

    session.add(state)
    session.commit()
