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
    match = sys.argv[4]
    qr = """SELECT cities.name FROM
            cities WHERE cities.state_id = (SELECT id FROM states WHERE name = %s)"""
    cursor.execute(qr, (match, ))
    rows = cursor.fetchall()
    print(", ".join([row[0] for row in rows]))
    cursor.close()
    db.close()
