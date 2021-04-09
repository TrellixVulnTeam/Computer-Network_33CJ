import pymongo

test_client = pymongo.MongoClient("mongodb+srv://admin:admin@ComputerNetwork.e5eod.mongodb.net/ComputerNetwork?authSource=admin&replicaSet=atlas-129xya-shard-0&w=majority&readPreference=primary&appname=MongoDB%20Compass&retryWrites=true&ssl=true")

mydb = test_client["Tong"]
mycol = mydb["people"]


#print(list(db.find()))
#db.delete_many({})


"""
data = {'name': 'Tong','memu':'','price':'40'}
mycol.insert_one(data)
"""

"""
data_list = [{'name': 'ying','memu':'ข้าวผัด','price':'45'} , {'name': 'mob','memu':',ข้าวไก่กรอบ','price':'60'} ,
             {'name': 'Tong','memu':'ข้าวมันไก่','price':'40'},{'name': 'Tong','memu':'ข้าวขาหมู','price':'45'},
             {'name': 'Tong','memu':'ข้าวไข่เจียว','price':'40'}]
mycol.insert_many(data_list)
"""


"""
tmp = mycol.find({'name':'Tong'})
print("==================================")
for i in tmp:
    print(i)
print("==================================")
"""

"""
foods = ["F001", "F001", "F002"]

food_dict = {}
for i in foods:
    try:
        food_dict[i] += 1
    except KeyError:
        food_dict[i] = 1
"""
