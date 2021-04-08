
"""
    server_command => ฟังก์ชันที่จำทำงานบนทุกๆ User
"""
from time import sleep
from threading import Thread
from socket import socket, gethostname
from function.member import login, line_break, register
from pickle import dumps, loads, UnpicklingError


def server_command(c, addr):
    print('Connection from :', addr)
    c.send(file)

    try:
        while True:
            sleep(2)
            client_data = c.recv(1024)
            if hasattr(client_data, "decode"):
                try:
                    print("pickle")
                    tmp = loads(client_data)

                    if tmp["function"] == "register":
                        (user, name, password) = tmp["params"]
                        c.send(
                            dumps(line_break)
                        )
                        register(user, name, password)
                except UnpicklingError:
                    print("except else:")
                    if client_data.upper() == 'EXIT':
                        print("Ex else in")
                        c.close()
                        break
                    print("Ex after loop to")

            else:
                print("Special case")

            c.send("exit".encode())

    except UnicodeDecodeError:
        # print("Unit code error :", client_data)
        print("Unit code error :")

    except ConnectionAbortedError:
        line_break(f"Client {addr[0]}:{addr[1]} has been disconnect!!")
        
    except ConnectionResetError:
        line_break(f"Client {addr[0]}:{addr[1]} has been shutdown!!")


s = socket()
host = gethostname()
print("Server name:", host)

port = 1234
s.bind((host, port))
s.listen()

file = dumps(login)
while True:
    c, addr = s.accept()
    Thread(target=server_command, args=(c, addr)).start()
