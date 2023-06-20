#!/usr/bin/python3
"""
This module lists all states LIKE passed argument
from the database 'hbtn_0e_0_usa'; it is also safe from MySQL injections.
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
            injection_safe_query = """
            SELECT id, name FROM states
            WHERE name = BINARY %s
            """

            with connection.cursor() as cursor:
                cursor.execute(injection_safe_query, (sys.argv[4],))
                for id, name in cursor.fetchall():
                    print("({}, \'{}\')".format(id, name))
    except Error as err_msg:
        print(err_msg)
