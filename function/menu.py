# Comment
"""
    pages_text(page_index, all_pages) : use to texting option in select
"""

import pymongo
from os import system
from tabulate import tabulate
from IPython.display import clear_output
import pickle

def menu():
    def pages_text(i, pages):
        if i == 0:
            pages_text = '''[N] => Next page'''
        elif i == (len(pages)-1):
            pages_text = '''[P] => Previous'''
        else:
            pages_text = '''[N] => Next page
            [P] => Previous'''
        return pages_text

    mongo = pickle.load(open("../Data/mongo.p", 'rb'))
    client = pymongo.MongoClient(mongo['local'])
    db = client.ComputerNetwork
    data = list(db.Menu.find({}))

    headers = data[0].keys()
    rows = [x.values() for x in data]

    size = 10
    pages = [rows[x:x+size] for x in range(0, len(rows), size)]


    def table_menu_pages():
        size = 10
        pages = [rows[x:x+size] for x in range(0, len(rows), size)]

        page_index = 0
        while True:
            print(tabulate(pages[page_index], headers, tablefmt="grid"))
            print(f'''Option:
            [S] => Select Food
            {pages_text(page_index, pages)}
            [E] => Exit
            ''')

            select = input("Enter your menu ID: ")

            if select.lower() == 's':
                break
            elif select.lower() == 'n' and page_index < (len(pages)-1):
                _ = system('cls')
                clear_output()
                page_index += 1
            elif select.lower() == 'p' and page_index != 0:
                _ = system('cls')
                clear_output()
                page_index -= 1
            elif select.lower() == 'e':
                break
            else:
                _ = system('cls')
                clear_output()
                line_break = "=====" * 10
                print(f"""
                {line_break}
                Incorrect options: Please enter your option Again!!
                {line_break}\n""", end="\r")

    def table_all_menu():
        select_menu = {}
        while True:
            print(tabulate(rows, headers, tablefmt="grid"))
            print(f'''Option:
            [S] => Select Food
            [E] => Exit
            ''')

            select = input("Enter your menu ID: ")

            if select.lower() == 's':
                break
            elif select.lower() == 'e':
                break
            else:
                clear_output()
                line_break = "=====" * 10
                print(f"""
                {line_break}
                Incorrect options: Please enter your option Again!!
                {line_break}\n""", end="\r")
                
    table_menu_pages()

menu()