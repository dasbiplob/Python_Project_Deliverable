import time
import json
import logging
import paho.mqtt.client as mqtt
from database import save_message


# MQTT Broker Configuration
BROKER_ADDRESS = 'test.mosquitto.org'
BROKER_PORT = 1883
TOPIC = 'charger/1/connector/1/session/1'

# Logging Configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# MQTT Event Callbacks
def on_connect(client, userdata, flags, rc):
    logger.info("Connected to MQTT broker with result code %s", str(rc))
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())
        logger.info("Received MQTT message: %s", payload)
        # Save the message to the database
        save_message(payload)
    except Exception as e:
        logger.error("Error processing MQTT message: %s", str(e))

def on_disconnect(client, userdata, rc):
    if rc != 0:
        logger.warning("Unexpected disconnection from MQTT broker")

# MQTT Subscriber Setup
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect

# Connect to the MQTT broker
client.connect(BROKER_ADDRESS, BROKER_PORT)

# Start the MQTT loop (blocking)
client.loop_start()

# Keep the application running
while True:
    try:
        # Create a new session payload
        session_id = 1
        energy_delivered = 30
        duration = 45
        session_cost = 70
        payload = {
            "session_id": session_id,
            "energy_delivered_in_kWh": energy_delivered,
            "duration_in_seconds": duration,
            "session_cost_in_cents": session_cost
        }
        # Publish the new session payload to the MQTT topic
        try:
            client.publish(TOPIC, json.dumps(payload))
        except Exception as e:
            print(f"Failed to publish MQTT message: {e}")

        # Publish new sessions every 1 minute (to be implemented later)
        time.sleep(60)
    except KeyboardInterrupt:
        break

# Gracefully disconnect from the MQTT broker
client.loop_stop()
client.disconnect()

