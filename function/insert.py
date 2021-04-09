import pymongo
import pickle
import pandas as pd
from time import sleep
from os import system
from tabulate import tabulate
from menu import menu

from IPython.display import clear_output

client = pymongo.MongoClient("mongodb+srv://admin:admin@computernetwork.e5eod.mongodb.net/ComputerNetwork?authSource=admin&replicaSet=atlas-129xya-shard-0&w=majority&readPreference=primary&appname=MongoDB%20Compass&retryWrites=true&ssl=true")
db = client.ComputerNetwork

# Pymongo
print(db.Request_logs.find_one())
