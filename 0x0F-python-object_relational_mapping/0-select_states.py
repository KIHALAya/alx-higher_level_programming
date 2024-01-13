#!/usr/bin/python3
import MySQLdb
import sys

"""
0-select_states.py - Script that lists all states from
the database hbtn_0e_0_usa.

Usage: ./0-select_states.py <username> <password> <database>

Arguments:
    <username>: MySQL username
    <password>: MySQL password
    <database>: Database name

Requirements:
    - Your script should use the module MySQLdb (import MySQLdb)
    - Connect to a MySQL server running on localhost at port 3306
    - Results sorted in ascending order by states.id
    - Results displayed as they are in the example below
    - Code should not be executed when imported
"""

if __name__ == "__main__":

    arguments = sys.argv[1:]
    conn = MySQLdb.connect(
        host="localhost",
        user=arguments[0],
        port=3306,
        password=arguments[1],
        db=arguments[2]
    )
    query0 = "USE {}".format(arguments[2])
    query1 = "SELECT id, name FROM states ORDER BY  states.id"
    mycursor = conn.cursor()
    mycursor.execute(query0)
    mycursor.execute(query1)
    rows = mycursor.fetchall()
    for row in rows:
        print(row)
    mycursor.close()
    conn.close()
