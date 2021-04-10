
from pickle import load
from pymongo import MongoClient

path = load(open('Data/mongo.p', 'rb'))
client = MongoClient(path['server'])
db = client.ComputerNetwork

# Pymongo
print(db.Request_logs.find_one())

# db.Port.insert_one({
#     "_id": "tong",
#     "port": 9999
# })