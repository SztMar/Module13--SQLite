# app/models.py
from datetime import datetime
from app import db

class Book(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   bookname = db.Column(db.String(100), index=True, unique=True)
   publishment_house = db.Column(db.String(200), index=True)
   details = db.relationship("BookDetails", backref= "bookname", lazy="dynamic")
   storage = db.relationship("Storage", backref= "bookname", lazy="dynamic")

   def __str__(self):
       return f"<Book {self.bookname}>"

class BookDetails(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   main_author = db.Column(db.String(100), index=True)
   sec_author = db.Column(db.String(100), index=True)
   description = db.Column(db.Text)
   publishment_year = db.Column(db.String(10), index=True)
   pages = db.Column(db.String(10), index=True)   
   book_id = db.Column(db.Integer, db.ForeignKey('book.id'))

   def __str__(self):
       return f"<Details {self.id} {self.main_author} {self.sec_author} {self.description[:100]}...>"
    
class Storage(db.Model):
    id = db.Column(db.Integer, primary_key=True)    
    loaned_date = db.Column(db.String(20), index=True)
    returned_date = db.Column(db.String(20), index=True)
    availability = db.Column(db.String(100), index=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))


    def __str__(self):
       return f"<Availability {self.id} {self.availability} >"

       