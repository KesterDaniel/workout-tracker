import os
import datetime as dt
import requests
from dotenv import load_dotenv
load_dotenv()
today = dt.datetime.now()

# IMPORTANT KEYS
APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")

# API ENDPOINTS
sheety_endpoint = "https://api.sheety.co/67381695094c88fc68cb8d316be6f66a/myWorkouts/workouts"
nutritionix_exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"


# HEADERS
sheety_header = {
    "Content-Type": "application/json",
    "Authorization": os.getenv("AUTHORIZATION")
}

nutritionix_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

# CONFIDENTIAl 😎
nutritionix_request_body = {
    "query": input("What exercises did you do? "),
    "gender": "male",
    "weight_kg": 72.5,
    "height_cm": 167.64,
    "age": 20
}

# Getting Exercise data using nutritionix API natural language processing
exercise_response = requests.post(url=nutritionix_exercise_endpoint, json=nutritionix_request_body, headers=nutritionix_headers)
exercise_response.raise_for_status()
exercise_data = exercise_response.json()

# Adding a row for each exercise to spreadsheet using sheety API.(sheety sounds funny LOL)
for exercise in exercise_data["exercises"]:
    shetty_params = {
        "workout": {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%I:%M"),
            "exercise": exercise["name"],
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    shetty_response = requests.post(url=sheety_endpoint, json=shetty_params, headers=sheety_header)
    shetty_response.raise_for_status()
    shetty_data = shetty_response.json()
    print(shetty_data)