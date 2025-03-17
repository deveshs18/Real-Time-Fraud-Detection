import json
from kafka import KafkaConsumer
from pymongo import MongoClient

# MongoDB setup
client = MongoClient('mongo', 27017)
db = client['fraud_detection']
collection = db['flagged_transactions']

# Kafka Consumer setup
consumer = KafkaConsumer(
    'flagged_transactions',
    bootstrap_servers='kafka:9093',
    value_deserializer=lambda m: m.decode('utf-8'),  # Decode message to string
    group_id='fraud_detection_group'
)

# Consuming messages from Kafka and inserting them into MongoDB
for msg in consumer:
    print(f"Raw received message: {msg.value}")  # Print the raw message for debugging
    
    try:
        # Parse the raw message as JSON
        transaction = json.loads(msg.value)  # Convert string to JSON
        
        print(f"Parsed transaction: {transaction}")  # Print parsed message for debugging
        
        # Insert into MongoDB
        result = collection.insert_one(transaction)
        print(f"Inserted transaction with ID: {result.inserted_id}")  # Confirm insertion
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
    except Exception as e:
        print(f"Error inserting into MongoDB: {e}")
