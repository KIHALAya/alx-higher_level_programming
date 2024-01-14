#!/usr/bin/python3

"""
4-cities_by_state.py - Script that lists all cities
from the database hbtn_0e_4_usa.

Usage: ./4-cities_by_state.py <username> <password> <database>

Arguments:
    <username>: MySQL username
    <password>: MySQL password
    <database>: Database name

Requirements:
    - Your script should use the module MySQLdb (import MySQLdb)
    - Connect to a MySQL server running on localhost at port 3306
    - Results must be sorted in ascending order by cities.id
    - Use only execute() once
    - Results must be displayed as they are in the example below
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
    query = """SELECT cities.id, cities.name, states.name
               FROM cities  JOIN states
               ON cities.state_id = states.id
               ORDER BY cities.id"""

    mycursor = conn.cursor()
    mycursor.execute(query)
    rows = mycursor.fetchall()
    for row in rows:
        print(row)
    mycursor.close()
    conn.close()
