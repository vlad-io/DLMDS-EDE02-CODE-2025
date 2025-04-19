import os
from quixstreams import Application
from quixstreams.kafka.configuration import ConnectionConfig

DRONE_ID = int(os.getenv("DRONE_ID", "1"))

connection = ConnectionConfig(bootstrap_servers="PLAINTEXT://kafka:9092")

app = Application(
    broker_address=connection,
    consumer_group="text-splitter-v1",
    auto_offset_reset="earliest",
)
messages_topic = app.topic(name=f"drone_{DRONE_ID}", value_serializer="json")

# generate drone flight path coordinates
messages = [
    {"drone_id": DRONE_ID, "X":0, "Y":0.3},
    {"drone_id": DRONE_ID, "X":1, "Y":2.2},
    {"drone_id": DRONE_ID, "X":2, "Y":3.4},
    {"drone_id": DRONE_ID, "X":4, "Y":4.7},
]


def main():
    with app.get_producer() as producer:
        for message in messages:
            # Serialize chat message to send it to Kafka
            # Use "chat_id" as a Kafka message key
            kafka_msg = messages_topic.serialize(
                key=f"drone_{DRONE_ID}", value=message)

            # Produce chat message to the topic
            print(
                f'Produce event with key="{kafka_msg.key}" value="{kafka_msg.value}"')
            producer.produce(
                topic=messages_topic.name,
                key=kafka_msg.key,
                value=kafka_msg.value,
            )


if __name__ == "__main__":
    main()
