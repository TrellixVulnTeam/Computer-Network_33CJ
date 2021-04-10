import pymongo
import datetime

client = pymongo.MongoClient("mongodb+srv://admin:admin@ComputerNetwork.e5eod.mongodb.net/ComputerNetwork?authSource=admin&replicaSet=atlas-129xya-shard-0&w=majority&readPreference=primary&appname=MongoDB%20Compass&retryWrites=true&ssl=true")
db = client["ComputerNetwork"]

if ch == 'H':
    print(mycol.find({}))