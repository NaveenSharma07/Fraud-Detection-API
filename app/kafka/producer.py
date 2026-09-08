from kafka import KafkaProducer

from faker import Faker

import json
import time
import random

fake = Faker()

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode()
)

while True:

    transaction = {

        "amount":random.randint(100,100000),

        "country":fake.country_code(),

        "device":random.choice(["known","new"])
    }

    producer.send("transactions",transaction)

    print(transaction)

    time.sleep(1)