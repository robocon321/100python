import requests

url = 'http://api.open-notify.org/iss-now.json'
response = requests.get(url = url)
response.raise_for_status()
data = response.json()

position = (data["iss_position"]["longitude"], data["iss_position"]["latitude"])

print(position)