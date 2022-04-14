Suggested to create a virtual environment

```
python3 -m venv venv
```

Activate this environment with

```
source venv/bin/activate
```

Into this virtual environment install CO2Meter

```
pip install git+https://github.com/heinemml/CO2Meter
```

You may find that you need to install 'wheel' first:

```
pip3 install wheel
```

Other dependencies:

```
flask (for dashboard and json API)
plotly (for dashboard)
requests (for dashboard)
```

## Usage

### Start collecting Data

```
bash getdata.sh
```

This assumes you have configured your user to have hidraw access as 
per the CO2Meter readme. If you have followed the instructions and it
still isn't working, you may need to restart your machine/raspberry pi.


### Start sharing data

Run

```
python3 myapp.py
```

### Start visualising data

Run

```
python3 dashboard.py
```
