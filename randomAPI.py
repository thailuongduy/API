from flask import Flask, jsonify, request
import pandas as pd
import random
from collections import OrderedDict

app = Flask(__name__)

# Đọc dữ liệu từ file CSV
airlines_df = pd.read_csv('C:\\Users\\thail\\Music\\data\\jan_2019_ontime.csv')

# Chuyển dữ liệu từ DataFrame sang danh sách từ điển
airlines = airlines_df.to_dict(orient='records')

# Hàm tạo chuyến bay ngẫu nhiên từ dữ liệu thật
def generate_random_flight():
    flight = random.choice(airlines)
    
    return OrderedDict([
        ("DAY_OF_MONTH", flight["DAY_OF_MONTH"]),
        ("DAY_OF_WEEK", flight["DAY_OF_WEEK"]),
        ("OP_UNIQUE_CARRIER", flight["OP_UNIQUE_CARRIER"]),
        ("OP_CARRIER_AIRLINE_ID", flight["OP_CARRIER_AIRLINE_ID"]),
        ("OP_CARRIER", flight["OP_CARRIER"]),
        ("TAIL_NUM", flight["TAIL_NUM"]),
        ("OP_CARRIER_FL_NUM", flight["OP_CARRIER_FL_NUM"]),
        ("ORIGIN_AIRPORT_ID", flight["ORIGIN_AIRPORT_ID"]),
        ("ORIGIN_AIRPORT_SEQ_ID", flight["ORIGIN_AIRPORT_SEQ_ID"]),
        ("ORIGIN", flight["ORIGIN"]),
        ("DEST_AIRPORT_ID", flight["DEST_AIRPORT_ID"]),
        ("DEST_AIRPORT_SEQ_ID", flight["DEST_AIRPORT_SEQ_ID"]),
        ("DEST", flight["DEST"]),
        ("DEP_TIME", flight["DEP_TIME"]),
        ("DEP_DEL15", flight["DEP_DEL15"]),
        ("DEP_TIME_BLK", flight["DEP_TIME_BLK"]),
        ("ARR_TIME", flight["ARR_TIME"]),
        ("ARR_DEL15", flight["ARR_DEL15"]),
        ("CANCELLED", flight["CANCELLED"]),
        ("DIVERTED", flight["DIVERTED"]),
        ("DISTANCE", flight["DISTANCE"])
    ])

@app.route('/randomflight', methods=['GET'])
def random_flight():
    count = request.args.get('count', default=1, type=int)
    flights = [generate_random_flight() for _ in range(count)]
    return jsonify(flights)

@app.route('/airports', methods=['GET'])
def get_airports():
    return jsonify(airlines)

@app.route('/airlines', methods=['GET'])
def get_airlines():
    return jsonify(airlines)

if __name__ == '__main__':
    app.run(debug=True)
