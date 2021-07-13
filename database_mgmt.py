import sqlite3
from sqlite3 import Error


def restaurant_names():
    conn = None
    try:
        conn = sqlite3.connect('schema.sql')
        curs = conn.cursor()
        curs.execute("INSERT INTO restaurant(rest_name) VALUES('KFC','Halal restaurant')")
        curs.execute("COMMIT")
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def menu_item():
    conn = None
    try:
        conn = sqlite3.connect('schema.sql')
        curs = conn.cursor()
        curs.execute("INSERT INTO menu(item_name) VALUES('chicken fry','chicken gravy')")
        curs.execute("COMMIT")

    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def customer():
    conn = None
    try:
        conn = sqlite3.connect('schema.sql')
        curs = conn.cursor()
        curs.execute("INSERT INTO customer(cust_name) VALUES('paul')")
        curs.execute("COMMIT")

    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
