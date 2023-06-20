#!/usr/bin/python3
"""
List all states from the database 'hbtn_0e_0_usa'
SPECS:
    a. The script takes 3 args: mysql username, mysql password & database name
    b. Connect to a MySQL server running on localhost at port 3306
    c. Results must be sorted in ascending order by states.id

CONSTRAINTS:
    a. The module 'MySQLdb' must be used.
    b. The code should not be executed when imported.
"""
from mysql.connector import connect, Error
import sys
import MySQLdb


if __name__ == "__main__":
    try:
        with MySQLdb.connect(
                host='localhost',
                user=sys.argv[1],
                port=3306,
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
