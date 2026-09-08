from kafka import KafkaConsumer

import json

consumer = KafkaConsumer(

    "transactions",

    bootstrap_servers="localhost:9094",

    value_deserializer=lambda m: json.loads(m.decode())

)

for message in consumer:

    tx = message.value

    print("Received:",tx)

    # later:
    # score transaction
    # save to postgres
    # cache in redis
    # broadcast websocket