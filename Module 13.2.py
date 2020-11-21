# `ex_01_conection_to_db.py`

import sqlite3
from sqlite3 import Error

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

def execute_sql(conn, sql):
   """ Execute sql
   :param conn: Connection object
   :param sql: a SQL script
   :return:
   """
   try:
       c = conn.cursor()
       c.execute(sql)
   except Error as e:
       print(e)

def add_projekt(conn, projekt):
   """
   Create a new projekt into the projects table
   :param conn:
   :param projekt:
   :return: projekt id
   """
   sql = '''INSERT INTO projects(nazwa, start_date, end_date)
             VALUES(?,?,?)'''
   cur = conn.cursor()
   cur.execute(sql, projekt)
   conn.commit()
   return cur.lastrowid


if __name__ == "__main__":

   create_projects_sql = """
   -- projects table
   CREATE TABLE IF NOT EXISTS projects (
      id integer PRIMARY KEY,
      nazwa text NOT NULL,
      start_date text,
      end_date text
   );
   
   """

   create_tasks_sql = """
   -- zadanie table
   CREATE TABLE IF NOT EXISTS tasks (
      id integer PRIMARY KEY,
      projekt_id integer NOT NULL,
      nazwa VARCHAR(250) NOT NULL,
      opis TEXT,
      status VARCHAR(15) NOT NULL,
      start_date text NOT NULL,
      end_date text NOT NULL,
      FOREIGN KEY (projekt_id) REFERENCES projects (id)
   );
   """

   add_project_1 = """
   -- insert into table projects
   INSERT INTO projects(id, nazwa, start_date, end_date)
   VALUES (1,
           "Zrób zadania",
           "2020-05-08 00:00:00",
           "2020-05-10 00:00:00"
    );
    """

   add_project_2 = """
   -- insert into table projects
   INSERT INTO projects(nazwa, start_date, end_date)
   VALUES ( "Zrób zadania 2",
           "2020-05-08 00:00:00",
           "2020-05-10 00:00:00"
    );
    """

   db_file = "database.db"

   conn = create_connection(db_file)
   projekt = ("Powtórka z angielskiego", "2020-05-11 00:00:00", "2020-05-13 00:00:00")
   pr_id = add_projekt(conn, projekt)
   
   if conn is not None:
       #execute_sql(conn, create_projects_sql)
       #execute_sql(conn, add_project_1)
       #execute_sql(conn, add_project_2)
       #execute_sql(conn, create_tasks_sql)
       pr_id
       conn.close()


       