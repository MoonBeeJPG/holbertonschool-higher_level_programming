#!/usr/bin/python3
""" Script that lists all cities from the database hbtn_0e_4_usa """
if __name__ == "__main__":
    import MySQLdb
    import sys

    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    connection = MySQLdb.connect(host='localhost', port=3306,
                                 user=user, passwd=passwd, db=db)
    cursor = connection.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities\
                    JOIN states ON states.id=cities.state_id ORDER BY id ASC")
    rows = cursor.fetchall()
    for i in rows:
        print(i)
    connection.close()
