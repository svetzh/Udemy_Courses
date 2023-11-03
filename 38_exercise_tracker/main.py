import requests
from datetime import datetime as dt
import os
from dotenv import load_dotenv


AGE = 39
GENDER = "male"
WEIGHT = 89.3
HEIGHT = 180

APP_ID = os.environ["NUTRI_APP_ID"]  # NUTRI_APP_ID
API_KEY = os.environ["NUTRI_API_KEY"]  # NUTRI_API_KEY

# SHEETY_USERNAME = "svet"
# SHEETY_PASSWORD = "jWfWwwxZI3UcQezoiDzc"


exercises_txt = input("Tell me which exercises you did: ")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = os.environ["SHEET_ENDPOINT"]

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

params = {
    "query": exercises_txt,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
}

response = requests.post(exercise_endpoint, json=params, headers=headers)
res = response.json()


today_date = dt.now().strftime("%d-%m-%Y")

# Sheety Project API. Check your Google sheet name and Sheety endpoint
now_time = dt.now().strftime("%X")
bearer_headers = {
    "Authorization": f"Bearer {os.environ['TOKEN']}"
}



for ex in res["exercises"]:
    sheet_inputs = {
        'workouts': {
            "date": today_date,
            "time": now_time,
            "exercise": ex["name"].title(),
            "duration": ex["duration_min"],
            "calories": ex["nf_calories"]
        }
    }
    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        headers=bearer_headers
        )

    print(f"Sheety Response: \n{sheet_response.text}")