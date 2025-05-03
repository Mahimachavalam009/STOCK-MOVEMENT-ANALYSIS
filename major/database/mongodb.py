from pymongo import MongoClient
import certifi

def MongoDB():
    try:
        MONGO_URI = "mongodb+srv://armanofficial2401:bZXEkvK2xPsQSRan@cluster0.1erhs.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
        client = MongoClient(MONGO_URI, tls=True, tlsCAFile=certifi.where())
        db = client["total_records"]
        print("✅ Connected to MongoDB")
        return db
    except Exception as e:
        print(f"❌ MongoDB Connection Error: {e}")
        return None