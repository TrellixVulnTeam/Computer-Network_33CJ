
from sys import exit


def options():
    while True:
        print("""\nSelect options
[M] Menu
[C] Confirm
[H] History
[E] Exit
""", end="")
        option_ = input("Select option: ").upper()
        if option_ == 'M':
            print("Ying")

        elif option_ == 'C':
            pass
        elif option_ == 'H':
            pass
        elif option_ == 'E':
            exit()
            print("After")

    return "Options: "+option_


options()




