import json
from pymongo import MongoClient
import socket

# MongoDB Configuration
MONGO_HOST = 'mymongo'
#MONGO_HOST = socket.gethostbyname('mongodb')
MONGO_PORT = 27018
MONGO_DB = 'mqttpy'
MONGO_COLLECTION = 'mqttpy'

# Function to save the MQTT message to the database
def save_message(message):
    try:
        client = MongoClient(MONGO_HOST, MONGO_PORT)
        db = client[MONGO_DB]
        collection = db[MONGO_COLLECTION]
        #data = json.loads(message)
        collection.insert_one(message)
        print('Data saved to MongoDB!')
        client.close()
    except Exception as e:
        print(f"An error occurred while saving to the database: {e}")
        
        