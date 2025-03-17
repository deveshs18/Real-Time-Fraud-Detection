import faker
import json
import time
import random
import logging
from kafka import KafkaProducer

# Set up logging
logging.basicConfig(level=logging.DEBUG)

fake = faker.Faker()

# Kafka container's broker (supports both local & container communication)
KAFKA_BROKER = "localhost:9092"

# Kafka producer setup
try:
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BROKER,
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    logging.info("Kafka Producer connected successfully.")
except Exception as e:
    logging.error(f" Error connecting to Kafka: {e}")
    exit(1)

# Generate a fake transaction
def generate_transaction():
    return {
        "transaction_id": str(fake.uuid4()),
        "amount": round(random.uniform(1, 5000), 2),
        "timestamp": fake.iso8601(),
        "merchant": fake.company(),
        "category": random.choice(["Retail", "Grocery", "Electronics"]),
    }

# Continuously generate transactions
while True:
    transaction = generate_transaction()
    try:
        producer.send('credit_card_transactions', transaction)
        producer.flush()
        logging.info(f" Sent: {transaction}")
    except Exception as e:
        logging.error(f" Error sending message: {e}")

    time.sleep(1)  # Adjust as needed







