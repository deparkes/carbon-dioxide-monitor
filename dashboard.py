from flask import Flask, render_template
import json
import requests
import plotly
import plotly.graph_objects as go
from plotly.subplots import make_subplots

app = Flask(__name__)

@app.route('/')
def notdash():
    r = requests.get('http://localhost:5000/api/v2')
    data = r.json()
    co2_1 = [(x['timestamp'], x['value']) for x in data if x['deviceid'] == 1 and x['key'] == 'co2' ]
    co2_1 = [x[1] for x in co2_1]


    t1 = [(x['timestamp'], x['value']) for x in data if x['deviceid'] == 1 and x['key'] == 'temperature' ]
    temperature_1 = [x[1] for x in t1]
    timestamp_1 = [x[0] for x in t1]

    t2 = [(x['timestamp'], x['value']) for x in data if x['deviceid'] == 2 and x['key'] == 'temperature' ]
    temperature_2 = [x[1] for x in t2]
    timestamp_2 = [x[0] for x in t2]

    h2 = [(x['timestamp'], x['value']) for x in data if x['deviceid'] == 2 and x['key'] == 'humidity' ]
    humidity_2 = [x[1] for x in h2]
    timestamp_h2 = [x[0] for x in h2]

    b2 = [(x['timestamp'], x['value']) for x in data if x['deviceid'] == 2 and x['key'] == 'battery' ]
    battery_2 = [x[1] for x in b2]
    timestamp_b2 = [x[0] for x in b2]   

    r2 = [(x['timestamp'], x['value']) for x in data if x['deviceid'] == 2 and x['key'] == 'rssi' ]
    rssi_2 = [x[1] for x in r2]
    timestamp_r2 = [x[0] for x in r2]

    t3 = [(x['timestamp'], x['value']) for x in data if x['deviceid'] == 3 and x['key'] == 'temperature' ]
    temperature_3 = [x[1] for x in t3]
    timestamp_3 = [x[0] for x in t3]

    h3 = [(x['timestamp'], x['value']) for x in data if x['deviceid'] == 3 and x['key'] == 'humidity' ]
    humidity_3 = [x[1] for x in h3]
    timestamp_h3 = [x[0] for x in h3]

    b3 = [(x['timestamp'], x['value']) for x in data if x['deviceid'] == 3 and x['key'] == 'battery' ]
    battery_3 = [x[1] for x in b3]
    timestamp_b3 = [x[0] for x in b3] 

    r3 = [(x['timestamp'], x['value']) for x in data if x['deviceid'] == 3 and x['key'] == 'rssi' ]
    rssi_3 = [x[1] for x in r3]
    timestamp_r3 = [x[0] for x in r3]

    t4 = [(x['timestamp'], x['value']) for x in data if x['deviceid'] == 4 and x['key'] == 'temperature' ]
    temperature_4 = [x[1] for x in t4]
    timestamp_4 = [x[0] for x in t4]

    h4 = [(x['timestamp'], x['value']) for x in data if x['deviceid'] == 4 and x['key'] == 'humidity' ]
    humidity_4= [x[1] for x in h4]
    timestamp_h4 = [x[0] for x in h4]

    b4 = [(x['timestamp'], x['value']) for x in data if x['deviceid'] == 4 and x['key'] == 'battery' ]
    battery_4 = [x[1] for x in b4]
    timestamp_b4 = [x[0] for x in b4] 

    r4 = [(x['timestamp'], x['value']) for x in data if x['deviceid'] == 4 and x['key'] == 'rssi' ]
    rssi_4 = [x[1] for x in r4]
    timestamp_r4 = [x[0] for x in r4]

    t5 = [(x['timestamp'], x['value']) for x in data if x['deviceid'] == 5 and x['key'] == 'temperature' ]
    temperature_5 = [x[1] for x in t5]
    timestamp_5 = [x[0] for x in t5]

    h5 = [(x['timestamp'], x['value']) for x in data if x['deviceid'] == 5 and x['key'] == 'humidity' ]
    humidity_5= [x[1] for x in h5]
    timestamp_h5 = [x[0] for x in h5]

    b5 = [(x['timestamp'], x['value']) for x in data if x['deviceid'] == 5 and x['key'] == 'battery' ]
    battery_5 = [x[1] for x in b5]
    timestamp_b5 = [x[0] for x in b5] 

    r5 = [(x['timestamp'], x['value']) for x in data if x['deviceid'] == 5 and x['key'] == 'rssi' ]
    rssi_5 = [x[1] for x in r5]
    timestamp_r5 = [x[0] for x in r5]

    fig_1 = make_subplots(specs=[[{'secondary_y': True}]])
    fig_2 = make_subplots(specs=[[{'secondary_y': True}]])
    fig_3 = make_subplots(specs=[[{'secondary_y': True}]])
    fig_4 = make_subplots(specs=[[{'secondary_y': True}]])
    fig_5 = make_subplots(specs=[[{'secondary_y': True}]])

    fig_1_n = min(len(temperature_1), 8500)
    fig_2_n = min(len(temperature_2), 4000)
    fig_3_n = min(len(temperature_3), 4000)
    fig_4_n = min(len(temperature_4), 4000)
    fig_5_n = min(len(temperature_5), 4000)


    # Temperature
    fig_1.add_trace(go.Scatter(x=timestamp_1[-fig_1_n:],
                             y=temperature_1[-fig_1_n:],
                             name="Nook (deg. C)"),
                             secondary_y=False
                )

    fig_1.add_trace(go.Scatter(x=timestamp_2[-fig_2_n:],
                             y=temperature_2[-fig_2_n:],
                             name="Middle Room (deg. C)"),
                             secondary_y=False)

    fig_1.add_trace(go.Scatter(x=timestamp_3[-fig_3_n:],
                             y=temperature_3[-fig_3_n:],
                             name="Bedroom (deg. C)"),
                             secondary_y=False)

    fig_1.add_trace(go.Scatter(x=timestamp_4[-fig_4_n:],
                             y=temperature_4[-fig_4_n:],
                             name="Living room (deg. C)"),
                             secondary_y=False)

    fig_1.add_trace(go.Scatter(x=timestamp_5[-fig_5_n:],
                             y=temperature_5[-fig_5_n:],
                             name="Kitchen (deg. C)"),
                             secondary_y=False)                         

    # Humidity
    fig_2.add_trace(go.Scatter(x=[],
                            y=[],
                             name="Nook (%)"),
                             secondary_y=False)

    fig_2.add_trace(go.Scatter(x=timestamp_h2[-fig_2_n:],
                            y=humidity_2[-fig_2_n:],
                             name="Middle Room (%)"),
                             secondary_y=False)

    fig_2.add_trace(go.Scatter(x=timestamp_h3[-fig_3_n:],
                            y=humidity_3[-fig_3_n:],
                            name="Bedroom (%)"),
                            secondary_y=False)

    fig_2.add_trace(go.Scatter(x=timestamp_h4[-fig_4_n:],
                            y=humidity_4[-fig_4_n:],
                            name="Living room (%)"),
                            secondary_y=False)

    fig_2.add_trace(go.Scatter(x=timestamp_h5[-fig_5_n:],
                            y=humidity_5[-fig_5_n:],
                            name="Kitchen (%)"),
                            secondary_y=False)

    # Co2
    fig_3.add_trace(go.Scatter(x=timestamp_1[-fig_1_n:],
                            y=co2_1[-fig_1_n:],
                            name="CO2 (ppm)"),
                            secondary_y=False)


    # Battery
    fig_4.add_trace(go.Scatter(x=[],
                            y=[],
                             name="Nook"),
                             secondary_y=False)

    fig_4.add_trace(go.Scatter(x=timestamp_b2[-fig_2_n:],
                            y=battery_2[-fig_2_n:],
                             name="Middle Room (%)"),
                             secondary_y=False)

    fig_4.add_trace(go.Scatter(x=timestamp_b3[-fig_3_n:],
                            y=battery_3[-fig_3_n:],
                            name="Bedroom (%)"),
                            secondary_y=False)

    fig_4.add_trace(go.Scatter(x=timestamp_b4[-fig_4_n:],
                            y=battery_4[-fig_4_n:],
                            name="Living room (%)"),
                            secondary_y=False)

    fig_4.add_trace(go.Scatter(x=timestamp_b5[-fig_5_n:],
                            y=battery_5[-fig_5_n:],
                            name="Kitchen (%)"),
                            secondary_y=False)

    # RSSI
    fig_5.add_trace(go.Scatter(x=[],
                            y=[],
                             name="Nook"),
                             secondary_y=False)

    fig_5.add_trace(go.Scatter(x=timestamp_r2[-fig_2_n:],
                            y=rssi_2[-fig_2_n:],
                             name="Middle Room"),
                             secondary_y=False)

    fig_5.add_trace(go.Scatter(x=timestamp_r3[-fig_3_n:],
                            y=rssi_3[-fig_3_n:],
                            name="Bedroom"),
                            secondary_y=False)

    fig_5.add_trace(go.Scatter(x=timestamp_r4[-fig_4_n:],
                            y=rssi_4[-fig_4_n:],
                            name="Living room"),
                            secondary_y=False)

    fig_5.add_trace(go.Scatter(x=timestamp_r5[-fig_5_n:],
                            y=rssi_5[-fig_5_n:],
                            name="Kitchen"),
                            secondary_y=False)

    graphJSON1 = json.dumps(fig_1, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON2 = json.dumps(fig_2, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON3 = json.dumps(fig_3, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON4 = json.dumps(fig_4, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON5 = json.dumps(fig_5, cls=plotly.utils.PlotlyJSONEncoder)    

    return render_template('dashboard.html', 
            graphJSON1=graphJSON1,
            graphJSON2=graphJSON2,
            graphJSON3=graphJSON3,
            graphJSON4=graphJSON4,
            graphJSON5=graphJSON5,
            latest_upstairs_temp=temperature_1[-1],
            latest_downstairs_temp=temperature_2[-1],
            latest_bedroom_temp=temperature_3[-1],
            latest_livingroom_temp=temperature_4[-1],
            latest_kitchen_temp=temperature_5[-1]
            )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
