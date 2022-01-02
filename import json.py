import json
from pymongo import MongoClient
import os

con = MongoClient("mongodb+srv://mke:mekmok43@cluster0.lw4j6.mongodb.net/test?authSource=admin&replicaSet=atlas-3rf2h2-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true")
db = con.get_database("test")

for file in os.listdir(r'C:\Users\Dell\Desktop'):
    if file.endswith(".json"):
        print (str(file))
        obj = db.araimairu
        a = 'c:/Users/Dell/Desktop/{0}'.format(file)
        with open(a, encoding='utf8') as f:
            data = json.load(f)
        obj.insert(data)