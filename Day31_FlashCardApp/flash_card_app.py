from tkinter import *
from tkinter import messagebox
import os
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

# Load Data
try:
    data_df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_df = pd.read_csv("data/vietnamese_common_words.csv")
    data_dict = original_df.to_dict(orient="records")
else:
    restart = messagebox.askyesno(title="Continue Progress?", message="Would you like to continue your previous progress?")
    if restart:
        data_dict = data_df.to_dict(orient="records")
    else:
        os.remove("data/words_to_learn.csv")
        original_df = pd.read_csv("data/vietnamese_common_words.csv")
        data_dict = original_df.to_dict(orient="records")


current_card = {}
flip_timer = None
is_vietnamese = True

# Function to flip the card after 3 seconds
def flip_card():
    global is_vietnamese
    if is_vietnamese:
        canvas.itemconfig(card_image, image=back_img)
        canvas.itemconfig(title_text, text="English", fill="white")
        canvas.itemconfig(word_text, text=current_card["English"], fill="white")
        is_vietnamese = False
    else:
        is_vietnamese = True
        canvas.itemconfig(card_image, image=front_img)
        canvas.itemconfig(title_text, text="Vietnamese", fill="black")
        canvas.itemconfig(word_text, text=current_card["Vietnamese"], fill="black")

# Generate a new card and reset flip timer
def generate_new_card():
    global current_card
    current_card = random.choice(data_dict)
    canvas.itemconfig(card_image, image=front_img)
    canvas.itemconfig(title_text, text="Vietnamese", fill="black")
    canvas.itemconfig(word_text, text=current_card["Vietnamese"], fill="black")

# Remove known card
def known_card():
    data_dict.remove(current_card)
    data = pd.DataFrame(data_dict)
    data.to_csv("data/words_to_learn.csv", index=False)
    generate_new_card()
    update_word_counter()

# Update the word counter whenever a card is marked known
def update_word_counter():
    words_left_label.config(text=f"Words Left: {len(data_dict)}")

# UI setup
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 263, image=front_img)

# Add Text to Canvas
title_text = canvas.create_text(400, 150, text="Vietnamese", font=("Arial", 40, "italic"), fill="black")
word_text = canvas.create_text(
    400, 263, text="Xin chào",
    font=("Arial", 40, "bold"), fill="black",
    width=700
)

canvas.grid(column=0, row=0, columnspan=3)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=generate_new_card)
wrong_button.grid(column=0, row=1, pady=10)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=known_card)
right_button.grid(column=1, row=1, pady=10)

flip_image = PhotoImage(file="images/flip_button.png")
flip_button = Button(image=flip_image, highlightthickness=0, command=flip_card, height=100, width=100)
flip_button.grid(column=2, row=1, pady=10)

words_left_label = Label(window, text=f"Words Left: {len(data_dict)}", font=("Arial", 16), bg=BACKGROUND_COLOR)
words_left_label.grid(column=0, row=2, columnspan=3, pady=10)

generate_new_card()  # Initial flip timer

window.mainloop()
