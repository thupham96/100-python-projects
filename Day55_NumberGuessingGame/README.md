# Day 55: 🔢 Flask Number Guessing Game 🎯

Build a fun and interactive number guessing game using Python and Flask! This simple web app generates a random number between 0 and 100 and gives users hints through colorful text and GIFs based on their guesses.

## 🚀 How It Works

1. **Start Page**: Navigate to the root URL to receive instructions.
2. **Guess by URL**: Append a number to the URL (e.g., `/50`) to make a guess.
3. **Feedback**:

   * Too low → red message + GIF
   * Too high → purple message + GIF
   * Correct → green message + victory GIF
4. **Guess Count**: Each attempt increments a visible guess counter.
5. **Reset Option**: Visit `/reset` to start a new game with a fresh random number.

## 🧠 Features

* 🎯 Random number is fixed per game session
* 🎨 Styled HTML responses with GIFs for fun feedback
* 🔁 Reset functionality for endless replay
* 📈 Guess tracking for each session

## 🛠️ How to Run

1. Clone the project:

   ```bash
   git clone https://github.com/thupham96/100-python-projects.git
   cd Day55_NumberGuessingGame
   ```

2. Install Flask:

   ```bash
   pip install flask
   ```

3. Run the app:

   ```bash
   python main.py
   ```

4. Open your browser and go to `http://127.0.0.1:5000/`.

5. Start guessing by entering numbers in the URL path (e.g., `http://127.0.0.1:5000/42`).

## 🖼️ Example Output

* `/`
  *"Guess a number between 0 and 100"* + loading GIF

* `/25`
  **Too low, try again!** + red text + funny GIF

* `/90`
  **Too high, try again!** + purple text + reaction GIF

* `/random_number`
  **You found me!** + green text + celebration GIF

## 🧪 Technologies Used

* Python 3
* Flask
* Random module
* GIFs for visual feedback (via Giphy)

## 🎓 What I Learned

* Setting up Flask routes and dynamic URL parameters
* Managing global state in a Flask app
* Enhancing UX with styled HTML and embedded GIFs
* Resetting game logic without restarting the server

---

💡 This project is perfect for beginners diving into Flask and looking to combine backend logic with playful frontend interaction!
