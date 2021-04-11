from socket import (
    socket,
    gethostname
)
import socket
import time,sys

from pickle import dumps,loads

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
host = gethostname()
print("Server name:", host)

port = 7777
s.bind((host, port))
s.listen()

while True:
    print("Waiting for connection")

    connection,client_address = s.accept()
    try:
        print("Connection from :",client_address)
        #รับข้อมูลจาก client
        while True:
            #กำหนดขนาดข้อมูลที่จะรับใน recv()
            data = connection.recv(1024)
            print("Received : ",data)

        # ถ้ามีข้อมูลส่งเข้ามาให้ส่งกลับไปหา client
            if data:
                print("Sending data back to the client")
                connection.send(data)

            # ถ้าไม่มีข้อมูลให้จบการรอรับข้อมูล
            else:
                print("No more data from ",client_address)
                break

    # รับข้อมูลเสร็จแล้วทำการปิดการเชื่อมต่อ
    finally:
        connection.close()
        print("Closed Connection")




# print("\nWelcome to Chat Room\n")
# print("Initialising....\n")
# time.sleep(1)
#
#
# port = 7777
# s.bind((host, port))
# print(host, "(", host, ")\n")
# name = input(str("Enter your name: "))
#
# s.listen(1)
# print("\nWaiting for incoming connections...\n")
# conn, addr = s.accept()
# print("Received connection from ", addr[0], "(", addr[1], ")\n")
#
# s_name = conn.recv(1024)
# s_name = s_name.decode()
# print(s_name, "has connected to the chat room\nEnter [e] to exit chat room\n")
# conn.send(name.encode())
#
# while True:
#     message = input(str("Me : "))
#     if message == "[e]":
#         message = "Left chat room!"
#         conn.send(message.encode())
#         print("\n")
#         break
#     conn.send(message.encode())
#     message = conn.recv(1024)
#     message = message.decode()
#     print(s_name, ":", message)


