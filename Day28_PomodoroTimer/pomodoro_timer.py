from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
paused = False
remaining_time = 0
timer_running = False

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps, paused, timer_running
    if timer:
        window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    checkmark_label.config(text="")
    reps = 0
    paused = False
    timer_running = False
    pause_button.config(text="Pause")

# ---------------------------- PAUSE/RESUME ------------------------------- #
def pause_resume_timer():
    global paused, timer_running
    if not timer_running:
        return

    if paused:
        paused = False
        pause_button.config(text="Pause")
        count_down(remaining_time)
    else:
        paused = True
        pause_button.config(text="Resume")
        window.after_cancel(timer)

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps, timer_running

    if timer_running:
        return

    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    timer_running = True

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer, remaining_time, timer_running
    remaining_time = count

    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")

    if count > 0 and not paused:
        timer = window.after(1000, count_down, count - 1)
    elif count == 0:
        timer_running = False
        start_timer()
        mark = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            mark += "✔"
        checkmark_label.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", font=(FONT_NAME, 30, "bold"), bg=YELLOW, fg=GREEN)
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", font=(FONT_NAME, 15, "bold"), highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2, pady=10)

pause_button = Button(text="Pause", font=(FONT_NAME, 15, "bold"), highlightthickness=0, command=pause_resume_timer)
pause_button.grid(column=1, row=2, pady=10)

reset_button = Button(text="Reset", font=(FONT_NAME, 15, "bold"), highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2, pady=10)

checkmark_label = Label(font=(FONT_NAME, 15, "bold"), fg=GREEN, bg=YELLOW)
checkmark_label.grid(column=1, row=3)

window.mainloop()
