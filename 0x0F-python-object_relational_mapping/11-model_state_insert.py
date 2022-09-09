#!/usr/bin/python3
"""
This module runs a script to get the first state in the
states table
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

    new_state = State(name="Louisiana")
    session.add(new_state)
    get_new_state = session.query(State)\
        .filter(State.name == "Louisiana").first()
    print(get_new_state.id)
    session.commit()
    session.close()
