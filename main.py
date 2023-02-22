import os

import requests
from dotenv import load_dotenv
load_dotenv()

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

request_body = {
    "query": input("What exercises did you do? "),
    "gender": "male",
    "weight_kg": 72.5,
    "height_cm": 167.64,
    "age": 20
}

nutritionix_exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

response = requests.post(url=nutritionix_exercise_endpoint, json=request_body, headers=headers)
print(response.json())