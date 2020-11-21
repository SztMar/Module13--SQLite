import json
import sqlite3
from sqlite3 import Error

class Todos:
    def __init__(self):
        db_file = "ToDoDB.db"
        self.conn = self.create_connection(db_file)
        cur = self.conn.cursor()
        db = cur.execute("SELECT * FROM tasks")
        db_result = []
        for row in db:
            Key, title, description, status = row
            db_result.append({"Key":Key, "title":title, "description":description, "status": status})

        self.todos = db_result
        
        

    def create_connection(self,db_file):
        conn = None

        try:
            conn =sqlite3.connect(db_file)
            return conn
        except sqlite3.Error as e:
            print(Error)
        return conn
    
    def select_all(self):
        return self.todos
    
    def add_record(self, record):
        db_record = []
        record.pop('csrf_token')
        for k, v in record.items():
            db_record.append(v)
        
        self.added = tuple(db_record)
        db_file = "ToDoDB.db"
        sql = f"INSERT INTO tasks (title, description, status) VALUES(?,?,?)"
        self.conn = self.create_connection(db_file)
        cur = self.conn.cursor()
        cur.execute(sql,self.added)
        self.conn.commit()
        
        
    
    def get_key(self,Key):
        return self.todos[Key]
    
    def update_record(self, Key, record):
        db_keys = []
        db_values = []        
        record.pop('csrf_token')    

        for k, v in record.items():
            db_keys.append(f'{k} = ?')
            db_values.append(v)

        db_values.append(Key + 1)
        db_keys = ", ".join(db_keys)               
        self.keys = db_keys
        self.values = tuple(db_values)       
        
        db_file = "ToDoDB.db"
        sql = f"UPDATE tasks SET {self.keys} WHERE Key = ?"
        self.conn = self.create_connection(db_file)
        cur = self.conn.cursor()
        cur.execute(sql,self.values)
        self.conn.commit()
    
    def delete_record(self, Key, record):
        db_keys = []
        db_values = []        
        record.pop('csrf_token')

        for k, v in record.items():
            db_keys.append(f'{k} = ?')
            db_values.append(v) 
        
        db_keys = " AND ".join(db_keys)
        self.keys = db_keys
        self.values = tuple(db_values)
        db_file = "ToDoDB.db"
        sql = f'DELETE FROM tasks WHERE {self.keys}'
        self.conn = self.create_connection(db_file)
        cur = self.conn.cursor()
        cur.execute(sql,self.values)
        self.conn.commit()
        
        
        

todos = Todos()
