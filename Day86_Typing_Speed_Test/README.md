# Day 86: Typing Speed Test – Python GUI with Tkinter 

This project is an interactive **Typing Speed Test** application built using **Tkinter**. It challenges users to type randomized text passages within 60 seconds, measuring typing speed and accuracy. The GUI disables paste and delete to ensure honest performance and provides real-time color-coded feedback as the user types.

---

## Features

* Loads randomized test text from `text_collection.txt`
* 60-second countdown timer
* Real-time visual feedback:

  * **Blue** for correct characters
  * **Red** for incorrect characters
* Live tracking of:

  * **Words Per Minute (WPM)**
  * **Corrected Characters Per Minute (CPM % accuracy)**
* Paste (`Ctrl+V`/`Cmd+V`) and deletion (`Backspace`/`Delete`) are disabled
* Simple GUI interface with reset functionality

---

## Technologies Used

* **Python**
* **Tkinter** – GUI development
* **time** – for performance tracking
* **random & os** – for loading randomized text passages

---

## How to Run

1. Ensure your `text_collection.txt` file is in the same directory as `main.py`. It should contain multiple entries separated by:

   ```
   \n\n---\n\n
   ```

2. Clone the repository or copy the code:

   ```bash
   git clone https://github.com/thupham96/100-python-projects.git
   cd Day86_Typing_Speed_Test
   ```

3. Run the application:

   ```bash
   python main.py
   ```

---

## Example Usage

1. Launch the app – a random text appears.
2. Start typing in the entry field.
3. The timer will start once you begin typing.
4. Watch live updates of WPM and accuracy.
5. Use the **Restart** button to try a new round.

---

## What I Learned

* Handling real-time GUI updates and timers in Tkinter.
* Preventing specific key actions (paste, delete) to ensure test integrity.
* Parsing and displaying text with live color-coded character-level feedback.
* Measuring typing speed and accuracy with dynamic user interaction.
