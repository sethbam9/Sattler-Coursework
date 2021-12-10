import sqlite3
from sqlite3 import Error

db = r"C:\Users\sethb\OneDrive\Desktop\Sattler College\5. Fall 2020\CS 202 Object-Oriented Design\bible-sqlite.db"

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM bible_version_key")

    rows = cur.fetchall()

    for row in rows:
        print(row)


def select_task_by_priority(conn, a, b):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM bible_version_key WHERE %s = %s" % (a, b))

    rows = cur.fetchall()

    for row in rows:
        print(row)
        for item in row:
            print (item)


def main():
    database = db

    # create a database connection
    conn = create_connection(database)
    with conn:
        print("1. Query task by priority:")
        select_task_by_priority(conn, "id", 6)

        print("2. Query all tasks")
        select_all_tasks(conn)

#
# if __name__ == '__main__':
#     main()

def main_program():
    tmp_array = [69, 32, 116, 110, 101, 108, 108, 101, 99, 120, 69]
    counter = len(tmp_array) - 1
    foo(tmp_array, counter)

def foo(a_data_array, a_counter):
    if a_counter >= 1:
        print(chr(a_data_array[a_counter]))
        foo(a_data_array, a_counter - 1)
    elif a_counter <= 0:
        print("45A!")

main_program()
