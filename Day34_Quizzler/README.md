# Day 34: Quizzler 🧠🎮

Welcome to **Quizzler** – a fun and interactive trivia quiz app built with Python and Tkinter! Test your knowledge across multiple categories and difficulties with real-time questions fetched from an online trivia database. Perfect for quick brain workouts or friendly challenges! 💡✨

## How It Works

1. **Category & Difficulty Selection**: Choose your quiz preferences from dropdown menus.
2. **Question Fetching**: Grabs 10 True/False questions from the Open Trivia Database API based on your selection.
3. **Interactive GUI**: Displays each question in a user-friendly interface with real-time feedback.
4. **Score Tracking**: Keeps track of your current score as you answer questions.
5. **Quiz Completion**: Notifies you when you’ve finished the quiz and disables input buttons.

## Example Run

- **Selected Options**:
  - Category: Science & Nature
  - Difficulty: Medium

- **Output**:
  - Questions appear one-by-one with “True” and “False” buttons.
  - Canvas background turns **green** for correct and **red** for incorrect answers.
  - Score updates after each answer.
  - Message at the end:
    ```
    You've reached the end of the quiz.
    ```

## Features

- ✅ Customizable trivia (category & difficulty)
- 🧠 Real-time API integration with Open Trivia DB
- 🎨 Clean and intuitive GUI with visual feedback
- 🏆 Score tracking to monitor progress
- 🛑 End-of-quiz detection with button disabling

## How to Use

1. Clone or download the repository:
   ```bash
   git clone https://github.com/thupham96/python-projects.git
   cd Day34_Quizzler
   ```

2. Ensure you have the required project structure:
   - `main.py`
   - `ui.py`
   - `quiz_brain.py`
   - `question_model.py`
   - `data.py`
   - `/images/true.png` and `/images/false.png`

3. Run the quiz:
   ```bash
   python quizzler.py
   ```

## Technologies Used

- Python 3
- `Tkinter` for GUI
- `requests` for API calls
- `html` for decoding question text
- Open Trivia Database (https://opentdb.com)

## What I Learned

- Building GUIs with `Tkinter` and managing layout/styling
- Parsing and using external API data
- Creating clean, object-oriented code with multiple classes
- Implementing visual feedback and user interaction logic
- Combining multiple modules into a complete app experience

Put your brain to the test with **Quizzler** and see how much you really know! 🤓📚
