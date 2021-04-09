import pymongo

test_client = pymongo.MongoClient("mongodb+srv://admin:admin@ComputerNetwork.e5eod.mongodb.net/ComputerNetwork?authSource=admin&replicaSet=atlas-129xya-shard-0&w=majority&readPreference=primary&appname=MongoDB%20Compass&retryWrites=true&ssl=true")

mydb = test_client["Tong"]
mycol = mydb["people"]

if ch == 'H':
    print(mycol.find({}))