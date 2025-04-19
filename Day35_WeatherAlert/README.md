# Day 35: Weather Alert with Twilio ☁️📱

Stay ahead of the weather with **Weather Alert** – a Python script that checks your local forecast and sends real-time alerts via WhatsApp using the Twilio API. Ideal for daily reminders to bring an umbrella or dress accordingly! 🌦️🔔

## How It Works

1. **Weather Forecast Fetching**: Pulls the next 12 hours of weather data (3-hour intervals) from OpenWeatherMap.
2. **Rain Detection**: Checks for any precipitation codes in the forecast.
3. **Summary Generation**: Averages temperatures and summarizes weather descriptions.
4. **WhatsApp Notification**: Sends a custom alert message using Twilio if rain is detected or just to share daily weather info.

## Example Output

- **Location**: Long Island City, NYC  
- **Forecast**:  
  ```text
  Today's forecast: Light rain, 21°C. Carry an umbrella and stay dry!
  ```
- **Delivery**: Sent directly to your WhatsApp using the Twilio number.

## Features

- ☁️ Real-time weather data from OpenWeatherMap
- 🌡️ Temperature averaging for daily summary
- 🌧️ Rain detection logic based on weather codes
- 📲 Twilio WhatsApp integration for instant alerts
- 🔁 Runs daily or on-demand

## How to Use

1. Clone or download the script:
   ```bash
   git clone https://github.com/thupham96/python-projects.git
   cd Day35_WeatherAlert
   ```

2. Replace credentials with your own in a `.env` file or directly in the script (not recommended for production):
   - `account_sid`, `auth_token` from Twilio
   - `api_key` from OpenWeatherMap

3. Run the script:
   ```bash
   python weather_alert.py
   ```

## Technologies Used

- Python 3
- `requests` for API calls
- `twilio` for WhatsApp messaging
- OpenWeatherMap API (https://openweathermap.org/)
- WhatsApp Business API via Twilio

## What I Learned

- Interacting with external APIs and handling JSON responses
- Automating alerts via WhatsApp using Twilio
- Processing and summarizing time-series weather data
- Using conditional logic to trigger smart notifications
- Writing scripts with real-world utility

Stay informed and dry with **Weather Alert** – the forecast is now just a ping away! ☔📩
