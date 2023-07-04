# Containerized MQTT Subscriber and API
This repository contains two containerized applications: MQTT Subscriber and API. The MQTT Subscriber subscribes to an MQTT topic, receives messages, and saves them to a MongoDB database. The API provides endpoints to retrieve the saved messages from the database.
# Prerequisites
Docker installed on your machine
# Setup Env:
##Clone the repository:
git clone <repository-url>
# Navigate to the project directory:
1.cd <project-directory>
2.virtualenv venv
3.source <project-directory>/venv/bin/activate
4.docker-compose up --build
