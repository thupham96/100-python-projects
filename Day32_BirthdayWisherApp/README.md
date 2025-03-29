# Day 32: Birthday Wisher App 🎉📧

Welcome to the **Birthday Wisher App**! This Python automation project checks for birthdays from a CSV file and sends personalized birthday greetings via email using customizable templates. It's a great way to automate thoughtfulness and make someone's day extra special.

## How It Works

1. **Read Birthdays**: Loads birthday data from a CSV file.
2. **Match Today's Date**: Checks for any birthdays that match the current date.
3. **Select a Template**: Randomly selects one of the pre-written birthday letters.
4. **Personalize & Send Email**: Replaces the name placeholder in the letter and sends the email via Gmail.

## Example Run

- **CSV Input (`birthdays.csv`)**:
  ```csv
  name,email,year,month,day,interest
  John,john@example.com,1990,3,29,Gaming
  ```

- **Console Output**:
  ```
  Birthdays today (3/29):
  - John (john@example.com, Gaming)
  Email sent to John
  ```

## Features

- **Email Automation**: Uses SMTP to send personalized emails through Gmail.
- **Dynamic Templates**: Randomly selects from multiple letter templates to keep things fresh.
- **Data-Driven**: Reads all data from a CSV file, making it easy to update or scale.
- **Date Matching**: Automatically checks for birthdays that match today’s date.

## How to Use

1. Clone or download the repository:
   ```bash
   git clone https://github.com/thupham96/python-projects.git
   cd Day32_BirthdayWisherApp
   ```

2. Prepare the following files:
   - A CSV file named `birthdays.csv` in the project folder with these columns:
     `name,email,year,month,day,interest`
   - A folder named `letter_templates/` with 3 templates:
     - `letter_1.txt`
     - `letter_2.txt`
     - `letter_3.txt`
     > Make sure each template contains `[NAME]` as a placeholder for personalization.

3. Replace the email and password with your own Gmail credentials.
   > **Tip**: Use an [App Password](https://myaccount.google.com/apppasswords) instead of your regular password for better security.

4. Run the script:
   ```bash
   python birthday_wisher.py
   ```

## Technologies Used

- Python 3
- Pandas for reading CSV data
- `datetime` for current date detection
- `random` for template selection
- `smtplib` for sending emails

## What I Learned

- Automating routine tasks using Python.
- Reading and manipulating CSV files with Pandas.
- Sending emails with Python’s built-in `smtplib`.
- Using placeholder text for dynamic content replacement.
- Organizing data for scalable automation tasks.

Spread birthday cheer the smart way with the **Birthday Wisher App**! 🎂🎁
