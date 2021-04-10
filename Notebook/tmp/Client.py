
from socket import socket, gethostname
from function.member import register
from pickle import dumps, loads

s = socket()
host = gethostname()
port = 1234

s.connect(
    (host, port)
)

server_data = s.recv(1024)
params = loads(server_data)()
if params:
    s.send(dumps(
        {
            "func": register,
            "params": params
        }
    ))
else:
    print("Params")
    s.send("exit".encode())

while True:
    server_data = s.recv(1024)

    if hasattr(server_data, "decode"):
        try:
            tmp = loads(server_data)
            tmp("Create user complete!!")
            loads(server_data)
            break
        except:
            print("Cilent exception inside")
            if server_data.decode().upper() == ("EXIT"):
                print("hello in")
                s.send('exit'.encode())
                break
            else:
                print(server_data.decode())

    else:
        print("hello")
        if server_data.decode().upper() == ("EXIT"):
            print("hello in")
            s.send('exit'.encode())
            break
        else:
            print(server_data.decode())


s.close()
