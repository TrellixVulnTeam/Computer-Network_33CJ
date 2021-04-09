
import pymongo
import pickle
import os


# Connect Database
try:
    mongo = pickle.load(open("Data/mongo.p", 'rb'))
    client = pymongo.MongoClient(mongo['local'])
    db = client.ComputerNetwork
except FileNotFoundError as f:
    print(os.listdir())


"""
    ฟังก์ชันช่วยเหลือ
===========================================================================================
    line_break => ช่วยในการทำข้อความให้เด่น    
===========================================================================================
    
    
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
        
    
def login():
    user = input("Username (create new at first-time): ")
    while not have_user(user):
        select = input(f"\nDo you need to create user: {user}\n"+
                       f"[Y]=Yes / [Any]=No: ")
        if select.upper() == 'Y':
            password = input("\nCreate your password: ")
            while password != input("Repeat your password: "):
                line_break("Password not match!!")
            name = input("Pick your name: ")
            return {
                'function': 'register',
                'params': (user, name, password)
            }
        else:
            user = input("\nUsername (create new at first-time): ")

    member = db.Member.find_one({"username": user})
    print(f"\nWelcome user: {member['name']}!!")
    password = input("Please enter your password: ")
    
    while True:
        if member["password"] == password:
            line_break("Login Success!!!")
            return {
                "function": 'login',
                "params": user
            }
        else:
            line_break("Password not match!!")
            password = input("Please enter your correct password: ")


def register(username, name, password):
    """ username := username ของผู่ใช้ """
    db.Member.insert_one({
        "username": username,
        "name": name,
        "password": password
    })
    
    
def line_break(text):
    line_break = "=====" * 10
    print(f"""
    {line_break}
    {text}
    {line_break}\n\n""")
