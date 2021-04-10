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

while True:
    c, addr = s.accept()
    print('Connection from :', addr)
