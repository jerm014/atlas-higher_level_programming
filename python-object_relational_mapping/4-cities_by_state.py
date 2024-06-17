#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
"""

import sys
import MySQLdb


if __name__ == "__main__":
    # Get command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    # search = sys.argv[4]
    sql = "SELECT cities.id, cities.name, states.name "
    sql += "FROM states INNER JOIN cities ON "
    sql += "cities.state_id = states.id "
    sql += "ORDER BY cities.id"
    # sql += 'WHERE name = %s "

    # Connect to MySQL server
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
