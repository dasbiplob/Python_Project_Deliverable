import json
from pymongo import MongoClient

# MongoDB Configuration
MONGO_HOST = '127.0.0.1'
MONGO_PORT = 27017
MONGO_DB = 'mqttpy'
MONGO_COLLECTION = 'mqttpy'

# MongoDB Connection Setup
try:
    client = MongoClient(MONGO_HOST, MONGO_PORT)
    db = client[MONGO_DB]
    collection = db[MONGO_COLLECTION]
    
    print("Connected to MongoDB successfully!")
except ConnectionError:
    print("Failed to connect to MongoDB. Check if MongoDB server is running.")
except Exception as e:
    print("Timeout: Unable to connect to the MongoDB server.")

# Function to save the MQTT message to the database
def save_message(message):
    try:
        data = json.loads(message)
        collection.insert_one(message)
        print("Message saved to MongoDB successfully!")
    except ConnectionError:
        print("Failed to save the message. Check the MongoDB connection.")
    except Exception as e:
        print("An error occurred while saving the message:", e)
        
        