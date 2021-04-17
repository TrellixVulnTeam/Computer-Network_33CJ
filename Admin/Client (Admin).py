from socket import (
    gethostname
)
from function.connect import ask_port
import socket
import pickle
from function.member import line_break
import time,sys

host = gethostname()

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

while True:
    try:
        port = ask_port(True)
        s.connect((host,port))
    except ConnectionRefusedError:
        line_break("Server was closed.")
    else:
        break

s.send(pickle.dumps('Hello Server'))

data = s.recv(1024)
print('Received : ',pickle.loads(data))













