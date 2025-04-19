import requests
from twilio.rest import Client

# Twilio credentials (use environment variables in production)
account_sid = "your_twilio_account_sid"
auth_token = "your_twilio_auth_token"

# OpenWeatherMap setup
weather_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "your_openweathermap_api_key"
weather_params = {
    "lat": 40.7440,  # Long Island City, NYC
    "lon": -73.9488,
    "appid": api_key,
    "cnt": 4,  # Next 12 hours (3-hour intervals)
    "units": "metric"
}

# Fetch weather data
weather_response = requests.get(weather_endpoint, params=weather_params)
weather_data = weather_response.json()["list"]

# Track summary info
will_rain = False
descriptions = []
temps = []

# Process forecast
for forecast in weather_data:
    weather_id = forecast["weather"][0]["id"]
    description = forecast["weather"][0]["description"]
    temp = forecast["main"]["temp"]

    descriptions.append(description)
    temps.append(temp)

    if weather_id < 700:
        will_rain = True

# Prepare summary
avg_temp = round(sum(temps) / len(temps))
main_weather = descriptions[0].capitalize()
summary_message = f"Today's forecast: {main_weather}, {avg_temp}°C."
if will_rain:
    summary_message += " Carry an umbrella and stay dry!"

# Send WhatsApp message
client = Client(account_sid, auth_token)
message = client.messages.create(
    from_='whatsapp:+your_twilio_whatsapp_number',
    body=summary_message,
    to='whatsapp:+recipient_whatsapp_number'
)

print(message.status)
