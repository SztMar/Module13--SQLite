# library.py

from app import app, db
from app.models import Book, BookDetails, Storage

@app.shell_context_processor
def make_shell_context():
   return {
       "db": db,
       "Book": Book,
       "BookDetails": BookDetails,
       "Storage": Storage
   }