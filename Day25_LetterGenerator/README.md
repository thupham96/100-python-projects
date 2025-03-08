# Day 25: Personalized Event Letter Generator

Welcome to the Personalized Event Letter Generator! This handy Python script generates custom invitation letters for your events. Quickly create individualized invitations with ease.


## How It Works

### Step-by-Step Guide:

1. **Prepare Your Names List**:
   - Add the invitees' names into `invited_names.txt` within the `Input/Names` directory, one name per line.

2. **Customize Letter Template**:
   - Use placeholders `[name]`, `[event_name]`, `[event_date]`, and `[event_location]` in the `starting_letter.txt` located in `Input/Letters`.

3. **Run the Script**:
   - Execute the Python script, and provide event details when prompted.

4. **View Generated Letters**:
   - Find personalized letters saved individually in the `Output/ReadyToSend` folder.

### Example Run:
```plaintext
Enter the event name: Annual Gala
Enter the event date (e.g., March 15, 2025): June 10, 2025
Enter the event location: Grand Ballroom, Hilton Hotel

Letters have been successfully created in 'ReadyToSend' folder.
```

## Features

- **Dynamic Letter Personalization**: Automatically fills placeholders with specific event details and invitee names.
- **Efficient Batch Processing**: Quickly generates multiple personalized letters simultaneously.
- **Easy-to-use Template System**: Customizable template allows flexibility for various types of events.

## How to Use

1. Clone the repository and navigate to the `Day25_LetterGenerator` folder:
   ```bash
   git clone https://github.com/yourusername/100-python-projects.git
   cd 100-python-projects/Day25_LetterGenerator
   ```

2. Run the script:
   ```bash
   python letter_generator.py
   ```

3. Follow the prompts to customize your event invitations.

## Technologies Used

- Python 3
- File handling and string manipulation

## What I Learned

- Reading from and writing to files in Python.
- Automating the process of generating personalized content.
- Handling placeholders and dynamic string replacement.

Simplify event planning with personalized invitations! 🎉✉️

