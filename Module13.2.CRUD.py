# ex_03.py
import sqlite3

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
   except sqlite3.Error as e:
       print(e)
   return conn

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

def add_zadanie(conn, zadanie):
   """
   Create a new zadanie into the tasks table
   :param conn:
   :param zadanie:
   :return: zadanie id
   """
   sql = '''INSERT INTO tasks(projekt_id, nazwa, opis, status, start_date, end_date)
             VALUES(?,?,?,?,?,?)'''
   cur = conn.cursor()
   cur.execute(sql, zadanie)
   conn.commit()
   return cur.lastrowid

def select_all(conn, table):
   """
   Query all rows in the table
   :param conn: the Connection object
   :return:
   """
   cur = conn.cursor()
   cur.execute(f"SELECT * FROM {table}")

   rows = cur.fetchall()

   return rows

def select_where(conn, table, **query):
   """
   Query tasks from table with data from **query dict
   :param conn: the Connection object
   :param table: table name
   :param query: dict of attributes and values
   :return:
   """
   cur = conn.cursor()
   qs = []
   values = ()
   for k, v in query.items():
       qs.append(f"{k}=?")
       values += (v,)
   q = " AND ".join(qs)
   cur.execute(f"SELECT * FROM {table} WHERE {q}", values)
   rows = cur.fetchall()
   return rows

def update(conn, table, id, **kwargs):
   """
   update status, begin_date, and end date of a task
   :param conn:
   :param table: table name
   :param id: row id
   :return:
   """
   conn = 1
   parameters = [f"{k} = ?" for k in kwargs]
   parameters = ", ".join(parameters)
   values = tuple(v for v in kwargs.values())
   values += (id, )

   print(parameters)
   print(values)




if __name__ == "__main__":   

   #conn = create_connection("ToDoDB.db")
   #add project
   #projekt = ("Powtórka z angielskiego", "2020-05-11 00:00:00", "2020-05-13 00:00:00")
   #pr_id = add_projekt(conn, projekt)
   
   # add task
   '''zadanie = (
       pr_id,
       "Czasowniki regularne",
       "Zapamiętaj czasowniki ze strony 35",
       "started",
       "2020-05-11 12:00:00",
       "2020-05-11 15:00:00"
   )'''

   #zadanie_id = add_zadanie(conn, zadanie)
   #print(pr_id, zadanie_id)
   #conn.commit()

   # select all records
   #result = select_all(conn, "tasks")
   #print(result)
   #conn.commit()

   # select record with clause where
   #results = select_where(conn,"tasks",status="started")
   #print(results)
   #conn.commit()

   # update record by id
   update(conn, "tasks",2, status="ended", opis="zapamiętaj czasowniki ze strony 20")
   #conn.close
   

   #delete record by id
   #delete_where(conn, "tasks", id=3)

   # delete all records
   #delete_all(conn, "tasks")
   print(conn.total_changes)