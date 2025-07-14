from tkinter import Tk, messagebox, Label, Entry, Canvas, Button, Text
import time
import random
import os

# Test text
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "text_collection.txt")
with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()

entries = content.split("\n\n---\n\n")
test_text = random.choice(entries)

# Initialize variables
test_started = False
start_time = None
end_time = None
correct_characters = 0
time_remaining = 60

# Restart
def restart():
    global test_started, start_time, test_text, end_time, correct_characters, time_remaining

    test_text = random.choice(entries)
    text.config(state="normal")
    text.delete("1.0", "end")
    text.insert("end", test_text, "black")
    text.config(state="disabled")

    user_input.config(state="normal")
    user_input.delete(0, "end")
    accuracy.config(text="Corrected CPM: ?")
    wpm.config(text="WPM: ?")
    time_remaining = 60
    time_left.config(text=f"Time left: {time_remaining}")

    test_started = False
    start_time = None
    end_time = None
    correct_characters = 0

# Start test
def start_test():
    global test_started, start_time, end_time

    test_started=True
    start_time = time.time()
    end_time = None
    countdown()
    user_input.focus()

# Clear text
def clear_text_display():
    text.config(state="normal")
    text.delete("1.0", "end")
    text.config(state="disabled")

# Check input
def check_input(event):
    global test_started, end_time, correct_characters

    if user_input["state"]=="disabled":
        return

    if not test_started:
        start_test()

    user_input_text = user_input.get()
    correct_characters = 0
    for i in range(len(user_input_text)):
        if i < len(test_text):
            if user_input_text[i] != test_text[i]:
                position = text.index(f"1.0 + {i} chars")
                text.config(state="normal")
                text.tag_add("red", position, f"{position} + 1c")
                text.tag_config("red", foreground="red")
                text.config(state="disabled")
            else:
                position = text.index(f"1.0 + {i} chars")
                text.config(state="normal")
                text.tag_add("blue", position, f"{position} + 1c")
                text.tag_config("blue", foreground="blue")
                text.config(state="disabled")
                correct_characters += 1
    if len(user_input_text) >= len(test_text):
        test_started = False
        user_input.config(state="disabled")

    end_time = time.time()
    calculate_results()

# Count down
def countdown():
    global time_remaining, test_started, end_time

    if time_remaining > 0 and test_started:
        time_remaining -= 1
        time_left.config(text=f"Time left: {time_remaining}")
        window.after(1000, countdown)
    elif test_started:
        end_time = time.time()
        user_input.config(state="disabled")
        test_started = False
        calculate_results()

# Calculate results
def calculate_results():
    if start_time is None or end_time is None:
        return

    time_taken = end_time - start_time  # in seconds
    if time_taken==0:
        return

    time_minutes = time_taken / 60
    total_chars = len(user_input.get())
    if total_chars==0:
        return

    wpm_rate = int((total_chars / 5) / time_minutes)
    wpm.config(text=f"WPM: {str(wpm_rate)}")

    total_characters_in_input = len(user_input.get())
    accuracy_rate = round((correct_characters / total_characters_in_input) * 100, 2)
    accuracy.config(text=f"Corrected CPM: {accuracy_rate}%")

# GUI
window = Tk()
window.title("Typing Speed Test")
window.config(padx=20, pady=20, bg='white')

# Text area and user input
text = Text(width=55, height=20, bg='light gray', wrap="word")
text.insert("end", test_text, "black")
text.grid(row=0, column=0, pady=10, columnspan=4)
user_input = Entry(width=60)
user_input.grid(row=1, column=0, pady=10, columnspan=4)
user_input.bind("<Control-v>", lambda e: "break")
user_input.bind("<Command-v>", lambda e: "break")  # for Mac

def block_deletion_keys(event):
    if event.keysym in ("BackSpace", "Delete"):
        return "break"

user_input.bind("<KeyPress>", block_deletion_keys)
user_input.bind("<KeyRelease>", check_input)

# Create canvas
canvas = Canvas(width=400, height=150, highlightthickness=0, bg='light gray')
canvas.grid(row=2, column=0, columnspan=4, pady=10)

# Create labels and buttons
wpm = Label(canvas, text="WPM: ?", bg='white')
accuracy = Label(canvas, text="Corrected CPM: ?", bg='white')
time_left = Label(canvas, text="Time left: 60", bg='white')
restart_button = Button(canvas, text="Restart", bg='white', command=restart)

# Place labels and buttons inside the canvas
canvas.create_window(50, 50, window=wpm)
canvas.create_window(200, 50, window=accuracy)
canvas.create_window(350, 50, window=time_left)
canvas.create_window(200, 100, window=restart_button)

window.mainloop()
