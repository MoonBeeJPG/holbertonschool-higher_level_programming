#!/usr/bin/python3
""" a script that takes in an argument and displays all values in the states
    table of hbtn_0e_0_usa where name matches the argument """

if __name__ == "__main__":
    import MySQLdb
    import sys

    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    connection = MySQLdb.connect(host='localhost', port=3306,
                                 user=user, passwd=passwd, db=db)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER\
                    BY id ASC".format(sys.argv[4]))
    rows = cursor.fetchall()
    for i in rows:
        print(i)
    connection.close()
