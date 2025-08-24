import random

letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = list("0123456789")
symbols = list("!#$%&()*+")

print("Welcome to the PyPassword Generator!")

while True:
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input("How many symbols would you like?\n"))
    nr_numbers = int(input("How many numbers would you like?\n"))

    total_length = nr_letters + nr_symbols + nr_numbers

    # ✅ Validation
    if total_length < 6:
        print("⚠️ Password too short! Please choose at least 6 characters.\n")
        continue
    elif total_length > 50:
        print("⚠️ Password too long! Please choose fewer than 50 characters.\n")
        continue
    else:
        break  # valid length, exit loop

chosen_letters = random.choices(letters, k=nr_letters)
chosen_symbols = random.choices(symbols, k=nr_symbols)
chosen_numbers = random.choices(numbers, k=nr_numbers)

combined_choices = chosen_letters + chosen_symbols + chosen_numbers
password = "".join(random.sample(combined_choices, len(combined_choices)))

print(f"\nYour password is: {password}")
