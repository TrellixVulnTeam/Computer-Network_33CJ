
import pymongo
from function.member import line_break

client = pymongo.MongoClient("mongodb+srv://admin:admin@computernetwork.e5eod.mongodb.net/ComputerNetwork?authSource=admin&replicaSet=atlas-129xya-shard-0&w=majority&readPreference=primary&appname=MongoDB%20Compass&retryWrites=true&ssl=true")
db = client.ComputerNetwork



from pandas import DataFrame
from tabulate import tabulate
from datetime import datetime
from pymongo import MongoClient

from function.member import line_break


client = MongoClient("mongodb+srv://admin:admin@computernetwork.e5eod.mongodb.net/ComputerNetwork?authSource=admin&replicaSet=atlas-129xya-shard-0&w=majority&readPreference=primary&appname=MongoDB%20Compass&retryWrites=true&ssl=true")
db = client.ComputerNetwork


# def show_detail(food):
#     tmp = []
#     for key, value in food.items():
#         data = db.Menu.find_one({
#             "_id": key
#         })
#         data['amount'] = value
#         tmp.append(data)
#
#     df = DataFrame(tmp)
#     print(tabulate(
#         df,
#         headers="keys",
#         tablefmt="grid"
#     ))
#     print("ราคารวมทั้งหมด:", sum(df.price * df.amount))
#
#
# def insert_menu(user=None, select_menu=None):
#     if not select_menu:
#         line_break("Sorry, Please select food first!!")
#     else:
#         show_detail(select_menu)
#         confirm = input("Are you sure to confirm this menu? [Y/N]: ")
#         if confirm.upper() == "Y":
#             db.Request_logs.insert_one({
#                 "create_date": datetime.now(),
#                 "username": user,
#                 "food_detail": select_menu,
#                 "status": 0
#             })
#             return True
#
#food_detail = list(db.Request_logs.find({'status': 0}))

def show_history(food_detail):
    tmp = []

    for key, value in food_detail.items():
        data = db.Menu.find_one({
            "_id": key
        })
        data['amount'] = value
        tmp.append(data)

    df = DataFrame(tmp)
    print(tabulate(
        df,
        headers="keys",
        tablefmt="grid"
    ))


# Main
def history(user=None):
    data = list(db.Request_logs.find({'username': user}))
    if not data:
        line_break("Sorry,No history to show")
    else:
        show_history(data)


