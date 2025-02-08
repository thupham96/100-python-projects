class QuizBrain:
    def __init__(self, question_bank):
        """
        Initializes the QuizBrain object.
        :param question_bank: List of Question objects
        """
        self.question_number = 0  # Keeps track of the current question number
        self.question_list = question_bank  # Stores the list of questions
        self.score = 0  # Tracks the user's score

    def still_has_questions(self):
        """
        Checks if there are still questions left in the quiz.
        :return: True if there are more questions, False otherwise
        """
        if self.question_number < len(self.question_list):
            return True
        return False

    def check_answer(self, user_answer, correct_answer):
        """
        Compares the user's answer with the correct answer and updates the score.
        :param user_answer: User's input answer
        :param correct_answer: Correct answer to the question
        """
        # Validate if the user input is either 'true' or 'false'
        if user_answer.lower() not in ["true", "false"]:
            print("Your answer is invalid.")
        elif user_answer.lower() == correct_answer.lower():
            self.score += 1  # Increase score if the answer is correct
            print("You got it right!")
        else:
            print("That's wrong.")

        # Display the correct answer and the current score
        print(f"The correct answer is: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}.")
        print("\n")  # Add spacing for readability

    def next_question(self):
        """
        Fetches the next question from the list, prompts the user for an answer, 
        and checks the response.
        """
        current_question = self.question_list[self.question_number]  # Get the current question object
        current_question_text = current_question.text  # Extract the question text
        self.question_number += 1  # Increment the question number

        # Prompt user for an answer and pass it to check_answer function
        user_answer = input(f"{self.question_number}: {current_question_text} (True/False)?: ")
        self.check_answer(user_answer, current_question.answer)
