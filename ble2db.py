import json
import sqlite3
from datetime import datetime

try:
    with open('test.file', 'r') as f:
        last_line = f.readlines()[-1]

        last_line = last_line.strip("Temperature info").replace("'", '"')

        json_line = json.loads(last_line)

        conn = sqlite3.connect("co2meter.db")
        cursor = conn.cursor()

        cursor.executemany("INSERT INTO data VALUES (?,?,?,?)",
                [(datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    None,
                    json_line['temperature'],
                    2)
                 ]
                )
        conn.commit()
except:
    print("Unable to load ble data")
