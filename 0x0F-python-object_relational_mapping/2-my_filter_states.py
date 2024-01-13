#!/usr/bin/python3

"""
2-my_filter_states.py - Script that takes in an argument and displays all
values in the states table of hbtn_0e_0_usa where name matches the argument.

Usage: ./2-my_filter_states.py <username> <password> <database> <state_name>

Arguments:
    <username>: MySQL username
    <password>: MySQL password
    <database>: Database name
    <state_name>: Name of the state to search for in the states table

Requirements:
    - Your script should use the module MySQLdb (import MySQLdb)
    - Connect to a MySQL server running on localhost at port 3306
    - Use format to create the SQL query with the user input
    - Results must be filtered based on the provided state_name
    - Results sorted in ascending order by states.id
    - Results displayed as they are in the example below
    - Code should not be executed when imported
"""

import MySQLdb
import sys


if __name__ == "__main__":
    arguments = sys.argv[1:]

    conn = MySQLdb.connect(
        host="localhost",
        user=arguments[0],
        port=3306,
        password=arguments[1],
        db=arguments[2]
    )

    query = """SELECT *
               FROM states
               WHERE name LIKE BINARY '{}'
               ORDER BY id""".format(arguments[3])
    mycursor = conn.cursor()
    mycursor.execute(query)
    rows = mycursor.fetchall()
    for row in rows:
        print(row)
    mycursor.close()
    conn.close()
