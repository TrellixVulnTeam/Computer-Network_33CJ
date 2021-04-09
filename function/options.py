
from function.member import line_break

options_text = """
Select options
[M] Menu
[C] Confirm
[H] History
[E] Exit
"""


def options():
    while True:
        print(options_text, end="")
        option_ = input("Select option: ").upper()
        if option_ == 'M':
            print("Ying")

        elif option_ == 'C':
            print("Pond")
            pass
        elif option_ == 'H':
            print("Tong")
            pass
        elif option_ == 'E':
            line_break("Thank you, have a nice day")
            break

    return "Options: " + option_


options()
