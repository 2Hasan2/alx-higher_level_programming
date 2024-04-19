#!/usr/bin/env python3
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker,  declarative_base
from os import getenv

# Create an engine to connect to the database
engine = create_engine(
    f"mysql+mysqldb://{getenv('HBNB_MYSQL_USER')}:{getenv('HBNB_MYSQL_PWD')}@localhost:{getenv('HBNB_MYSQL_HOST')}/{getenv('HBNB_MYSQL_DB')}",
    pool_pre_ping=True
)

# Define the User table
Base = declarative_base()

# Create a sessionmaker bound to the engine
Session = sessionmaker(bind=engine)

# Create a session
session = Session()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    age = Column(Integer)


# Create the table in the database
Base.metadata.create_all(engine)

# Create a new user object
new_user = User(name='John', age=30)

# Add the new user to the session
session.add(new_user)

# Commit the session to persist the changes to the database
session.commit()

# Query the database to retrieve the user
user = session.query(User).filter_by(name='John').first()
# Print the user
print(user)

# Close the session
session.close()