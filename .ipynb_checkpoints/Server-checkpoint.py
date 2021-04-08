from socket import socket,gethostname
from function.command import options


s = socket()
host = gethostname()
print(host)

port = 1234
s.bind((host, port))
s.listen()

MSG = f'login("{host}", "{port}")'.encode()

while True:
    c, addr = s.accept()
    print('Connection from :', addr)
    c.send(MSG)
    
    try:
        while True:
            CMSG = c.recv(1024).decode()
            options(CMSG)
            c.send("exit".encode())

            if CMSG.upper() == 'EXIT':
                c.close()
                break
                
    except ConnectionAbortedError:
        print(f"Client {addr[0]}:{addr[1]} has been disconnect!!")