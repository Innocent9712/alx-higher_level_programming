#!/usr/bin/python3
"""
This module runs a script to fetch everything from the
cities table with the corresponding state name based
on the ForeignKey for state id from the the states table
"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    get_cities = session.query(State, City)\
        .filter(City.state_id == State.id).order_by(City.id).all()
    for state, city in get_cities:
        # print(city)
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
