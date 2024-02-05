# ------------------------------
# 6. Database
# ------------------------------
# Description:
# This script contains the database
# connection and query functions.
# ------------------------------
# cursor : is a control structure used to traverse and fetch the records of the database.
# commit : is used to save the changes in the database.

# import libraries
import sqlite3

# create database and connect
db = sqlite3.connect('database.db')

# create cursor
cursor = db.cursor()

# create table and fields
# usage: cursor.execute("create table if not exists table_name (field1 type, field2 type)")
cursor.execute("create table if not exists users (user_id integer, name text)")
cursor.execute(
"create table if not exists skills (name text, progress integer, user_id integer)"
)

# insert data
# usage: cursor.execute("insert into table_name (field1, field2) values (value1, value2)")
# cursor.execute("insert into users (user_id, name) values (1, 'John')")
# cursor.execute("insert into users (user_id, name) values (2, 'Jane')")
# cursor.execute("insert into skills (name, progress, user_id) values ('Python', 75, 1)")
# cursor.execute("insert into skills (name, progress, user_id) values ('Python', 50, 2)")
# cursor.execute("insert into skills (name, progress, user_id) values ('Java', 25, 1)")
# cursor.execute("insert into skills (name, progress, user_id) values ('Java', 100, 2)")

list_of_users = ["John", "Jane", "Doe", "Smith", "Brown", "Harris", "Taylor", "Clark", "Lewis", "Lee"]
for key, user in enumerate(list_of_users):
	cursor.execute(f"insert into users (user_id, name) values ({key+1}, '{user}')")

list_of_skills = ["Python", "Java", "C++", "C#", "Ruby", "PHP", "JavaScript", "HTML", "CSS", "SQL"]


for key, skill in enumerate(list_of_skills):
	cursor.execute(f"insert into skills (name, progress, user_id) values ('{skill}', {key*10+5}, {key%10+1})")


# fetch data
# usage: cursor.execute("select * from table_name")
cursor.execute("select * from users")
print(cursor.fetchmany(2),"\n")
print(cursor.fetchall(),"\n")
cursor.execute("select * from skills")
print(cursor.fetchone())


# commit changes
db.commit()

# close database
db.close()