import requests
from datetime import datetime

API_KEY = "1b34b74176e3ff3e60b9e34f4e6dde6d"
API_ID = "f9736751"

API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY
}

query = input("Which exercise(s) have you done?")

parameters = {
    "query": query,
    "weight_kg": 65,
    "height_cm": 171.50,
    "age": 19
}

response = requests.post(url=API_ENDPOINT, headers=headers, json=parameters)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post("https://api.sheety.co/674cdb77c4dfc58e75bed40c9ba3dedc/myWorkouts/workouts", json=sheet_inputs)

    print(sheet_response.text)