#!/usr/bin/python3
""" Script that prints the first State object from the database hbtn_0e_6_usa
    """
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
    first = ss.query(State).first()
    if first:
        print("{}: {}".format(first.id, first.name))
    else:
        print('Nothing')
