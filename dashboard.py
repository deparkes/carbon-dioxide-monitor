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
    co2 = [x['co2'] for x in data]
    temperature = [x['temperature'] for x in data]
    timestamp = [x['timestamp'] for x in data]

    fig = make_subplots(specs=[[{'secondary_y': True}]])
    
    fig.add_trace(go.Scatter(x=timestamp,
                             y=co2,
                             name="CO2 (ppm)"),
                             secondary_y=False
                )

    fig.add_trace(go.Scatter(x=timestamp,
                             y=temperature,
                             name="Temperature (deg. C)"),
                             secondary_y=True)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('dashboard.html', graphJSON=graphJSON)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
