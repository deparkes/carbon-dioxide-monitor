from flask import Flask, render_template
import json
import plotly
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

app = Flask(__name__)

import requests



@app.route('/')
def notdash():
    r = requests.get('http://192.168.0.9:5000/api')
    data = r.json()
    co2 = [x['co2'] for x in data]
    temperature = [x['temperature'] for x in data]
    timestamp = [x['timestamp'] for x in data]
    # Create figure with secondary y-axis
    fig2 = make_subplots(specs=[[{"secondary_y": True}]])

    # Add traces
    fig2.add_trace(
        go.Scatter(x=timestamp, y=co2, name="CO2 (ppm)"),
        secondary_y=False,
    )

    fig2.add_trace(
        go.Scatter(x=timestamp, y=temperature, name="Temperature (deg C)"),
        secondary_y=True,
    )

    graphJSON2 = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)   

    return render_template('notdash.html', graphJSON=graphJSON2)


if __name__ == '__main__':
   app.run(port=3000, debug=True)