#!/usr/bin/python3
"""Write a script that prints the State object with the name"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    eng = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=eng)
    season = Session()

    fnd = False
    for state in season.query(State):
        if state.name == sys.argv[4]:
            print("{}".format(state.id))
            fnd = True
            break
    if fnd is False:
        print("Not found")
