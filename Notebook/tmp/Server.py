
"""
    server_command => ฟังก์ชันที่จำทำงานบนทุกๆ User
"""

from threading import Thread
from socket import socket, gethostname
from function.member import login, line_break
from pickle import dumps, loads


def server_command(c, addr):
    print('Connection from :', addr)
    c.send(file)

    try:
        while True:
            client_data = c.recv(1024)
            if  hasattr(client_data, "decode"):
                try:
                    print("pickle")
                    tmp = loads(client_data)

                    if tmp["func"].__name__ == "register":
                        func, (user, name, password) = tmp.values()
                        c.send(
                            dumps(line_break)
                        )
                        func(user, name, password)
                except:
                    print("Ex else:")
                    if client_data.upper() == 'EXIT':
                        print("Ex else in")
                        c.close()
                        break
                    print("Ex after loop to")

            else:
                print("server else:")
                if client_data.upper() == 'EXIT':
                    print("Server else in")
                    c.close()
                    break
                print("SEver after loop to")

            c.send("exit".encode())

    except UnicodeDecodeError:
        print("Unit code error :", client_data)

    except ConnectionAbortedError:
        line_break(f"Client {addr[0]}:{addr[1]} has been disconnect!!")


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
