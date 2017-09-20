## import libraries
import sqlite3

## create the connection object
conn = sqlite3.connect("newnum.db")

## create a cursor object to execute sqlite3
cursor = conn.cursor()

prompt = """
Select the operation you'd like to perform
1 - Average
2 - Max
3 - Min
4 - Sum
5 - Exit
"""

## while loop to obtain command from user
while True:
    ### get user input
    x = raw_input(prompt)

    ### if user selected a valid option, do it
    if x in set(["1","2","3","4"]):

        #### write operation
        operation = {1: "avg", 2: "max", 3: "min", 4:"sum"}[int(x)]

        #### query database
        cursor.execute("SELECT {}(num) from numbers".format(operation))

        #### fetch data
        get = cursor.fetchone()

        #### print results
        print operation + ": %f" % get[0]

    ### if user selected to exit via 5
    elif x == "5":
        print "Exit"
        break
