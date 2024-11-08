from pymongo import MongoClient

# Connect to MongoDB server (local or cloud)
client = MongoClient('mongodb://localhost:27017/')
db = client['my_database']
collection = db['my_collection']

# Find a single document where name is "John Doe"
result = collection.find_one({"name": "John Doe"})
print(result)

# Find all documents where age is greater than 30
results = collection.find({"age": {"$gt": 30}})
for result in results:
    print(result)

# Find all users but only return the 'name' and 'email' fields
results = collection.find({}, {"_id": 0, "name": 1, "email": 1})
for result in results:
    print(result)
