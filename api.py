from pymongo import MongoClient
from fastapi import FastAPI
import socket

# MongoDB Configuration
MONGO_HOST = 'mymongo'
#MONGO_HOST = socket.gethostbyname('mongodb')
MONGO_PORT = 27018
MONGO_DB = 'mqttpy'
MONGO_COLLECTION = 'mqttpy'
#collection = db[MONGO_COLLECTION]


app = FastAPI()

# Connect to MongoDB
while True:
    try:
        client = MongoClient(MONGO_HOST, MONGO_PORT)
        db = client[MONGO_DB]
        collection = db[MONGO_COLLECTION]
        break  # Break out of the loop if the connection is successful
    except Exception as e:
        print(f"Error connecting to MongoDB: {str(e)}")

# API endpoint to retrieve all messages
@app.get('/messages')
def get_messages():
    try:
            messages = list(collection.find())
            print(f"The value of messages: {messages}")
            for message in messages:
             message["_id"] = str(message["_id"])
            return {"messages": messages}
        
    except Exception as e:
        return {'message': f'Error retrieving messages: {str(e)}'}
