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
    
@app.route('/api')
def api():
    data = get_data()
    columns = ['timestamp', 'co2', 'temperature']
    result =  [{'timestamp': row[0], 'co2': row[1], 'temperature': row[2]}for row in data]    
    return jsonify(result)

@app.route('/')
def myapp():
    message = "To use this app: %sapi" % request.base_url
    return message

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
