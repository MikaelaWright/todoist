import sys

sys.path.insert(0, 'models')
sys.path.insert(1, 'core')
from Todo import *
from TodoService import *

choice = " "
todoService = TodoService()

while choice != "Q":
    choice = input("Enter C,R,U,D or Q to quit\n")
    if choice == "C":
        desc = input("Enter item description:\n")
        todoService.create(desc)

    if choice == "R":
        lst = todoService.retrieve()
        for i in lst:
            print(i.desc)

    if choice == "U":
        idx = int(input("Enter idx of item to be updated:\n"))
        new_desc = input("Enter new desc of item:\n")
        todoService.update(new_desc, idx)

    if choice == "D":
        idx = int(input("Enter idx of item to be deleted:\n"))
        todoService.delete(idx)
