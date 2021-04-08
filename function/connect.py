from pymongo import MongoClient
from pickle import load
from function.member import line_break
import os


def connect_mongo_db():
    try:
        path = load(open('Data/mongo.p', 'rb'))
        client = MongoClient(path['local'])
        return client.ComputerNetwork
    except FileNotFoundError as f:
        print("This:", os.getcwd())


def ask_port():
    select = input("คุณต้องการเชื่อมต่อผ่าน Port พิเศษ? [Y]Yes / [Any]No: ")
    if select.upper() == 'Y':
        try:
            while True:
                port = check_port()
                if port:
                    break
                line_break("ไม่พบเลข Port ดังกล่าว")
            return int(port['port'])
        except ValueError as v:
            line_break("กรุณากรอกเฉพาะตัวเลขเท่านั้น เช่น 1234")
            ask_port()
    return 1234


def check_port():
    return db.Port.find_one({"port": int(input("Enter special port: "))})


db = connect_mongo_db()
