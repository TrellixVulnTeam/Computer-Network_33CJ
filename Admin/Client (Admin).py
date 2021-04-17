from socket import (
    gethostname
)
from function.connect import ask_port
import socket
import pickle
from function.member import line_break
import time,sys

host = gethostname()
port = ask_port(True)

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

s.connect((host,port))

s.send(pickle.dumps('Hello Server'))

data = s.recv(1024)
print('Received : ',pickle.loads(data))

# user = 'tong'
# H = True
# if user == H :
#     db.find
#
#
#
# else :





# print("\nWelcome to Chat Room\n")
# print("Initialising....\n")
# time.sleep(1)
#
# print(host, "(", host, ")\n")
# host = input(str("Enter server address: "))
# name = input(str("\nEnter your name: "))
# port = 7777
# print("\nTrying to connect to ", host, "(", port, ")\n")
# time.sleep(1)
# s.connect((host, port))
# print("Connected...\n")
#
# s.send(name.encode())
# s_name = s.recv(1024)
# s_name = s_name.decode()
# print(s_name, "has joined the chat room\nEnter [e] to exit chat room\n")
#
# while True:
#     message = s.recv(1024)
#     message = message.decode()
#     print(s_name, ":", message)
#     message = input(str("Me : "))
#     if message == "[e]":
#         message = "Left chat room!"
#         s.send(message.encode())
#         print("\n")
#         break
#     s.send(message.encode())


