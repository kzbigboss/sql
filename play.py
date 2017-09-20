# SELECT statement

#import sqlite3

#with sqlite3.connect("new.db") as connection:
#    c = connection.cursor()

#    for row in c.execute("SELECT firstname, lastname from employees"):
#        print row

# again, without unicode character (u) in output

#import sqlite3

#with sqlite3.connect("new.db") as connection:
#    c = connection.cursor()

#    c.execute("SELECT firstname, lastname from employees")

#    rows = c.fetchall()

#    for r in rows:
#        print "First Name: " + r[0]

import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    cities = [
    ('Boston', 'MA', 600000),
    ('Los Angeles', 'CA', 38000000),
    ('Houston', 'TX', 2100000),
    ('Philadelphia', 'PA', 1500000),
    ('San Antonio', 'TX', 1400000),
    ('San Diego', 'CA', 130000),
    ('Dallas', 'TX', 1200000),
    ('San Jose', 'CA', 900000),
    ('Jacksonville', 'FL', 800000),
    ('Indianapolis', 'IN', 800000),
    ('Austin', 'TX', 800000), 
