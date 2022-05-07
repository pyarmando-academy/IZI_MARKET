import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn


def consulta_productos(conn, producto):
    products = ""
    my_data = ('%' + producto + '%',)
    q = "select articulo,precio from articulos where  articulo like ?"
    try:
        my_cursor = conn.execute(q, my_data)
        rows = my_cursor.fetchall()
        for row in rows:
            products += str(row) + "\n"
    except sqlite3.Error as my_error:
        print("error: ", my_error)
    return products


def oferta_productos(conn, cant):
    products = ""
    my_data = (cant,)
    q = "select articulo,precio from articulos where precio<= ?"
    try:
        my_cursor = conn.execute(q, my_data)
        rows = my_cursor.fetchall()
        for row in rows:
            products += str(row) + "\n"
    except sqlite3.Error as my_error:
        print("error: ", my_error)
    return products

# conn=create_connection('dbizimarket.db')
# print(oferta_productos(conn,1))
