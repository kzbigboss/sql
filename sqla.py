# create a SQLite3 database and table

# import the sqlite3 library
import sqlite3

# create database if doesn't exist
conn = sqlite3.connect("new.db")

# create cursor
cursor = conn.cursor()

#create table
cursor.execute("""CREATE TABLE population
(city TEXT, state TEXT, population INT)
""")

#close connection
conn.close()
