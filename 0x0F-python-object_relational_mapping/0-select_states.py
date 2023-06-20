#!/usr/bin/python3
"""List all states from the database 'hbtn_0e_0_usa'"""
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
            list_states_query = "SELECT * FROM `states`;"

            with connection.cursor() as cursor:
                cursor.execute(list_states_query)
                for id, name in cursor.fetchall():
                    print("({}, \'{}\')".format(id, name))
    except Error as err_msg:
        print(err_msg)
