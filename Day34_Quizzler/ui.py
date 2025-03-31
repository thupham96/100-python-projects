from tkinter import *
from quiz_brain import QuizBrain
from question_model import Question
from data import fetch_questions, CATEGORIES, DIFFICULTIES
import html

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.quiz = None
        self.dropdown_screen()
        self.window.mainloop()

    def dropdown_screen(self):
        Label(text="Select Category:", bg=THEME_COLOR, fg="white").grid(row=0, column=0, pady=10, padx=10, sticky="w")
        self.category_var = StringVar()
        self.category_var.set("Any")
        self.category_menu = OptionMenu(self.window, self.category_var, *CATEGORIES.keys())
        self.category_menu.grid(row=0, column=1)

        Label(text="Select Difficulty:", bg=THEME_COLOR, fg="white").grid(row=1, column=0, pady=10, padx=10, sticky="w")
        self.difficulty_var = StringVar()
        self.difficulty_var.set("Any")
        self.difficulty_menu = OptionMenu(self.window, self.difficulty_var, *DIFFICULTIES)
        self.difficulty_menu.grid(row=1, column=1)

        self.start_button = Button(text="Start Quiz", command=self.start_quiz)
        self.start_button.grid(row=2, column=0, columnspan=2, pady=20, padx=20)

    def start_quiz(self):
        # Clear dropdown screen
        for widget in self.window.winfo_children():
            widget.destroy()

        category_id = CATEGORIES.get(self.category_var.get())
        print(category_id)
        difficulty = self.difficulty_var.get().lower() if self.difficulty_var.get() != "Any" else None

        question_data = fetch_questions(category=category_id, difficulty=difficulty)

        question_bank = []
        for question in question_data:
            question_text = question["question"]
            question_answer = question["correct_answer"]
            question_bank.append(Question(question_text, question_answer))

        self.quiz = QuizBrain(question_bank)

        # GUI Setup
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0, pady=20)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, text="", fill=THEME_COLOR, font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.image = true_image
        self.true_button.grid(column=0, row=2, pady=20)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.image = false_image
        self.false_button.grid(column=1, row=2, pady=20)

        self.get_next_question()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
