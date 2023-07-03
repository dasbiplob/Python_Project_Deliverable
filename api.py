from pymongo import MongoClient
from fastapi import FastAPI
#from database import db

# MongoDB Configuration
MONGO_HOST = '127.0.0.1'
MONGO_PORT = 27017
MONGO_DB = 'mqttpy'
MONGO_COLLECTION = 'mqttpy'
#collection = db[MONGO_COLLECTION]

app = FastAPI()

# Connect to MongoDB
try:
        client = MongoClient(MONGO_HOST, MONGO_PORT)
        db = client[MONGO_DB]
        collection = db[MONGO_COLLECTION]
except Exception as e:
     print(f"Error connecting to MongoDB: {str(e)}")
    # Handle the error appropriately (e.g., log, raise, or return an error response)

# API endpoint to retrieve all messages
@app.get('/messages')
def get_messages():
    try:
            messages = list(collection.find())
            print("The value of messages" + messages)
            for message in messages:
             message["_id"] = str(message["_id"])
            return {"messages": messages}
        
    except Exception as e:
        return {'message': f'Error retrieving messages: {str(e)}'}
