import pymongo
import datetime

client = pymongo.MongoClient("mongodb+srv://admin:admin@ComputerNetwork.e5eod.mongodb.net/ComputerNetwork?authSource=admin&replicaSet=atlas-129xya-shard-0&w=majority&readPreference=primary&appname=MongoDB%20Compass&retryWrites=true&ssl=true")
db = client["ComputerNetwork"]


time = datetime.datetime.now()

#Insert data
# db.insert_one({
#     "create_date": time,
#     "username": "Tong",
#     "food_detail": {"F003":1,"F004":1,"F002":2}

# })


#เช็คดู oder ตามเงื่อนไข
# print("==================================")
# for i in db.find({'username':'Tong'}):
#     print(i)
# print("==================================")

#print([i for i in db.find({'username':'tong22'})])


'''
def fine_data():
    print([i for i in db.find()])

fine_data()
'''

from pandas import DataFrame
from tabulate import tabulate

user = "mobmap"
ch = 'H'
prepare_df = []
if ch == 'H':
    tmp = db.Request_logs.find_one({'username': user})
    print(f'''Date : {tmp['create_date']} \n''')
    for key,value in tmp['food_detail'].items():
        tmp2 = db.Menu.find_one({
            "_id": key,
        })
        tmp2["amount"] = value
        prepare_df.append(tmp2)

df = DataFrame(prepare_df)

print(
    tabulate(df,
             headers="keys",
             tablefmt="grid")
)

# print(tabulate.__doc__)