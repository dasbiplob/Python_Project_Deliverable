# restapi_fastapi_mongodb:
# Description:
This application subscribes to ti a MQTT topic,logs the received messages,and sends them to a database.The application access the data from database through the restapi.
# Prerequisites
Docker installed on your machine
Python installed on your machine
# Installation
1. Clone the project repository:
      git clone <repository-url>
      cd <project-directory>
2. Build and run the process:
   docker-compose up --build
# Access the API endpoint to retrieve the messages:
http://localhost:8000/docs or 
http://localhost:8080/docs#/default/get_all_messages_messages_get
