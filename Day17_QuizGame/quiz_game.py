# Importing the necessary modules
from question_model import Question  # Import the Question class for creating question objects
from data import question_data  # Import the question data containing a list of question dictionaries
from quiz_brain import QuizBrain  # Import the QuizBrain class for handling quiz logic

# Initialize an empty list to store question objects
question_bank = []

# Loop through each question dictionary in question_data
for i in question_data:
    # Create a Question object using the 'question' text and 'correct_answer' from the dictionary
    new_question = Question(i['question'], i['correct_answer'])
    # Add the newly created Question object to the question bank
    question_bank.append(new_question)

# Initialize a QuizBrain instance with the list of question objects
quiz = QuizBrain(question_bank)

# Print a welcome message
print("Welcome to the True/False Quiz Game!")

# Continue running the quiz while there are remaining questions
while quiz.still_has_questions():
    quiz.next_question()  # Ask the next question

# Print completion message and final score
print("You have completed the quiz!")
print(f"Your final score is {quiz.score}/{quiz.question_number}")
