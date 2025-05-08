# Day 38: Exercise Logger with Nutritionix & Sheety 💪📋

Track your workouts and stay on top of your fitness goals with **Exercise Logger** – a Python script that uses the Nutritionix API to analyze your exercise and logs the data into a Google Sheet via Sheety. See your daily progress in real time! 🏃‍♀️📈

## How It Works

1. **User Input**: You describe your workout (e.g., "ran 3km and did 10 pushups").
2. **Nutritionix API**: Parses your input, calculates calories burned and duration.
3. **Sheety API**: Logs your exercise data with date and time into a Google Sheet.
4. **Progress Summary**: Calculates total calories and duration for the day vs. your goals.

## Example Output

```text
Tell me which exercises you did: jogged 20 minutes and biked 5km

--- Daily Goal Summary ---
Total Calories Burned: 320.4 / 300
Total Duration: 35.0 min / 30 min
🔥 You've reached your calorie goal!
⏱️ You've hit your duration goal!
```

## Features

- 📥 Natural language input for exercises  
- 🔥 Automatic calorie and duration tracking with Nutritionix  
- 📊 Logs activity to a Google Sheet using Sheety  
- ✅ Tracks daily goals for calories and duration  
- 🕒 Smart summary of remaining effort to hit targets  

## How to Use

1. Clone the repo:
   ```bash
   git clone https://github.com/thupham96/100-python-projects.git
   cd Day38_ExerciseLogger
   ```

2. Replace API credentials in the script:
   - `APP_ID` and `API_KEY` from [Nutritionix](https://www.nutritionix.com/business/api)
   - `SHEETY_ENDPOINT` and `BEARER_TOKEN` from [Sheety](https://sheety.co)

3. Set your weight, height, and age for accurate calculation.

4. Run the script:
   ```bash
   python exercise_logger.py
   ```

5. Follow the prompt to describe your workout.

## Technologies Used

- Python 3
- `requests` for API communication
- [Nutritionix API](https://developer.nutritionix.com/) for exercise data
- [Sheety API](https://sheety.co/) for spreadsheet logging

## What I Learned

- Parsing user-friendly input with NLP-backed APIs
- Managing multiple API calls in one script
- Using `datetime` for timestamped entries
- Summarizing progress and comparing to daily goals
- Automating fitness tracking with Google Sheets

---

Build better habits with smarter tracking — **Exercise Logger** helps you get one rep closer to your goals every day! 🏋️‍♂️📆
