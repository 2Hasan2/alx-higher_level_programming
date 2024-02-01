# ------------------------------
# 6. Database
# ------------------------------
# Description:
# This script contains the database
# connection and query functions.
# ------------------------------

# import libraries
import sqlite3

# create database and connect
db = sqlite3.connect('database.db')

# create table and fields
db.execute(
	'CREATE TABLE IF NOT EXISTS skills (NAME TEXT, PROGRESS INT, USER_ID INT)'
	)

# close database
db.close()