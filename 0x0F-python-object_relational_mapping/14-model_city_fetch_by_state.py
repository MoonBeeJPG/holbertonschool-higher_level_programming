#!/usr/bin/python3
""" Prints all City objects from the database hbtn_0e_14_usa """

if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from model_city import City
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           user, passwd, db), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    ss = Session()
    for i, j in ss.query(City, State).filter(City.state_id == State.id):
        print("{}: ({}) {}".format(j.name, i.id, i.name))
