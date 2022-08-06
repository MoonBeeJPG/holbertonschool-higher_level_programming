#!/usr/bin/python3
""" Script that lists all states from the database hbtn_0e_0_usa """

if __name__ == "__main__":
    import MySQLdb
    import sys

    connection = MySQLdb.connect(host='localhost', port=3306,
        user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()
    for i in rows:
        print(i)
    connection.close()
