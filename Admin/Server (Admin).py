from socket import (
    socket,
    gethostname
)

s = socket()
host = gethostname()
print(host)

port = 7777
s.bind((host, port))
s.listen()

MSG = 'Hello User!'.encode()

while True:
    c, addr = s.accept()
    print('Connection from :', addr)
    c.send(MSG)

    while True:
        CMSG = c.recv(1024)
        c.send(b'Server: ' + CMSG)
        
        if CMSG.decode() == 'EXIT':
            c.close()
            break