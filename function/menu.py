# Comment
"""
    pages_text(page_index, all_pages) : use to texting option in select
    count_menu(x) : count the number of menus
    dict_of_menus(select_menu) : collect menu in Dictionary Format
    delete_menu(select_menu) : delete menu from select menu
    table_menu_pages(data) : search menu, show options, select options, select menus
"""

import pymongo
import pickle
import pandas as pd
from time import sleep
from os import system
from tabulate import tabulate

from IPython.display import clear_output

client = pymongo.MongoClient("mongodb+srv://admin:admin@computernetwork.e5eod.mongodb.net/ComputerNetwork?authSource=admin&replicaSet=atlas-129xya-shard-0&w=majority&readPreference=primary&appname=MongoDB%20Compass&retryWrites=true&ssl=true")
db = client.ComputerNetwork


def pages_text(i, pages):
    items = sum([len(item) for item in pages])
    if items <= 10:
        return ""
    elif i == 0 and (items > 10):
        pages_text = '''[N] => Next page'''
    elif i == (len(pages) - 1) and (items > 10):
        pages_text = '''[P] => Previous'''
    else:
        pages_text = '''[N] => Next page
           [P] => Previous'''
    return pages_text


def count_menu(x):
    items = {}
    for name_th in [i['name_th'] for i in x]:
        try:
            items[name_th] += 1
        except:
            items[name_th] = 1

    for key, value in items.items():
        print(f"\t{key} x {value}")


def dict_of_menus(select_menu):
    for i in select_menu:
        try:
            select_menu[i] += 1
        except KeyError:
            select_menu[i] = 1


def delete_menu(select_menu):
    tmp = []
    for key, value in select_menu.items():
        menu = db.Menu.find_one({"_id": key})
        menu["Amount"] = value
        tmp.append(menu)
    df = pd.DataFrame(tmp)[["_id", "name_th", "Amount"]].rename(columns={"_id": "ID"})\
                                                        .set_index("ID")
    print(tabulate(df, headers="keys", tablefmt="grid"))

    del_menu = input("ป้อนรหัสรายการที่ต้องการลบ: ")
    amount = int(input("จำนวนที่ต้องการลบ : "))

    if amount < select_menu[del_menu]:
        select_menu[del_menu] -= amount

    elif select_menu[del_menu] == amount:
        print(select_menu)
        select_menu.pop(del_menu, None)

    print("Please Correct")
    print(select_menu)


def menu():

    # mongodb+srv://admin:admin ~
    query = {"name_th": {
        "$regex": f'{input("ค้นหารายการอาหาร (ไม่ใส่หมายถึงค้นหาทั้งหมด): ")}'
    }}
    data = list(db.Menu.find(query).sort("_id", 1))

    def table_menu_pages(data):

        # if not data in db.Menu.find():
        #     print("Not found. Please enter new menu again.")
        #     query = {"name_th": {
        #         "$regex": f'{input("ค้นหารายการอาหาร (ไม่ใส่หมายถึงค้นหาทั้งหมด): ")}'
        #     }}
        #     data = list(db.Menu.find(query))

        size = 10
        headers = data[0].keys()
        rows = [x.values() for x in data]
        pages = [rows[x:x+size] for x in range(0, len(rows), size)]

        page_index = 0
        select_menu = {}
        while True:
            print(tabulate(pages[page_index], headers, tablefmt="grid"))
            if select_menu:
                print("Menu:")
                for key, value in select_menu.items():
                    print(f"\t{db.Menu.find_one({'_id':key})['name_th']} x {value}")

            print(f'''Option:
    [S] => Select Food
    {"[D] => Delete" if select_menu else ""}
    {pages_text(page_index, pages)}
    [E] => Exit
            ''')

            select = input("Select options: ")
            if select.lower() == 's':
                select = input("Enter Food ID: ")
                if not db.Menu.find_one({"_id": select.upper()}):
                    clear_output()

                    line_break = "=====" * 10
                    print(f"""
                                {line_break}
                                Incorrect options: Please enter your option Again!!
                                {line_break}\n""")
                    sleep(4)
                else:
                    tmp = db.Menu.find_one({"_id": select.upper()})["_id"]
                    print(tmp)
                    try:
                        select_menu[tmp] += 1
                    except KeyError:
                        select_menu[tmp] = 1
            elif select.lower() == 'd' and select_menu:
                _ = system('cls')
                clear_output()
                delete_menu(select_menu)

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
                line_break = "=====" * 10
                print("else")
                print(f"""
                {line_break}
                Incorrect options: Please enter your option Again!!
                {line_break}\n""", end="\r")
                _ = system('cls')
                clear_output()

        dict_of_menus(select_menu)

    table_menu_pages(data)


menu()
