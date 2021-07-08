import requests
import json

def test_api():
    url = "http://0.0.0.0:8083"
    payload = {}
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url, headers=headers, data=json.dumps(payload))
    return response.content


test_api()