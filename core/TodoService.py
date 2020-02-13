import sys

sys.path.insert(0, '../models')
from Todo import *


class TodoService:

    def __init__(self):
        self.items = []

    def create(self, s):
        todo = Todo()
        todo.desc = s
        self.items.append(todo)

    def retrieve(self):
        return self.items

    def update(self, s, idx):
        old_item = self.items[idx]
        old_item.desc = s

    def delete(self, idx):
        thing = self.items[idx]
        self.items.remove(thing)
