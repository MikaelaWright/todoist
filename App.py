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


choice = " "
while choice != "Q":
    choice = input("Enter C,R,U,D or Q to quit\n")
    if choice == "C":
        desc = input("Enter item description:\n")
        create(desc)

    if choice == "R":
        lst = retrieve()
        for i in lst:
            print(i.desc)

    if choice == "U":
        idx = int(input("Enter idx of item to be updated:\n"))
        new_desc = input("Enter new desc of item:\n")
        update(new_desc, idx)

    if choice == "D":
        idx = int(input("Enter idx of item to be deleted:\n"))
        delete(idx)
