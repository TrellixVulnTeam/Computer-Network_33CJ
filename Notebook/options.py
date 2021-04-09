
from sys import exit

options_text = """
Select options
[M] Menu
[C] Confirm
[H] History
[E] Exit
"""


def options():
    while True:
        print(option_text, end="")
        option_ = input("Select option: ").upper()
        if option_ == 'M':
            print("Ying")

        elif option_ == 'C':
            print("Ying")
            pass
        elif option_ == 'H':
            print("Ying")
            pass
        elif option_ == 'E':
            print("Ying")
            break

    return "Options: " + option_


options()




