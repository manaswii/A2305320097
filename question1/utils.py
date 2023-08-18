import requests
import os

url = 'http://20.244.56.144/train/trains'

def getData():
    req = requests.get(url, headers= {"Authorization" : os.getenv(key="AUTH_TOKEN")})
    print(req.status_code)
    data = req.json()
    return data
    # implement error handling

