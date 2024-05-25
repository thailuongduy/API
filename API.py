from flask import Flask, jsonify, request
from faker import Faker
import random

app = Flask(__name__)
fake = Faker()

def generate_random_flight():
    return {
        "DAY_OF_MONTH": random.randint(1, 31),
        "DAY_OF_WEEK": random.randint(1, 7),
        "OP_UNIQUE_CARRIER": fake.lexify(text='???'),
        "OP_CARRIER_AIRLINE_ID": random.randint(10000, 99999),
        "OP_CARRIER": fake.lexify(text='??'),
        "TAIL_NUM": fake.bothify(text='??-#####'),
        "OP_CARRIER_FL_NUM": random.randint(1, 9999),
        "ORIGIN_AIRPORT_ID": random.randint(1000, 9999),
        "ORIGIN_AIRPORT_SEQ_ID": random.randint(1000000, 9999999),
        "ORIGIN": fake.city(),
        "DEST_AIRPORT_ID": random.randint(1000, 9999),
        "DEST_AIRPORT_SEQ_ID": random.randint(1000000, 9999999),
        "DEST": fake.city(),
        "DEP_TIME": random.randint(0, 2359),
        "DEP_DEL15": random.choice([0, 1]),
        "DEP_TIME_BLK": fake.time(),
        "ARR_TIME": random.randint(0, 2359),
        "ARR_DEL15": random.choice([0, 1]),
        "CANCELLED": random.choice([0, 1]),
        "DIVERTED": random.choice([0, 1]),
        "DISTANCE": random.randint(50, 5000)
    }

@app.route('/randomflight', methods=['GET'])
def random_flight():
    count = request.args.get('count', default=1, type=int)
    flights = [generate_random_flight() for _ in range(count)]
    return jsonify(flights)

airports = [
    {"id": 1, "name": "Los Angeles International Airport", "code": "LAX", "city": "Los Angeles", "state": "CA"},
    {"id": 2, "name": "John F. Kennedy International Airport", "code": "JFK", "city": "New York", "state": "NY"},
    # Thêm các sân bay khác ở đây
]

airlines = [
    {"id": 1, "name": "Delta Air Lines", "code": "DL"},
    {"id": 2, "name": "American Airlines", "code": "AA"},
    # Thêm các hãng hàng không khác ở đây
]

@app.route('/airports', methods=['GET'])
def get_airports():
    return jsonify(airports)

@app.route('/airlines', methods=['GET'])
def get_airlines():
    return jsonify(airlines)

if __name__ == '__main__':
    app.run(debug=True)
