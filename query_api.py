import requests

r = requests.get('http://localhost:5000/api/v2')
data = r.json()

data2 = [
    {'deviceid': 1,
        'key': 'temperature',
        'timestamp': '2022-03-30 18:54:05', 
        'value': 17.7},
    {'deviceid': 1, 
        'key': 'temperature', 
        'timestamp': '2022-03-30 19:03:22',
        'value': 17.6},
    {'deviceid': 1, 
        'key': 'temperature',
        'timestamp': '2022-03-30 19:12:02', 
        'value': 17.6}, 
    {'deviceid': 1,
        'key': 'temperature',
        'timestamp': '2022-03-30 19:15:58', 
        'value': 17.6},
    {'deviceid': 2, 
        'key': 'temperature',
        'timestamp': '2022-03-30 19:25:11', 
        'value': 17.6}]

#print(data[:5])

# timestamp_1, temperature_1  = [(x['timestamp'], x['value']) for x in data if x['deviceid'] == 1 ]
x  = [(x['timestamp'], x['value']) for x in data if x['key']=='co2']


temperature_1 = [(x['timestamp'], x['value']) for x in data if x['deviceid'] == 1 and x['key'] == 'temperature' ]
temperature_1 = [x[1] for x in temperature_1]
timestamp_1 = [x[0] for x in temperature_1]

timestamp = [x[0] for x in x]
temperature = [x[1] for x in x]
print(x[:5])
print(temperature_1[:5])