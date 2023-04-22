import os
import requests
from datetime import datetime

API_ID = os.environ['NUTRITION_API_ID']
API_KEY = os.environ['NUTRITION_API_KEY']
USER_ID = 0
URL = 'https://trackapi.nutritionix.com'
SHEETY_TOKEN = os.environ['SHEETY_TOKEN']

headers = {
    'x-app-id': API_ID,
    'x-app-key': API_KEY,
    'x-remote-user-id': '0'
}

body = {
    "query": input("What do you do?")
}

endpoint = '/v2/natural/exercise'

response = requests.post(f"{URL}{endpoint}", json = body, headers = headers)
response.raise_for_status()
data = response.json()

date_format = "%Y/%m/%d"
date = datetime.now().strftime(date_format)

time_format = "%X"
time = datetime.now().strftime(time_format)

exercises = data["exercises"]

workouts = [{"workout": {
    "date": date,
    "time": time,
    "exercise": exercise["name"].title(),
    "duration": f'{round(exercise["duration_min"])}',
    "calories": f'{round(exercise["nf_calories"])}'

}} for exercise in exercises]

request_sheet_headers = {
    'Authorization': SHEETY_TOKEN
}

for workout in workouts:
    response_sheet = requests.post(url = 'https://api.sheety.co/715b37d5c4b06c54b6a983d5c287dd34/myWorkout/workouts', json = workout, headers=request_sheet_headers)
    response_sheet.raise_for_status()

print("Complete!")