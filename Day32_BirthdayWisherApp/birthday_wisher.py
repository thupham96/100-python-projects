import pandas as pd
import datetime as dt
import random
import smtplib

# Email and password
my_email = "[YOUR EMAIL]"
my_password = "[YOUR PASSWORD]"

# Get today's date
today = (dt.datetime.now().month, dt.datetime.now().day)

# Load CSV data
birthdays = pd.read_csv("birthdays.csv")

# Create a dictionary mapping each date to a list of people with birthdays on that date
birthdays_dict = {}
for _, row in birthdays.iterrows():
    date_key = (int(row['month']), int(row['day']))
    birthdays_dict.setdefault(date_key, []).append(row)

# Check today's birthdays
if today in birthdays_dict:
    birthday_people = birthdays_dict[today]
    print(f"Birthdays today ({today[0]}/{today[1]}):")

    for person in birthday_people:
        name = person['name']
        recipient_email = person['email']
        interest = person['interest']

        print(f"- {name} ({recipient_email}, {interest})")

        # Pick random template
        template_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"

        # Open the template and replace placeholder
        with open(template_path, "r") as file:
            email_body = file.read().replace("[NAME]", name)

        # Send email
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=recipient_email,
                msg=f"Subject:Happy Birthday!\n\n{email_body}"
            )
            print(f"Email sent to {name}")
else:
    print("No birthdays today.")
