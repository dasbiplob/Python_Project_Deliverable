import json
from pymongo import MongoClient

# MongoDB Configuration
MONGO_HOST = '172.23.0.2'
#MONGO_HOST = 'mongodb'
MONGO_PORT = 27017
MONGO_DB = 'mqttpy'
MONGO_COLLECTION = 'mqttpy'

# Function to save the MQTT message to the database
def save_message(message):
    try:
        client = MongoClient(MONGO_HOST, MONGO_PORT)
        db = client[MONGO_DB]
        collection = db[MONGO_COLLECTION]
        data = json.loads(message)
        collection.insert_one(data)
        print('Data saved to MongoDB!')
        client.close()
    except Exception as e:
        print(f"An error occurred while saving to the database: {e}")
        
        