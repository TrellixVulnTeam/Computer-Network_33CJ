
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
                print("pass")
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
                    command = client_data.decode().upper()
                    if  command == 'EXIT':
                        c.send("exit".encode())
                        line_break(f"Client {addr[0]}:{addr[1]} has been disconnect!!")
                        c.close()
                        break
                    elif command == 'OPTION':
                        c.send('option'.encode())

            else:
                print("Special case")

    except UnicodeDecodeError:
        print("Unit code error :")

    except ConnectionAbortedError as con:
        print(con)
        
    except ConnectionResetError:
        line_break(f"Client {addr[0]}:{addr[1]} has been shutdown!!")

    except EOFError:
        line_break(f"Client not sending anything!!")


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
