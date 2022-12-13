import sqlite3
from flask import Flask, request, make_response, jsonify
import io
import os
import csv

app = Flask(__name__)

database_name = 'co2meter.db'

def get_db():
    conn = sqlite3.connect(database_name)
    return conn

def get_data():
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT * FROM data"
    cursor.execute(statement)
    return cursor.fetchall()

def get_data_multi_sensor():
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT * FROM data_multi_sensor"
    cursor.execute(statement)
    return cursor.fetchall()

@app.route('/api')
def api():
    data = get_data()
    columns = ['timestamp', 'co2', 'temperature', 'deviceid']
    result =  [{'timestamp': row[0], 'co2': row[1], 'temperature': row[2], 'deviceid': row[3]} for row in data]    
    return jsonify(result)

@app.route('/api/v2')
def api_v2():
    data = get_data_multi_sensor()
    columns = ['timestamp', 'deviceid', 'key', 'value']
    result =  [{'timestamp': row[0], 'deviceid': row[1], 'key': row[2], 'value': row[3]} for row in data]    
    return jsonify(result)

@app.route('/')
def myapp():
    message = "To use this app: %sapi" % request.base_url
    return message

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
