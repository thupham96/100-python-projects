# Import required libraries
import requests
from datetime import datetime
import smtplib
import time

# Your current latitude and longitude coordinates
MY_LAT = 92
MY_LONG = 36

# Email credentials for sending notifications
my_email = "[your email address]"
my_password = "[your app password]"

# Check if ISS is currently overhead (within ±5 degrees)
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT - 5 < iss_latitude < MY_LAT + 5 and MY_LONG - 5 < iss_longitude < MY_LONG + 5:
        return True

# Check if it's currently nighttime at your location
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

# Loop to check every 60 seconds
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        # Send email notification
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg="Subject:Look Up!\n\nThe ISS is currently above you in the sky!"
            )
