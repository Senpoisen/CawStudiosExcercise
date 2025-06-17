from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27018")
db = client["support_chat"]
cases = db["tickets"]
