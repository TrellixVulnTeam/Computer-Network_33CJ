from function.member import login
from function.menu import menu

def options(order):
    """ Order := คำสั่งที่รับมา """
    print(order)
    exec(order)

def exit():
    return 0