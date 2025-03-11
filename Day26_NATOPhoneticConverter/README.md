# Day 26: NATO Phonetic Alphabet Converter

Welcome to the NATO Phonetic Alphabet Converter! This interactive tool allows you to convert any word into its phonetic alphabet equivalent. Additionally, you can customize the phonetic words for each letter to personalize your experience.

## How It Works

1. The program loads the NATO phonetic alphabet from a CSV file.
2. It provides an option to customize the phonetic words for any letter.
3. The user enters a word, and it is converted into the phonetic alphabet.
4. The user can continue converting words or exit the program.

## Example Run:
```plaintext
📖 Welcome to the NATO Phonetic Alphabet Converter! 🔠
Convert any word into its phonetic alphabet equivalent.
You can also customize the phonetic alphabet! ✏️

Would you like to customize the phonetic alphabet? (yes/no): yes
Enter the letter you want to modify (A-Z): B
Enter the new phonetic word for B: BravoX
✅ Updated: B -> BravoX

Would you like to customize the phonetic alphabet? (yes/no): no

Enter a word: HELLO
🔠 Phonetic Code: Hotel Echo Lima Lima Oscar

🔄 Would you like to try another word? (yes/no): no
👋 Thank you for using the NATO Phonetic Alphabet Converter! Goodbye! 🚀
```

## Features

- **Customizable Phonetic Alphabet**: Modify phonetic words for specific letters.
- **User-Friendly Interface**: Provides clear instructions and feedback.
- **Robust Input Handling**: Ensures valid inputs for customization and word conversion.

## How to Use

1. Clone the repository and navigate to the `Day26_NATOPhoneticConverter` folder:
   ```bash
   git clone https://github.com/thupham96/100-python-projects.git
   cd 100-python-projects/Day26_NATOPhoneticConverter
   ```
2. Ensure the `nato_phonetic_alphabet.csv` file is present in the same directory.
3. Run the script:
   ```bash
   python nato_phonetic_converter.py
   ```
4. Follow the prompts to customize and convert words into phonetic codes.

## Technologies Used

- Python 3
- Pandas for CSV data processing
- Dictionary for phonetic word lookup
- String manipulation for dynamic output

## What I Learned

- Handling CSV data with `pandas`.
- Using dictionaries for quick lookups.
- Implementing user input validation.
- Providing a customizable user experience.

Try it out and explore the phonetic world! 🔡🚀
