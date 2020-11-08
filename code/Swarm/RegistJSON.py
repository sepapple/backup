import requests
import json

def read():
    url = 'http://localhost:8500/bzz:/'
    dicdata = {
            "time": 1601095328458,
            "lat": 34.7631232,
            "lon": 135.4791424,
            "accel_x": {
                "1": -0.0670013,
                "2": -0.0670013,
                "3": 0.1962127,
                "4": 0.406784,
                "5": -0.0861358,
                "6": -0.2081756,
                "7": 0.3517456,
                "8": 0.2871399,
                "9": -0.1459655,
                "10": -0.0765686
                },
            "accel_y": {
                "1": -2.2994996,
                "2": -3.0915222,
                "3": -2.9718934,
                "4": -2.904892,
                "5": -2.6895294,
                "6": -2.8378906,
                "7": -2.868988,
                "8": -2.778061,
                "9": -2.7302094,
                "10": -2.864212
                },
            "accel_z": {
                "1": 9.6406864,
                "2": 9.006592,
                "3": 9.702896,
                "4": 9.1812592,
                "5": 9.1549376,
                "6": 9.4372864,
                "7": 9.0568392,
                "8": 9.5521544,
                "9": 9.131012,
                "10": 9.1334072
                }
            }

                           
    json_data = json.dumps(dicdata).encode("utf-8")
    result = requests.post(url,json_data,headers={'Content-Type': 'application/json'})
    print(result.text)
    string = result.text
    high = string[:32]
    low = string[32:]
    print(high)
    print(len(high))
    print(low)
    print(len(low))

if __name__ == '__main__':
    read()

