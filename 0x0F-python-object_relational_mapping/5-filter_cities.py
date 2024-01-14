#!/usr/bin/python3

"""
5-filter_cities.py - Script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa.

Usage: ./5-filter_cities.py <username> <password> <database> <state_name>

Arguments:
    <username>: MySQL username
    <password>: MySQL password
    <database>: Database name
    <state_name>: Name of the state to filter cities by

Requirements:
    - Your script should use the module MySQLdb (import MySQLdb)
    - Connect to a MySQL server running on localhost at port 3306
    - Results must be sorted in ascending order by cities.id
    - Use only execute() once
    - The results must be displayed as they are in the example below
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
    query = """SELECT cities.name
               FROM cities  JOIN states
               ON cities.state_id = states.id
               WHERE states.name = '{}'
               ORDER BY cities.id""".format(str(arguments[3]))

    mycursor = conn.cursor()
    mycursor.execute(query)
    rows = mycursor.fetchall()
    cities = [row[0] for row in rows]
    print(', '.join(cities))
    mycursor.close()
    conn.close()
