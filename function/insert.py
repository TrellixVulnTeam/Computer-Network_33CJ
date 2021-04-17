
from pickle import load
from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:admin@computernetwork.e5eod.mongodb.net/ComputerNetwork?authSource=admin&replicaSet=atlas-129xya-shard-0&w=majority&readPreference=primary&appname=MongoDB%20Compass&retryWrites=true&ssl=true")
db = client.ComputerNetwork


def insert_menu(select_menu=None):
    pass


# Pymongo
print(db.Request_logs.find_one())
