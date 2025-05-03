from pymongo import MongoClient
import certifi

# Replace with your actual MongoDB connection string
MONGO_URI = "mongodb+srv://armanofficial2401:bZXEkvK2xPsQSRan@cluster0.1erhs.mongodb.net/"

try:
    client = MongoClient(MONGO_URI, tlsCAFile=certifi.where())
    db = client.get_database("total_records")

    # Test the connection
    print("Databases:", client.list_database_names())
    print("Collections in 'total_records':", db.list_collection_names())

except Exception as e:
    print(f"MongoDB Connection Error: {e}")