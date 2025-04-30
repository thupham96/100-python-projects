import requests
from datetime import datetime
import os

# ----------------------------- #
#         CONFIGURATION         #
# ----------------------------- #

# Load credentials from environment variables for security
APP_ID = os.getenv("NUTRITIONIX_APP_ID")
API_KEY = os.getenv("NUTRITIONIX_API_KEY")
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")
BEARER_TOKEN = os.getenv("SHEETY_BEARER_TOKEN")

# User profile info for exercise calculations
WEIGHT_KG = 55
HEIGHT_CM = 160
AGE = 29

# Sheety headers for authentication
sheety_headers = {
    "Authorization": f"Bearer {BEARER_TOKEN}"
}

# Daily goals
DAILY_CALORIE_GOAL = 300
DAILY_DURATION_GOAL = 30  # in minutes

# ----------------------------- #
#     USER INPUT & NUTRITIONIX  #
# ----------------------------- #

# Get exercise description from user
exercise_text = input("Tell me which exercises you did: ")

# Build headers and payload for Nutritionix API
nutritionix_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

exercise_params = {
    "query": exercise_text,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

# Call Nutritionix API
response = requests.post(
    url="https://trackapi.nutritionix.com/v2/natural/exercise",
    json=exercise_params,
    headers=nutritionix_headers
)
result = response.json()
exercises = result["exercises"]

# ----------------------------- #
#      DATE & EXISTING LOGS     #
# ----------------------------- #

# Get current date and time
today = datetime.now()
today_date = today.strftime("%m/%d/%Y")
current_time = today.strftime("%H:%M:%S")

# Fetch existing entries from Sheety
sheet_data = requests.get(url=SHEETY_ENDPOINT, headers=sheety_headers).json()
all_rows = sheet_data.get("sheet1", [])

# Initialize daily totals from existing entries
total_calories = 0
total_duration = 0

for row in all_rows:
    if row['date'] == today_date:
        total_calories += float(row["calories"])
        total_duration += float(row["duration"])

# ----------------------------- #
#     LOG NEW EXERCISES & SUM   #
# ----------------------------- #

for exercise in exercises:
    # Add new exercise to Sheety
    sheet_inputs = {
        "sheet1": {
            "date": today_date,
            "time": current_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    # Update daily totals with new exercise
    total_calories += exercise["nf_calories"]
    total_duration += exercise["duration_min"]

    # Send data to Sheety
    sheet_response = requests.post(url=SHEETY_ENDPOINT, json=sheet_inputs, headers=sheety_headers)

# ----------------------------- #
#         GOAL SUMMARY          #
# ----------------------------- #

print("\n--- Daily Goal Summary ---")
print(f"Total Calories Burned: {total_calories:.1f} / {DAILY_CALORIE_GOAL}")
print(f"Total Duration: {total_duration:.1f} min / {DAILY_DURATION_GOAL} min")

if total_calories >= DAILY_CALORIE_GOAL:
    print("🔥 You've reached your calorie goal!")
else:
    print(f"💪 {DAILY_CALORIE_GOAL - total_calories:.1f} calories to go!")

if total_duration >= DAILY_DURATION_GOAL:
    print("⏱️ You've hit your duration goal!")
else:
    print(f"🕒 {DAILY_DURATION_GOAL - total_duration:.1f} minutes to go!")
