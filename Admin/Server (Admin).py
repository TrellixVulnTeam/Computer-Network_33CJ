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






