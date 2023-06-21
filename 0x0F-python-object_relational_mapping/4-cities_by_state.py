#!/usr/bin/python3
"""
This module lists all cities from the database 'hbtn_0e_4_usa'.
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
            list_cities_query = """
            SELECT cities.id, cities.name, states.name
              FROM cities
                   INNER JOIN states
                   ON cities.state_id = states.id
             ORDER BY cities.id;
            """

            with connection.cursor() as cursor:
                cursor.execute(list_cities_query)
                for id, name, state in cursor.fetchall():
                    print("({}, \'{}\', \'{}\')".format(id, name, state))
    except Error as err_msg:
        print(err_msg)
