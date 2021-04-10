
from socket import socket, gethostname
from pickle import dumps, loads
from pickle import UnpicklingError
from function.connect import ask_port
from function.member import line_break

s = socket()
host = gethostname()
port = ask_port()

try:
    try:
        s.connect(
            (host, port)
        )

    except ConnectionRefusedError as con:
        line_break("Server was closed.")
        exit()

    server_data = s.recv(1024)
    data = loads(server_data)()
    if data['function'] == 'register':
        print("Params:", data)
        s.send(dumps(
            {
                "function": 'register',
                "params": data['params']
            }
        ))
        user = data['params'][0]

    else:
        user = data['params']
        s.send("exit".encode())

    print("Login:", user)
    while True:
        server_data = s.recv(1024)

        if hasattr(server_data, "decode"):
            try:
                tmp = loads(server_data)
                tmp("Create user complete!!")
                break

            except UnpicklingError as e:
                print("Client Exception")
                if server_data.decode().upper() == "EXIT":
                    print("Exception Exit")

                    s.send('exit'.encode())
                    break
                else:
                    print("Exception Not Exit")
                    print(server_data.decode())

        else:
            print("Else")
            if server_data.decode().upper() == "EXIT":
                print("Else if in")
                s.send('exit'.encode())
                break
            else:
                print(server_data.decode())


    s.close()

except ConnectionResetError:
    line_break("Server has been shutdown!!")



