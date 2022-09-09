#!/usr/bin/python3
"""
This module runs a script to update the name
of a row from the states table
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

    get_new_state = session.query(State).filter_by(id=2).first()
    get_new_state.name = 'New Mexico'
    session.add(get_new_state)
    session.commit()
    session.close()
