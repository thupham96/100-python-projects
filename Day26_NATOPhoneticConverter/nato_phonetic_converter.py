import pandas as pd

# Load the NATO phonetic alphabet CSV into a dictionary
alphabet_df = pd.read_csv("nato_phonetic_alphabet.csv")
alphabet_dict = {row["letter"]: row["code"] for _, row in alphabet_df.iterrows()}


# Welcome message
def welcome():
    print("\n" + "=" * 40)
    print("📖 Welcome to the NATO Phonetic Alphabet Converter! 🔠")
    print("Convert any word into its phonetic alphabet equivalent.")
    print("You can also customize the phonetic alphabet! ✏️")
    print("=" * 40 + "\n")


# Function to customize the phonetic alphabet
def customize_alphabet():
    while True:
        choice = input("\nWould you like to customize the phonetic alphabet? (yes/no): ").strip().lower()
        if choice=="yes":
            letter = input("Enter the letter you want to modify (A-Z): ").strip().upper()
            if len(letter)==1 and letter in alphabet_dict:
                new_word = input(f"Enter the new phonetic word for {letter}: ").strip().capitalize()
                alphabet_dict[letter] = new_word
                print(f"✅ Updated: {letter} -> {new_word}")
            else:
                print("❌ Invalid letter. Please enter a single letter from A-Z.")
        elif choice=="no":
            break
        else:
            print("❌ Invalid input. Please enter 'yes' or 'no'.")


# Function to convert user input into phonetic code
def convert_to_phonetic():
    while True:
        user_input = input("\nEnter a word: ").strip().upper()
        if not any(char.isalpha() for char in user_input):
            print("❌ Please enter at least one letter from A-Z.")
            continue

        # Filter out non-alphabet characters
        result = [alphabet_dict[letter] for letter in user_input if letter in alphabet_dict]

        if result:
            print("\n🔠 Phonetic Code:", " ".join(result))
            break
        else:
            print("❌ Only enter letters from A-Z. Please try again.")


# Run the program
welcome()  # Display welcome message
customize_alphabet()  # Allow customization

# Convert user input into phonetic code in a loop
while True:
    convert_to_phonetic()
    while True:  # Ensure valid yes/no input
        retry = input("\n🔄 Would you like to try another word? (yes/no): ").strip().lower()
        if retry in ("yes", "no"):
            break
        print("❌ Invalid input. Please enter 'yes' or 'no'.")

    if retry=="no":
        print("\n👋 Thank you for using the NATO Phonetic Alphabet Converter! Goodbye! 🚀")
        break
