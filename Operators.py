from pymongo import MongoClient

# Connect to MongoDB server (local or cloud)
client = MongoClient('mongodb://localhost:27017/')
db = client['my_database']
collection = db['my_collection']

# 💡 1. Comparison Operators 💡

# $eq (equal): Matches values that are equal to a specified value.
db.collection.find({"age": {"$eq": 25}})

# $ne (not equal): Matches values that are not equal to a specified value.
db.collection.find({"age": {"$ne": 25}})

# $gt (greater than): Matches values that are greater than a specified value.
db.collection.find({"age": {"$gt": 25}})

# $gte (greater than or equal): Matches values that are greater than or equal to a specified value.
db.collection.find({"age": {"$gte": 25}})

# $lt (less than): Matches values that are less than a specified value.
db.collection.find({"age": {"$lt": 25}})

# $lte (less than or equal): Matches values that are less than or equal to a specified value.
db.collection.find({"age": {"$lte": 25}})

# $in: Matches values that are in a specified array.
db.collection.find({"age": {"$in": [20, 25, 30]}})

# $nin (not in): Matches values that are not in a specified array.
db.collection.find({"age": {"$nin": [20, 25, 30]}})


# 💡 2. Logical Operators 💡

# $and: Matches documents that satisfy all conditions in the array.
db.collection.find({"$and": [{"age": {"$gte": 25}}, {"age": {"$lt": 40}}]})

# $or: Matches documents that satisfy at least one of the conditions in the array.
db.collection.find({"$or": [{"age": {"$lt": 20}}, {"age": {"$gte": 30}}]})

# $not: Inverts the effect of a query operator (e.g., match all documents except those that are greater than 25).
db.collection.find({"age": {"$not": {"$gt": 25}}})

# $nor: Matches documents that do not satisfy any of the conditions in the array.
db.collection.find({"$nor": [{"age": {"$lt": 25}}, {"age": {"$gt": 40}}]})


# 💡 3. Element Operators 💡

# $exists: Matches documents that have a field.
db.collection.find({"address": {"$exists": True}})

# $type: Matches documents where the field is of a specific type.
db.collection.find({"age": {"$type": "int"}})


# 💡 4. String Operators 💡

# $regex: Matches documents that contain a specific pattern.
db.collection.find({"name": {"$regex": "^J"}})

# $options: Specifies options for regex (e.g., case-insensitive search).
db.collection.find({"name": {"$regex": "^j", "$options": "i"}})


# 💡 5. Array Operators 💡

# $all: Matches documents where the field is an array that contains all the specified values.
db.collection.find({"tags": {"$all": ["music", "pop"]}})

# $elemMatch: Matches documents where at least one array element matches the query.
db.collection.find({"comments": {"$elemMatch": {"user": "John", "score": {"$gte": 5}}}})

# $size: Matches documents where the array has a specific size.
db.collection.find({"tags": {"$size": 3}})

