import pprint

import requests
import json

url="https://api.tvmaze.com/singlesearch/shows"
show=input()
params={"q":show}

response = requests.get(url,params)
if response.status_code==200:
    data = json.loads(response.text)
    # pprint.pprint
    name=data['name']
    premiered=data['premiered']
    print(f"{name} premiered on {premiered}")
else:
    print(f"error:{response.status_code}")