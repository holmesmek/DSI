import pandas as pd
from pymongo import MongoClient
con = MongoClient("mongodb+srv://mke:mekmok43@cluster0.lw4j6.mongodb.net/test?authSource=admin&replicaSet=atlas-3rf2h2-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true")
print("Server Connected")
db = con.get_database("DSIdb")
print("Database Connected")
df = pd.read_csv(r'C:\Users\Dell\Downloads\2561.01-2561.05_finish')
print ("pandas is Done")