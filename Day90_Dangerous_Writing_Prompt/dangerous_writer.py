import tkinter as tk
import random
import time

# Constants
IDLE_LIMIT = 5  # seconds before deletion
PROMPT_DURATION = 10 * 60  # total prompt time in seconds (e.g., 10 minutes)

class DangerousWriter():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Dangerous Writing Prompt")
        self.root.configure(bg='black', width=300, height=300)

        self.text = tk.Text(self.root, font=('Courier', 16), bg='black', fg='white', insertbackground='white', wrap='word')
        self.text.pack(expand=True, fill='both')

        self.restart_btn = tk.Button(self.root, text="Restart", command=self.restart)
        self.restart_btn.pack(side='bottom', pady=10)

        self.start_btn = tk.Button(self.root, text="Start", command=self.start)
        self.start_btn.pack(side='bottom', pady=10)

        self.status = tk.Label(self.root, text="", fg="white", bg="black", font=("Courier", 12))
        self.status.pack(side='bottom', pady=10)

        self.last_keypress = None
        self.last_idle_check = None
        self.prompt_timer_id = None

        self.load_prompt()
        self.text.config(state='disabled')
        self.root.mainloop()

    def load_prompt(self):
        try:
            with open("prompts.txt") as file:
                prompts = file.readlines()
            prompt = random.choice(prompts).strip()
            self.text.insert("1.0", f"{prompt}\n\n")
            self.text.mark_set("insert", "end")
        except FileNotFoundError:
            self.text.insert("1.0", "⚠️ prompts.txt not found.\n\n")
            self.text.mark_set("insert", "end")

    def delete_text(self):
        self.text.delete("1.0", "end")
        self.status.config(text="💥 Everything is gone.")

    def reset_timer(self, event=None):
        if self.last_keypress:
            self.root.after_cancel(self.last_keypress)
        self.last_keypress = self.root.after(IDLE_LIMIT * 1000, self.delete_text)
        self.last_input_time = time.time()

    # Checks if the user has been idle for too long
    def check_idle(self):
        elapsed = int(time.time() - self.last_input_time)
        remaining_idle = IDLE_LIMIT - elapsed
        remaining_idle = max(0, remaining_idle)

        mins, secs = divmod(self.prompt_time_left, 60)
        self.status.config(
            text=f"🕒 Time left: {mins:02}:{secs:02} | ⏳ Idle for {elapsed}s (deleting in {remaining_idle})"
        )

        if elapsed >= IDLE_LIMIT:
            self.delete_text()
            if self.prompt_timer_id:
                self.root.after_cancel(self.prompt_timer_id)
                self.prompt_timer_id = None
        else:
            self.last_idle_check = self.root.after(1000, self.check_idle)

    # (Re)starts the idle-check loop
    def start_idle_check(self):
        self.reset_timer()
        if self.last_idle_check:
            self.root.after_cancel(self.last_idle_check)
        self.last_idle_check = self.root.after(1000, self.check_idle)

    def update_prompt_timer(self):
        if self.prompt_time_left > 0:
            self.prompt_time_left -= 1
            self.prompt_timer_id = self.root.after(1000, self.update_prompt_timer)
        else:
            if self.last_keypress:
                self.root.after_cancel(self.last_keypress)
            if self.last_idle_check:
                self.root.after_cancel(self.last_idle_check)

            self.text.config(state='disabled')  # Disable editing
            self.root.unbind("<Key>")  # Stop tracking keys
            self.status.config(text="⏰ Time's up! Your writing session has ended.")

    def start(self):
        self.text.config(state='normal')

        self.last_input_time = time.time()
        self.prompt_time_left = PROMPT_DURATION

        self.root.bind("<Key>", self.reset_timer)
        self.root.bind("<Escape>", lambda e: self.root.destroy())  # ESC to quit

        self.start_idle_check()
        self.update_prompt_timer()

        self.start_btn.config(state='disabled')

    def restart(self):
        # Cancel timers
        if self.last_keypress:
            self.root.after_cancel(self.last_keypress)
            self.last_keypress = None
        if self.last_idle_check:
            self.root.after_cancel(self.last_idle_check)
            self.last_idle_check = None
        if self.prompt_timer_id:
            self.root.after_cancel(self.prompt_timer_id)
            self.prompt_timer_id = None

        # Reset text and timers
        self.text.config(state='normal')
        self.text.delete("1.0", "end")
        self.status.config(text="", fg="white")

        self.load_prompt()
        self.text.config(state='disabled')
        self.start_btn.config(state='normal')