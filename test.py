import requests

url = "https://sensor-stream.onrender.com/reading"

payload = {
    "x_value": 1,
    "y_value": 2.3,
}

headers = {"content-type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print(response.text)