#!/usr/bin/python3
""" Script that takes in the name of a state as an argument and lists all
    cities of that state, using the database hbtn_0e_4_usa """
if __name__ == "__main__":
    import MySQLdb
    import sys

    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    connection = MySQLdb.connect(host='localhost', port=3306,
                                 user=user, passwd=passwd, db=db)
    cursor = connection.cursor()
    cursor.execute("SELECT cities.name FROM cities JOIN states ON\
                   states.id = cities.state_id WHERE states.name = %s\
                   ORDER BY cities.id", (sys.argv[4],))
    rows = cursor.fetchall()
    print(", ".join(i[0] for i in rows))
    connection.close()
