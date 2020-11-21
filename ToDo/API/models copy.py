import json


class Books:
    def __init__(self):
        try:
            with open("books.json", "r",encoding= 'utf8') as f:
                self.books = json.load(f)
                               
        except FileNotFoundError:
            self.books = []

    def all(self):
        return self.books
    
    def get(self, id):
        book = [book for book in self.all() if book['id'] == id]
        if book:
            return book[id]
        return []
            
    def create(self, data):
        data.pop('csrf_token')
        self.books.append(data)

    def save_all(self):
        with open("books.json", "w") as f:
            json.dump(self.books, f)

    def update(self, id, data):
        self.books[id] = data
        self.save_all

    def remove(self,id):
        self.books.remove(id)

    

books = Books()

