#!/usr/bin/python3

"""
1-filter_states.py - Script that lists all states
with a name starting with 'N'(upper N) from the database hbtn_0e_0_usa.

Usage: ./1-filter_states.py <username> <password> <database>

Arguments:
    <username>: MySQL username
    <password>: MySQL password
    <database>: Database name

Requirements:
    - Your script should use the module MySQLdb (import MySQLdb)
    - Connect to a MySQL server running on localhost at port 3306
    - Results must be filtered to include only states
    with names starting with 'N'
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
               WHERE name like BINARY 'N%'
               ORDER BY id"""
    mycursor = conn.cursor()
    mycursor.execute(query)
    rows = mycursor.fetchall()
    for row in rows:
        print(row)
    mycursor.close()
    conn.close()
