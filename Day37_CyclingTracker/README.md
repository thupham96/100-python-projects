# Day 37: Cycling Tracker with Pixela 🚴📈

Stay motivated with **Cycling Tracker** – a Python script that logs and tracks your daily cycling distance using the Pixela API. Whether you're training for a race or just staying healthy, this simple tool keeps you on track! 🚀💪

## How It Works

1. **User Creation (Optional)**: Creates a new Pixela account if you don't already have one.
2. **Graph Setup (Optional)**: Creates a graph to visualize your cycling progress.
3. **Daily Logging**: Input how many kilometers you cycled today and record it.
4. **View Data**: Check today's recorded distance easily.

## Example Output

- **Prompt**:  
  ```text
  What do you want to do today?
  1. Add/Update today's pixel
  2. View today's pixel data
  ```
- **User Input**: `1`
- **Result**:  
  ```text
  Successfully added: 10 km 🚴
  ```
  
or

- **User Input**: `2`
- **Result**:  
  ```text
  Today's cycling record: 10 km 🚴
  ```

## Features

- 🚴 Log daily cycling distances  
- 📊 View today's progress instantly  
- 🔧 Auto-update if today's record already exists  
- 🛠️ Easy setup for new users and graphs  
- ⏳ Simple date handling with Python `datetime`

## How to Use

1. Clone the repo:
   ```bash
   git clone https://github.com/thupham96/python-projects.git
   cd Day37_CyclingTracker
   ```

2. Replace credentials with your own:
   - `USERNAME`
   - `TOKEN`
   
   *(Consider using environment variables for safety in real-world usage.)*

3. Run the script:
   ```bash
   python cycling_tracker.py
   ```

4. Choose your option:
   - `1` to add/update today's cycling record
   - `2` to view today's record

## Technologies Used

- Python 3
- `requests` for API communication
- Pixela API (https://pixe.la/)

## What I Learned

- Working with RESTful APIs (POST, PUT, GET)
- Handling user inputs and invalid selections
- Updating vs creating resources via API
- Automating daily fitness tracking with simple tools

Stay consistent with your goals and celebrate every kilometer — **Cycling Tracker** makes it easy to ride toward your best self! 🚴🌟
