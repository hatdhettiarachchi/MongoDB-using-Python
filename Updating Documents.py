from pymongo import MongoClient

# Connect to MongoDB server (local or cloud)
client = MongoClient('mongodb://localhost:27017/')
db = client['my_database']
collection = db['my_collection']

# To update documents, use the 
    # 🥇 update_one 
    # 🥇 update_many
    # 🥇 replace_one


# 💡 Update a Single Document 💡
# Update the age of the person with name "John Doe"
collection.update_one(
    {"name": "John Doe"},  # Query filter
    {"$set": {"age": 31}}  # Update operation
)

# 💡 Update Multiple Document 💡
# Increase the age by 1 for everyone whose age is less than 30
collection.update_many(
    {"age": {"$lt": 30}},
    {"$inc": {"age": 1}}  # Increment age by 1
)