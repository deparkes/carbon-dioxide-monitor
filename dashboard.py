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

    t3 = [(x['timestamp'], x['value']) for x in data if x['deviceid'] == 3 and x['key'] == 'temperature' ]
    temperature_3 = [x[1] for x in t3]
    timestamp_3 = [x[0] for x in t3]

    h3 = [(x['timestamp'], x['value']) for x in data if x['deviceid'] == 3 and x['key'] == 'humidity' ]
    humidity_3 = [x[1] for x in h3]
    timestamp_h3 = [x[0] for x in h3]


    t4 = [(x['timestamp'], x['value']) for x in data if x['deviceid'] == 4 and x['key'] == 'temperature' ]
    temperature_4 = [x[1] for x in t4]
    timestamp_4 = [x[0] for x in t4]

    h4 = [(x['timestamp'], x['value']) for x in data if x['deviceid'] == 4 and x['key'] == 'humidity' ]
    humidity_4= [x[1] for x in h4]
    timestamp_h4 = [x[0] for x in h4]

    fig_1 = make_subplots(specs=[[{'secondary_y': True}]])
    fig_2 = make_subplots(specs=[[{'secondary_y': True}]])
    fig_3 = make_subplots(specs=[[{'secondary_y': True}]])
    


    fig_1_n = min(len(temperature_1), 8500)
    fig_2_n = min(len(temperature_2), 4000)
    fig_3_n = min(len(temperature_3), 4000)
    fig_4_n = min(len(temperature_4), 4000)
    
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

    fig_3.add_trace(go.Scatter(x=[],
                            y=[],
                            name="CO2 (ppm)"),
                            secondary_y=False)

    fig_3.add_trace(go.Scatter(x=timestamp_3[-fig_3_n:],
                            y=temperature_3[-fig_3_n:],
                            name="Temperaure (dec. C)"),
                            secondary_y=True)

    graphJSON1 = json.dumps(fig_1, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON2 = json.dumps(fig_2, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON3 = json.dumps(fig_3, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('dashboard.html', 
            graphJSON1=graphJSON1,
            graphJSON2=graphJSON2,
            graphJSON3=graphJSON3,
            latest_upstairs_temp=temperature_1[-1],
            latest_downstairs_temp=temperature_2[-1],
            latest_bedroom_temp=temperature_3[-1],
            latest_livingroom_temp=temperature_4[-1]
            )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
