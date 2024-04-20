#!/usr/bin/python3
""" list cities by state """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)
    cursor = db.cursor()
    qr = """SELECT cities.id, cities.name, states.name FROM
            cities INNER JOIN states on cities.state_id = states.id """
    cursor.execute(qr)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
