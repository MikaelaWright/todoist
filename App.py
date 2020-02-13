class Todo:
    desc = ""


items = []


def create(s):
    todo = Todo()
    todo.desc = s
    items.append(todo)


def retrieve():
    return items


def update(s, idx):
    old_item = items[idx]
    old_item.desc = s


def delete(idx):
    thing = items[idx]
    items.remove(thing)
