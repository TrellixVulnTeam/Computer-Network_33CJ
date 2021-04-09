
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
        menu_option = input("Select option: ").upper()
        if menu_option == 'M':
            print("Ying")

        elif menu_option == 'C':
            print("Pond")
            pass
        elif menu_option == 'H':
            print("Tong")
            pass
        elif menu_option == 'E':
            break

    return "Options: " + menu_option


options()
