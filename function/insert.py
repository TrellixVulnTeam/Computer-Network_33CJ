import pymongo
import pickle
import pandas as pd
from time import sleep
from os import system
from tabulate import tabulate
from menu import menu
from IPython.display import clear_output
from pickle import load
from pymongo import MongoClient

path = load(open('Data/mongo.p', 'rb'))
client = MongoClient(path['server'])
db = client.ComputerNetwork

# Pymongo
print(db.Request_logs.find_one())
