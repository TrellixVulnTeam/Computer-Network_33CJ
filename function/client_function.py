
from datetime import datetime
from os import system
from time import sleep
from pickle import (
    dumps, loads, UnpicklingError
)

from function.options import options
from function.member import line_break
from function.connect import connect_mongo_db


def insert_login_logs(user):
    db = connect_mongo_db()
    db.Connection_logs.insert_one({
        "username": user,
        "login_at": datetime.now(),
        "logout_at": None
    })

    return True


def update_logout_logs(user):
    db = connect_mongo_db()
    uid = db.Connection_logs.find_one({
        "username": user
    }, sort=[("login_at", -1)])["_id"]

    db.Connection_logs.update({
        "_id": uid
    }, {
        "$set": {
            "logout_at": datetime.now()
        }
    })


def login(s):
    server_data = s.recv(1024)
    data = loads(server_data)()
    func = data['function']
    if func == 'register':
        s.send(dumps(
            {
                "function": 'register',
                "params": data['params']
            }
        ))
        return data['params'][0]
    else:
        return data['params']


def workflow(s, user):
    s.send("option".encode())
    server_data = s.recv(1024)
    if hasattr(server_data, "decode"):
        try:
            tmp = loads(server_data)
            tmp("Create user complete!!")
            sleep(2)
            options(user)

        except UnpicklingError as e:
            command = server_data.decode().upper()

            if command == "EXIT":
                s.send('exit'.encode())
                return 'break'

            elif command == "OPTION":
                system("cls")
                line_break("Welcome to food delivery!!")
                options(user)

            else:
                print(server_data.decode())