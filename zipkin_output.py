import json
import pandas
import requests
import sys
import time

start_time = int(time.time() * 1000)
lookback = 2 * int(sys.argv[1]) * 1000
name = sys.argv[2]
epcho = sys.argv[3]

url = "http://119.23.52.13:9411/zipkin/api/v2/traces?endTs={0}&limit={2}&lookback={1}".format(start_time, lookback,
                                                                                              epcho)
print(url)
response = requests.get(url)
data = response.text
data = json.loads(data)
json_data = []

for i in data:
    api_dict = {}
    for j in reversed(i):
        try:
            json_data.append(dict(api=j["tags"]["http.path"], duration=j["duration"]))
        except:
            continue
data_frame = pandas.DataFrame(data=json_data)
data_frame.to_csv("json_data_{0}.csv".format(name), index=False)
