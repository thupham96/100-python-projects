# Day 82: Morse Code Translator

This project implements a **Morse Code Translator** that can both encode text into Morse code and decode Morse code back into readable text. It provides an interactive console interface for translating messages using the international Morse code standard.

---

## Project Features

* Converts text (letters, numbers, punctuation) into Morse code.
* Decodes valid Morse code into English text.
* Handles word separation and unknown characters gracefully.
* Interactive user input for encoding or decoding.
* Runs in a loop for multiple translations until the user chooses to exit.

---

## Technologies Used

* **Python** — for core implementation
* **Standard I/O** — for user interaction

---

## How to Run

1. Clone the repository and navigate to the project directory:

   ```bash
   git clone https://github.com/thupham96/100-python-projects.git
   cd Day82_Morse_Code_Translator
   ```

2. Run the translator:

   ```bash
   python morse_code_translator.py
   ```

---

## Example Usage

```
Welcome to Morse Code Translator!
Would you like to encode or decode? encode
What string would you like to encode/decode? Hello, World!
The translated message is: .... . .-.. .-.. --- --..-- / .-- --- .-. .-.. -.. -.-.--
Would you like to encode or decode another string? (y/n) y
Would you like to encode or decode? decode
What string would you like to encode/decode? .... . .-.. .-.. --- / .-- --- .-. .-.. -..
The translated message is: HELLO WORLD
Would you like to encode or decode another string? (y/n) n
```

---

## What I Learned

* How to build a bidirectional translator using Python dictionaries.
* Techniques for handling unknown inputs and ensuring robust translation logic.
* Managing user interaction loops in Python scripts.
* Applying string manipulation and list operations for text processing.
