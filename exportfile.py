from pymongo import MongoClient
con = MongoClient("mongodb+srv://mke:mekmok43@cluster0.lw4j6.mongodb.net/test?authSource=admin&replicaSet=atlas-3rf2h2-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true")
db = con.get_database("test")
obj = db.ทดลอง.find()
my_id = obj['_id']
