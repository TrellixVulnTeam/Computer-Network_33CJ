
from os import system
from time import sleep

from function.menu import menu
from function.history import history
from function.member import line_break
from function.insert import insert_menu


options_text = """
Select options
[M] Menu
[C] Confirm
[H] History
[E] Exit
"""


def options():
    select_food = None
    while True:
        sleep(2)
        system("cls")
        print(options_text, end="")
        menu_option = input("Select option: ").upper()
        if menu_option == 'M':
            print("Ying")
            select_food = menu()

        elif menu_option == 'C':
            print("Pond")
            if not select_food:
                line_break("Sorry, Please select food first!!")
            else:
                print(select_food)
                insert_menu(select_food)

        elif menu_option == 'H':
            print("Tong")
            history()

        elif menu_option == 'E':
            break

    return "Options: " + menu_option
