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
        cursor.execute("SELECT * FROM devices WHERE identifier=?", (json_line['mac address'],))
        rows = cursor.fetchall()
        deviceid = rows[0][0]
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.executemany("INSERT INTO data VALUES (?,?,?,?)",
                [(timestamp,
                    None,
                    json_line['temperature'],
                    deviceid)
                 ]
                )

        cursor.executemany("INSERT INTO data_multi_sensor VALUES (?,?,?,?)",
                [(timestamp,
                    deviceid,
                    'temperature',
                    json_line['temperature'],
                    )
                    ]
                    )

        cursor.executemany("INSERT INTO data_multi_sensor VALUES (?,?,?,?)",
                [(timestamp,
                    deviceid,
                    'humidity',
                    json_line['humidity'],
                    )
                    ]
                    )

        conn.commit()
except Exception as e:
    print("Unable to load ble data")
    print(e)
