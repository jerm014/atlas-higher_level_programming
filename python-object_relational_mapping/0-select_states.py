#!/usr/bin/python3
"""
SQLPython - Object-relational mapping (Project 2193, Task 0)

Write a script that lists all states from the database hbtn_0e_0_usa:

 * Your script should take 3 arguments: mysql username, mysql password and
   database name (no argument validation needed)
 * You must use the module MySQLdb (import MySQLdb)
 * Your script should connect to a MySQL server running on localhost at
   port 3306
 * Results must be sorted in ascending order by states.id
 * Results must be displayed as they are in the example below
 * Your code should not be executed when imported
"""

import sys
import MySQLdb


if __name__ == "__main__":
    # Get command-line arguments
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=db_name)

    # Create a cursor object
    cursor = db.cursor()

    # Execute the query
    cursor.execute("SELECT * FROM `states` ORDER BY `id`")

    # Fetch all results
    results = cursor.fetchall()

    # Print the results
    for row in results:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
