#!/usr/bin/python3
"""
List all states starting with 'N' from the 'hbtn_0e_0_usa' database.
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
            list_states_with_N_query = """
            SELECT id, name FROM states
            WHERE name LIKE BINARY 'N%';
            """

            with connection.cursor() as cursor:
                cursor.execute(list_states_with_N_query)
                for id, name in cursor.fetchall():
                    print("({}, \'{}\')".format(id, name))
    except Error as err_msg:
        print(err_msg)
