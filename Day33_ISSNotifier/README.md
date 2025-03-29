# Day 33: ISS Overhead Notifier 🚀✨

Welcome to the **ISS Overhead Notifier**! This Python automation tool checks if the International Space Station (ISS) is currently flying over your location **at night**, and notifies you via email so you can look up and try to spot it in the sky! 🌌

## How It Works

1. **ISS Location Tracking**: Uses a public API to fetch the current position of the ISS.
2. **Nighttime Detection**: Determines whether it’s dark at your location using sunrise-sunset data.
3. **Location Matching**: Checks if the ISS is within ±5 degrees of your coordinates.
4. **Email Notification**: Sends you an alert when the ISS is overhead **and** it’s dark enough to see it.

## Example Run

- **Conditions**:
  - Your location: latitude `92`, longitude `36`
  - Time: 9:00 PM
  - ISS is overhead

- **Output**:
  - An email is sent with the subject:
    ```
    Subject:Look Up!
    
    The ISS is currently above you in the sky!
    ```

## Features

- **Real-Time Tracking**: Checks ISS position every 60 seconds.
- **Nighttime Validation**: Avoids unnecessary alerts during daylight.
- **Email Alerts**: Sends instant notification to ensure you don’t miss the moment.
- **Customizable**: Easily adapt to any location by changing coordinates.

## How to Use

1. Clone or download the repository:
   ```bash
   git clone https://github.com/thupham96/python-projects.git
   cd Day33_ISSNotifier
   ```

2. Replace `MY_LAT` and `MY_LONG` with your actual latitude and longitude values:
   ```python
   MY_LAT = 51.5074
   MY_LONG = -0.1278
   ```

3. Enter your email credentials:
   ```python
   my_email = "your_email@gmail.com"
   my_password = "your_app_password"
   ```
   > Use an [App Password](https://myaccount.google.com/apppasswords) for Gmail instead of your regular password.

4. Run the script:
   ```bash
   python iss_notifier.py
   ```

## Technologies Used

- Python 3
- `requests` for API interaction
- `datetime` for time-based checks
- `smtplib` for sending emails
- `time` for loop intervals

## What I Learned

- Working with real-time APIs and JSON data.
- Scheduling tasks using Python loops and delays.
- Automating notifications using SMTP.
- Calculating dynamic geographic conditions (like night time).
- Writing clean, modular functions for condition-based logic.

Never miss a chance to spot the ISS again with the **ISS Overhead Notifier**! 🌠📬
