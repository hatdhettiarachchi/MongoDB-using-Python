from pymongo import MongoClient

# Connect to MongoDB server (local or cloud)
client = MongoClient('mongodb://localhost:27017/')
db = client['my_database']
collection = db['my_collection']

document = {
    "name": "John Doe",
    "age": 30,
    "email": "john.doe@example.com"
}

# Insert one document into the collection
collection.insert_one(document)

documents = [
    {"name": "Alice", "age": 28, "email": "alice@example.com"},
    {"name": "Bob", "age": 35, "email": "bob@example.com"}
]

# Insert multiple documents
collection.insert_many(documents)