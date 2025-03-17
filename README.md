This project simulates a real-time credit card transaction monitoring system. It detects suspicious transactions using Apache Kafka, Apache Flink, and MongoDB, orchestrated with Docker.

Key Components:

Kafka: Message broker for real-time streaming transactions.
Flink SQL: Real-time analytics & processing (windowing, aggregations).
MongoDB: Storage for flagged transactions.
Python Producer: Generates simulated credit card transactions.
Kafka Connect MongoDB Sink: Pushes processed results into MongoDB.

How it works.
Transaction Simulation:
producer.py sends JSON-formatted fake credit card transactions to Kafka topic credit_card_transactions.

Real-Time Processing with Flink SQL:
Flink reads from Kafka, applies windowed aggregations to detect patterns.

Storing Flagged Transactions:
Processed/flagged transactions are written to MongoDB either via:

Kafka Connect Sink Connector.
OR via custom Python consumer (mongodb_writer.py).
