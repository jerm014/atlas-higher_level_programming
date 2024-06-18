#!/usr/bin/python3
"""
SQLPython - Object-relational mapping (Project 2193, Task 4)

Write a script that lists all cities from the database hbtn_0e_4_usa

 * Your script should take 3 arguments: mysql username, mysql password and
   database name
 * You must use the module MySQLdb (import MySQLdb)
 * Your script should connect to a MySQL server running on localhost at
   port 3306
 * Results must be sorted in ascending order by cities.id
 * You can use only execute() once
 * Results must be displayed as they are in the example below
 * Your code should not be executed when imported
"""

import sys
import MySQLdb


if __name__ == "__main__":
    # Get command-line arguments
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # search = sys.argv[4]
    sql = "SELECT `cities`.`id`, `cities`.`name`, `states`.`name` "
    sql += "FROM `states` INNER JOIN `cities` "
    sql += "ON `cities`.`state_id` = `states`.`id` "
    sql += "ORDER BY `cities`.`id`"

    # Connect to MySQL
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=db_name)

    # Create a cursor object
    cursor = db.cursor()

    # Execute the query
    cursor.execute(sql)

    # Fetch all results
    results = cursor.fetchall()

    # Print the results
    for row in results:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
