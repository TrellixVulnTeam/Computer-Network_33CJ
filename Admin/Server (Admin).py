from socket import (
    socket,
    gethostname
)
from pickle import dumps,loads

s = socket()
host = gethostname()
print(host)

port = 7777
s.bind((host, port))
s.listen()

print("Tong")
print("อะไรสักอย่าง")

while True:
    c, addr = s.accept()
    print('Connection from :', addr)
    c.send(dumps('Hi...I am groot'))