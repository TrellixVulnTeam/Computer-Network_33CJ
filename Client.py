
from os import system
from time import sleep

from socket import socket, gethostname
from pickle import dumps, loads, UnpicklingError

from function.options import options
from function.connect import ask_port
from function.member import line_break


def connect(s):
    s.connect(
        (host, port)
    )


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


def workflow(s):
    s.send("option".encode())
    server_data = s.recv(1024)
    if hasattr(server_data, "decode"):
        try:
            tmp = loads(server_data)
            tmp("Create user complete!!")
            return 'break'

        except UnpicklingError as e:
            command = server_data.decode().upper()

            if command == "EXIT":
                s.send('exit'.encode())
                return 'break'

            elif command == "OPTION":
                options(user)

            else:
                print(server_data.decode())


s = socket()
host = gethostname()
port = ask_port()

try:
    system("cls")
    connect(s)
    user = login(s)

    while True:
        status = workflow(s)
        if status == 'break':
            break
        else:
            s.send("exit".encode())

except ConnectionResetError:
    line_break("Exiting...")
    sleep(2)
    system("cls")
    line_break("Thank you!!")


except ConnectionRefusedError:
    line_break("Server was closed.")

except EOFError:
    line_break("Server not sending anything!!")

