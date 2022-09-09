#!/usr/bin/python3
"""
This module runs a script to get the state.id belonging
to the state name provided
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state_id = session.query(State.id).filter_by(name=argv[4]).first()
    if state_id is None:
        print("Not found")
    else:
        print(state_id[0])
    session.close()
