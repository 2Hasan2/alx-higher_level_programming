#!/usr/bin/python3
""" filter states """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)
    cursor = db.cursor()
    match = sys.argv[4]
    qr = """SELECT * FROM states WHERE name LIKE %s"""
    cursor.execute(qr, (match, ))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
