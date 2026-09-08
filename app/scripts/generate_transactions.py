import requests
import random

countries=["IN","US","RU","BR"]

while True:

    payload={

        "amount":random.randint(100,100000),

        "country":random.choice(countries),

        "device":"new"
    }

    requests.post(
        "http://localhost:8000/transactions/",
        json=payload
    )