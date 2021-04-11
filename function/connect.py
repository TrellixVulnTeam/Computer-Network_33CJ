from pymongo import MongoClient
from function.member import line_break
from IPython.display import clear_output
from os import system
from time import sleep


def connect_mongo_db():
    client = MongoClient("mongodb+srv://admin:admin@computernetwork.e5eod.mongodb.net/ComputerNetwork?authSource"
                         "=admin&replicaSet=atlas-129xya-shard-0&w=majority&readPreference=primary&appname=MongoDB"
                         "%20Compass&retryWrites=true&ssl=true")
    return client.ComputerNetwork


def ask_port(special=False):
    if not special:
        return 1234

    try:
        while True:
            port = check_port(input("Enter special port: "))
            if port:
                break
            line_break("ไม่พบเลข Port ดังกล่าว")
            sleep(2)
            _ = system('cls')
            clear_output()
        return int(port['port'])
    except Exception as e:
        print("Special:", e)


def check_port(input_data="1234"):
    db = connect_mongo_db()
    return db.Port.find_one({"port": input_data})
