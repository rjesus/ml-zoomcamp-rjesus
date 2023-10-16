import requests

url = "http://127.0.0.1:5000/predict"
client = {"job": "unknown", "duration": 270, "poutcome": "failure"}
print(requests.post(url, json=client).json())