import os
import random
import time
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



def main():
    # take off point
    x = 0
    y = 0
    a = DRONE_ID # the slope of flight proxy with the DRONE_ID
    with app.get_producer() as producer:
        while True:
            x = x + 1
            y = y + a + random.random() - .5

            message = {"drone_id": DRONE_ID, "X":x, "Y":y}
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
            time.sleep(1)


if __name__ == "__main__":
    main()
