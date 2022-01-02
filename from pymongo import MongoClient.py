from pymongo import MongoClient

client = MongoClient("mongodb://host:port/")
database = client["DSIdb"]
collection = database["\u0E44\u0E1E\u0E25\u0E34\u0E19"]

# Created with Studio 3T, the IDE for MongoDB - https://studio3t.com/

query = {}


cursor = collection.find(query)
try:
    for doc in cursor:
        print(doc)
finally:
    client.close()
