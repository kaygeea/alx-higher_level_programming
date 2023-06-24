#!/usr/bin/python3
"""
This module takes in the name of a state as an argument and
lists all cities of that state, all from the database hbtn_0e_4_usa.
"""
from mysql.connector import connect, Error
import sys
import MySQLdb


if __name__ == "__main__":
    try:
        with MySQLdb.connect(
                user=sys.argv[1],
                passwd=sys.argv[2],
                db=sys.argv[3]
                ) as connection:
            list_cities_by_state_query = """
            SELECT cities.name
              FROM cities
                   INNER JOIN states
                   ON cities.state_id = states.id
                   WHERE states.name = %s
             ORDER BY cities.id;
            """

            with connection.cursor() as cursor:
                cursor.execute(list_cities_by_state_query, (sys.argv[4],))
                city = cursor.fetchall()
                print(', '.join([name[0] for name in city]))
    except Error as err_msg:
        print(err_msg)
