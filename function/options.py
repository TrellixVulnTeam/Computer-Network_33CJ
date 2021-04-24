
from os import system
from time import sleep

from function.menu import menu
from function.history import history
from function.member import line_break
from function.insert import insert_menu


options_text = """
    Select options:
    
    [M] Menu
    [C] Confirm
    [H] History
    [E] Exit
    
"""


def options(user=None):
    select_food = None
    while True:
        sleep(2)
        system("cls")
        print("\n   Welcome:", user)
        print(options_text, end="")
        menu_option = input("   Select option: ").upper()
        if menu_option == 'M':
            print()
            select_food = menu()

        elif menu_option == 'C':
            confirm = insert_menu(user, select_food)
            if confirm:
                select_food = None

        elif menu_option == 'H':
            history(user)

        elif menu_option == 'E':
            line_break("Exiting...")
            sleep(2)
            system("cls")
            line_break("Thank you!!")
            break

        else:
            line_break(
                "Please, select the correct option!!"
            )

    return "Options: " + menu_option
