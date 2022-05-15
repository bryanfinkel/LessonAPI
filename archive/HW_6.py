import requests
import json

url = "http://127.0.0.1:8000/api/v1/math/add"

payload = "{\n   \"variable1\": 21\n   \"variable2\": 3\n}"
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
