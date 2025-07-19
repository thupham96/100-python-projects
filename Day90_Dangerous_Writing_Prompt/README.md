# Day 90: 📝 Dangerous Writing Prompt – Idle Challenge Timer App ⏳🔥

This project is a focused writing tool inspired by the "dangerous writing" concept: if you stop typing for too long, your words disappear. Built using **Python** and **Tkinter**, it pushes writers to stay in flow by combining a countdown timer with an inactivity limit.

---

## Features

* Random **writing prompt** loaded from `prompts.txt`
* **Idle timer**: Stop typing for more than 5 seconds and your writing is deleted
* **Prompt timer**: Total session time limit (e.g., 10 seconds, adjustable)
* Visual **status display** showing time left and idle countdown
* **Start** and **Restart** buttons
* Text editing disabled when time runs out
* Clean, distraction-free **black-and-white interface**

---

## Technologies Used

* **Python**
* **Tkinter** – for GUI layout and event handling
* **random** – to pick a prompt
* **time** – to track activity and prompt duration

---

## How to Run

1. Save the files:

   * `main.py`
   * `dangerous_writer.py`
   * `prompts.txt`

2. Clone the repository or copy the code:

   ```bash
   git clone https://github.com/thupham96/100-python-projects.git
   cd Day90_Dangerous_Writing_Prompt
   ```

3. Run the application:

   ```bash
   python main.py
   ```

---

## Example Usage

1. Launch the app — a writing prompt appears.
2. Click **Start** to begin your timed writing session.
3. Keep typing — if you're idle for more than 5 seconds, your work will be deleted.
4. Once the timer ends, your session is locked, and the text is preserved.
5. Click **Restart** to load a new prompt and try again.

---

## What I Learned

* Implementing **event-driven behavior** using Tkinter’s `after()` loop.
* Managing simultaneous timers for both **idle detection** and **session duration**.
* Dynamically updating GUI elements like status displays and buttons.
* Structuring clean and responsive GUI logic in a modular Python application.
