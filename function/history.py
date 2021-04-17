
import pymongo
from function.member import line_break

client = pymongo.MongoClient("mongodb+srv://admin:admin@computernetwork.e5eod.mongodb.net/ComputerNetwork?authSource=admin&replicaSet=atlas-129xya-shard-0&w=majority&readPreference=primary&appname=MongoDB%20Compass&retryWrites=true&ssl=true")
db = client.ComputerNetwork

# Main
def history(user=None):
    data = list(db.Request_logs.find({'usename': user}))
    if not data:
        line_break("Sorry,No history to show")
    else:
        print(data)