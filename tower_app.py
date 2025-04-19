import os
from datetime import datetime

from quixstreams import Application
from quixstreams.kafka.configuration import ConnectionConfig
from quixstreams.sinks.community.postgresql import PostgreSQLSink
# from quixstreams.models.topics.admin import TopicAdmin

# from mysqldb_lib import insert_into_mysql

DRONE_QUANTITY = int(os.getenv("DRONE_QUANTITY", "7"))
connection = ConnectionConfig(
    bootstrap_servers="PLAINTEXT://kafka:9092",
)

app = Application(
    broker_address=connection,
    consumer_group="text-splitter-v1",
    auto_offset_reset="earliest",
    )

postgres_sink = PostgreSQLSink(
    host="postgres-db",
    port=5432,
    dbname="mydatabase",
    user="appuser",
    password="password",
    table_name="drone_coordinate",
    schema_auto_update=True
)

def read_topic(topic_name):
    # Define a topic with chat messages in JSON format
    messages_topic = app.topic(name=topic_name, value_deserializer="json")

    # Create a StreamingDataFrame - the stream processing pipeline
    # with a Pandas-like interface on streaming data
    sdf = app.dataframe(topic=messages_topic)

    # Print the input data
    sdf = sdf.update(lambda message: print(f"INPUT:  {message}"))
    sdf = sdf[["drone_id","X", "Y"]]
    sdf["timestamp_received"]= sdf.apply(lambda data: datetime.now().__str__())

    sdf.sink(postgres_sink)
    sdf = sdf.update(lambda row: print(f"TRANSFORM: {row}"))

for drone_id in range(1, DRONE_QUANTITY+1):
    topic = f"drone_{drone_id}"
    read_topic(topic)
    print(f"Topic created: {topic}")

# Run the streaming application
if __name__ == "__main__":
    app.run()