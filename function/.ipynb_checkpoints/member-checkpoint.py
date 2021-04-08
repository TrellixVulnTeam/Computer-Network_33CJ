# import 
import pymongo
from socket import socket
from tabulate import tabulate


# Connect Database
client = pymongo.MongoClient("mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false")
db = client.ComputerNetwork



"""
    ฟังก์ชันช่วยเหลือ
===========================================================================================
    line_break => ช่วยในการทำข้อความให้เด่น    ===========================================================================================
    
    
    คำอธิบาย
===========================================================================================
    options => รับคำสั่งแล้วใช้งานฟังก์ชัน
    login => ทำการ Login
    register => สมัครสมาชิก
    have_user => มี user นี้ไหม
===========================================================================================
    
"""
def have_user(user):
    """ user := user ที่ต้องการเช็ค """
    return db.Member.find_one({"username": user})
        
    
def login(host=None, port=None):
    user = input("Please enter yor phone number: ")
    if not have_user(user):
        password = input("\nCreate your password: ")
        name = input("Pick your name: ")
        s = socket()
        s.connect(
            (host, int(port))
        )
        s.send(f'register("{user}", "{name}", "{password}")'.encode())
    
    
    member = db.Member.find_one({"username": user})
    print(f"\nWelcome user: {member['name']}!!")
    password = input("Please enter your password: ")
    
    while True:
        if member["password"] == password:
            line_break("Login Success!!!")
            break
        else:
            password = input("Please enter your correct password: ")
        
def register(username, name, password):
    """ username := username ของผู่ใช้ """
    
    
    db.Member.insert_one({
        "username": username,
        "name": name,
        "password": password
    })
    
    print("Create user complete!!")
    
    
def line_break(text):
    line_break = "=====" * 10
    print(f"""
    {line_break}
    {text}
    {line_break}\n\n""")
    