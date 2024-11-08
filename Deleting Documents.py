from pymongo import MongoClient

# Connect to MongoDB server (local or cloud)
client = MongoClient('mongodb://localhost:27017/')
db = client['my_database']
collection = db['my_collection']

# To update documents, use the 
    # 🥇 delete_one 
    # 🥇 delete_many

# 💡 Delete a Single Document 💡
# Delete a document where name is "John Doe"
collection.delete_one({"name": "John Doe"})

# 💡 Update Multiple Document 💡
# Delete all documents where age is greater than 40
collection.delete_many({"age": {"$gt": 40}})