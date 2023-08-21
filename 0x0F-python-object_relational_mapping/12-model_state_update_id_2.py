#!/usr/bin/python3
"""Write a script that changes the name of a State"""
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

    state = season.query(State).filter_by(id=2).first()
    state.name = "New Mexico"
    season.commit()
