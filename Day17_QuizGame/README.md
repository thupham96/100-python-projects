# Day 17: Quiz Game with OOP

Welcome to the Quiz Game project! This Python program implements a **True/False Quiz Game**, designed using **Object-Oriented Programming (OOP)** principles. This structured approach enhances code reusability, scalability, and maintainability while providing a fun and interactive user experience.

---

## How It Works

### Game Setup:

- The quiz consists of a series of **True/False** questions.
- The game presents one question at a time, and the user inputs their answer.
- After each response, the program evaluates whether the answer is correct and updates the score.
- The game continues until all questions have been answered.

---

### Program Design with OOP:

1. **Classes and Responsibilities**:
   - **`Question`**: Represents a single quiz question, storing its text and correct answer.
   - **`QuizBrain`**: Controls the game flow, tracking progress, asking questions, and checking answers.
   - **`UserInterface`**: Handles user interactions, displaying questions, accepting input, and showing scores.

2. **Encapsulation**:
   - The quiz logic is encapsulated within the `QuizBrain` class, ensuring a clear separation of concerns.
   - The questions are stored separately in a `data.py` file.

3. **Reusability**:
   - Additional question formats or difficulty levels can be introduced without modifying the core game logic.
   - The modular structure allows easy integration with different question sources (e.g., API-based questions).

---

### User Interactions:

1. **Start the Quiz**:
   - The game begins with a welcome message and the first question is presented.

2. **Answer Questions**:
   - The user inputs either `True` or `False`.
   - The game verifies the answer and provides immediate feedback.

3. **Track Score**:
   - After each question, the user's score is displayed.

4. **End of Quiz**:
   - Once all questions are answered, the final score is shown.
   - The user is thanked for playing.

---

### Key Features:

1. **Static Question Handling**:
   - The game loads an extendable list of questions from `data.py`, making it adaptable to different topics.

2. **Score Tracking**:
   - Users receive real-time feedback and see their total score after each response.

3. **Error Handling**:
   - Ensures valid input (`True` or `False`) and prevents crashes from invalid entries.

4. **Encapsulation & Modularity**:
   - Separates concerns between question storage, game logic, and user interaction for better maintainability.

---

## How to Run

1. Clone the repository and navigate to the `Day17_QuizGame_OOP` folder:
   ```bash
   git clone https://github.com/thupham96/100-python-projects.git
   cd 100-python-projects/Day17_QuizGame
   ```

2. Ensure `data.py` is present in the same directory, as it contains the quiz questions.

3. Run the program:
   ```bash
   python quiz_game.py
   ```

4. Follow the on-screen prompts to answer questions and track your score.

---

## Example Run

```plaintext
Welcome to the True/False Quiz Game!

1: The proof for the Chinese Remainder Theorem used in Number Theory was NOT developed by its first publisher, Sun Tzu. (True/False)?: true
You got it right!
The correct answer is: True.
Your current score is: 1/1.


2: The set of all algebraic numbers is countable. (True/False)?: false
That's wrong.
The correct answer is: True.
Your current score is: 1/2.


3: Popcorn was invented in 1871 by Frederick W. Rueckheim in the USA where he sold the snack on the streets of Chicago. (True/False)?: true
That's wrong.
The correct answer is: False.
Your current score is: 1/3.

You have completed the quiz!
You final score is 1/3.
Thanks for playing!
```

---

## Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- Classes for modular design
- Input handling for user interactions
- List data structures for question storage

---

## What I Learned

- Implementing OOP principles to create structured, reusable game logic.
- Separating concerns for better program design.
- Handling user input and validating responses in an interactive setting.
- Managing game flow with an encapsulated class-based approach.

Enjoy playing the Quiz Game and feel free to customize it with your own questions! 🎉
