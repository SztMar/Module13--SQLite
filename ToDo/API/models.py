import json


class Todos:
    def __init__(self):
        try:
            with open("books.json", "r",encoding= 'utf8') as f:
                self.todos = json.load(f)
                               
        except FileNotFoundError:
            self.todos = []

    def all(self):
        return self.todos
    
    def get(self, id):
        todo = [todo for todo in self.all() if todo['id'] == id]
        if todo:
            return todo[0]
        return []

    def create(self, data):
        self.todos.append(data)
        self.save_all()

    def save_all(self):
        with open("books.json", "w") as f:
            json.dump(self.books, f)

    def update(self, id, data):
        self.books[id] = data
        self.save_all

    def remove(self,id):
        self.books.remove(id)
    

todos = Todos()

