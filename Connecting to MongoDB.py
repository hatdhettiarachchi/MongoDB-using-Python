from pymongo import MongoClient

# Connect to MongoDB server (local or cloud)
client = MongoClient('mongodb://localhost:27017/')  # Local connection

# If using MongoDB Atlas, use the URI provided in your MongoDB Atlas dashboard
# client = MongoClient('<your_atlas_connection_uri>')

# Select a database (if it doesn't exist, MongoDB will create it for you)
db = client['my_database']

# Select a collection (again, MongoDB creates it if it doesn't exist)
collection = db['my_collection']