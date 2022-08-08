#!/usr/bin/python3
""" Script that prints the State object with the name passed as argument from
    the database hbtn_0e_6_usa """

if __name__ == "__main__":
    import sys
    from model_state import Base, State
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
    fil = ss.query(State).filter(State.name == sys.argv[4])
    if len(fil.all()) == 0:
        print('Not found')
    else:
        for i in fil:
            print(i.id)
