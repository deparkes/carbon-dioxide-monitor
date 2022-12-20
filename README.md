## Setup
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
Activate the virtual environment if you are using it

```
source venv/bin/activate
```


### Start collecting Data

```
bash runapp.sh
```

This assumes you have configured your user to have hidraw access as 
per the CO2Meter readme. If you have followed the instructions and it
still isn't working, you may need to restart your machine/raspberry pi.


### Start sharing data

Run

```
python3 api.py
```

### Start visualising data

Run

```
python3 dashboard.py
```

### Access the dashboard
<ip_address>:3000

### Adding a new MI device
Go to https://atc1441.github.io/TelinkFlasher.html and follow the instructions.

Key steps:
- Turn on the new device
- Click 'Connect' to see available devices
- Select 'pair' for the device you are interested in 
- Click 'Do Activation'
- Download the relevant firmware from https://atc1441.github.io/TelinkFlasher.html
- Click 'Start Flashing'
- Once it finishes flashing, the data should be visible when ble2db.py is run

# Todo
- Check for existing database file and create one if it does not exist
- Explore option for rolling log
- Have single script to run in one go
- Clarify hidraw user settings
- Make IP address for server/raspberry pi configurable e.g. via env var
- Try out other firmware versions - do they output data in the same format?
- Create 'add device' page for dashboard
- Only query a subset of the stored data e.g. 50k rows or 


