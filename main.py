import requests
from datetime import datetime
import os

APP_ID = 'e03d864e'
API_KEY = os.environ['APIKEY']
BASE_API_ENDPOINT = 'https://trackapi.nutritionix.com'
natural_exercise_url = '/v2/natural/exercise'
now = datetime.now()
TODAY = now.strftime('%d/%m/%Y')
now_time = now.strftime('%X')

headers = {
    'x-app-key': API_KEY,
    'x-app-id': APP_ID,
}
parameters = {
    'query': input('what exercises you have done today'),
    'gender': 'male',
    'weight_kg': 87,
    'height_cm': 180,
    'age': 20
}

response = requests.post(url=f'{BASE_API_ENDPOINT}{natural_exercise_url}', json=parameters, headers=headers)
response.raise_for_status()
data = response.json()

BASE_UPLOAD_SHEETS_URL = 'https://api.sheety.co/69f888dcecb38a8884b36ac1e4dc15fd/copyOfMyWorkouts/workouts'

sheety_parameters = {
    "workout": {
        "date": TODAY,
        'time': now_time,
        'exercise': data['exercises'][0]['name'],
        'duration': data['exercises'][0]['duration_min'],
        'calories': data['exercises'][0]['nf_calories']
    }
}
headers = {
    'Authorization': os.environ['BEARER']
}

shetty_response = requests.post(url=BASE_UPLOAD_SHEETS_URL, json=sheety_parameters, headers=headers)
print(shetty_response.text)
