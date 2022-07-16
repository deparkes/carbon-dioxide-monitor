from flask import Flask, render_template
import json
import requests
import plotly
import plotly.graph_objects as go
from plotly.subplots import make_subplots

app = Flask(__name__)

@app.route('/')
def notdash():
    r = requests.get('http://localhost:5000/api')
    data = r.json()
    co2_1 = [x['co2'] for x in data if x['deviceid'] == 1 ]
    temperature_1 = [x['temperature'] for x in data if x['deviceid'] == 1 ]
    timestamp_1 = [x['timestamp'] for x in data if x['deviceid'] == 1]

    fig_1 = make_subplots(specs=[[{'secondary_y': True}]])
    
    fig_1.add_trace(go.Scatter(x=timestamp_1,
                             y=co2_1,
                             name="CO2 (ppm)"),
                             secondary_y=False
                )

    fig_1.add_trace(go.Scatter(x=timestamp_1,
                             y=temperature_1,
                             name="Temperature (deg. C)"),
                             secondary_y=True)
    graphJSON = json.dumps(fig_1, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('dashboard.html', graphJSON=graphJSON)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
