# sqlalchemy_ex_02.py
from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy import create_engine

engine = create_engine('sqlite:///database.db', echo=True)

meta = MetaData()

students = Table(
   'students', meta,
   Column('id', Integer, primary_key=True),
   Column('name', String),
   Column('lastname', String),
)
# add records into db
'''meta.create_all(engine)
ins = students.insert().values(name='Eric', lastname='Idle')
conn = engine.connect()
result = conn.execute(ins)
conn.execute(ins, [
   {'name': 'John', 'lastname': 'Cleese'},
   {'name': 'Graham', 'lastname': 'Chapman'},
])
conn.close()'''
#print(engine.table_names())

# select records from db
conn = engine.connect()
s = students.select().where(students.c.id > 2)
result = conn.execute(s)

for row in result:
   print(row)