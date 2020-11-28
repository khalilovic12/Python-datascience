import sqlite3
from sqlite3 import Error
import csv

" Create data base SQLite "

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

"Create table in database"
def create_table(conn, create_table_sql):

    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)   
    except Error as e:
        print(e)

#Insert data from code_pays.csv file       

def insert_data_pays(conn, data):
    try:
        c = conn.cursor()
        with open (data,'r') as fin:

            dr = csv.DictReader(fin)
            to_db = [(i['Name'], i['Code']) for i in dr]
        c.executemany('insert into pays values(?,?)', to_db)
    except Error as e:
        print('Error :', e)
    else:
        conn.commit()
        print('data inserted')

def insert_data_jours_feries(conn, i, j):
    try:

        c = conn.cursor()
        c.execute('insert into jours_feries values(?,?)',(i['Name'], j['date']))

    except Error as e:

        print('Error :', e)
    else:

        conn.commit()
        print('data inserted')  