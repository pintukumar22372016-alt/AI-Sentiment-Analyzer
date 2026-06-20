from pymongo import MongoClient
import datetime

class MongoDBClient:
    def __init__(self, uri="mongodb://localhost:27017/"):
        try:
            self.client = MongoClient(uri, serverSelectionTimeoutMS=5000)
            self.db = self.client['sentiment_analyzer']
            self.collection = self.db['history']
            # Test connection
            self.client.server_info()
            self.connected = True
        except Exception as e:
            print(f"MongoDB connection failed: {e}")
            self.connected = False

    def insert_record(self, text, classification, scores):
        if not self.connected:
            return None
        
        record = {
            "text": text,
            "classification": classification,
            "scores": scores,
            "timestamp": datetime.datetime.now()
        }
        
        try:
            result = self.collection.insert_one(record)
            return str(result.inserted_id)
        except Exception as e:
            print(f"Failed to insert record: {e}")
            return None

    def get_recent_records(self, limit=50):
        if not self.connected:
            return []
            
        try:
            records = self.collection.find().sort("timestamp", -1).limit(limit)
            return [
                {
                    "text": doc["text"],
                    "classification": doc["classification"],
                    "scores": doc["scores"],
                    "timestamp": doc["timestamp"].isoformat()
                }
                for doc in records
            ]
        except Exception as e:
            print(f"Failed to fetch records: {e}")
            return []
