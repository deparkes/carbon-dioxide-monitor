#!/bin/env python
import time
import sqlite3
from datetime import datetime

import CO2Meter

Meter = CO2Meter.CO2Meter("/dev/hidraw0")
conn = sqlite3.connect("co2meter.db")
cursor = conn.cursor()
no_measurement = True
while no_measurement:
#for i in range(3):
    measurement = Meter.get_data()
    measurement.update({'timestamp': datetime.now()})
    try:
        print(measurement['timestamp'].strftime("%Y-%m-%d %H:%M:%S"),
        measurement['co2'], 
        measurement['temperature'],
        sep=","
        )
        
        cursor.executemany("INSERT INTO data VALUES (?,?,?)",
                [(measurement['timestamp'].strftime("%Y-%m-%d %H:%M:%S"),
                    measurement['co2'],
                    measurement['temperature'])]
                    )
        conn.commit()
        no_measurement = False

    except Exception as e:
        #print(str(e))
        pass # not all calls result in data to display
#time.sleep(1)
