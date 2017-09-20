# create a SQLite3 database and table

# import the libraries
import sqlite3
import csv

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    # open csv
    employees = csv.reader(open("employees.csv", "rU"))

    # create table
    c.execute("CREATE TABLE employees (firstname TEXT, lastname TEXT)")

    # insert data into table
    c.executemany("INSERT INTO employees(firstname, lastname) values (?,?)", employees)
